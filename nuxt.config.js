export default {
  buildModules: ['@nuxt/typescript-build'],
  plugins: [
    '~/plugins/composition-api',
    { src: '~plugins/ga.js', mode: 'client' }
  ],
  link: [
    {
      rel: 'icon',
      type: 'image/png',
      href: 'favicon.png',
    },
  ],
}
