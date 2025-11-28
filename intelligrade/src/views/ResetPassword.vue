<template>
  <div class="auth-wrapper">
    <!-- Geometric background shapes -->
    <div class="geometric-shapes">
      <!-- Educational floating elements -->
      <div class="floating-element element-1">
        <svg width="40" height="40" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M12,17A2,2 0 0,0 14,15C14,13.89 13.1,13 12,13A2,2 0 0,0 10,15A2,2 0 0,0 12,17M18,8A2,2 0 0,1 20,10V20A2,2 0 0,1 18,22H6A2,2 0 0,1 4,20V10C4,8.89 4.9,8 6,8H7V6A5,5 0 0,1 12,1A5,5 0 0,1 17,6V8H18M12,3A3,3 0 0,0 9,6V8H15V6A3,3 0 0,0 12,3Z"/>
        </svg>
      </div>
      
      <div class="floating-element element-2">
        <svg width="35" height="35" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M9,22A1,1 0 0,1 8,21V18H4A2,2 0 0,1 2,16V4C2,2.89 2.9,2 4,2H20A2,2 0 0,1 22,4V16A2,2 0 0,1 20,18H13.9L10.2,21.71C10,21.9 9.75,22 9.5,22V22H9M10,16V19.08L13.08,16H20V4H4V16H10Z"/>
        </svg>
      </div>

      <div class="floating-element element-3">
        <svg width="32" height="32" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M17,7H22V17H17V19A1,1 0 0,0 18,20H20V22H17.5C16.95,22 16,21.55 16,21C16,21.55 15.05,22 14.5,22H12V20H14A1,1 0 0,0 15,19V5A1,1 0 0,0 14,4H12V2H14.5C15.05,2 16,2.45 16,3C16,2.45 16.95,2 17.5,2H20V4H18A1,1 0 0,0 17,5V7Z"/>
        </svg>
      </div>
    </div>
    
    <div class="auth-container">
      <div class="auth-box">
        <div class="header-section">
          <div class="logo-section">
            <div class="logo-icon">
              <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12,17A2,2 0 0,0 14,15C14,13.89 13.1,13 12,13A2,2 0 0,0 10,15A2,2 0 0,0 12,17M18,8A2,2 0 0,1 20,10V20A2,2 0 0,1 18,22H6A2,2 0 0,1 4,20V10C4,8.89 4.9,8 6,8H7V6A5,5 0 0,1 12,1A5,5 0 0,1 17,6V8H18M12,3A3,3 0 0,0 9,6V8H15V6A3,3 0 0,0 12,3Z"/>
              </svg>
            </div>
            <h1>IntelliGrade</h1>
          </div>
          <h2>Create New Password</h2>
          <p class="subtitle">Enter your new password below. Make sure it's strong and secure.</p>
        </div>

        <form @submit.prevent="submitReset" class="auth-form">
          <div v-if="error" class="error-display">
            <p>{{ error }}</p>
          </div>

          <div class="form-group">
            <label>New Password</label>
            <div class="input-wrapper">
              <svg class="input-icon" width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12,17A2,2 0 0,0 14,15C14,13.89 13.1,13 12,13A2,2 0 0,0 10,15A2,2 0 0,0 12,17M18,8A2,2 0 0,1 20,10V20A2,2 0 0,1 18,22H6A2,2 0 0,1 4,20V10C4,8.89 4.9,8 6,8H7V6A5,5 0 0,1 12,1A5,5 0 0,1 17,6V8H18M12,3A3,3 0 0,0 9,6V8H15V6A3,3 0 0,0 12,3Z"/>
              </svg>
              <input 
                :type="showPassword ? 'text' : 'password'"
                placeholder="Enter your new password" 
                v-model="password"
                required
                minlength="6"
              />
              <button 
                type="button" 
                class="password-toggle"
                @click="togglePasswordVisibility"
                tabindex="-1"
              >
                <svg v-if="!showPassword" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12,9A3,3 0 0,1 15,12A3,3 0 0,1 12,15A3,3 0 0,1 9,12A3,3 0 0,1 12,9M12,4.5C17,4.5 21.27,7.61 23,12C21.27,16.39 17,19.5 12,19.5C7,19.5 2.73,16.39 1,12C2.73,7.61 7,4.5 12,4.5M12,7A5,5 0 0,0 7,12A5,5 0 0,0 12,17A5,5 0 0,0 17,12A5,5 0 0,0 12,7Z"/>
                </svg>
                <svg v-else width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M2,5.27L3.28,4L20,20.72L18.73,22L15.65,18.92C14.5,19.3 13.28,19.5 12,19.5C7,19.5 2.73,16.39 1,12C1.69,10.24 2.79,8.69 4.19,7.46L2,5.27M12,9A3,3 0 0,1 15,12C15,12.35 14.94,12.69 14.83,13L11,9.17C11.31,9.06 11.65,9 12,9M12,4.5C17,4.5 21.27,7.61 23,12C22.18,14.08 20.79,15.88 19,17.19L17.58,15.76C18.94,14.82 20.06,13.54 20.82,12C19.17,8.64 15.76,6.5 12,6.5C10.91,6.5 9.84,6.68 8.84,7L7.3,5.47C8.74,4.85 10.34,4.5 12,4.5M3.18,12C4.83,15.36 8.24,17.5 12,17.5C12.69,17.5 13.37,17.43 14,17.29L11.72,15C10.29,14.85 9.15,13.71 9,12.28L5.6,8.87C4.61,9.72 3.78,10.78 3.18,12Z"/>
                </svg>
              </button>
            </div>
          </div>

          <div class="form-group">
            <label>Confirm New Password</label>
            <div class="input-wrapper">
              <svg class="input-icon" width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12,17A2,2 0 0,0 14,15C14,13.89 13.1,13 12,13A2,2 0 0,0 10,15A2,2 0 0,0 12,17M18,8A2,2 0 0,1 20,10V20A2,2 0 0,1 18,22H6A2,2 0 0,1 4,20V10C4,8.89 4.9,8 6,8H7V6A5,5 0 0,1 12,1A5,5 0 0,1 17,6V8H18M12,3A3,3 0 0,0 9,6V8H15V6A3,3 0 0,0 12,3Z"/>
              </svg>
              <input 
                :type="showConfirmPassword ? 'text' : 'password'"
                placeholder="Confirm your new password" 
                v-model="confirmPassword"
                required
                minlength="6"
              />
              <button 
                type="button" 
                class="password-toggle"
                @click="toggleConfirmPasswordVisibility"
                tabindex="-1"
              >
                <svg v-if="!showConfirmPassword" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12,9A3,3 0 0,1 15,12A3,3 0 0,1 12,15A3,3 0 0,1 9,12A3,3 0 0,1 12,9M12,4.5C17,4.5 21.27,7.61 23,12C21.27,16.39 17,19.5 12,19.5C7,19.5 2.73,16.39 1,12C2.73,7.61 7,4.5 12,4.5M12,7A5,5 0 0,0 7,12A5,5 0 0,0 12,17A5,5 0 0,0 17,12A5,5 0 0,0 12,7Z"/>
                </svg>
                <svg v-else width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M2,5.27L3.28,4L20,20.72L18.73,22L15.65,18.92C14.5,19.3 13.28,19.5 12,19.5C7,19.5 2.73,16.39 1,12C1.69,10.24 2.79,8.69 4.19,7.46L2,5.27M12,9A3,3 0 0,1 15,12C15,12.35 14.94,12.69 14.83,13L11,9.17C11.31,9.06 11.65,9 12,9M12,4.5C17,4.5 21.27,7.61 23,12C22.18,14.08 20.79,15.88 19,17.19L17.58,15.76C18.94,14.82 20.06,13.54 20.82,12C19.17,8.64 15.76,6.5 12,6.5C10.91,6.5 9.84,6.68 8.84,7L7.3,5.47C8.74,4.85 10.34,4.5 12,4.5M3.18,12C4.83,15.36 8.24,17.5 12,17.5C12.69,17.5 13.37,17.43 14,17.29L11.72,15C10.29,14.85 9.15,13.71 9,12.28L5.6,8.87C4.61,9.72 3.78,10.78 3.18,12Z"/>
                </svg>
              </button>
            </div>
          </div>

          <button type="submit" class="reset-btn" :disabled="loading || !isValidForm">
            <svg v-if="!loading" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M21,7L9,19L3.5,13.5L4.91,12.09L9,16.17L19.59,5.59L21,7Z"/>
            </svg>
            <div v-else class="loading-spinner"></div>
            {{ loading ? 'Resetting...' : 'Reset Password' }}
          </button>

          <div v-if="message" class="success-message">
            <div class="success-icon">
              <svg width="48" height="48" viewBox="0 0 24 24" fill="#4A9B8E">
                <path d="M21,7L9,19L3.5,13.5L4.91,12.09L9,16.17L19.59,5.59L21,7Z"/>
              </svg>
            </div>
            <h3 class="success-title">Password Reset Successful! 🎉</h3>
            <p class="success-text">{{ message }}</p>
            <p class="success-subtext">You can now access your account with your new password.</p>
            
            <div class="action-buttons">
              <router-link to="/teacher-dashboard" class="dashboard-btn primary">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M13,3V9H21V3M13,21H21V11H13M3,21H11V15H3M3,13H11V3H3V13Z"/>
                </svg>
                Go to Dashboard
              </router-link>
              
              <router-link to="/login" class="login-btn secondary">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M10,17V14H3V10H10V7L15,12L10,17M10,2H19A2,2 0 0,1 21,4V20A2,2 0 0,1 19,22H10A2,2 0 0,1 8,20V18H10V20H19V4H10V6H8V4A2,2 0 0,1 10,2Z"/>
                </svg>
                Go to Login
              </router-link>
            </div>
          </div>
        </form>

        <div class="back-section">
          <router-link to="/login" class="back-link">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z"/>
            </svg>
            Back to Login
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { supabase } from '@/supabase.js';

