import './assets/main.css'  // Import global styles (CSS)
import { createApp } from 'vue'  // Import Vue's createApp function
import { createPinia } from 'pinia'  // Import Pinia for state management
import App from './App.vue'  // Import the root App component
import router from './router'  // Import the router configuration

// Create a Vue app instance
const app = createApp(App)

// Use Pinia for state management
const pinia = createPinia()
app.use(pinia)

// Use Vue Router for navigation
app.use(router)

// Initialize theme store after Pinia is set up
import { useThemeStore } from './stores/theme.ts'
console.log('Main.ts - Initializing theme store...')
const themeStore = useThemeStore()
themeStore.initDarkMode()
console.log('Main.ts - Theme store initialized')

// Mount the Vue app to the DOM
app.mount('#app')
