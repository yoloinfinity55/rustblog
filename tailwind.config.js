module.exports = {
  content: ['./templates/**/*.{html,md}', './content/**/*.{html,md}'],
  darkMode: '[data-theme="dark"]',
  theme: {
    extend: {
      colors: {
        accent: 'rgb(var(--color-accent) / <alpha-value>)',
        bg: 'rgb(var(--color-bg) / <alpha-value>)',
        text: 'rgb(var(--color-text) / <alpha-value>)',
        gray: {
          100: 'rgb(var(--color-gray-100) / <alpha-value>)',
          200: 'rgb(var(--color-gray-200) / <alpha-value>)',
          700: 'rgb(var(--color-gray-700) / <alpha-value>)',
        },
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
            color: theme('colors.text'),
            'a': { color: theme('colors.accent') },
            'a:hover': { color: theme('colors.accent'), 'text-decoration': 'underline' },
            'h1, h2, h3, h4, h5, h6': { color: theme('colors.text') },
            'code': { background: theme('colors.gray.700'), color: theme('colors.text') },
            'pre': { background: theme('colors.gray.700'), color: theme('colors.text') },
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