export default {
  name: 'ResetPassword',
  data() {
    return {
      password: '',
      confirmPassword: '',
      showPassword: false,
      showConfirmPassword: false,
      loading: false,
      message: '',
      error: ''
    };
  },
  computed: {
    isValidForm() {
      return this.password && 
             this.confirmPassword && 
             this.password === this.confirmPassword && 
             this.password.length >= 6;
    }
  },
  async mounted() {
    // Supabase sends the access_token as a URL hash parameter
    // We need to check if this is a password recovery session
    const { data: { session }, error } = await supabase.auth.getSession();
    
    if (error || !session) {
      this.error = 'Invalid or missing reset token. Please request a new password reset.';
    }
  },
  methods: {
    togglePasswordVisibility() {
      this.showPassword = !this.showPassword;
    },
    
    toggleConfirmPasswordVisibility() {
      this.showConfirmPassword = !this.showConfirmPassword;
    },
    
    async submitReset() {
      if (!this.isValidForm) {
        this.error = 'Please fill in all fields correctly.';
        return;
      }

      if (this.password !== this.confirmPassword) {
        this.error = 'Passwords do not match.';
        return;
      }

      this.loading = true;
      this.message = '';
      this.error = '';
      
      try {
        // Update the user's password using Supabase
        const { data, error } = await supabase.auth.updateUser({
          password: this.password
        });

        if (error) {
          throw error;
        }

        this.message = 'Your password has been reset successfully!';
        
      } catch (err) {
        console.error('Reset password error:', err);
        this.error = err.message || 'Failed to reset password. Please try again or request a new reset link.';
      } finally {
        this.loading = false;
      }
    }
  }
};
</script>

