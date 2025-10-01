## Project Overview

This is a minimalist static blog built with Zola and Tailwind CSS. The blog is deployed to GitHub Pages and features a responsive, monochromatic design with a dark mode toggle. Content is written in Markdown, and the site includes dynamic home and blog pages, as well as pages for tags and categories.

## Building and Running

### Prerequisites

- Zola (v0.19.1+)
- Node.js (v18+)
- npm

### Development

1.  **Install npm dependencies:**
    ```bash
    npm install
    ```

2.  **Start the Zola server:**
    ```bash
    zola serve
    ```
    The site will be available at `http://localhost:1111`.

3.  **Watch for CSS changes:**
    In a separate terminal, run the following command to watch for changes to the Tailwind CSS files and automatically rebuild the CSS:
    ```bash
    npm run watch:css
    ```

### Production Build

To build the site for production, run the following command:

```bash
npm run build
```

This will build the CSS and then build the Zola site. The output will be in the `public/` directory.

## Development Conventions

- **Content:** Blog posts are located in the `content/blog/` directory. Each post is a Markdown file with front matter for the title, date, tags, and categories.
- **Styling:** Styling is done with Tailwind CSS. The main CSS file is `static/css/tailwind.css`. The `tailwind.config.js` file is configured to use CSS variables for colors, allowing for flexible theming.
- **Templates:** The HTML templates are located in the `templates/` directory. The base template is `base.html`, and the other templates extend it.
- **Deployment:** The site is deployed to GitHub Pages via a GitHub Actions workflow defined in `.github/workflows/deploy.yml`.
- **Front Matter Automation:** A Python script, `add_frontmatter.py`, is available to automatically generate front matter for new blog posts.
