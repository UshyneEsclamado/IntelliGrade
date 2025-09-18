<template>
  <div class="auth-wrapper">
    <div class="geometric-shapes"></div>
    <div class="floating-elements">
      <div class="floating-circle circle-1"></div>
      <div class="floating-circle circle-2"></div>
      <div class="floating-circle circle-3"></div>
    </div>
    
    <div class="auth-container">
      <div class="auth-box">
        <!-- Header Section -->
        <div class="logo-section">
          <div class="class-icon">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12,3L1,9L12,15L21,10.09V17H23V9M5,13.18V17.18L12,21L19,17.18V13.18L12,17L5,13.18Z"/>
            </svg>
          </div>
          <h1>Join Section</h1>
          <p class="subtitle">Enter the section code provided by your teacher</p>
        </div>

        <!-- Section Code Input -->
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
                placeholder="Enter section code (e.g., ENG7-A71727L)"
                class="w-full px-4 py-3 pl-12 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                :class="{ 'border-red-500': hasError }"
                required
              >
              <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"></path>
                </svg>
              </div>
            </div>
            <p class="text-xs text-gray-500 mt-1">
              Section codes are provided by your teacher and contain both subject and section information
            </p>
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
                <p class="text-sm text-green-600 mt-1">Redirecting to dashboard...</p>
              </div>
            </div>
          </div>

          <!-- Section Info Display (shown after successful validation but before joining) -->
          <div v-if="validatedSection" class="bg-blue-50 rounded-lg p-4">
            <div class="text-sm text-blue-600 font-medium">Ready to Join:</div>
            <div class="text-lg font-semibold text-blue-800">{{ validatedSection.subject_name }}</div>
            <div class="text-sm text-blue-600">Section: {{ validatedSection.section_name }}</div>
            <div class="text-xs text-blue-500 mt-1">Teacher: {{ validatedSection.teacher_name }}</div>
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
            {{ isLoading ? 'Joining Section...' : 'Join Section' }}
          </button>
        </form>

        <!-- Action Buttons -->
        <div class="mt-6 flex flex-col space-y-2">
          <button
            @click="goBack"
            class="w-full bg-gray-100 hover:bg-gray-200 text-gray-700 font-medium py-2 px-4 rounded-lg transition-colors flex items-center justify-center"
          >
            <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path>
            </svg>
            Back to Join Options
          </button>
        </div>

        <!-- Help Section -->
        <div class="mt-8 text-center">
          <div class="flex items-center justify-center text-blue-600 mb-2">
            <svg class="w-5 h-5 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
            <span class="text-sm font-medium">Need Help?</span>
          </div>
          <div class="text-sm text-gray-600 space-y-1">
            <p>Ask your teacher for the section code.</p>
            <p class="font-mono text-xs bg-gray-100 px-2 py-1 rounded">Example: ENG7-A71727L</p>
            <p>This code contains both the subject and section information you need.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { supabase } from '@/supabase'

