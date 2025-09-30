module.exports = {
  content: ['./templates/**/*.{html,md}', './content/**/*.{html,md}'],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        accent: '#1E40AF', // Unchanged for light mode
        bg: '#F7F7F7', // Unchanged light mode background
        text: '#1F2A44', // Unchanged light mode text
        darkBg: '#1A1A1E', // New dark mode background (deep charcoal)
        darkText: '#F4F4F9', // New dark mode text (soft off-white)
        darkAccent: '#3B82F6', // Lighter accent for dark mode links
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
            'a': { color: theme('colors.darkAccent'), 'text-decoration': 'none', 'transition': 'color 0.2s', 'font-weight': '500' },
            'a:hover': { color: theme('colors.darkAccent'), 'text-decoration': 'underline' },
            'h1, h2, h3, h4, h5, h6': { color: theme('colors.darkText'), 'font-weight': '600' },
            'code': { background: '#2D2D34', color: theme('colors.darkText'), padding: '2px 4px', borderRadius: '2px', 'font-size': '0.9em' },
            'pre': { background: '#2D2D34', color: theme('colors.darkText'), padding: '1rem', borderRadius: '4px' },
            'p': { margin: '1.5rem 0' },
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