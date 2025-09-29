<template>
  <div class="auth-wrapper" :class="{ 'dark-mode': isDarkMode }">
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
          <h1>Enter Class Code</h1>
          <p class="subtitle">Enter the class code provided by your teacher</p>
        </div>

        <!-- Class Code Form -->
        <div class="code-form-container">
          <form @submit.prevent="handleSubmit" class="code-form">
            <div class="form-group">
              <label>Class Code</label>
              <div class="input-wrapper">
                <svg class="input-icon" width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M9,7H15L13.5,5.5L14.92,4.08L18.84,8L14.92,11.92L13.5,10.5L15,9H9A4,4 0 0,0 5,13A4,4 0 0,0 9,17H13V19H9A6,6 0 0,1 3,13A6,6 0 0,1 9,7Z"/>
                </svg>
                <input 
                  type="text" 
                  placeholder="Enter class code (e.g., MATH101)" 
                  v-model="classCode"
                  @input="formatClassCode"
                  required
                  :disabled="isLoading"
                />
              </div>
            </div>

            <!-- Error Message -->
            <div v-if="error" class="error-message">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path d="M13,13H11V7H13M13,17H11V15H13M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2Z"/>
              </svg>
              {{ error }}
            </div>

            <!-- Success Message -->
            <div v-if="successMessage" class="success-message">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12,2A10,10 0 0,1 22,12A10,10 0 0,1 12,22A10,10 0 0,1 2,12A10,10 0 0,1 12,2M11,16.5L18,9.5L16.59,8.09L11,13.67L7.41,10.09L6,11.5L11,16.5Z"/>
              </svg>
              {{ successMessage }}
            </div>

            <button 
              type="submit" 
              class="submit-btn"
              :disabled="isLoading || !classCode.trim()"
            >
              <svg v-if="!isLoading" width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                <path d="M9,20.42L2.79,14.21L5.62,11.38L9,14.77L18.88,4.88L21.71,7.71L9,20.42Z"/>
              </svg>
              <div v-if="isLoading" class="spinner"></div>
              {{ isLoading ? 'Validating...' : 'Continue' }}
            </button>
          </form>

          <!-- Help Section -->
          <div class="help-section">
            <div class="help-card">
              <div class="help-icon">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M11,18H13V16H11V18M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,20C7.59,20 4,16.41 4,12C4,7.59 7.59,4 12,4C16.41,4 20,7.59 20,12C20,16.41 16.41,20 12,20M12,6A4,4 0 0,0 8,10H10A2,2 0 0,1 12,8A2,2 0 0,1 14,10C14,12 11,11.75 11,15H13C13,12.75 16,12.5 16,10A4,4 0 0,0 12,6Z"/>
                </svg>
              </div>
              <div class="help-content">
                <h4>Need Help?</h4>
                <p>Ask your teacher for the class code. It usually looks like "MATH101", "ENG2024", or similar format.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Back Button -->
        <div class="back-section">
          <button class="back-link" @click="goBack">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z"/>
            </svg>
            Back to Login
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { supabase } from "../../supabase.js";