<style scoped>
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
  background: transparent !important;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1rem;
  font-family: 'Inter', sans-serif;
  overflow: hidden;
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
    linear-gradient(45deg, transparent 48%, rgba(255,255,255,0.08) 50%, transparent 52%) 0 0 / 60px 60px,
    linear-gradient(-45deg, transparent 48%, rgba(255,255,255,0.08) 50%, transparent 52%) 0 0 / 60px 60px,
    radial-gradient(circle at 20% 30%, rgba(255,255,255,0.12) 0, transparent 40px),
    radial-gradient(circle at 80% 20%, rgba(255,255,255,0.12) 0, transparent 60px),
    radial-gradient(circle at 60% 80%, rgba(255,255,255,0.08) 0, transparent 50px);
  mix-blend-mode: overlay;
}

/* Floating educational elements */
.floating-element {
  position: absolute;
  opacity: 0.6;
  animation: educationalFloat 15s ease-in-out infinite;
  z-index: 1;
}

.element-1 {
  top: 15%;
  left: 10%;
  animation-delay: 0s;
}

.element-2 {
  top: 60%;
  right: 15%;
  animation-delay: -5s;
}

.element-3 {
  bottom: 20%;
  left: 20%;
  animation-delay: -10s;
}

@keyframes educationalFloat {
  0%, 100% { 
    transform: translateY(0px) translateX(0px) rotate(0deg); 
    opacity: 0.6;
  }
  20% { 
    transform: translateY(-20px) translateX(10px) rotate(5deg); 
    opacity: 0.8;
  }
  50% { 
    transform: translateY(-40px) translateX(-5px) rotate(-3deg); 
    opacity: 0.7;
  }
  80% { 
    transform: translateY(-10px) translateX(15px) rotate(2deg); 
    opacity: 0.9;
  }
}

