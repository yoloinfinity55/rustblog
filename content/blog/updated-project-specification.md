+++
title = "Updated RustBlog Project Specification"
date = 2025-10-03
[taxonomies]
tags = ["project", "specification", "updates"]
categories = ["documentation"]
+++
## Specification: RustBlog - Minimalist Markdown Blog with Zola and Tailwind CSS (Updated)

---

### 1. Project Overview
- **Name**: RustBlog
- **Objective**: Build a minimalist static blog using Zola and Tailwind CSS on a Mac mini M1, deployed to GitHub Pages.
- **Platform**: macOS (M1, ARM64, Ventura/Sonoma+)
- **Deployment**: GitHub Pages
- **Features**:
  - Responsive, minimalist blog with homepage, blog index, and post pages.
  - Markdown content with syntax highlighting.
  - Tags and categories with dedicated pages.
  - Tailwind CSS with a clean, monochromatic design and dark mode toggle.
  - Automated deployment via GitHub Actions.

### 2. Requirements
- **Hardware**: Mac mini M1 (macOS Ventura/Sonoma+)
- **Software**:
  - Zola (v0.19.1+, ARM64)
  - Node.js (v18+, ARM64), npm
  - Homebrew, Git
  - VS Code (or similar)
- **Dependencies**:
  - Tailwind CSS, PostCSS, Autoprefixer, `@tailwindcss/typography`
  - Alpine.js (via CDN for dark mode and mobile menu)
  - GitHub repository

### 3. Project Setup
1. **Install Dependencies**:
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

2. **Initialize Project**:
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