export default {
  name: "ClassCodeEntry",
  data() {
    return {
      classCode: "",
      isLoading: false,
      error: null,
      successMessage: null,
    };
  },
  methods: {
    formatClassCode() {
      // Convert to uppercase and remove spaces
      this.classCode = this.classCode.toUpperCase().replace(/\s/g, '');
      // Clear any existing errors when user types
      this.error = null;
      this.successMessage = null;
    },

    async handleSubmit() {
      if (!this.classCode.trim()) {
        this.error = "Please enter a class code.";
        return;
      }

      this.isLoading = true;
      this.error = null;
      this.successMessage = null;

      try {
        // Check if class code exists in the database
        const { data: classData, error: classError } = await supabase
          .from("classes")
          .select("id, name, teacher_id, class_code")
          .eq("class_code", this.classCode)
          .single();

        if (classError && classError.code === 'PGRST116') {
          // No class found with this code
          this.error = "Invalid class code. Please check with your teacher and try again.";
          return;
        }

        if (classError) {
          throw classError;
        }

        // Get current user
        const { data: { user } } = await supabase.auth.getUser();
        
        if (!user) {
          this.error = "Please log in first.";
          this.$router.push("/join-class");
          return;
        }

        // Check if student is already enrolled in this class
        const { data: existingEnrollment, error: enrollmentCheckError } = await supabase
          .from("enrollments")
          .select("id")
          .eq("student_id", user.id)
          .eq("class_id", classData.id)
          .single();

        if (existingEnrollment) {
          this.error = "You are already enrolled in this class.";
          return;
        }

        if (enrollmentCheckError && enrollmentCheckError.code !== 'PGRST116') {
          throw enrollmentCheckError;
        }

        // Success! Class code is valid and student can join
        this.successMessage = `Class "${classData.name}" found! Proceeding to section selection...`;
        
        // Store class data in session storage or pass as route params
        sessionStorage.setItem('selectedClass', JSON.stringify(classData));
        
        // Redirect to section selection after a short delay
        setTimeout(() => {
          this.$router.push("/join-class/select-section");
        }, 1500);

      } catch (err) {
        console.error("Class code validation error:", err);
        this.error = err.message || "Something went wrong. Please try again.";
      } finally {
        this.isLoading = false;
      }
    },

    goBack() {
      this.$router.push("/login");
    },
  },

  mounted() {
    // Check if user is authenticated
    const checkAuth = async () => {
      const { data: { user } } = await supabase.auth.getUser();
      if (!user) {
        // Redirect to join class auth if not authenticated
        this.$router.push("/join-class");
      }
    };
    
    checkAuth();
  }
};
</script>

<style scoped>
/* Base styles - inherited from JoinClassAuth component */
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

.geometric-shapes::before {
  content: '';
  position: absolute;
  width: 100%;
  height: 100%;
  background: 
    linear-gradient(45deg, transparent 48%, rgba(255,255,255,0.05) 50%, transparent 52%) 0 0 / 80px 80px,
    linear-gradient(-45deg, transparent 48%, rgba(255,255,255,0.05) 50%, transparent 52%) 0 0 / 80px 80px,
    radial-gradient(circle at 20% 30%, rgba(255,255,255,0.08) 0, transparent 60px),
    radial-gradient(circle at 80% 20%, rgba(255,255,255,0.08) 0, transparent 80px),
    radial-gradient(circle at 10% 80%, rgba(255,255,255,0.08) 0, transparent 70px),
    radial-gradient(circle at 90% 70%, rgba(255,255,255,0.08) 0, transparent 90px);
  animation: moveBackground 40s linear infinite;
}

.geometric-shapes::after {
  content: '';
  position: absolute;
  inset: 0;
  background:
    radial-gradient(circle at 15% 25%, rgba(255,255,255,0.1) 0, transparent 250px),
    radial-gradient(circle at 85% 75%, rgba(255,255,255,0.1) 0, transparent 250px),
    radial-gradient(circle at 50% 50%, rgba(255,255,255,0.05) 0, transparent 400px);
  animation: floatShapes 25s ease-in-out infinite;
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
  animation-delay: 0s; 
}

.circle-2 { 
  width: 140px; 
  height: 140px; 
  background: #A3D1C6; 
  bottom: 20%; 
  right: 15%; 
  animation-delay: 3s; 
}

.circle-3 { 
  width: 120px; 
  height: 120px; 
  background: #B3D8A8; 
  top: 60%; 
  left: 70%; 
  animation-delay: 6s; 
}

.auth-container {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  max-width: 500px;
  z-index: 1;
  position: relative;
}