export default {
  name: 'JoinSection',
  data() {
    return {
      sectionCode: '',
      isLoading: false,
      hasError: false,
      hasSuccess: false,
      errorMessage: '',
      validatedSection: null
    }
  },
  mounted() {
    this.checkAuthAndSetup()
  },
  methods: {
    async checkAuthAndSetup() {
      // Check if user is authenticated
      const { data: { user } } = await supabase.auth.getUser()
      if (!user) {
        this.$router.push('/login')
        return
      }

      // Check if this is a direct URL join (with section code in params)
      if (this.$route.params.sectionCode) {
        this.sectionCode = this.$route.params.sectionCode
        // Optionally auto-validate the section code
        this.validateSectionCode()
      }
    },

    async validateSectionCode() {
      if (!this.sectionCode.trim()) return

      try {
        const { data, error } = await supabase
          .from('sections')
          .select(`id, section_name, section_code, subjects (id, subject_name, profiles (full_name))`)
          .eq('section_code', this.sectionCode.trim().toUpperCase())
          .single()

        if (error) throw error

        this.validatedSection = {
          id: data.id,
          section_name: data.section_name,
          section_code: data.section_code,
          subject_name: data.subjects.subject_name,
          teacher_name: data.subjects.profiles.full_name
        }

        this.hasError = false
      } catch (error) {
        console.error('Section validation error:', error)
        this.validatedSection = null
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
        const { data: { user } } = await supabase.auth.getUser()
        if (!user) {
          throw new Error('User not authenticated')
        }

        // First validate the section exists
        const { data: sectionData, error: sectionError } = await supabase
          .from('sections')
          .select(`id, section_name, section_code, subject_id, subjects (id, subject_name, profiles (full_name))`)
          .eq('section_code', this.sectionCode.trim().toUpperCase())
          .single()

        if (sectionError || !sectionData) {
          throw new Error('Section not found')
        }

        // Check if student is already enrolled
        const { data: existingEnrollment } = await supabase
          .from('enrollments')
          .select('id')
          .eq('student_id', user.id)
          .eq('section_id', sectionData.id)
          .single()

        if (existingEnrollment) {
          this.showError('You are already enrolled in this section.')
          return
        }

        // Create enrollment
        const { error: enrollmentError } = await supabase
          .from('enrollments')
          .insert({
            student_id: user.id,
            section_id: sectionData.id,
            subject_id: sectionData.subject_id,
            enrolled_at: new Date().toISOString()
          })

        if (enrollmentError) {
          throw enrollmentError
        }

        this.hasSuccess = true

        // Redirect to student dashboard after success
        setTimeout(() => {
          this.$router.push({
            name: 'studentDashboard',
            query: {
              enrolled: 'true',
              sectionCode: this.sectionCode,
              sectionName: sectionData.section_name,
              subjectName: sectionData.subjects.subject_name
            }
          })
        }, 2000)

      } catch (error) {
        console.error('Join section error:', error)

        if (error.message === 'Section not found') {
          this.showError('Invalid section code. Please check and try again.')
        } else if (error.code === '23505') { // Unique constraint violation
          this.showError('You are already enrolled in this section.')
        } else {
          this.showError('Unable to join section. Please try again later.')
        }
      } finally {
        this.isLoading = false
      }
    },

    goBack() {
      // Navigate back to join class auth
      this.$router.push({ name: 'JoinClassAuth' })
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
  },
  watch: {
    sectionCode() {
      // Debounce section code validation
      clearTimeout(this.validationTimeout)
      this.validationTimeout = setTimeout(() => {
        if (this.sectionCode.trim().length >= 5) {
          this.validateSectionCode()
        } else {
          this.validatedSection = null
        }
      }, 500)
    }
  },
  beforeUnmount() {
    if (this.validationTimeout) {
      clearTimeout(this.validationTimeout)
    }
  }
}
</script>


<style scoped>
/* Base styles - inherited from joinClassAuth component */
* { 
  margin: 0; 
  padding: 0; 
  box-sizing: border-box; 
}

.auth-wrapper {
  position: absolute; 
  inset: 0;
  background: transparent !important;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  padding: 40px;
  font-family: 'Inter', sans-serif;
  overflow-y: auto;
}

.geometric-shapes {
  position: fixed;
  inset: 0;
  z-index: 0;
  overflow: hidden;
  background: linear-gradient(135deg, #A3D1C6 0%, #B3D8A8 50%, #FBFFE4 100%);
}

.floating-circle {
  position: absolute;
  border-radius: 50%;
  opacity: 0.08;
  animation: float 10s ease-in-out infinite;
}

.circle-1 { 
  width: 100px; 
  height: 100px; 
  background: #3D8D7A; 
  top: 15%; 
  left: 10%; 
}

.circle-2 { 
  width: 140px; 
  height: 140px; 
  background: #A3D1C6; 
  bottom: 20%; 
  right: 15%; 
}

.circle-3 { 
  width: 120px; 
  height: 120px; 
  background: #B3D8A8; 
  top: 60%; 
  left: 70%; 
}

.auth-container {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  max-width: 600px;
  z-index: 1;
  position: relative;
}

.auth-box {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  padding: 50px 45px;
  border-radius: 24px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  width: 100%;
  text-align: center;
  position: relative;
}

.logo-section {
  margin-bottom: 40px;
}

.class-icon {
  width: 90px;
  height: 90px;
  margin: 0 auto 25px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(61, 141, 122, 0.08);
  border-radius: 50%;
  color: #3D8D7A;
  box-shadow: 0 8px 20px rgba(61, 141, 122, 0.1);
}

h1 {
  color: #3D8D7A;
  font-size: 32px;
  font-weight: 700;
  margin-bottom: 12px;
  letter-spacing: -0.5px;
}

.subtitle {
  color: #3D8D7A;
  font-size: 17px;
  opacity: 0.75;
  font-weight: 500;
}

.form-group label {
  display: block;
  color: #3D8D7A;
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 12px;
  letter-spacing: 0.2px;
}

.input-wrapper {
  position: relative;
  display: flex;
  align-items: center;
}

.input-icon {
  position: absolute;
  left: 18px;
  color: rgba(61, 141, 122, 0.5);
  z-index: 1;
}

input {
  width: 100%;
  padding: 18px 18px 18px 50px;
  font-size: 16px;
  border: 2px solid rgba(61, 141, 122, 0.15);
  border-radius: 16px;
  outline: none;
  background: rgba(255, 255, 255, 0.9);
  color: #3D8D7A;
  transition: all 0.3s ease;
  font-weight: 500;
}

input:focus {
  border-color: rgba(61, 141, 122, 0.4);
  box-shadow: 0 0 0 6px rgba(61, 141, 122, 0.08);
  background: white;
}

input::placeholder {
  color: rgba(61, 141, 122, 0.45);
  font-size: 15px;
  font-weight: 400;
}

.auth-btn {
  width: 100%;
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: white;
  padding: 18px;
  font-size: 17px;
  font-weight: 600;
  border: none;
  border-radius: 16px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  margin-top: 20px;
  box-shadow: 0 6px 20px rgba(61, 141, 122, 0.2);
}

.auth-btn:hover:not(:disabled) {
  transform: translateY(-3px);
  box-shadow: 0 12px 30px rgba(61, 141, 122, 0.25);
}

.auth-btn:active:not(:disabled) {
  transform: translateY(-1px);
}

.auth-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.forgot-section {
  margin: 25px 0;
  text-align: center;
}

.forgot-section a {
  color: #3D8D7A;
  font-size: 16px;
  text-decoration: none;
  font-weight: 500;
  transition: all 0.3s ease;
  padding-bottom: 3px;
  border-bottom: 2px solid transparent;
}

.forgot-section a:hover {
  border-bottom-color: rgba(61, 141, 122, 0.5);
}

@keyframes float {
  0%, 100% { 
    transform: translateY(0) rotate(0deg); 
  }
  50% { 
    transform: translateY(-25px) rotate(180deg); 
  }
}

@media (max-width: 768px) {
  .auth-wrapper {
    padding: 25px;
  }
  
  .auth-box {
    padding: 40px 35px;
  }

  .class-icon {
    width: 80px;
    height: 80px;
  }

  h1 {
    font-size: 28px;
  }

  .subtitle {
    font-size: 16px;
  }
}

</style>
