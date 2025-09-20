import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useThemeStore = defineStore('theme', () => {
  const isDarkMode = ref(false)

  const initDarkMode = () => {
    // Check localStorage first
    const savedMode = localStorage.getItem('darkMode')
    console.log('Theme Store - Saved mode from localStorage:', savedMode)
    
    if (savedMode !== null) {
      isDarkMode.value = savedMode === 'true'
    } else {
      // Default to light mode if no preference is saved
      isDarkMode.value = false
    }
    
    console.log('Theme Store - isDarkMode value after init:', isDarkMode.value)
    applyDarkMode()
  }

  const applyDarkMode = () => {
    console.log('Theme Store - Applying dark mode:', isDarkMode.value)
    
    if (isDarkMode.value) {
      document.documentElement.classList.add('dark')
      document.body.classList.add('dark-mode')
      console.log('Theme Store - Added dark classes')
    } else {
      document.documentElement.classList.remove('dark')
      document.body.classList.remove('dark-mode')
      console.log('Theme Store - Removed dark classes')
    }
    
    console.log('Theme Store - document.documentElement classes:', document.documentElement.className)
  }

  const toggleDarkMode = () => {
    console.log('Theme Store - Toggle called, current isDarkMode:', isDarkMode.value)
    isDarkMode.value = !isDarkMode.value
    localStorage.setItem('darkMode', isDarkMode.value.toString())
    console.log('Theme Store - New isDarkMode value:', isDarkMode.value)
    console.log('Theme Store - Saved to localStorage:', isDarkMode.value.toString())
    applyDarkMode()
    
    // Emit custom event for any components that need to listen
    window.dispatchEvent(new CustomEvent('darkModeChanged', { 
      detail: isDarkMode.value 
    }))
    console.log('Theme Store - Dispatched darkModeChanged event')
  }

  return {
    isDarkMode,
    toggleDarkMode,
    initDarkMode,
    applyDarkMode
  }
})