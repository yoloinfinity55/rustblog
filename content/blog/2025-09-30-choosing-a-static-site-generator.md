+++
title = "Why We Chose a Static Site Generator for Our New Website"
date = 2025-09-30
[taxonomies]
tags = ["tech", "zola", "jamstack", "web-development"]
categories = ["blog"]
+++

Hello, friends! We're excited to announce that we're planning to build a new website for Integracy. Before diving into development, we established a few key conditions for what we wanted to achieve.

### Our Core Requirements

Our primary goals for the new website were:
1.  **Speed:** The website needed to be exceptionally fast, with pages loading almost instantly. The best way to achieve this is by serving static pages, eliminating any server-side processing for each request.
2.  **Hosting Cost:** The hosting costs should be minimal, ideally close to zero.
3.  **Customization:** We needed the flexibility to easily customize any part of the site's appearance and functionality.
4.  **Easy Content Management:** We wanted to add new content without writing any HTML or CSS code.

### Evaluating Our Options

With these conditions in mind, we considered two main approaches.

#### 1. Traditional Web Technologies

Our first thought was to use traditional web technologies like WordPress or Django. In these systems, when you visit a URL (e.g., `www.xyz.com`), your request hits a web server. The server then processes the request, generates an HTML page on the fly, and sends it back to your browser.

However, this approach doesn't align with our goals. The on-the-fly processing inherently slows down the site and means it isn't purely static. This also necessitates a web server for hosting, which introduces costs that we wanted to avoid.

#### 2. Static Site Generators (Jamstack)

This led us to our second option: a static site generator (SSG) based on the Jamstack architecture. In a Jamstack setup, all the pages are pre-rendered into static HTML files during a build process. When a user requests a page, the pre-built file is served directly, often from a Content Delivery Network (CDN).

This approach perfectly matches our conditions:
-   **Fast:** Serving static pages is incredibly fast since there's no on-demand processing.
-   **Secure:** With no server-side processing on request, the attack surface is significantly reduced compared to traditional technologies.
-   **Cost-Effective:** Static sites can be hosted for free on platforms like GitHub Pages, GitLab Pages, and Netlify.
-   **Scalable:** Static assets are easy to scale. You can distribute them across a global CDN to ensure fast loading times for users anywhere in the world.
-   **Simple Content Creation:** SSGs typically use Markdown as an input for creating new content, which satisfies our requirement of not needing to write HTML.

### Why Zola?

After deciding to use a static site generator, we had to choose which one. While there are many popular options like Hugo, Gatsby, and VuePress, we decided to go with **Zola** for a few key reasons:

-   **Simplicity:** Zola is a single executable file. There's no complex installation process; you just download the binary and run it.
-   **Built-in Features:** It comes with powerful features out-of-the-box, such as syntax highlighting, shortcodes, and internal link management.
-   **Familiar Templating:** The main reason we chose Zola is its templating language, Tera, which is very similar to Jinja2 (used in Django and other Python applications). Since our team is familiar with Python and Jinja, it will be much easier for us to develop and customize the website.

### What's Next?

In our next post, we'll walk you through creating the website using a pre-built Zola theme. We'll show you how to add your own content using Markdown, customize the theme to your liking, and build your own site. If you follow along, you'll be able to create your own fast, modern, and easily updatable website.

Thank you for reading!
