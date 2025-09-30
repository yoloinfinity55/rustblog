import os
import re
from datetime import datetime

# Predefined lists for automatic tag/category detection
PREDEFINED_TAGS = ["Rust", "Zola", "Tailwind CSS", "Programming", "Web Development", "Tutorial"]
PREDEFINED_CATEGORIES = ["Technology", "Blog Updates", "Personal"]

def add_default_front_matter(filepath):
    """
    Adds default Zola front matter to a Markdown file if it doesn't already have one.
    Automatically detects tags and categories based on predefined lists.
    """
    with open(filepath, 'r+', encoding='utf-8') as f:
        content = f.read()

        # Check if front matter already exists
        if content.strip().startswith('+++'):
            print(f"Skipping '{filepath}': Already has front matter.")
            return

        # Extract title from filename
        filename = os.path.basename(filepath)
        title_without_ext = os.path.splitext(filename)[0]
        # Convert kebab-case or snake_case to Title Case
        title = ' '.join(word.capitalize() for word in re.split(r'[-_]', title_without_ext))

        # Get current date
        current_date = datetime.now().strftime('%Y-%m-%d')

        # --- Automatic Tag and Category Detection ---
        found_tags = []
        for tag in PREDEFINED_TAGS:
            # Use regex for whole word, case-insensitive matching
            if re.search(r'\b' + re.escape(tag) + r'\b', content, re.IGNORECASE):
                found_tags.append(f'"{tag}"') # Add quotes for TOML array format

        found_categories = []
        for category in PREDEFINED_CATEGORIES:
            if re.search(r'\b' + re.escape(category) + r'\b', content, re.IGNORECASE):
                found_categories.append(f'"{category}"') # Add quotes for TOML array format

        # Format lists for TOML
        tags_str = f"[{', '.join(found_tags)}]" if found_tags else "[]"
        categories_str = f"[{', '.join(found_categories)}]" if found_categories else "[]"
        # --- End Automatic Detection ---

        # Construct default front matter
        front_matter = f"""+++
title = "{title}"
date = {current_date}
template = "page.html"
[taxonomies]
tags = {tags_str}
categories = {categories_str}
+++

"""
        f.seek(0)  # Go to the beginning of the file
        f.write(front_matter + content)
    print(f"Added default front matter to '{filepath}'.")

def process_blog_directory(blog_dir):
    """
    Processes all Markdown files in the given blog directory.
    """
    print(f"Scanning directory: {blog_dir}")
    for root, _, files in os.walk(blog_dir):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                add_default_front_matter(filepath)

if __name__ == "__main__":
    blog_content_directory = "/Users/minijohn/Documents/github-repo/rustblog/content/blog/"

    if not os.path.isdir(blog_content_directory):
        print(f"Error: Directory '{blog_content_directory}' not found.")
        print("Please update 'blog_content_directory' in the script to the correct path.")
    else:
        process_blog_directory(blog_content_directory)