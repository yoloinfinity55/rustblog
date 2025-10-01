use std::fs;
use std::io::{self, Write};
use std::path::Path;
use chrono::Local;

fn main() -> io::Result<()> {
    let blog_dir = Path::new("/Users/minijohn/Documents/github-repo/rustblog/content/blog/");

    // Ensure the blog directory exists
    if !blog_dir.exists() {
        fs::create_dir_all(blog_dir)?;
    }

    // Prompt for user input
    print!("Enter the path to the .txt file you want to convert: ");
    io::stdout().flush()?;
    let mut txt_file_path_str = String::new();
    io::stdin().read_line(&mut txt_file_path_str)?;
    let txt_file_path = Path::new(txt_file_path_str.trim());

    // Validate the input file
    if !txt_file_path.exists() {
        eprintln!("Error: File not found at '{}'", txt_file_path.display());
        return Ok(())
    }
    if txt_file_path.extension().and_then(|s| s.to_str()) != Some("txt") {
        eprintln!("Error: The provided file is not a .txt file.");
        return Ok(())
    }

    // Read the content of the .txt file
    let content = fs::read_to_string(txt_file_path)?;

    // Get the base name for the title and new filename
    let base_name = txt_file_path
        .file_stem()
        .and_then(|s| s.to_str())
        .unwrap_or("Untitled");

    // Create a Zola-compatible filename (kebab-case)
    let md_filename_str = format!("{}.md", base_name.replace(' ', "-").to_lowercase());
    let md_file_path = blog_dir.join(&md_filename_str);

    // Get today's date
    let today = Local::now().date_naive().format("%Y-%m-%d").to_string();

    // Create the front matter
    let front_matter = format!(
        "+++\n         title = \"{}\"\n         date = {}\n         [taxonomies]\n         tags = [\"converted\"]\n         categories = [\"blog\"]\n         +++\n\n",
        base_name.replace('-', " ").to_uppercase(), // Make title more readable
        today
    );

    // Combine front matter and content
    let full_content = format!("{}{}", front_matter, content);

    // Write the new Markdown file
    fs::write(&md_file_path, full_content)?;

    println!(
        "Successfully converted '{}' to '{}'",
        txt_file_path.display(),
        md_file_path.display()
    );

    Ok(())
}
