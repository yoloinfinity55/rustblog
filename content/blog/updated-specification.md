+++
title = "Updated Specification by python script"
date = 2025-10-01
[taxonomies]
tags = ["converted"]
categories = ["blog"]
+++

Specification: RustBlog - Minimalist Markdown Blog with Zola and Tailwind CSS (Updated)

## 1. Project Overview
- Name: RustBlog
- Objective: Build a minimalist static blog using Zola and Tailwind CSS on a Mac mini M1, deployed to GitHub Pages.
- Platform: macOS (M1, ARM64, Ventura/Sonoma+)
- Deployment: GitHub Pages
- Features:
    - Responsive, minimalist blog with dynamic homepage (latest posts), blog index, and post pages.
    - Markdown content with syntax highlighting.
    - Tags and categories with dedicated pages.
    - Tailwind CSS with a clean, monochromatic design, flexible theming via CSS variables, and an improved dark mode toggle.
    - Automated deployment via GitHub Actions.
    - Automated front matter generation for new posts.

## 2. Requirements
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

## 3. Project Setup
1.  **Install Dependencies**:
    ```bash
    # Install Homebrew (if not installed)
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

    # Install Node.js
    brew install node

    # Install Zola (v0.19.1, ARM64)
    curl -L https://github.com/getzola/zola/releases/download/v0.19.1/zola-v0.19.1-aarch64-apple-darwin.tar.gz | tar -xz
    chmod +x zola
    sudo mv zola /usr/local/bin/

    # Install Git
    brew install git
    ```
2.  **Initialize Project**:
    ```bash
    # Create and enter project directory
    mkdir rustblog && cd rustblog

    # Initialize Zola in the current directory
    zola init .
    # Set base_url to http://localhost:1111 when prompted

    # Initialize Node.js and install Tailwind CSS
    npm init -y
    npm install -D tailwindcss postcss autoprefixer @tailwindcss/typography
    npx tailwindcss init -p
    ```

## 4. File Structure
```
rustblog/
├── .github/workflows/deploy.yml
├── config.toml
├── content/
│   ├── _index.md
│   └── blog/
│       ├── _index.md
│       ├── first-post.md
│       ├── second-post.md
│       ├── third-post.md
│       ├── Directory-Structure.md
│       ├── analysis.md
│       └── ... (other posts)
├── static/css/
│   ├── tailwind.css
│   ├── theme.css
│   └── output.css
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── blog.html
│   ├── blog-page.html
│   ├── page.html
│   ├── taxonomy.html
│   └── taxonomies.html
├── package.json
├── postcss.config.js
├── tailwind.config.js
├── add_frontmatter.py
└── .gitignore
```

**Create Structure**:
```bash
mkdir -p .github/workflows content/blog static/css templates
touch .github/workflows/deploy.yml config.toml
touch content/_index.md content/blog/_index.md content/blog/first-post.md content/blog/second-post.md content/blog/third-post.md
touch static/css/tailwind.css static/css/theme.css static/css/output.css
touch templates/base.html templates/index.html templates/blog.html templates/blog-page.html
touch templates/page.html templates/taxonomy.html templates/taxonomies.html
touch .gitignore postcss.config.js
```

## 5. Configuration
-   **`config.toml`**:
    ```toml
    title = "RustBlog"
    base_url = "http://localhost:1111"
    description = "A minimalist blog with Zola and Tailwind CSS"
    default_language = "en"

    [taxonomies]
    tags = ["tags"]
    categories = ["categories"]

    [markdown]
    highlight_code = true
    ```
-   **`tailwind.config.js`**:
    ```javascript
    /** @type {import('tailwindcss').Config} */
    module.exports = {
      content: [
        './templates/**/*.{html,md}',
        './content/**/*.{html,md}',
      ],
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            accent: 'var(--color-accent)',
            bg: 'var(--color-bg)',
            text: 'var(--color-text)',
            darkBg: 'var(--color-bg)',
            darkText: 'var(--color-text)',
          },
          typography: ({ theme }) => ({
            DEFAULT: {
              css: {
                '--tw-prose-body': theme('colors.text'),
                '--tw-prose-headings': theme('colors.text'),
                '--tw-prose-links': theme('colors.accent'),
              },
            },
            dark: {
              css: {
                '--tw-prose-body': theme('colors.darkText'),
                '--tw-prose-headings': theme('colors.darkText'),
                '--tw-prose-links': theme('colors.accent'),
              },
            },
          }),
          fontFamily: {
            sans: ['Inter', 'ui-sans-serif', 'system-ui', '-apple-system', 'sans-serif'],
          },
        },
      },
      plugins: [require('@tailwindcss/typography')],
    }
    ```
