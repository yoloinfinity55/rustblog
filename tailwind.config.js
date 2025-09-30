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