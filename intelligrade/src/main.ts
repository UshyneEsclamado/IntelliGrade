import './assets/main.css'  // Import global styles (CSS)
import { createApp } from 'vue'  // Import Vue's createApp function
import { createPinia } from 'pinia'  // Import Pinia for state management
import App from './App.vue'  // Import the root App component
import router from './router'  // Import the router configuration

// Initialize dark mode from localStorage on app start
const initializeDarkMode = () => {
  const savedTheme = localStorage.getItem('darkMode');
  if (savedTheme === 'true') {
    document.documentElement.classList.add('dark');
  } else {
    document.documentElement.classList.remove('dark');
  }
};

// Initialize dark mode immediately
initializeDarkMode();

// Create a Vue app instance
const app = createApp(App)

// Use Pinia for state management
app.use(createPinia())

// Use Vue Router for navigation
app.use(router)

// Mount the Vue app to the DOM
app.mount('#app')
