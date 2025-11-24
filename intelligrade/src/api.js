// src/api.js
// This file handles ALL backend API calls

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

export { API_URL }

// Export helper functions if needed
export const api = {
  get baseUrl() {
    return API_URL
  },
  
  // Helper for common fetch with error handling
  async fetch(endpoint, options = {}) {
    const url = `${API_URL}${endpoint}`
    const response = await fetch(url, options)
    if (!response.ok) {
      throw new Error(`API Error: ${response.statusText}`)
    }
    return response.json()
  }
}

export default api