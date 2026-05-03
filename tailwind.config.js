/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        navy: "#0B192C",
        saffron: "#FF671F",
        indiagreen: "#046A38",
        bglight: "#FAFAFA",
      },
      fontFamily: {
        cabinet: ['Cabinet Grotesk', 'sans-serif'],
        ibm: ['IBM Plex Sans', 'sans-serif'],
      }
    },
  },
  plugins: [],
}
