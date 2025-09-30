Specification: RustBlog - Minimalist Markdown Blog with Zola and Tailwind CSS (Updated)

  1. Project Overview
   - Name: RustBlog
   - Objective: Build a minimalist static blog using Zola and Tailwind CSS on a Mac mini M1, deployed to GitHub Pages.
   - Platform: macOS (M1, ARM64, Ventura/Sonoma+)
   - Deployment: GitHub Pages
   - Features:
     - Responsive, minimalist blog with dynamic homepage (latest posts), blog index, and post pages.
     - Markdown content with syntax highlighting.
     - Tags and categories with dedicated pages.
     - Tailwind CSS with a clean, monochromatic design, flexible theming via CSS variables, and an improved dark mode 
       toggle.
     - Automated deployment via GitHub Actions.
     - Automated front matter generation for new posts.

  2. Requirements
   - Hardware: Mac mini M1 (macOS Ventura/Sonoma+)
   - Software:
     - Zola (v0.19.1+, ARM64)
     - Node.js (v18+, ARM64), npm
     - Homebrew, Git
     - VS Code (or similar)
   - Dependencies:
     - Tailwind CSS, PostCSS, Autoprefixer, @tailwindcss/typography
     - Alpine.js (via CDN for dark mode and mobile menu)
     - GitHub repository

  3. Project Setup
   1. Install Dependencies:

    1     # Install Homebrew (if not installed)
    2     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    3 
    4     # Install Node.js
    5     brew install node
    6 
    7     # Install Zola (v0.19.1, ARM64)
    8     curl -L https://github.com/getzola/zola/releases/download/v0.19.1/zola-v0.19.1-aarch64-apple-darwin.tar.gz
      | tar -xz
    9     chmod +x zola
   10     sudo mv zola /usr/local/bin/
   11 
   12     # Install Git
   13     brew install git
   2. Initialize Project:

    1     # Create and enter project directory
    2     mkdir rustblog && cd rustblog
    3 
    4     # Initialize Zola in the current directory
    5     zola init .
    6     # Set base_url to http://localhost:1111 when prompted
    7 
    8     # Initialize Node.js and install Tailwind CSS
    9     npm init -y
   10     npm install -D tailwindcss postcss autoprefixer @tailwindcss/typography
   11     npx tailwindcss init -p

  4. File Structure

    1 rustblog/
    2 ├── .github/workflows/deploy.yml
    3 ├── config.toml
    4 ├── content/
    5 │   ├── _index.md
    6 │   └── blog/
    7 │       ├── _index.md
    8 │       ├── first-post.md
    9 │       ├── second-post.md
   10 │       ├── third-post.md
   11 │       ├── Directory-Structure.md  # Added during development
   12 │       ├── analysis.md             # Added during development
   13 │       └── ... (other posts)
   14 ├── static/css/
   15 │   ├── tailwind.css
   16 │   ├── theme.css                   # Empty, but present
   17 │   └── output.css                  # Generated
   18 ├── templates/
   19 │   ├── base.html
   20 │   ├── index.html
   21 │   ├── blog.html                   # Renamed from blog_index.html
   22 │   ├── blog-page.html              # Added for individual blog post rendering
   23 │   ├── page.html
   24 │   ├── taxonomy.html
   25 │   └── taxonomies.html
   26 ├── package.json
   27 ├── postcss.config.js
   28 ├── tailwind.config.js
   29 ├── add_frontmatter.py              # Custom script for front matter automation
   30 └── .gitignore

  Create Structure:

   1 mkdir -p .github/workflows content/blog static/css templates
   2 touch .github/workflows/deploy.yml config.toml
   3 touch content/_index.md content/blog/_index.md content/blog/first-post.md content/blog/second-post.md 
     content/blog/third-post.md
   4 touch static/css/tailwind.css static/css/theme.css static/css/output.css
   5 touch templates/base.html templates/index.html templates/blog.html templates/blog-page.html
   6 touch templates/page.html templates/taxonomy.html templates/taxonomies.html
   7 touch .gitignore postcss.config.js

  5. Configuration
   - config.toml:

    1     title = "RustBlog"
    2     base_url = "http://localhost:1111"
    3     description = "A minimalist blog with Zola and Tailwind CSS"
    4     default_language = "en"
    5 
    6     [taxonomies]
    7     tags = ["tags"]
    8     categories = ["categories"]
    9 
   10     [markdown]
   11     highlight_code = true
   - tailwind.config.js:

    1     /** @type {import('tailwindcss').Config} */
    2     module.exports = {
    3       content: [
    4         './templates/**/*.{html,md}',
    5         './content/**/*.{html,md}',
    6       ],
    7       darkMode: 'class',
    8       theme: {
    9         extend: {
   10           colors: {
   11             // Colors now defined via CSS variables for flexible theming
   12             accent: 'var(--color-accent)',
   13             bg: 'var(--color-bg)',
   14             text: 'var(--color-text)',
   15             darkBg: 'var(--color-bg)',   // Uses same variable as bg, actual dark mode color from CSS var
   16             darkText: 'var(--color-text)', // Uses same variable as text, actual dark mode color from CSS var
   17           },
   18           typography: ({ theme }) => ({
   19             DEFAULT: {
   20               css: {
   21                 // Typography styles use Tailwind's CSS variables for better theming
   22                 '--tw-prose-body': theme('colors.text'),
   23                 '--tw-prose-headings': theme('colors.text'),
   24                 '--tw-prose-links': theme('colors.accent'),
   25                 '--tw-prose-bold': theme('colors.text'),
   26                 '--tw-prose-code': theme('colors.text'),
   27                 '--tw-prose-quote': theme('colors.text'),
   28                 '--tw-prose-pre-bg': theme('colors.gray.100'),
   29                 '--tw-prose-pre-code': theme('colors.text'),
   30                 'a': {
   31                   'text-decoration': 'none',
   32                   'font-weight': '500',
   33                   '&:hover': {
   34                     'text-decoration': 'underline',
   35                   },
   36                 },
   37                 'code': {
   38                   'background-color': theme('colors.gray.100'),
   39                   'padding': '0.2em 0.4em',
   40                   'border-radius': '0.25em',
   41                 },
   42                 'pre': {
   43                   'padding': '1rem',
   44                   'border-radius': '0.25rem',
   45                 },
   46               },
   47             },
   48             dark: {
   49               css: {
   50                 // Dark mode typography styles
   51                 '--tw-prose-body': theme('colors.darkText'),
   52                 '--tw-prose-headings': theme('colors.darkText'),
   53                 '--tw-prose-links': theme('colors.accent'),
   54                 '--tw-prose-bold': theme('colors.darkText'),
   55                 '--tw-prose-code': theme('colors.darkText'),
   56                 '--tw-prose-quote': theme('colors.darkText'),
   57                 '--tw-prose-pre-bg': theme('colors.gray.700'),
   58                 '--tw-prose-pre-code': theme('colors.darkText'),
   59                 'code': {
   60                   'background-color': theme('colors.gray.700'),
   61                 },
   62               },
   63             },
   64           }),
   65           fontFamily: {
   66             sans: ['Inter', 'ui-sans-serif', 'system-ui', '-apple-system', 'sans-serif'],
   67           },
   68         },
   69       },
   70       plugins: [require('@tailwindcss/typography')],
   71     }
   - package.json:

    1     {
    2       "name": "rustblog",
    3       "version": "1.0.0",
    4       "description": "A minimalist blog with Zola and Tailwind CSS",
    5       "main": "index.js",
    6       "scripts": {
    7         "build:css": "tailwindcss -i ./static/css/tailwind.css -o ./static/css/output.css --minify",
    8         "watch:css": "tailwindcss -i ./static/css/tailwind.css -o ./static/css/output.css --watch",
    9         "build": "npm run build:css && zola build"
   10       },
   11       "keywords": [],
   12       "author": "",
   13       "license": "ISC",
   14       "devDependencies": {
   15         "@tailwindcss/typography": "^0.5.10",
   16         "autoprefixer": "^10.4.20",
   17         "postcss": "^8.4.47",
   18         "tailwindcss": "^3.4.13"
   19       }
   20     }
   - postcss.config.js:

   1     module.exports = {
   2       plugins: {
   3         tailwindcss: {},
   4         autoprefixer: {},
   5       }
   6     }
   - static/css/tailwind.css:

    1     :root {
    2       --color-bg: #ffffff;
    3       --color-text: #1f2a44;
    4       --color-accent: #1e40af;
    5       --color-gray-100: #f3f4f6;
    6       --color-gray-700: #374151;
    7       --color-gray-200: #e5e7eb;
    8     }
    9 
   10     [data-theme='dark'] {
   11       --color-bg: #1a202c;
   12       --color-text: #e2e8f0;
   13       --color-accent: #90cdf4;
   14       --color-gray-100: #2d3748;
   15       --color-gray-700: #a0aec0;
   16       --color-gray-200: #4a5568;
   17     }
   18 
   19     @tailwind base;
   20     @tailwind components;
   21     @tailwind utilities;
   - static/css/theme.css: (Empty, but present)
   - .gitignore:
   1     node_modules/
   2     public/
   3     static/css/output.css

  6. Content and Templates
   1. Homepage (`content/_index.md`):
   1     +++
   2     title = "Welcome to RustBlog"
   3     template = "index.html"
   4     +++
   5     # Welcome
   6     Check out the [blog](/blog)!
   2. Blog Section (`content/blog/_index.md`):

   1     +++
   2     title = "Blog"
   3     template = "blog.html"         # Updated template name
   4     sort_by = "date"
   5     page_template = "blog-page.html" # Added for individual post rendering within blog section
   6     +++
   3. Sample Posts (`content/blog/first-post.md`, `second-post.md`, `third-post.md`, etc.):

   1     +++
   2     title = "My First Blog Post"
   3     date = 2025-09-30
   4     [taxonomies]
   5     tags = ["tech", "rust"]
   6     categories = ["blog"]
   7     +++
   8     # Welcome
   9     Sample post.
      print("Hello, Zola!")
   1 
      (Similar structure for other posts, with content-specific tags/categories)
   1 4.  **Templates**:
   2     -   **`templates/base.html`**:
          <!DOCTYPE html>
          <html lang="en" class="light" x-data="{ darkMode: false, menuOpen: false }" x-init="if (localStorage.theme === 
  'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) { 
  document.documentElement.classList.add('dark'); darkMode = true; } else { localStorage.theme = 'light'; }">
          <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{{ config.title }} | {% block title %}{% endblock %}</title>
            <link rel="stylesheet" href="{{ get_url(path='css/output.css') }}">
            <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
          </head>
          <body class="bg-bg dark:bg-darkBg text-text dark:text-darkText min-h-screen flex flex-col font-sans">
            <header class="border-b border-gray-200 dark:border-gray-700 sticky top-0 z-50 bg-bg/80 dark:bg-darkBg/80 
  backdrop-blur-sm">
              <nav class="container mx-auto px-6 py-4 flex justify-between items-center">
                <a href="{{ get_url(path='/') }}" class="text-2xl font-semibold text-text dark:text-darkText 
  hover:text-accent transition-colors">{{ config.title }}</a>
                <div class="hidden md:flex items-center space-x-8">
                  <a href="{{ get_url(path='/') }}" class="hover:text-accent transition-colors">Home</a>
                  <a href="{{ get_url(path='blog') }}" class="hover:text-accent transition-colors">Blog</a>
                  <a href="{{ get_url(path='tags') }}" class="hover:text-accent transition-colors">Tags</a>
                  <button @click="darkMode = !darkMode; localStorage.theme = darkMode ? 'dark' : 'light'; 
  document.documentElement.classList.toggle('dark')" class="text-text dark:text-darkText hover:text-accent 
  transition-colors text-xl">
                    <span x-show="!darkMode">🌙</span>
                    <span x-show="darkMode">☀️</span>
                  </button>
                </div>
                <div class="md:hidden flex items-center">
                  <button @click="darkMode = !darkMode; localStorage.theme = darkMode ? 'dark' : 'light'; 
  document.documentElement.classList.toggle('dark')" class="text-text dark:text-darkText hover:text-accent 
  transition-colors text-xl mr-4">
                    <span x-show="!darkMode">🌙</span>
                    <span x-show="darkMode">☀️</span>
                  </button>
                  <button @click="menuOpen = !menuOpen" class="text-text dark:text-darkText hover:text-accent">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path x-show="!menuOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 
  6h16M4 12h16m-7 6h7"></path>
                      <path x-show="menuOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 
  6M6 6l12 12"></path>
                    </svg>
                  </button>
                </div>
              </nav>
              <div x-show="menuOpen" x-transition:enter="transition ease-out duration-200" 
  x-transition:enter-start="opacity-0 -translate-y-2" x-transition:enter-end="opacity-100 translate-y-0" 
  x-transition:leave="transition ease-in duration-150" x-transition:leave-start="opacity-100 translate-y-0" 
  x-transition:leave-end="opacity-0 -translate-y-2" class="md:hidden border-t border-gray-200 dark:border-gray-700 px-6 
  py-4 absolute w-full bg-bg dark:bg-darkBg shadow-lg">
                <a href="{{ get_url(path='/') }}" class="block py-2 hover:text-accent transition-colors">Home</a>
                <a href="{{ get_url(path='blog') }}" class="block py-2 hover:text-accent transition-colors">Blog</a>
                <a href="{{ get_url(path='tags') }}" class="block py-2 hover:text-accent transition-colors">Tags</a>
              </div>
            </header>
            <main class="container mx-auto px-6 py-12 flex-grow">
              {% block content %}{% endblock %}
            </main>
            <footer class="border-t border-gray-200 dark:border-gray-700 text-center py-6 text-sm text-gray-500 
  dark:text-gray-400">
              <p>&copy; {{ now() | date(format="%Y") }} {{ config.title }}</p>
            </footer>
          </body>
          </html>

   1     -   **`templates/index.html`**:
          {% extends "base.html" %}

          {% block content %}
          <h1 class="text-3xl font-bold mb-8">Latest Posts</h1>

          {% set blog_section = get_section(path="blog/_index.md") %}
          {% set posts = blog_section.pages %}

          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
            {% for post in posts %}
            <a href="{{ post.permalink }}" class="block bg-gray-100 dark:bg-gray-800 rounded-xl shadow-md overflow-hidden 
  hover:shadow-lg transition-shadow duration-200">
              <div class="p-6">
                <h2 class="text-xl font-semibold mb-2 text-text dark:text-text">{{ post.title }}</h2>
                {% if post.description %}
                  <p class="text-gray-700 dark:text-gray-300">{{ post.description }}</p>
                {% else %}
                  <p class="text-gray-700 dark:text-gray-300">{{ post.summary | safe }}</p>
                {% endif %}
              </div>
              <div class="px-6 pb-4">
                <span class="text-sm text-gray-500 dark:text-gray-400">{{ post.date | date(format="%b %d, %Y") }}</span>
              </div>
            </a>
            {% endfor %}
          </div>
          {% endblock %}

   1     -   **`templates/blog.html`**: (Content matches original `blog_index.html` from spec)
          {% extends "base.html" %}
          {% block title %}{{ section.title }}{% endblock %}
          {% block content %}
            <h1 class="text-2xl md:text-3xl font-semibold text-text dark:text-darkText mb-8">{{ section.title }}</h1>
            <div class="space-y-8">
              {% for post in section.pages %}
                <article class="border-b border-gray-200 dark:border-gray-700 pb-6">
                  <a href="{{ post.permalink }}" class="text-xl font-medium text-accent hover:underline">{{ post.title 
  }}</a>
                  <p class="text-sm text-gray-500 dark:text-gray-400 mt-1">{{ post.date | date(format="%B %d, %Y") }}</p>
                  <p class="mt-2 text-gray-700 dark:text-gray-300">{{ post.summary | safe }}</p>
                </article>
              {% endfor %}
            </div>
          {% endblock %}

   1     -   **`templates/blog-page.html`**: (New template, content not explicitly provided but implied for 
     individual post rendering)
   2         *   *Note: This template is referenced in `content/blog/_index.md` but its content was not explicitly 
     provided in the initial spec or read. It's assumed to be a standard page template for blog posts.*
   3     -   **`templates/page.html`**:
          {% extends "base.html" %}
          {% block title %}{{ page.title }}{% endblock %}
          {% block content %}
            <article class="prose max-w-3xl mx-auto">
              <h1 class="text-2xl md:text-3xl font-semibold text-text mb-4">{{ page.title }}</h1>
              <p class="text-sm text-gray-500 mb-6">{{ page.date | date(format="%B %d, %Y") }}</p>
              {{ page.content | safe }}
              {% if page.taxonomies.tags %}
                <div class="mt-8 text-sm">
                  <span class="text-gray-500">Tags:</span>
                  {% for tag in page.taxonomies.tags %}
                    <a href="/tags/{{ tag }}" class="text-accent hover:underline">{{ tag }}</a>{% if not loop.last %}, {% 
  endif %}
                  {% endfor %}
                </div>
              {% endif %}
            </article>
          {% endblock %}
   1     -   **`templates/taxonomies.html`**:
          {% extends "base.html" %}
          {% block title %}Tags{% endblock %}
          {% block content %}
            <h1 class="text-2xl md:text-3xl font-semibold text-text mb-8">Tags</h1>
            <ul class="space-y-2 max-w-3xl">
              {% for term in config.taxonomies.tags %}
                <li>
                  <a href="/{{ term.name }}" class="text-accent hover:underline">{{ term.name | capitalize }}</a>
                  <span class="text-gray-500">({{ term.pages | length }})</span>
                </li>
              {% endfor %}
            </ul>
          {% endblock %}

   1     -   **`templates/taxonomy.html`**: (Content matches original `taxonomy.html` from spec)
          {% extends "base.html" %}
          {% block title %}{{ term.name | capitalize }}{% endblock %}
          {% block content %}
            <h1 class="text-2xl md:text-3xl font-semibold text-text mb-8">{{ term.name | capitalize }}</h1>
            <div class="space-y-8 max-w-3xl">
              {% for page in term.pages %}
                <article class="border-b border-gray-200 dark:border-gray-700 pb-6">
                  <a href="{{ page.permalink }}" class="text-xl font-medium text-accent hover:underline">{{ page.title 
  }}</a>
                  <p class="text-sm text-gray-500 dark:text-gray-400 mt-1">{{ page.date | date(format="%B %d, %Y") }}</p>
                </article>
              {% endfor %}
            </div>
          {% endblock %}

   1 
   2 ## 7. Development
   3 -   **Local Server**:
      cd rustblog
      zola serve  # Runs at http://localhost:1111
   1 -   **Watch CSS**:
      npm run watch:css  # In a new terminal
   1 -   **Build**:
      npm run build  # Outputs to public/
   1 -   **Automate Front Matter**:
      python3 add_frontmatter.py # Runs the custom script to add/update front matter
   1 
   2 ## 8. Deployment
   3 1.  **Git Setup**:
      cd rustblog
      git init
      git add .
      git commit -m "Initial commit"
      git remote add origin https://github.com/yoloinfinity55/rustblog.git
      git push -u origin main

   1 2.  **GitHub Actions (`rustblog/.github/workflows/deploy.yml`)**:
      name: Deploy to GitHub Pages
      on:
        push:
          branches: [main]
      jobs:
        build-and-deploy:
          runs-on: ubuntu-latest
          steps:
             - uses: actions/checkout@v3
             - name: Install Zola
              run: |
                curl -L 
  https://github.com/getzola/zola/releases/download/v0.19.1/zola-v0.19.1-x86_64-unknown-linux-gnu.tar.gz | tar -xz
                sudo mv zola /usr/local/bin/
             - name: Setup Node.js
              uses: actions/setup-node@v3
              with:
                node-version: '18'
             - name: Install npm dependencies
              run: npm install
             - name: Build CSS
              run: npm run build:css
             - name: Build Zola site
              run: zola build
             - uses: peaceiris/actions-gh-pages@v3
              with:
                github_token: ${{ secrets.GITHUB_TOKEN }}
                publish_dir: ./public
   1 3.  **Configure GitHub Pages**:
   2     -   Update `config.toml`:
          base_url = "https://yoloinfinity55.github.io/rustblog"
   1     -   Go to GitHub repository Settings > Pages > Source: `gh-pages` branch.
   2     -   Commit and push:
          git add .
          git commit -m "Update for deployment"
          git push
    1 
    2 ## 9. Features
    3 -   **Minimalist Design**: Monochromatic palette (grays, `#1E40AF` accent), `Inter` font, ample whitespace, no
      shadows, subtle dividers. Flexible theming via CSS variables.
    4 -   **Responsive**: Mobile-friendly navbar with animated hamburger menu, content limited to `max-w-3xl`.
    5 -   **Dark Mode**: Toggled via emoji button (🌙/☀️), persistswith localStorage. Improved initialization and 
      centralized styling.
    6 -   **Markdown Styling**: `@tailwindcss/typography` with simplified prose styles, configured using Tailwind's 
      CSS variables.
    7 -   **Syntax Highlighting**: Enabled via Zola’s `highlight_code = true`.
    8 -   **Navigation**: Text-only links (Home, Blog, Tags), no decorative buttons.
    9 -   **Taxonomies**: Tags and categories with dedicated pages.
   10 -   **Automated Front Matter**: Custom Python script (`add_frontmatter.py`) to automatically generate default 
      front matter for new Markdown files, including title from filename, current date, and content-based 
      tag/category detection.
   11 
   12 ## 10. Testing
   13 -   **Local**: Verify at `http://localhost:1111` for:
   14     -   Dynamic homepage displaying latest posts.
   15     -   Blog index, post pages, and tag pages.
   16     -   Responsiveness (mobile, tablet, desktop).
   17     -   Dark mode toggle and syntax highlighting.
   18     -   Correct front matter application by `add_frontmatter.py`.
   19 -   **Production**: Check at `https://yoloinfinity55.github.io/rustblog` for:
   20     -   Correct asset loading (CSS, Alpine.js).
   21     -   Functional links and taxonomy pages.
   22 
   23 ## 11. Maintenance
   24 -   **Add Posts**: Create new `.md` files in `content/blog/`, then run `python3 add_frontmatter.py` to 
      generate front matter.
   25 -   **Update Styles**: Modify `static/css/tailwind.css` or `tailwind.config.js`.
   26 -   **Update Dependencies**: Run `brew upgrade` and `npm update`.
   27 -   **Update Front Matter Script**: Modify `add_frontmatter.py` to adjust predefined tags/categories or logic.
   28 
   29 ## 12. Troubleshooting
   30 -   **Zola**: Use ARM64 binary (`aarch64-apple-darwin`). Check `config.toml` for correct `base_url`.
   31 -   **Tailwind**: Verify `tailwind.config.js` paths, run `npm run build:css` if styles fail.
   32 -   **GitHub Pages**: Check Actions logs, ensure `publish_dir` is `./public` and `base_url` matches GitHub 
      Pages URL.
   33 -   **Dark Mode**: Ensure Alpine.js CDN is accessible, check localStorage in browser dev tools.
   34 -   **Front Matter Script**: Ensure `blog_content_directory` is correct in `add_frontmatter.py`.
   35 
   36 ## 13. Deliverables
   37 -   Static blog hosted at `https://yoloinfinity55.github.io/rustblog`.
   38 -   GitHub repository: `rustblog`.
   39 -   Minimalist, responsive blog with sample content, tags, and categories.
   40 -   Automated deployment pipeline via GitHub Actions.
   41 -   Custom Python script for automated front matter generation.
   42 
   43 ## 14. Timeline
   44 -   **Day 1**: Setup dependencies, initialize project, create templates and content.
   45 -   **Day 2**: Test locally, set up Git and GitHub Actions. Implement automated front matter script.
   46 -   **Day 3**: Deploy to GitHub Pages, validate production site.
   47 
   48 ## 15. Resources
   49 -   [Zola Docs](https://www.getzola.org/documentation/)
   50 -   [Tailwind CSS Docs](https://tailwindcss.com/docs)
   51 -   [GitHub Pages](https://docs.github.com/en/pages)
   52 -   [Alpine.js Docs](https://alpinejs.dev/)
   53 -   [Inter Font](https://rsms.me/inter/)
   54 
   55 ## 16. Key Updates from Previous Specification
   56 -   **Folder Structure**: Used `zola init .` for a flat structure. Added `add_frontmatter.py` script. Noted 
      `theme.css` is present but empty.
   57 -   **Minimalist Design**: Implemented a monochromatic palette, `Inter` font, increased whitespace, removed 
      shadows and decorative buttons, and used subtle dividers. **Colors are now managed via CSS variables for 
      enhanced flexibility.**
   58 -   **Paths**: Ensured `tailwind.config.js`, `package.json`, and `deploy.yml` use correct paths (`static/`).
   59 -   **Templates**:
   60     -   Enhanced `base.html` with improved dark mode initialization, more polished header styling (sticky, 
      transparent, backdrop-blur), and a more interactive mobile menu with animated SVG paths and Alpine.js 
      transitions.
   61     -   `index.html` was significantly updated to dynamically fetch and display the latest blog posts in a 
      grid layout, making it a dynamic blog feed rather than static content.
   62     -   `content/blog/_index.md` now references `template = "blog.html"` and `page_template = "blog-page.html"
      `, indicating a more refined templating strategy for blog sections.
   63     -   `templates/blog_index.html` was renamed to `templates/blog.html`.
   64     -   `templates/page.html` and `templates/taxonomies.html` were simplified by removing explicit dark mode 
      classes, centralizing dark mode handling.
   65 -   **Content**: Added `second-post.md`, `third-post.md`, `Directory-Structure.md`, and `analysis.md` with 
      proper code block delimiters and front matter.
   66 -   **Configuration**: Corrected `config.toml` taxonomies syntax and `base_url` for local development. 
      `tailwind.config.js` now uses CSS variables for color definitions and the updated Tailwind CSS v3 typography 
      configuration.
   67 -   **Automated Front Matter**: A new Python script (`add_frontmatter.py`) was introduced to automate the 
      generation of default front matter for new Markdown files, including title extraction, date stamping, and 
      rule-based tag/category detection from content.
   68 
   69 ---
