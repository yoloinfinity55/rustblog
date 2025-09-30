module.exports = {
  content: ['./rustblog/templates/**/*.{html,md}', './rustblog/content/**/*.{html,md}'],
  theme: { extend: { colors: { primary: '#1E40AF' } } },
  plugins: [require('@tailwindcss/typography')],
}