.auth-container {
  position: relative;
  z-index: 10;
  width: 100%;
  max-width: 450px;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border-radius: 20px;
  box-shadow: 
    0 25px 50px rgba(61, 141, 122, 0.15),
    0 0 0 1px rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(163, 209, 198, 0.3);
}

.auth-box {
  padding: 2rem;
}

.header-section {
  text-align: center;
  margin-bottom: 2rem;
}

.logo-section {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.75rem;
  margin-bottom: 1.5rem;
}

.logo-icon {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  box-shadow: 0 8px 20px rgba(61, 141, 122, 0.2);
}

.header-section h1 {
  font-size: 1.75rem;
  font-weight: 700;
  background: linear-gradient(135deg, #3D8D7A 0%, #5ba394 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin: 0;
}

.header-section h2 {
  font-size: 1.4rem;
  font-weight: 600;
  color: #3D8D7A;
  margin-bottom: 0.5rem;
}

.subtitle {
  font-size: 0.85rem;
  color: rgba(61, 141, 122, 0.7);
  line-height: 1.4;
}

.auth-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.form-group label {
  font-size: 0.8rem;
  font-weight: 600;
  color: #3D8D7A;
  margin-bottom: 0.25rem;
}

.input-wrapper {
  position: relative;
  display: flex;
  align-items: center;
}

.input-icon {
  position: absolute;
  left: 0.75rem;
  color: rgba(61, 141, 122, 0.5);
  z-index: 2;
}

input {
  width: 100%;
  padding: 0.75rem 3rem 0.75rem 2.5rem;
  font-size: 0.85rem;
  border: 2px solid rgba(61, 141, 122, 0.2);
  border-radius: 9px;
  outline: none;
  background: rgba(255, 255, 255, 0.8);
  color: #3D8D7A;
  transition: all 0.3s ease;
  font-weight: 500;
}

input:focus {
  border-color: rgba(61, 141, 122, 0.5);
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
  background: white;
}

input::placeholder {
  color: rgba(61, 141, 122, 0.4);
  font-size: 0.8rem;
  font-weight: 400;
}

.password-toggle {
  position: absolute;
  right: 0.75rem;
  background: none;
  border: none;
  color: rgba(61, 141, 122, 0.6);
  cursor: pointer;
  padding: 0.25rem;
  border-radius: 4px;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 2;
}

.password-toggle:hover {
  color: #3D8D7A;
  background: rgba(61, 141, 122, 0.1);
}

.password-toggle:focus {
  outline: none;
  box-shadow: 0 0 0 2px rgba(61, 141, 122, 0.2);
}

.reset-btn {
  width: 100%;
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: white;
  padding: 0.75rem;
  font-size: 0.85rem;
  font-weight: 600;
  border: none;
  border-radius: 9px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.4rem;
  margin-top: 0.5rem;
  box-shadow: 0 4px 15px rgba(61, 141, 122, 0.2);
}

.reset-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(61, 141, 122, 0.3);
}