-   **`package.json`**:
    ```json
    {
      "name": "rustblog",
      "version": "1.0.0",
      "description": "A minimalist blog with Zola and Tailwind CSS",
      "main": "index.js",
      "scripts": {
        "build:css": "tailwindcss -i ./static/css/tailwind.css -o ./static/css/output.css --minify",
        "watch:css": "tailwindcss -i ./static/css/tailwind.css -o ./static/css/output.css --watch",
        "build": "npm run build:css && zola build"
      },
      "devDependencies": {
        "@tailwindcss/typography": "^0.5.10",
        "autoprefixer": "^10.4.20",
        "postcss": "^8.4.47",
        "tailwindcss": "^3.4.13"
      }
    }
    ```
-   **`postcss.config.js`**:
    ```javascript
    module.exports = {
      plugins: {
        tailwindcss: {},
        autoprefixer: {},
      }
    }
    ```
-   **`static/css/tailwind.css`**:
    ```css
    :root {
      --color-bg: #ffffff;
      --color-text: #1f2a44;
      --color-accent: #1e40af;
      --color-gray-100: #f3f4f6;
      --color-gray-700: #374151;
      --color-gray-200: #e5e7eb;
    }

    [data-theme='dark'] {
      --color-bg: #1a202c;
      --color-text: #e2e8f0;
      --color-accent: #90cdf4;
      --color-gray-100: #2d3748;
      --color-gray-700: #a0aec0;
      --color-gray-200: #4a5568;
    }

    @tailwind base;
    @tailwind components;
    @tailwind utilities;
    ```
-   **`.gitignore`**:
    ```
    node_modules/
    public/
    static/css/output.css
    ```

## 6. Content and Templates
1.  **Homepage (`content/_index.md`)**:
    ```markdown
    +++
    title = "Welcome to RustBlog"
    template = "index.html"
    +++
    # Welcome
    Check out the [blog](/blog)!
    ```
2.  **Blog Section (`content/blog/_index.md`)**:
    ```toml
    +++
    title = "Blog"
    template = "blog.html"
    sort_by = "date"
    page_template = "blog-page.html"
    +++
    ```
3.  **Sample Posts (`content/blog/first-post.md`)**:
    ```markdown
    +++
    title = "My First Blog Post"
    date = 2025-09-30
    [taxonomies]
    tags = ["tech", "rust"]
    categories = ["blog"]
    +++
    # Welcome
    Sample post.
    ```
