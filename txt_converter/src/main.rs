use std::fs;
use std::io::{self, Write};
use std::path::Path;
use chrono::Local;

fn main() -> io::Result<()> {
    let blog_dir = Path::new("/Users/minijohn/Documents/github-repo/rustblog/content/blog/");

    // Ensure the blog directory exists
    if !blog_dir.exists() {
        fs::create_dir_all(blog_dir).map_err(|e| {
            eprintln!("Error creating directory '{}': {}", blog_dir.display(), e);
            e
        })?;
    }

    // Prompt for user input for the .txt file path
    print!("Enter the path to the .txt file you want to convert: ");
    io::stdout().flush()?;
    let mut txt_file_path_str = String::new();
    io::stdin().read_line(&mut txt_file_path_str)?;
    let txt_file_path = Path::new(txt_file_path_str.trim());

    // Validate the input file
    if !txt_file_path.exists() {
        eprintln!("Error: File not found at '{}'", txt_file_path.display());
        return Ok(()); // Return Ok(()) to allow the program to continue if the user wants to try another file
    }
    if txt_file_path.extension().and_then(|s| s.to_str()) != Some("txt") {
        eprintln!("Error: The provided file '{}' is not a .txt file.", txt_file_path.display());
        return Ok(()); // Return Ok(()) to allow the user to try again
    }

    // Read the content of the .txt file
    let content = fs::read_to_string(txt_file_path).map_err(|e| {
        eprintln!("Error reading file '{}': {}", txt_file_path.display(), e);
        e
    })?;

    // Get the base name for the title and new filename
    let base_name = txt_file_path
        .file_stem()
        .and_then(|s| s.to_str())
        .unwrap_or("Untitled");

    // Prompt for user input for title
    print!("Enter the title for the post: ");
    io::stdout().flush()?;
    let mut title_str = String::new();
    io::stdin().read_line(&mut title_str).map_err(|e| {
        eprintln!("Error reading title input: {}", e);
        e
    })?;
    let title = title_str.trim().to_string();

    // Prompt for user input for tags
    print!("Enter tags (comma-separated, e.g., rust, programming): ");
    io::stdout().flush()?;
    let mut tags_str = String::new();
    io::stdin().read_line(&mut tags_str).map_err(|e| {
        eprintln!("Error reading tags input: {}", e);
        e
    })?;
    let tags: Vec<String> = tags_str
        .trim()
        .split(',')
        .map(|s| s.trim().to_string())
        .filter(|s| !s.is_empty()) // Filter out empty strings
        .collect();

    // Prompt for user input for categories
    print!("Enter categories (comma-separated, e.g., tech, tutorial): ");
    io::stdout().flush()?;
    let mut categories_str = String::new();
    io::stdin().read_line(&mut categories_str).map_err(|e| {
        eprintln!("Error reading categories input: {}", e);
        e
    })?;
    let categories: Vec<String> = categories_str
        .trim()
        .split(',')
        .map(|s| s.trim().to_string())
        .filter(|s| !s.is_empty()) // Filter out empty strings
        .collect();

    // Format tags and categories for front matter
    let tags_formatted = tags.iter().map(|t| format!("\"{}\"", t)).collect::<Vec<String>>().join(", ");
    let categories_formatted = categories.iter().map(|c| format!("\"{}\"", c)).collect::<Vec<String>>().join(", ");

    // Create a Zola-compatible filename (kebab-case)
    let md_filename_str = format!("{}.md", base_name.replace(' ', "-").to_lowercase());
    let md_file_path = blog_dir.join(&md_filename_str);

    // Get today's date
    let today = Local::now().date_naive().format("%Y-%m-%d").to_string();

    // Create the front matter
    let front_matter = format!(
        "+++\n         title = \"{}\"\n         date = {}\n         [taxonomies]\n         tags = [{}]\n         categories = [{}]\n         +++\n\n",
        title, // Use the user-provided title
        today,
        tags_formatted,
        categories_formatted
    );

    // Combine front matter and content
    let full_content = format!("{}{}", front_matter, content);

    // Write the new Markdown file
    fs::write(&md_file_path, full_content).map_err(|e| {
        eprintln!("Error writing file '{}': {}", md_file_path.display(), e);
        e
    })?;

    println!(
        "Successfully converted '{}' to '{}'",
        txt_file_path.display(),
        md_file_path.display()
    );

    Ok(())
}
