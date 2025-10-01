import os
import datetime

def convert_txt_to_md():
    blog_dir = "content/blog/"
    
    # Ensure the blog directory exists
    if not os.path.exists(blog_dir):
        os.makedirs(blog_dir)

    txt_file_path = input("Enter the path to the .txt file you want to convert: ").strip()

    if not os.path.exists(txt_file_path):
        print(f"Error: File not found at {txt_file_path}")
        return

    if not txt_file_path.lower().endswith(".txt"):
        print("Error: The provided file is not a .txt file.")
        return

    try:
        with open(txt_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Extract filename without extension for title and new filename
    base_name = os.path.splitext(os.path.basename(txt_file_path))[0]
    
    # Format for Zola-compatible filename (kebab-case)
    md_filename = base_name.replace(" ", "-").lower() + ".md"
    md_file_path = os.path.join(blog_dir, md_filename)

    # Get today's date for front matter
    today = datetime.date.today().isoformat()

    # Generate front matter
    front_matter = f"""+++
title = "{base_name.replace('-', ' ').title()}"
date = {today}
[taxonomies]
tags = ["converted"]
categories = ["blog"]
+++

"""
    
    full_content = front_matter + content

    try:
        with open(md_file_path, 'w', encoding='utf-8') as f:
            f.write(full_content)
        print(f"Successfully converted '{txt_file_path}' to '{md_file_path}'")
    except Exception as e:
        print(f"Error writing Markdown file: {e}")

if __name__ == "__main__":
    convert_txt_to_md()
