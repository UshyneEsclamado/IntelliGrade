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
          <h1>Enter Section Code</h1>
          <p class="subtitle">Enter the section code provided by your teacher</p>
        </div>

        <!-- Section Info Display -->
        <div v-if="selectedSection" class="class-preview">
          <div class="class-card">
            <h3>Selected Section: {{ selectedSection.name }}</h3>
            <p>Student Count: {{ selectedSection.student_count || 0 }}</p>
          </div>
        </div>

        <!-- Form Container -->
        <div class="auth-form-container">
          <form @submit.prevent="handleSubmit" class="section-code-form">
            <!-- Section Code Input -->
            <div class="form-group">
              <label for="sectionCode">Section Code</label>
              <div class="input-wrapper">
                <svg class="input-icon" width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12,3L1,9L12,15L21,10.09V17H23V9M5,13.18V17.18L12,21L19,17.18V13.18L12,17L5,13.18Z"/>
                </svg>
                <input
                  id="sectionCode"
                  v-model="sectionCode"
                  type="text"
                  required
                  placeholder="e.g., ENG7-S01123"
                  class="code-input"
                  :disabled="isLoading"
                />
              </div>
            </div>

            <!-- Error Display -->
            <div v-if="errorMessage" class="error-display">
              <div class="error-icon">⚠️</div>
              <p>{{ errorMessage }}</p>
            </div>

            <!-- Success Display -->
            <div v-if="successMessage" class="success-display">
              <div class="success-icon">✅</div>
              <p>{{ successMessage }}</p>
            </div>

            <!-- Submit Button -->
            <button
              type="submit"
              class="auth-btn"
              :disabled="isLoading || !sectionCode.trim()"
            >
              <svg v-if="!isLoading" width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12,3L1,9L12,15L21,10.09V17H23V9M5,13.18V17.18L12,21L19,17.18V13.18L12,17L5,13.18Z"/>
              </svg>
              <div v-else class="loading-spinner"></div>
              {{ isLoading ? 'Verifying...' : 'Join Section' }}
            </button>

            <!-- Back Button -->
            <button
              type="button"
              @click="goBack"
              class="back-button"
              :disabled="isLoading"
            >
              <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                <path d="M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z"/>
              </svg>
              Back to Section Selection
            </button>
          </form>
        </div>

        <!-- Help Section - Moved inside auth-box for better layout -->
        <div class="help-section">
          <div class="help-card">
            <div class="help-icon">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M11,18H13V16H11V18M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,20C7.59,20 4,16.41 4,12C4,7.59 7.59,4 12,4C16.41,4 20,7.59 20,12C20,16.41 16.41,20 12,20M12,6A4,4 0 0,0 8,10H10A2,2 0 0,1 12,8A2,2 0 0,1 14,10C14,12 11,11.75 11,15H13C13,12.75 16,12.5 16,10A4,4 0 0,0 12,6Z"/>
              </svg>
            </div>
            <h4>Need Help?</h4>
            <p>Ask your teacher for the section code. It usually looks like "ENG7-S01123" or similar format.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { supabase } from '@/supabase'

