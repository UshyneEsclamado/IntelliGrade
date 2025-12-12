import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router' // if you have router
import { useThemeStore } from './stores/theme'

// Import your CSS files
import './assets/main.css' // or whatever your main CSS file is called

const app = createApp(App)
const pinia = createPinia()

app.use(pinia)
app.use(router) // if you have router

// Mount the app first
app.mount('#app')

// Initialize theme after mount
const themeStore = useThemeStore()
themeStore.initDarkMode()