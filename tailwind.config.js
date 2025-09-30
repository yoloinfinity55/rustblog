module.exports = {
  content: ['./rustblog/templates/**/*.{html,md}', './rustblog/content/**/*.{html,md}'],
  darkMode: 'class', // Enable dark mode with class-based toggle
  theme: {
    extend: {
      colors: {
        primary: '#1E40AF', // Blue
        secondary: '#10B981', // Emerald green for accents
      },
      typography: (theme) => ({
        DEFAULT: {
          css: {
            color: theme('colors.gray.800'),
            'a': { color: theme('colors.primary'), 'text-decoration': 'underline', 'transition': 'color 0.2s' },
            'a:hover': { color: theme('colors.secondary') },
            'code': { background: theme('colors.gray.100'), padding: '2px 4px', borderRadius: '4px' },
            'pre': { background: theme('colors.gray.900'), padding: '1rem' },
          },
        },
        dark: {
          css: {
            color: theme('colors.gray.200'),
            'a': { color: theme('colors.secondary') },
            'a:hover': { color: theme('colors.primary') },
            'code': { background: theme('colors.gray.800'), color: theme('colors.gray.200') },
            'pre': { background: theme('colors.gray.800') },
          },
        },
      }),
    },
  },
  plugins: [require('@tailwindcss/typography')],
}
