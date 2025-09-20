import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useThemeStore = defineStore('theme', () => {
  const isDarkMode = ref(false)

  const initDarkMode = () => {
    // Check localStorage first
    const savedMode = localStorage.getItem('darkMode')
    
    if (savedMode !== null) {
      isDarkMode.value = savedMode === 'true'
    } else {
      // Default to light mode if no preference is saved
      isDarkMode.value = false
    }
    
    applyDarkMode()
  }

  const applyDarkMode = () => {
    console.log('Theme Store - Applying dark mode:', isDarkMode.value)
    console.log('Theme Store - Document element before:', document.documentElement.classList.toString())
    
    if (isDarkMode.value) {
      document.documentElement.classList.add('dark')
      document.body.classList.add('dark-mode')
    } else {
      document.documentElement.classList.remove('dark')
      document.body.classList.remove('dark-mode')
    }
    
    console.log('Theme Store - Document element after:', document.documentElement.classList.toString())
  }

  const toggleDarkMode = () => {
    console.log('Theme Store - Toggle called, current value:', isDarkMode.value)
    isDarkMode.value = !isDarkMode.value
    localStorage.setItem('darkMode', isDarkMode.value.toString())
    console.log('Theme Store - New value:', isDarkMode.value, 'Saved to localStorage')
    applyDarkMode()
    
    // Emit custom event for any components that need to listen
    window.dispatchEvent(new CustomEvent('darkModeChanged', { 
      detail: isDarkMode.value 
    }))
  }

  return {
    isDarkMode,
    toggleDarkMode,
    initDarkMode,
    applyDarkMode
  }
})