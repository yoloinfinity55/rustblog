import re
import os
import requests
from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai  # Gemini lib
from datetime import datetime

# Config - Use your existing Gemini key
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY') # or "your_gemini_key_here"  # Export: export GEMINI_API_KEY='AIza...'
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

PROJECT_DIR = '.'  # RustBlog root

def get_video_id(url):
    match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11}).*', url)
    return match.group(1) if match else None

def fetch_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return ' '.join([entry['text'] for entry in transcript])
    except:
        return "Transcript unavailable—fall back to manual summary."

def download_thumbnail(video_id, save_dir='static/thumbnails'):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
    response = requests.get(url)
    if response.status_code == 200:
        filename = f"youtube-{video_id}.jpg"
        filepath = os.path.join(PROJECT_DIR, save_dir, filename)
        with open(filepath, 'wb') as f:
            f.write(response.content)
        return f"/thumbnails/{filename}"
    return None

def generate_blog(transcript, title, image_path, video_id):
    prompt = f"""
    Generate a 800-word SEO-optimized Markdown blog from this YouTube transcript (test post in RustBlog).
    Title: {title}
    Structure: Intro, 2 H2 sections, conclusion.
    Keywords: Rust programming, YouTube tutorial.
    Start with YAML frontmatter: title='{title}' date='{datetime.now().strftime('%Y-%m-%d')}' slug='test-youtube-{title.lower().replace(" ", "-")[:10]}' extra.image='{image_path}' tags=['Rust', 'AI'].
    Transcript: {transcript[:1500]}
    End with embed: <iframe src="https://www.youtube.com/embed/{video_id}"></iframe>
    """
    response = model.generate_content(prompt)
    return response.text

def save_and_commit(md_content, slug):
    filepath = os.path.join(PROJECT_DIR, 'content/blog', f"{slug}.md")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(md_content)
    # Polish with your repo's frontmatter script
    os.system("python3 add_frontmatter.py")
    os.system(f"git add {filepath} && git commit -m 'Test: Added YouTube post with Gemini {slug}'")
    print(f"Post created: {filepath}. Run 'git push' to deploy.")

# Test Run
if __name__ == "__main__":
    url = input("Paste YouTube URL for test: ")
    video_id = get_video_id(url)
    if not video_id:
        print("Invalid URL")
        exit()
    
    print("1. Fetching transcript...")
    transcript = fetch_transcript(video_id)
    
    print("2. Downloading thumbnail...")
    image_path = download_thumbnail(video_id)
    
    title = input("Enter post title (default: 'Rust Tutorial Test'): ") or "Rust Tutorial Test"
    
    print("3. Gemini generating post...")
    md_content = generate_blog(transcript, title, image_path or "", video_id)
    
    slug = f"test-youtube-{title.lower().replace(' ', '-')[:10]}"
    save_and_commit(md_content, slug)
    
    print("Test complete! Preview with 'zola serve'.")
