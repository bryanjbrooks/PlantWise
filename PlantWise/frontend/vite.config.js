import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    react(),
    tailwindcss(),
  ],
  server: {
    proxy: {
      // Proxy /api/* to your FastAPI backend
      "/api": {
        target: "http://localhost:8000",  
        changeOrigin: true,
        secure: false,
        // Rewrite the path if your backend doesn't use the /api prefix
        // (you *are* using /api in your FastAPI, so you can omit rewrite)
        // rewrite: (path) => path.replace(/^\/api/, "/api"),
      },
    },
  },
})