### 4. File Structure
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
│       └── third-post.md
├── static/css/
│   ├── tailwind.css
│   └── output.css
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── blog_index.html
│   ├── page.html
│   ├── taxonomy.html
│   └── taxonomies.html
├── package.json
├── postcss.config.js
├── tailwind.config.js
└── .gitignore
```

**Create Structure**:
```bash
mkdir -p .github/workflows content/blog static/css templates
touch .github/workflows/deploy.yml config.toml
touch content/_index.md content/blog/_index.md content/blog/first-post.md
touch content/blog/second-post.md content/blog/third-post.md
touch static/css/tailwind.css static/css/output.css
touch templates/base.html templates/index.html templates/blog_index.html
touch templates/page.html templates/taxonomy.html templates/taxonomies.html
touch .gitignore postcss.config.js
```

### 5. Configuration
- **config.toml**:
  ```toml
  title = "RustBlog"
  base_url = "https://yoloinfinity55.github.io/rustblog"
  description = "A minimalist blog with Zola and Tailwind CSS"
  default_language = "en"

  taxonomies = [
    {name = "tags", paginate_by = 5},
    {name = "categories", paginate_by = 5},
  ]

  [markdown]
  highlight_code = true
  ```

- **tailwind.config.js**:
  ```javascript
  module.exports = {
    content: ['./templates/**/*.{html,md}', './content/**/*.{html,md}'],
    darkMode: 'class',
    theme: {
      extend: {
        colors: {
          accent: '#1E40AF',
          bg: '#F7F7F7',
          text: '#1F2A44',
          darkBg: '#1F2A44',
          darkText: '#E5E7EB',
        },
        typography: (theme) => ({
          DEFAULT: {
            css: {
              color: theme('colors.text'),
              'a': { color: theme('colors.accent'), 'text-decoration': 'none', 'transition': 'color 0.2s', 'font-weight': '500' },
              'a:hover': { color: theme('colors.accent'), 'text-decoration': 'underline' },
              'h1, h2, h3, h4, h5, h6': { color: theme('colors.text'), 'font-weight': '600' },
              'code': { background: theme('colors.gray.100'), padding: '2px 4px', borderRadius: '2px', 'font-size': '0.9em' },
              'pre': { background: theme('colors.gray.100'), padding: '1rem', borderRadius: '4px' },
              'p': { margin: '1.5rem 0' },
            },
          },
          dark: {
            css: {
              color: theme('colors.darkText'),
              'a': { color: theme('colors.accent') },
              'a:hover': { color: theme('colors.accent'), 'text-decoration': 'underline' },
              'h1, h2, h3, h4, h5, h6': { color: theme('colors.darkText') },
              'code': { background: theme('colors.gray.700'), color: theme('colors.darkText') },
              'pre': { background: theme('colors.gray.700') },
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

- **package.json**:
  ```json
  {
    "scripts": {
      "build:css": "tailwindcss -i static/css/tailwind.css -o static/css/output.css --minify",
      "watch:css": "tailwindcss -i static/css/tailwind.css -o static/css/output.css --watch",
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

- **postcss.config.js**:
  ```javascript
  module.exports = {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    }
  }
  ```

- **static/css/tailwind.css**:
  ```css
  @tailwind base;
  @tailwind components;
  @tailwind utilities;
  ```

- **.gitignore**:
  ```
  node_modules/
  public/
  static/css/output.css
  ```

### 6. Content and Templates
1. **Homepage (`content/_index.md`)**:
   ```markdown
   +++
   title = "Welcome to RustBlog"
   template = "index.html"
   +++
   # Welcome
   Check out the [blog](blog)!
   ```

2. **Blog Section (`content/blog/_index.md`)**:
   ```markdown
   +++
   title = "Blog"
   template = "blog_index.html"
   sort_by = "date"
   +++
   ```

3. **Sample Post (`content/blog/first-post.md`)**:
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

   
   print("Hello, Zola!")
   
   ```

4. **Second Sample Post (`content/blog/second-post.md`)**:
   ```markdown
   +++
   title = "My Second Blog Post"
   date = 2025-10-01
   [taxonomies]
   tags = ["test", "blogging"]
   categories = ["updates"]
   +++
   # Another Post
   This is my second test blog post. It's great to be blogging!

   
   console.log("Hello from the second post!");
   ```
   

5. **Third Sample Post (`content/blog/third-post.md`)**:
   ```markdown
   +++
   title = "My Third Blog Post"
   date = 2025-10-02
   [taxonomies]
   tags = ["thoughts", "personal"]
   categories = ["reflections"]
   +++
   # Third Time's the Charm
   This is my third blog post. Hopefully, this one deploys smoothly!

   
   fn main() {
       println!("Hello, third post!");
   }
   
   ```

6. **Templates**:
   - **`templates/base.html`**:
     <pre>
     ```
     <code class="language-html">
     &lt;!DOCTYPE html&gt;
     &lt;html lang="en" class="light" x-data="&lcub; darkMode: false, menuOpen: false &rcub;" x-init="if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) { document.documentElement.classList.add('dark'); darkMode = true; }"&gt;
     &lt;head&gt;
       &lt;meta charset="UTF-8"&gt;
       &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
       &lt;title&gt;&lcub;&lcub; config.title &rcub;&rcub; | &lcub;% block title %&rcub;&lcub;% endblock %&rcub;&lt;/title&gt;
       &lt;link rel="stylesheet" href="&lcub;&lcub; get_url(path='css/output.css') &rcub;&rcub;"&gt;
       &lt;script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"&gt;&lt;/script&gt;
     &lt;/head&gt;
     &lt;body class="bg-bg dark:bg-darkBg text-text dark:text-darkText min-h-screen flex flex-col font-sans"&gt;
       &lt;header class="border-b border-gray-200 dark:border-gray-700 sticky top-0"&gt;
         &lt;nav class="container mx-auto px-6 py-4 flex justify-between items-center"&gt;
           &lt;a href="&lcub;&lcub; get_url(path='/') &rcub;&rcub;" class="text-2xl font-semibold"&gt;&lcub;&lcub; config.title &rcub;&rcub;&lt;/a&gt;
           &lt;div class="hidden md:flex items-center space-x-8"&gt;
             &lt;a href="&lcub;&lcub; get_url(path='/') &rcub;&rcub;" class="hover:text-accent transition-colors"&gt;Home&lt;/a&gt;
             &lt;a href="&lcub;&lcub; get_url(path='blog') &rcub;&rcub;" class="hover:text-accent transition-colors"&gt;Blog&lt;/a&gt;
             &lt;a href="&lcub;&lcub; get_url(path='tags') &rcub;&rcub;" class="hover:text-accent transition-colors"&gt;Tags&lt;/a&gt;
             &lt;button @click="darkMode = !darkMode; localStorage.theme = darkMode ? 'dark' : 'light'; document.documentElement.classList.toggle('dark')" class="text-text dark:text-darkText hover:text-accent transition-colors"&gt;
               &lt;span x-show="!darkMode"&gt;🌙&lt;/span&gt;
               &lt;span x-show="darkMode"&gt;☀️&lt;/span&gt;
             &lt;/button&gt;
           &lt;/div&gt;
           &lt;div class="md:hidden"&gt;
             &lt;button @click="menuOpen = !menuOpen" class="text-text dark:text-darkText hover:text-accent"&gt;
               &lt;svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"&gt;
                 &lt;path :d="menuOpen ? 'M6 18L18 6M6 6l12 12' : 'M4 6h16M4 12h16m-7 6h7'" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"&gt;&lt;/path&gt;
               &lt;/svg&gt;
             &lt;/button&gt;
           &lt;/div&gt;
         &lt;/nav&gt;
         &lt;div x-show="menuOpen" class="md:hidden border-t border-gray-200 dark:border-gray-700 px-6 py-4"&gt;
           &lt;a href="&lcub;&lcub; get_url(path='/') &rcub;&rcub;" class="block py-2 hover:text-accent transition-colors"&gt;Home&lt;/a&gt;
           &lt;a href="&lcub;&lcub; get_url(path='blog') &rcub;&rcub;" class="block py-2 hover:text-accent transition-colors"&gt;Blog&lt;/a&gt;
           &lt;a href="&lcub;&lcub; get_url(path='tags') &rcub;&rcub;" class="block py-2 hover:text-accent transition-colors"&gt;Tags&lt;/a&gt;
           &lt;button @click="darkMode = !darkMode; localStorage.theme = darkMode ? 'dark' : 'light'; document.documentElement.classList.toggle('dark')" class="block py-2 hover:text-accent transition-colors"&gt;
             &lt;span x-text="darkMode ? '☀️ Light Mode' : '🌙 Dark Mode'"&gt;&lt;/span&gt;
           &lt;/button&gt;
         &lt;/div&gt;
       &lt;/header&gt;
       &lt;main class="container mx-auto px-6 py-12 flex-grow"&gt;
           &lcub;% block content %&rcub;&lcub;% endblock %&rcub;
         &lt;/main&gt;
         &lt;footer class="border-t border-gray-200 dark:border-gray-700 text-center py-6 text-sm text-gray-500 dark:text-gray-400"&gt;
           &lt;p&gt;&amp;copy; &lcub;&lcub; now() | date(format="%Y") &rcub;&rcub; &lcub;&lcub; config.title &rcub;&rcub;&lt;/p&gt;
         &lt;/footer&gt;
       &lt;/body&gt;
       &lt;/html&gt;
     </code></pre>

   - **`templates/index.html`**:
     <pre><code class="language-html">
     &lcub;% extends "base.html" %&rcub;
     &lcub;% block title %&lcub;&lcub; config.title &rcub;&rcub;&lcub;% endblock %&rcub;
     &lcub;% block content %&rcub;
       &lt;section class="py-16 text-center"&gt;
         &lt;h1 class="text-3xl md:text-4xl font-semibold mb-6"&gt;&lcub;&lcub; config.title &rcub;&rcub;&lt;/h1&gt;
         &lt;div class="prose dark:prose-invert max-w-3xl mx-auto"&gt;
           &lcub;&lcub; section.content | safe &rcub;&rcub;
         &lt;/div&gt;
       &lt;/section&gt;
     &lcub;% endblock %&rcub;
     </code>
     ```
     </pre>

   - **`templates/blog_index.html`**:
     <pre><code class="language-html">
     &lcub;% extends "base.html" %&rcub;
     &lcub;% block title %&lcub;&lcub; config.title &rcub;&rcub;&lcub;% endblock %&rcub;
     &lcub;% block content %&rcub;
       &lt;h1 class="text-2xl md:text-3xl font-semibold text-text dark:text-darkText mb-8"&gt;&lcub;&lcub; section.title &rcub;&rcub;&lt;/h1&gt;
       &lt;div class="space-y-8"&gt;
         &lcub;% for post in section.pages %&rcub;
           &lt;article class="border-b border-gray-200 dark:border-gray-700 pb-6"&gt;
             &lt;a href="&lcub;&lcub; post.permalink &rcub;&rcub;" class="text-xl font-medium text-accent hover:underline"&gt;&lcub;&lcub; post.title &rcub;&rcub;&lt;/a&gt;
             &lt;p class="text-sm text-gray-500 dark:text-gray-400 mt-1"&gt;&lcub;&lcub; post.date | date(format="%B %d, %Y") &rcub;&rcub;&lt;/p&gt;
             &lt;p class="mt-2 text-gray-700 dark:text-gray-300"&gt;&lcub;&lcub; post.summary | safe &rcub;&rcub;&lt;/p&gt;
           &lt;/article&gt;
         &lcub;% endfor %&rcub;
       &lt;/div&gt;
     &lcub;% endblock %&rcub;
     </code></pre>

   - **`templates/page.html`**:
     <pre><code class="language-html">
     &lcub;% extends "base.html" %&rcub;
     &lcub;% block title %&lcub;&lcub; page.title &rcub;&rcub;&lcub;% endblock %&rcub;
     &lcub;% block content %&rcub;
       &lt;article class="prose dark:prose-invert max-w-3xl mx-auto"&gt;
         &lt;h1 class="text-2xl md:text-3xl font-semibold text-text dark:text-darkText mb-4"&gt;&lcub;&lcub; page.title &rcub;&rcub;&lt;/h1&gt;
         &lt;p class="text-sm text-gray-500 dark:text-gray-400 mb-6"&gt;&lcub;&lcub; page.date | date(format="%B %d, %Y") &rcub;&rcub;&lt;/p&gt;
         &lcub;&lcub; page.content | safe &rcub;&rcub;
         &lcub;% if page.taxonomies.tags %&rcub;
           &lt;div class="mt-8 text-sm"&gt;
             &lt;span class="text-gray-500 dark:text-gray-400"&gt;Tags:&lt;/span&gt;
             &lcub;% for tag in page.taxonomies.tags %&rcub;
               &lt;a href="/tags/&lcub;&lcub; tag &rcub;&rcub;" class="text-accent hover:underline"&gt;&lcub;&lcub; tag &rcub;&rcub;&lt;/a&gt;&lcub;% if not loop.last %&rcub;, &lcub;% endif %&rcub;
             &lcub;% endfor %&rcub;
           &lt;/div&gt;
         &lcub;% endif %&rcub;
       &lt;/article&gt;
     &lcub;% endblock %&rcub;
     </code></pre>

   - **`templates/taxonomies.html`**:
     <pre><code class="language-html">
     &lcub;% extends "base.html" %&rcub;
     &lcub;% block title %&lcub;&lcub; config.title &rcub;&rcub;&lcub;% endblock %&rcub;
     &lcub;% block content %&rcub;
       &lt;h1 class="text-2xl md:text-3xl font-semibold text-text dark:text-darkText mb-8"&gt;Tags&lt;/h1&gt;
       &lt;ul class="space-y-2 max-w-3xl"&gt;
         &lcub;% for term in config.taxonomies.tags %&rcub;
           &lt;li&gt;
             &lt;a href="/&lcub;&lcub; term.name &rcub;&rcub;" class="text-accent hover:underline"&gt;&lcub;&lcub; term.name | capitalize &rcub;&rcub;&lt;/a&gt;
             &lt;span class="text-gray-500 dark:text-gray-400"&gt;(&lcub;&lcub; term.pages | length &rcub;&rcub;)&lt;/span&gt;
           &lt;/li&gt;
         &lcub;% endfor %&rcub;
       &lt;/ul&gt;
     &lcub;% endblock %&rcub;
     </code></pre>

   - **`templates/taxonomy.html`**:
     <pre><code class="language-html">
     &lcub;% extends "base.html" %&rcub;
     &lcub;% block title %&lcub;&lcub; term.name | capitalize &rcub;&rcub;&lcub;% endblock %&rcub;
     &lcub;% block content %&rcub;
       &lt;h1 class="text-2xl md:text-3xl font-semibold text-text dark:text-darkText mb-8"&gt;&lcub;&lcub; term.name | capitalize &rcub;&rcub;&lt;/h1&gt;
       &lt;div class="space-y-8 max-w-3xl"&gt;
         &lcub;% for page in term.pages %&rcub;
           &lt;article class="border-b border-gray-200 dark:border-gray-700 pb-6"&gt;
             &lt;a href="&lcub;&lcub; page.permalink &rcub;&rcub;" class="text-xl font-medium text-accent hover:underline"&gt;&lcub;&lcub; page.title &rcub;&rcub;&lt;/a&gt;
             &lt;p class="text-sm text-gray-500 dark:text-gray-400 mt-1"&gt;&lcub;&lcub; page.date | date(format="%B %d, %Y") &rcub;&rcub;&lt;/p&gt;
           &lt;/article&gt;
         &lcub;% endfor %&rcub;
       &lt;/div&gt;
     &lcub;% endblock %&rcub;
     </code></pre>

   ### 7. Development
   - **Local Server**:
     ```bash
     cd rustblog
     zola serve  # Runs at http://localhost:1111
     ```
   - **Watch CSS**:
     ```bash
     npm run watch:css  # In a new terminal
     ```
   - **Build**:
     ```bash
     npm run build  # Outputs to public/
     ```

   ### 8. Deployment
   1. **Git Setup**:
      ```bash
      cd rustblog
      git init
      git add .
      git commit -m "Initial commit"
      # Create GitHub repo named 'rustblog' (e.g., via `gh repo create rustblog --public`)
      git remote add origin https://github.com/yoloinfinity55/rustblog.git
      git push -u origin main
      ```

   2. **GitHub Actions (`rustblog/.github/workflows/deploy.yml`)**:
      ```yaml
      name: Deploy to GitHub Pages
      on:
        push:
          branches: [main]
      jobs:
        build-and-deploy:
          runs-on: ubuntu-latest
          steps:
            - uses: actions/checkout@v3
            - run: |
                curl -L https://github.com/getzola/zola/releases/download/v0.19.1/zola-v0.19.1-x86_64-unknown-linux-gnu.tar.gz | tar -xz
                sudo mv zola /usr/local/bin/
            - uses: actions/setup-node@v3
              with: { node-version: '18' }
            - run: npm install
            - run: npm run build:css
            - run: zola build
            - uses: peaceiris/actions-gh-pages@v3
              with:
                github_token: ${{ secrets.GITHUB_TOKEN }}
                publish_dir: ./public
      ```

   3. **Configure GitHub Pages**:
     - Update `config.toml` (already done):
       ```toml
       base_url = "https://yoloinfinity55.github.io/rustblog"
       ```
     - GitHub Settings > Pages > Source: `gh-pages` branch
     - Commit and push (already done):
       ```bash
       git add .
       git commit -m "Update for deployment"
       git push
       ```

   ### 9. Features
   - **Minimalist Design**: Monochromatic palette (grays, `#1E40AF` accent), clean `Inter` font, ample whitespace, no shadows, subtle dividers.
   - **Responsive**: Mobile-friendly navbar with hamburger menu, content limited to `max-w-3xl`.
   - **Dark Mode**: Toggled via emoji button (🌙/☀️), persists with localStorage.
   - **Markdown Styling**: `@tailwindcss/typography` with simplified prose styles.
   - **Syntax Highlighting**: Enabled via Zola’s `highlight_code = true`.
   - **Navigation**: Text-only links (Home, Blog, Tags), no decorative buttons.
   - **Taxonomies**: Tags and categories with dedicated pages.

   ### 10. Testing
   - **Local**: Verify at `http://localhost:1111` for:
     - Homepage, blog index, post pages, and tag pages.
     - Responsiveness (mobile, tablet, desktop).
     - Dark mode toggle and syntax highlighting.
   - **Production**: Check at `https://yoloinfinity55.github.io/rustblog` for:
     - Correct asset loading (CSS, Alpine.js).
     - Functional links and taxonomy pages.

   ### 11. Maintenance
   - **Add Posts**: Create new `.md` files in `content/blog/`.
   - **Update Styles**: Modify `static/css/tailwind.css` or `tailwind.config.js`.
   - **Update Dependencies**: Run `brew upgrade` and `npm update`.

   ### 12. Troubleshooting
   - **Zola**: Use ARM64 binary (`aarch64-apple-darwin`). Check `config.toml` for correct `base_url`.
   - **Tailwind**: Verify `tailwind.config.js` paths, run `npm run build:css` if styles fail.
   - **GitHub Pages**: Check Actions logs, ensure `publish_dir` is `./public` and `base_url` matches GitHub Pages URL.
   - **Dark Mode**: Ensure Alpine.js CDN is accessible, check localStorage in browser dev tools.

   ### 13. Deliverables
   - Static blog hosted at `https://yoloinfinity55.github.io/rustblog`.
   - GitHub repository: `rustblog`.
   - Minimalist, responsive blog with sample content, tags, and categories.
   - Automated deployment pipeline via GitHub Actions.

   ### 14. Timeline
   - **Day 1**: Setup dependencies, initialize project, create templates and content.
   - **Day 2**: Test locally, set up Git and GitHub Actions.
   - **Day 3**: Deploy to GitHub Pages, validate production site.

   ### 15. Resources
   - [Zola Docs](https://www.getzola.org/documentation/)
   - [Tailwind CSS Docs](https://tailwindcss.com/docs)
   - [GitHub Pages](https://docs.github.com/en/pages)
   - [Alpine.js Docs](https://alpinejs.dev/)
   - [Inter Font](https://rsms.me/inter/)

   ---

   ### Key Updates from Original Specification
   - **Folder Structure**: Eliminated nested `rustblog/rustblog/` by using `zola init .`, ensuring a flat structure (`rustblog/config.toml`, `rustblog/content/`, etc.).
   - **Minimalist Design**: Implemented a monochromatic palette, `Inter` font, increased whitespace, removed shadows and decorative buttons, and used subtle dividers.
   - **Paths**: Updated `tailwind.config.js`, `package.json`, and `deploy.yml` to reflect the new structure (`static/` instead of `rustblog/static/`). Corrected asset and navigation links in `templates/base.html` and `content/_index.md` to use Zola's `get_url` function or relative paths for proper GitHub Pages deployment.
   - **Templates**: Enhanced with minimalist styling, including a simplified navbar, emoji-based dark mode toggle, and flat post listings. Initialized `menuOpen` variable in Alpine.js `x-data` to prevent `ReferenceError`.
   - **Functionality**: Preserved responsive navigation, dark mode, syntax highlighting, and taxonomy pages.
   - **Content**: Added `second-post.md` and `third-post.md` for testing and demonstration.
   