export default {
  name: 'SectionCode',
  setup() {
    const router = useRouter()
    const route = useRoute()
    
    // Reactive data
    const sectionCode = ref('')
    const isLoading = ref(false)
    const errorMessage = ref('')
    const successMessage = ref('')
    const selectedSection = ref(null)
    
    // Get data from route params/query
    const classCode = ref(route.query.classCode || '')
    const providedSectionCode = ref(route.query.sectionCode || '')
    const userId = ref(null)

    // Get user data from localStorage or session
    onMounted(async () => {
      try {
        // Get current user from Supabase
        const { data: { user } } = await supabase.auth.getUser()
        
        if (!user) {
          errorMessage.value = 'User not authenticated. Please log in again.'
          return
        }

        userId.value = user.id
        
        // If we have a section code from URL, pre-fill it
        if (providedSectionCode.value) {
          sectionCode.value = providedSectionCode.value
        }
        
        // Validate required data
        if (!classCode.value) {
          errorMessage.value = 'Missing class information. Please start over.'
          return
        }
        
      } catch (error) {
        console.error('Error loading user data:', error)
        errorMessage.value = 'Error loading user information. Please try again.'
      }
    })

    // Handle form submission
    const handleSubmit = async () => {
      if (!sectionCode.value.trim()) {
        errorMessage.value = 'Please enter a section code.'
        return
      }

      isLoading.value = true
      errorMessage.value = ''
      successMessage.value = ''

      try {
        console.log('Looking for section with code:', sectionCode.value.trim())
        console.log('Class code from URL:', classCode.value)

        // 1. First find the section directly using the section code
        const { data: sectionData, error: sectionError } = await supabase
          .from('sections')
          .select(`
            id, 
            section_name, 
            subject_id, 
            section_code,
            subjects!inner (
              id,
              subject_name,
              grade_level,
              class_code
            )
          `)
          .eq('section_code', sectionCode.value.trim().toUpperCase())
          .single()

        console.log('Section query result:', sectionData, sectionError)

        if (sectionError || !sectionData) {
          errorMessage.value = 'Invalid section code. Please check and try again.'
          return
        }

        // 2. Verify the section belongs to the correct class
        if (sectionData.subjects.class_code !== classCode.value) {
          errorMessage.value = 'This section code does not belong to the selected class.'
          return
        }

        // 3. Check if student is already enrolled in this section
        const { data: existingEnrollment, error: enrollmentCheckError } = await supabase
          .from('student_sections')
          .select('id')
          .eq('student_id', userId.value)
          .eq('section_id', sectionData.id)
          .maybeSingle()

        if (existingEnrollment) {
          errorMessage.value = 'You are already enrolled in this section.'
          return
        }

        // 4. Enroll the student
        const { data: enrollmentData, error: enrollmentError } = await supabase
          .from('student_sections')
          .insert({
            student_id: userId.value,
            section_id: sectionData.id,
            created_at: new Date().toISOString()
          })
          .select()

        console.log('Enrollment result:', enrollmentData, enrollmentError)

        if (enrollmentError) {
          console.error('Enrollment error:', enrollmentError)
          errorMessage.value = 'Failed to enroll in section. Please try again.'
          return
        }

        // Success!
        successMessage.value = `Successfully enrolled in ${sectionData.subjects.subject_name} - ${sectionData.section_name}!`
        
        // Redirect to student dashboard after a brief delay
        setTimeout(() => {
          router.push('/student-dashboard')
        }, 2000)
        
      } catch (error) {
        console.error('Error enrolling student:', error)
        errorMessage.value = 'An unexpected error occurred. Please try again.'
      } finally {
        isLoading.value = false
      }
    }

    // Go back to section selection
    const goBack = () => {
      router.push({
        name: 'SectionSelection',
        query: {
          classCode: classCode.value
        }
      })
    }

    return {
      sectionCode,
      isLoading,
      errorMessage,
      successMessage,
      selectedSection,
      handleSubmit,
      goBack
    }
  }
}
</script>

<style scoped>
/* Reset and ensure full viewport usage */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.auth-wrapper {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  width: 100vw;
  height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1rem;
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  overflow: auto;
}

.geometric-shapes {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  overflow: hidden;
  pointer-events: none;
  z-index: 0;
}

.geometric-shapes::before {
  content: '';
  position: absolute;
  top: -50%;
  right: -50%;
  width: 100%;
  height: 100%;
  background: linear-gradient(45deg, rgba(255, 255, 255, 0.1) 0%, transparent 50%);
  transform: rotate(45deg);
}

.geometric-shapes::after {
  content: '';
  position: absolute;
  bottom: -50%;
  left: -50%;
  width: 100%;
  height: 100%;
  background: linear-gradient(-45deg, rgba(255, 255, 255, 0.05) 0%, transparent 50%);
  transform: rotate(-45deg);
}

.floating-elements {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
  z-index: 1;
}

.floating-circle {
  position: absolute;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
}

.circle-1 {
  width: 120px;
  height: 120px;
  top: 10%;
  left: 10%;
  animation: float 6s ease-in-out infinite;
}

.circle-2 {
  width: 180px;
  height: 180px;
  top: 60%;
  right: 15%;
  animation: float 8s ease-in-out infinite reverse;
}

.circle-3 {
  width: 100px;
  height: 100px;
  bottom: 20%;
  left: 20%;
  animation: float 7s ease-in-out infinite;
}

@keyframes float {
  0%, 100% {
    transform: translateY(0px) rotate(0deg);
  }
  50% {
    transform: translateY(-30px) rotate(180deg);
  }
}

.auth-container {
  width: 100%;
  max-width: 480px;
  position: relative;
  z-index: 10;
  margin: 0 auto;
}

.auth-box {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border-radius: 24px;
  padding: 2.5rem;
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
  border: 1px solid rgba(255, 255, 255, 0.2);
  width: 100%;
  position: relative;
}

.logo-section {
  text-align: center;
  margin-bottom: 2rem;
}

.class-icon {
  width: 64px;
  height: 64px;
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 1.5rem;
  color: white;
  box-shadow: 0 8px 20px rgba(61, 141, 122, 0.3);
}