.reset-btn:active:not(:disabled) {
  transform: translateY(-1px);
}

.reset-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.loading-spinner {
  width: 14px;
  height: 14px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top: 2px solid white;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.error-display {
  background: rgba(239, 68, 68, 0.1);
  border: 1px solid rgba(239, 68, 68, 0.2);
  border-radius: 8px;
  padding: 0.75rem;
  margin-bottom: 0.5rem;
}

.error-display p {
  color: #dc2626;
  font-size: 0.75rem;
  margin: 0;
  font-weight: 500;
}

.success-message {
  background: rgba(34, 197, 94, 0.1);
  border: 1px solid rgba(34, 197, 94, 0.2);
  border-radius: 12px;
  padding: 2rem 1.5rem;
  margin-top: 1rem;
  text-align: center;
}

.success-icon {
  margin-bottom: 1rem;
  display: flex;
  justify-content: center;
}

.success-title {
  color: #16a34a;
  font-size: 1.25rem;
  font-weight: 600;
  margin: 0 0 0.5rem 0;
}

.success-text {
  color: #16a34a;
  font-size: 0.875rem;
  margin: 0 0 0.5rem 0;
  font-weight: 500;
}

.success-subtext {
  color: #666;
  font-size: 0.8rem;
  margin: 0 0 1.5rem 0;
}

.action-buttons {
  display: flex;
  gap: 0.75rem;
  justify-content: center;
  flex-wrap: wrap;
}

.dashboard-btn, .login-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 600;
  font-size: 0.875rem;
  transition: all 0.2s ease;
  border: 2px solid transparent;
}

.dashboard-btn.primary {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: white;
}

.dashboard-btn.primary:hover {
  transform: translateY(-1px);
  box-shadow: 0 8px 25px rgba(61, 141, 122, 0.3);
}

.login-btn.secondary {
  background: transparent;
  color: #3D8D7A;
  border-color: #3D8D7A;
}

.login-btn.secondary:hover {
  background: #3D8D7A;
  color: white;
  transform: translateY(-1px);
}

.login-redirect {
  margin-top: 1rem;
}

.login-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: linear-gradient(135deg, #16a34a 0%, #22c55e 100%);
  color: white;
  text-decoration: none;
  padding: 0.6rem 1.5rem;
  border-radius: 8px;
  font-size: 0.8rem;
  font-weight: 600;
  transition: all 0.3s ease;
  box-shadow: 0 2px 10px rgba(34, 197, 94, 0.2);
}

.login-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 15px rgba(34, 197, 94, 0.3);
}

.back-section {
  margin-top: 1.5rem;
  text-align: center;
}

.back-link {
  color: #3D8D7A;
  font-size: 0.8rem;
  text-decoration: none;
  font-weight: 500;
  transition: all 0.3s ease;
  padding-bottom: 2px;
  border-bottom: 2px solid transparent;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
}

.back-link:hover {
  border-bottom-color: rgba(61, 141, 122, 0.5);
}

/* Responsive design */
@media (max-width: 768px) {
  .auth-wrapper {
    padding: 1rem;
  }
  
  .auth-box {
    padding: 1.5rem;
  }
  
  .header-section h1 {
    font-size: 1.5rem;
  }
  
  .header-section h2 {
    font-size: 1.2rem;
  }
}
</style>
