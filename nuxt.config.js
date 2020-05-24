export default {
  buildModules: ['@nuxt/typescript-build'],
  plugins: [
    '~/plugins/composition-api',
    { src: '~plugins/ga.js', mode: 'client' }
  ],
  head: {
    link: [
      {
        rel: 'icon',
        type: 'image/png',
        href: '/favicon.png',
      },
      {
        // Chrome audit
        // Consider adding `preconnect` or `dns-prefetch` resource hints to
        // establish early connections to important third-party origins.
        rel: "preconnect",
        href: "https://www.google-analytics.com",
      }
    ],
    meta: [
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
    ],
    htmlAttrs: {
      // Chrome audit
      // Avoid light house error `<html> element does not have a [lang] attribute`
      // Eg <html lang="en">
      lang: 'en'
    },
  }
}
