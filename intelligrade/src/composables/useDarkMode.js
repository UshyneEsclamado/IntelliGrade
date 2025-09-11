
import { ref, watch } from 'vue'

const isDarkMode = ref(false)

export function useDarkMode() {
  const initDarkMode = () => {
    // Check localStorage first
    const savedMode = localStorage.getItem('darkMode')
    if (savedMode !== null) {
      isDarkMode.value = savedMode === 'true'
    } else {
      // Check system preference
      isDarkMode.value = window.matchMedia('(prefers-color-scheme: dark)').matches
    }
    applyDarkMode()
  }

  const applyDarkMode = () => {
    if (isDarkMode.value) {
      document.documentElement.classList.add('dark')
      document.body.classList.add('dark-mode-body')
    } else {
      document.documentElement.classList.remove('dark')
      document.body.classList.remove('dark-mode-body')
    }
  }

  const toggleDarkMode = () => {
    isDarkMode.value = !isDarkMode.value
    localStorage.setItem('darkMode', isDarkMode.value.toString())
    applyDarkMode()
    
    // Emit custom event for any components that need to listen
    window.dispatchEvent(new CustomEvent('darkModeChanged', { 
      detail: isDarkMode.value 
    }))
  }

  // Watch for changes and apply them
  watch(isDarkMode, () => {
    applyDarkMode()
  })

  return {
    isDarkMode,
    toggleDarkMode,
    initDarkMode
  }
}