.auth-box {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  padding: 50px 45px;
  border-radius: 24px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  box-shadow: 
    0 25px 50px rgba(61, 141, 122, 0.08),
    0 10px 30px rgba(0, 0, 0, 0.04),
    inset 0 1px 0 rgba(255, 255, 255, 0.9);
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

/* Code Form Styles */
.code-form-container {
  text-align: left;
}

.form-group {
  margin-bottom: 25px;
}

.form-group label {
  display: block;
  color: #3D8D7A;
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 12px;
  letter-spacing: 0.2px;
  text-align: center;
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
  padding: 22px 18px 22px 55px;
  font-size: 18px;
  font-weight: 600;
  border: 2px solid rgba(61, 141, 122, 0.15);
  border-radius: 16px;
  outline: none;
  background: rgba(255, 255, 255, 0.9);
  color: #3D8D7A;
  transition: all 0.3s ease;
  text-align: center;
  letter-spacing: 2px;
  text-transform: uppercase;
}

input:focus {
  border-color: rgba(61, 141, 122, 0.4);
  box-shadow: 0 0 0 6px rgba(61, 141, 122, 0.08);
  background: white;
}

input::placeholder {
  color: rgba(61, 141, 122, 0.45);
  font-size: 16px;
  font-weight: 400;
  letter-spacing: 1px;
  text-transform: none;
}

.submit-btn {
  width: 100%;
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: white;
  padding: 20px;
  font-size: 18px;
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

.submit-btn:hover:not(:disabled) {
  transform: translateY(-3px);
  box-shadow: 0 12px 30px rgba(61, 141, 122, 0.25);
}

.submit-btn:active:not(:disabled) {
  transform: translateY(-1px);
}

.submit-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.spinner {
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

/* Message Styles */
.error-message,
.success-message {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 16px;
  border-radius: 12px;
  font-size: 14px;
  font-weight: 500;
  margin-bottom: 20px;
}

.error-message {
  background: rgba(239, 68, 68, 0.1);
  color: #dc2626;
  border: 1px solid rgba(239, 68, 68, 0.2);
}

.success-message {
  background: rgba(34, 197, 94, 0.1);
  color: #16a34a;
  border: 1px solid rgba(34, 197, 94, 0.2);
}

/* Help Section */
.help-section {
  margin: 30px 0;
}

.help-card {
  background: rgba(61, 141, 122, 0.05);
  border: 1px solid rgba(61, 141, 122, 0.1);
  border-radius: 16px;
  padding: 20px;
  display: flex;
  align-items: flex-start;
  gap: 15px;
}

.help-icon {
  width: 40px;
  height: 40px;
  background: rgba(61, 141, 122, 0.1);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #3D8D7A;
  flex-shrink: 0;
}

.help-content h4 {
  color: #3D8D7A;
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 5px;
}

.help-content p {
  color: rgba(61, 141, 122, 0.7);
  font-size: 14px;
  line-height: 1.5;
  margin: 0;
}

/* Back Section */
.back-section {
  text-align: center;
  margin-top: 25px;
}

.back-link {
  color: rgba(61, 141, 122, 0.7);
  background: none;
  border: none;
  font-size: 16px;
  font-weight: 500;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  transition: all 0.3s ease;
  padding: 8px 16px;
  border-radius: 8px;
  cursor: pointer;
}

.back-link:hover {
  color: #3D8D7A;
  background: rgba(61, 141, 122, 0.05);
}

/* Animations */
@keyframes float {
  0%, 100% { 
    transform: translateY(0) rotate(0deg); 
  }
  50% { 
    transform: translateY(-25px) rotate(180deg); 
  }
}

@keyframes moveBackground {
  0% {
    transform: translate(0, 0) rotate(0deg);
  }
  100% {
    transform: translate(-80px, -80px) rotate(3deg);
  }
}

@keyframes floatShapes {
  0%, 100% {
    transform: translate(0, 0);
  }
  50% {
    transform: translate(30px, 30px);
  }
}

/* Responsive */
@media (max-width: 768px) {
  .auth-wrapper {
    padding: 25px;
  }
  
  .auth-box {
    padding: 40px 30px;
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

  input {
    padding: 18px 16px 18px 50px;
    font-size: 16px;
  }

  .input-icon {
    left: 16px;
  }

  .submit-btn {
    font-size: 16px;
    padding: 18px;
  }

  .help-card {
    padding: 16px;
    gap: 12px;
  }

  .help-icon {
    width: 35px;
    height: 35px;
  }
}

@media (max-height: 700px) {
  .auth-wrapper {
    align-items: flex-start;
    padding-top: 30px;
  }
}
</style>