<template>
  <div class="min-h-screen bg-gradient-to-br from-purple-600 via-blue-600 to-indigo-700 flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl shadow-2xl p-8 w-full max-w-md">
      <!-- Header Icon -->
      <div class="flex justify-center mb-6">
        <div class="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center">
          <svg class="w-8 h-8 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path>
          </svg>
        </div>
      </div>

      <!-- Title -->
      <h1 class="text-2xl font-bold text-gray-800 text-center mb-2">Join Section</h1>
      <p class="text-gray-600 text-center mb-8">
        Enter the section code provided by your teacher to join the class
      </p>

      <!-- Class Info Display -->
      <div class="bg-blue-50 rounded-lg p-4 mb-6">
        <div class="text-sm text-blue-600 font-medium">Class Subject</div>
        <div class="text-lg font-semibold text-blue-800">{{ classCode || 'Loading...' }}</div>
        <div class="text-sm text-blue-600">{{ selectedSection || 'Section not selected' }}</div>
      </div>

      <!-- Section Code Form -->
      <form @submit.prevent="joinSection" class="space-y-6">
        <div>
          <label for="sectionCode" class="block text-sm font-medium text-gray-700 mb-2">
            Section Code
          </label>
          <div class="relative">
            <input
              id="sectionCode"
              v-model="sectionCode"
              type="text"
              placeholder="Enter section code"
              class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
              :class="{ 'border-red-500': hasError }"
              required
            >
            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
              <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"></path>
              </svg>
            </div>
          </div>
        </div>

        <!-- Error Message -->
        <div v-if="hasError" class="bg-red-50 border border-red-200 rounded-lg p-4">
          <div class="flex">
            <svg class="w-5 h-5 text-red-400 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd"></path>
            </svg>
            <div class="ml-3">
              <h3 class="text-sm font-medium text-red-800">{{ errorMessage }}</h3>
            </div>
          </div>
        </div>

        <!-- Success Message -->
        <div v-if="hasSuccess" class="bg-green-50 border border-green-200 rounded-lg p-4">
          <div class="flex">
            <svg class="w-5 h-5 text-green-400 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
            </svg>
            <div class="ml-3">
              <h3 class="text-sm font-medium text-green-800">Successfully joined the section!</h3>
            </div>
          </div>
        </div>

        <!-- Join Button -->
        <button
          type="submit"
          :disabled="isLoading || !sectionCode.trim()"
          class="w-full bg-green-600 hover:bg-green-700 disabled:bg-gray-400 disabled:cursor-not-allowed text-white font-semibold py-3 px-4 rounded-lg transition-colors flex items-center justify-center"
        >
          <svg v-if="isLoading" class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
          <svg v-else class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path>
          </svg>
          {{ isLoading ? 'Joining...' : 'Join Section' }}
        </button>
      </form>

      <!-- Help Section -->
      <div class="mt-8 text-center">
        <div class="flex items-center justify-center text-blue-600 mb-2">
          <svg class="w-5 h-5 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
          </svg>
          <span class="text-sm font-medium">Need Help?</span>
        </div>
        <p class="text-sm text-gray-600">
          Ask your teacher for the section code. It should look like: ENG7-A71727L
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'JoinSection',
  data() {
    return {
      sectionCode: '',
      isLoading: false,
      hasError: false,
      hasSuccess: false,
      errorMessage: '',
      classCode: '',
      selectedSection: ''
    }
  },
  mounted() {
    this.loadRouteData()
  },
  methods: {
    loadRouteData() {
      // Get class code and section from route params/query
      this.classCode = this.$route.query.classCode || this.$route.params.classCode
      this.selectedSection = this.$route.query.selectedSection || this.$route.params.selectedSection
      
      // If no class code, redirect back to start
      if (!this.classCode) {
        this.$router.push('/joinclassauth')
        return
      }
    },

    async joinSection() {
      if (!this.sectionCode.trim()) {
        this.showError('Please enter a section code')
        return
      }

      this.isLoading = true
      this.hasError = false
      this.hasSuccess = false

      try {
        // API call to join section
        const response = await this.$http.post('/api/join-section', {
          classCode: this.classCode,
          sectionCode: this.sectionCode.trim(),
          selectedSection: this.selectedSection
        })

        if (response.data.success) {
          this.hasSuccess = true
          
          // Redirect to student dashboard after brief success display
          setTimeout(() => {
            this.$router.push({
              name: 'StudentDashboard',
              query: {
                enrolled: 'true',
                classCode: this.classCode,
                sectionCode: this.sectionCode
              }
            })
          }, 1500)
        } else {
          this.showError(response.data.message || 'Invalid section code. Please check and try again.')
        }
      } catch (error) {
        console.error('Join section error:', error)
        
        if (error.response?.status === 400) {
          this.showError('Invalid section code. Please check and try again.')
        } else if (error.response?.status === 404) {
          this.showError('Section not found. Please verify the code with your teacher.')
        } else if (error.response?.status === 409) {
          this.showError('You are already enrolled in this section.')
        } else {
          this.showError('Unable to join section. Please try again.')
        }
      } finally {
        this.isLoading = false
      }
    },

    showError(message) {
      this.errorMessage = message
      this.hasError = true
      this.hasSuccess = false
      
      // Clear error after 5 seconds
      setTimeout(() => {
        this.hasError = false
      }, 5000)
    }
  }
}
</script>