h1 {
  font-size: 2rem;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 0.5rem;
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.subtitle {
  color: #6b7280;
  font-size: 1rem;
  line-height: 1.5;
}

/* Class Preview */
.class-preview {
  margin-bottom: 2rem;
}

.class-card {
  background: rgba(61, 141, 122, 0.08);
  border: 2px solid rgba(61, 141, 122, 0.15);
  border-radius: 16px;
  padding: 20px;
  text-align: center;
}

.class-card h3 {
  color: #3D8D7A;
  font-size: 18px;
  font-weight: 700;
  margin-bottom: 8px;
}

.class-card p {
  color: rgba(61, 141, 122, 0.8);
  font-size: 14px;
  margin: 0;
}

/* Form Styles */
.auth-form-container {
  margin-bottom: 1.5rem;
}

.section-code-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.form-group {
  display: flex;
  flex-direction: column;
}

.form-group label {
  color: #374151;
  font-weight: 600;
  font-size: 0.9rem;
  margin-bottom: 0.75rem;
}

.input-wrapper {
  position: relative;
  display: flex;
  align-items: center;
}

.input-icon {
  position: absolute;
  left: 1rem;
  color: #9ca3af;
  z-index: 2;
  pointer-events: none;
}

.code-input {
  width: 100%;
  padding: 1rem 1rem 1rem 3rem;
  border: 2px solid rgba(209, 213, 219, 0.8);
  border-radius: 16px;
  font-size: 1rem;
  font-family: 'Courier New', monospace;
  text-transform: uppercase;
  text-align: center;
  letter-spacing: 1px;
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(10px);
  transition: all 0.3s ease;
}

.code-input:focus {
  outline: none;
  border-color: rgba(61, 141, 122, 0.6);
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
  background: rgba(255, 255, 255, 0.95);
}

.code-input:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

/* Help Section */
.help-section {
  margin-top: 1.5rem;
}

.help-card {
  background: rgba(59, 130, 246, 0.05);
  border: 2px solid rgba(59, 130, 246, 0.1);
  border-radius: 12px;
  padding: 1rem;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.75rem;
}

.help-icon {
  color: #3b82f6;
}

.help-card h4 {
  color: #1f2937;
  font-size: 1rem;
  font-weight: 600;
  margin: 0;
}

.help-card p {
  color: #6b7280;
  font-size: 0.875rem;
  line-height: 1.5;
  margin: 0;
}

/* Message Displays */
.error-display {
  background: rgba(239, 68, 68, 0.1);
  border: 2px solid rgba(239, 68, 68, 0.2);
  border-radius: 12px;
  padding: 1rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.error-icon {
  font-size: 1.25rem;
}

.error-display p {
  color: #dc2626;
  font-size: 0.9rem;
  margin: 0;
  font-weight: 500;
}

.success-display {
  background: rgba(34, 197, 94, 0.1);
  border: 2px solid rgba(34, 197, 94, 0.2);
  border-radius: 12px;
  padding: 1rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.success-icon {
  font-size: 1.25rem;
}

.success-display p {
  color: #059669;
  font-size: 0.9rem;
  margin: 0;
  font-weight: 500;
}

/* Buttons */
.auth-btn {
  width: 100%;
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: white;
  border: none;
  padding: 1rem 1.5rem;
  border-radius: 16px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  box-shadow: 0 4px 15px rgba(61, 141, 122, 0.2);
}

.auth-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(61, 141, 122, 0.3);
}

.auth-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
}

.back-button {
  width: 100%;
  background: rgba(107, 114, 128, 0.1);
  color: #4b5563;
  border: 2px solid rgba(107, 114, 128, 0.2);
  padding: 0.875rem 1.5rem;
  border-radius: 16px;
  font-size: 0.95rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  margin-top: 0.5rem;
}

.back-button:hover:not(:disabled) {
  background: rgba(107, 114, 128, 0.15);
  border-color: rgba(107, 114, 128, 0.3);
  transform: translateY(-1px);
}

.back-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Loading Spinner */
.loading-spinner {
  width: 18px;
  height: 18px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top: 2px solid white;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* Responsive Design */
@media (max-width: 640px) {
  .auth-wrapper {
    padding: 0.5rem;
  }
  
  .auth-box {
    padding: 2rem;
  }
  
  .auth-container {
    max-width: 100%;
  }
}

@media (max-width: 480px) {
  .auth-wrapper {
    padding: 0.25rem;
  }
  
  .auth-box {
    padding: 1.5rem;
    border-radius: 20px;
  }
  
  h1 {
    font-size: 1.75rem;
  }
  
  .class-icon {
    width: 56px;
    height: 56px;
  }
}
</style>