4.  **Templates**:
    -   **`templates/base.html`**:
        ```markdown
        <!DOCTYPE html>
        <html lang="en" class="light" x-data="{ darkMode: false, menuOpen: false }" x-init="if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) { document.documentElement.classList.add('dark'); darkMode = true; } else { localStorage.theme = 'light'; }">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>{{ config.title }} | {% block title %}{% endblock %}</title>
          <link rel="stylesheet" href="{{ get_url(path='css/output.css') }}">
          <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
        </head>
        <body class="bg-bg dark:bg-darkBg text-text dark:text-darkText min-h-screen flex flex-col font-sans">
          <header class="border-b border-gray-200 dark:border-gray-700 sticky top-0 z-50 bg-bg/80 dark:bg-darkBg/80 backdrop-blur-sm">
            <nav class="container mx-auto px-6 py-4 flex justify-between items-center">
              <a href="{{ get_url(path='/') }}" class="text-2xl font-semibold text-text dark:text-darkText hover:text-accent transition-colors">{{ config.title }}</a>
              <div class="hidden md:flex items-center space-x-8">
                <a href="{{ get_url(path='/') }}" class="hover:text-accent transition-colors">Home</a>
                <a href="{{ get_url(path='blog') }}" class="hover:text-accent transition-colors">Blog</a>
                <a href="{{ get_url(path='tags') }}" class="hover:text-accent transition-colors">Tags</a>
                <button @click="darkMode = !darkMode; localStorage.theme = darkMode ? 'dark' : 'light'; document.documentElement.classList.toggle('dark')" class="text-text dark:text-darkText hover:text-accent transition-colors text-xl">
                  <span x-show="!darkMode">🌙</span>
                  <span x-show="darkMode">☀️</span>
                </button>
              </div>
              <div class="md:hidden flex items-center">
                <button @click="darkMode = !darkMode; localStorage.theme = darkMode ? 'dark' : 'light'; document.documentElement.classList.toggle('dark')" class="text-text dark:text-darkText hover:text-accent transition-colors text-xl mr-4">
                  <span x-show="!darkMode">🌙</span>
                  <span x-show="darkMode">☀️</span>
                </button>
                <button @click="menuOpen = !menuOpen" class="text-text dark:text-darkText hover:text-accent">
                  <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path x-show="!menuOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path>
                    <path x-show="menuOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                  </svg>
                </button>
              </div>
            </nav>
            <div x-show="menuOpen" x-transition:enter="transition ease-out duration-200" x-transition:enter-start="opacity-0 -translate-y-2" x-transition:enter-end="opacity-100 translate-y-0" x-transition:leave="transition ease-in duration-150" x-transition:leave-start="opacity-100 translate-y-0" x-transition:leave-end="opacity-0 -translate-y-2" class="md:hidden border-t border-gray-200 dark:border-gray-700 px-6 py-4 absolute w-full bg-bg dark:bg-darkBg shadow-lg">
              <a href="{{ get_url(path='/') }}" class="block py-2 hover:text-accent transition-colors">Home</a>
              <a href="{{ get_url(path='blog') }}" class="block py-2 hover:text-accent transition-colors">Blog</a>
              <a href="{{ get_url(path='tags') }}" class="block py-2 hover:text-accent transition-colors">Tags</a>
            </div>
          </header>
          <main class="container mx-auto px-6 py-12 flex-grow">
            {% block content %}{% endblock %}
          </main>
          <footer class="border-t border-gray-200 dark:border-gray-700 text-center py-6 text-sm text-gray-500 dark:text-gray-400">
            <p>&copy; {{ now() | date(format="%Y") }} {{ config.title }}</p>
          </footer>
        </body>
        </html>
        ```
    -   **`templates/index.html`**:
        ```markdown
        {% extends "base.html" %}
        {% block content %}
        <h1 class="text-3xl font-bold mb-8">Latest Posts</h1>
        {% set blog_section = get_section(path="blog/_index.md") %}
        {% set posts = blog_section.pages %}
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
          {% for post in posts %}
          <a href="{{ post.permalink }}" class="block bg-gray-100 dark:bg-gray-800 rounded-xl shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-200">
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
        ```
    -   **`templates/blog.html`**:
        ```markdown
        {% extends "base.html" %}
        {% block title %}{{ section.title }}{% endblock %}
        {% block content %}
          <h1 class="text-2xl md:text-3xl font-semibold text-text dark:text-darkText mb-8">{{ section.title }}</h1>
          <div class="space-y-8">
            {% for post in section.pages %}
              <article class="border-b border-gray-200 dark:border-gray-700 pb-6">
                <a href="{{ post.permalink }}" class="text-xl font-medium text-accent hover:underline">{{ post.title }}</a>
                <p class="text-sm text-gray-500 dark:text-gray-400 mt-1">{{ post.date | date(format="%B %d, %Y") }}</p>
                <p class="mt-2 text-gray-700 dark:text-gray-300">{{ post.summary | safe }}</p>
              </article>
            {% endfor %}
          </div>
        {% endblock %}
        ```
    -   **`templates/page.html`**:
        ```markdown
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
                  <a href="/tags/{{ tag }}" class="text-accent hover:underline">{{ tag }}</a>{% if not loop.last %}, {% endif %}
                {% endfor %}
              </div>
            {% endif %}
          </article>
        {% endblock %}
        ```
    -   **`templates/taxonomies.html`**:
        ```markdown
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
        ```
    -   **`templates/taxonomy.html`**:
        ```markdown
        {% extends "base.html" %}
        {% block title %}{{ term.name | capitalize }}{% endblock %}
        {% block content %}
          <h1 class="text-2xl md:text-3xl font-semibold text-text mb-8">{{ term.name | capitalize }}</h1>
          <div class="space-y-8 max-w-3xl">
            {% for page in term.pages %}
              <article class="border-b border-gray-200 dark:border-gray-700 pb-6">
                <a href="{{ page.permalink }}" class="text-xl font-medium text-accent hover:underline">{{ page.title }}</a>
                <p class="text-sm text-gray-500 dark:text-gray-400 mt-1">{{ page.date | date(format="%B %d, %Y") }}</p>
              </article>
            {% endfor %}
          </div>
        {% endblock %}
        ```