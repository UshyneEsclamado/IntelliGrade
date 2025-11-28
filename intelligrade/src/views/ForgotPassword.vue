<template>
  <div class="auth-wrapper">
    <!-- Geometric background shapes -->
    <div class="geometric-shapes">
      <!-- Educational floating elements -->
      <div class="floating-element element-1">
        <svg width="40" height="40" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M12,3L1,9L12,15L21,9V16H23V9M5,13.18V17.18L12,21L19,17.18V13.18L12,17L5,13.18Z"/>
        </svg>
      </div>
      
      <div class="floating-element element-2">
        <svg width="35" height="35" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M19,3H5C3.89,3 3,3.89 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5C21,3.89 20.1,3 19,3M13.5,16H10V15H13.5V16M13.5,14H10V13H13.5V14M14,10.5V9.5C14,8.1 12.9,7 11.5,7S9,8.1 9,9.5V10.5H8V12H16V10.5H14Z"/>
        </svg>
      </div>

      <div class="floating-element element-3">
        <svg width="32" height="32" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M20,8L12,13L4,8V6L12,11L20,6M20,4H4C2.89,4 2,4.89 2,6V18A2,2 0 0,0 4,20H20A2,2 0 0,0 22,18V6C22,5.89 21.1,4 20,4Z"/>
        </svg>
      </div>
    </div>
    
    <div class="auth-container">
      <div class="auth-box">
        <div class="header-section">
          <div class="logo-section">
            <div class="logo-icon">
              <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12,3L1,9L12,15L21,9V16H23V9M5,13.18V17.18L12,21L19,17.18V13.18L12,17L5,13.18Z"/>
              </svg>
            </div>
            <h1>IntelliGrade</h1>
          </div>
          <h2>Reset Your Password</h2>
          <p class="subtitle">Enter your email address and we'll send you a link to reset your password.</p>
        </div>

        <form @submit.prevent="submitEmail" class="auth-form">
          <div v-if="error" class="error-display">
            <p>{{ error }}</p>
          </div>

          <div class="form-group">
            <label>Email Address</label>
            <div class="input-wrapper">
              <svg class="input-icon" width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
                <path d="M20,8L12,13L4,8V6L12,11L20,6M20,4H4C2.89,4 2,4.89 2,6V18A2,2 0 0,0 4,20H20A2,2 0 0,0 22,18V6C22,5.89 21.1,4 20,4Z"/>
              </svg>
              <input 
                type="email" 
                placeholder="Enter your email" 
                v-model="email"
                required
              />
            </div>
          </div>

          <button type="submit" class="reset-btn" :disabled="loading">
            <svg v-if="!loading" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M20,8L12,13L4,8V6L12,11L20,6M20,4H4C2.89,4 2,4.89 2,6V18A2,2 0 0,0 4,20H20A2,2 0 0,0 22,18V6C22,5.89 21.1,4 20,4Z"/>
            </svg>
            <div v-else class="loading-spinner"></div>
            {{ loading ? 'Sending...' : 'Send Reset Link' }}
          </button>

          <div v-if="message" class="success-message">
            <p>{{ message }}</p>
            
            <!-- Development helper -->
            <div v-if="showDevHelper" class="dev-helper">
              <div class="dev-title">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M9,19L7,17L5,19V10A2,2 0 0,1 7,8H17A2,2 0 0,1 19,10V18A2,2 0 0,1 17,20H11L9,22V20Z"/>
                </svg>
                Development Mode
              </div>
              <p class="dev-instruction">Since we're in development mode, check the backend console for your reset link, or use the button below to get your reset link:</p>
              <button @click="getResetLink" class="dev-button" :disabled="gettingLink">
                <svg v-if="!gettingLink" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M10.59,13.41C11,13.8 11,14.4 10.59,14.81C10.2,15.2 9.6,15.2 9.19,14.81L7.77,13.39L9.19,12L10.59,13.41M14.5,4L16.04,5.54L4.5,17.08L2.96,15.54L14.5,4M15.41,7.41C15.8,7.8 16.4,7.8 16.81,7.41C17.2,7 17.2,6.4 16.81,6L15.41,4.58L14,6L15.41,7.41M18.08,10.59C18.5,11 19.1,11 19.5,10.59C19.9,10.2 19.9,9.6 19.5,9.19L18.08,7.77L16.67,9.19L18.08,10.59Z"/>
                </svg>
                <div v-else class="loading-spinner"></div>
                {{ gettingLink ? 'Getting Link...' : 'Get Reset Link for Testing' }}
              </button>
              
              <div v-if="resetLinkData" class="reset-link-display">
                <p><strong>Your reset link:</strong></p>
                <div class="link-box">
                  <input readonly :value="resetLinkData.reset_link" class="link-input" ref="linkInput"/>
                  <button @click="copyLink" class="copy-btn">
                    <svg v-if="!copied" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M19,21H8V7H19M19,5H8A2,2 0 0,0 6,7V21A2,2 0 0,0 8,23H19A2,2 0 0,0 21,21V7A2,2 0 0,0 19,5M16,1H4A2,2 0 0,0 2,3V17H4V3H16V1Z"/>
                    </svg>
                    <svg v-else width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M21,7L9,19L3.5,13.5L4.91,12.09L9,16.17L19.59,5.59L21,7Z"/>
                    </svg>
                  </button>
                </div>
                <p class="token-info">Use token: <code>{{ resetLinkData.token }}</code></p>
                <a :href="resetLinkData.reset_link" target="_blank" class="direct-link">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M14,3V5H17.59L7.76,14.83L9.17,16.24L19,6.41V10H21V3M19,19H5V5H12V3H5C3.89,3 3,3.9 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V12H19V19Z"/>
                  </svg>
                  Open Reset Page
                </a>
              </div>
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
  name: 'ForgotPassword',
  data() {
    return {
      email: '',
      loading: false,
      message: '',
      error: ''
    };
  },
  methods: {
    async submitEmail() {
      if (!this.email) {
        this.error = "Please enter your email address.";
        return;
      }

      // Clear previous messages
      this.loading = true;
      this.message = '';
      this.error = '';
      
      try {
        const { error } = await supabase.auth.resetPasswordForEmail(this.email, {
          redirectTo: 'http://localhost:5173/reset-password'
        });

        if (error) {
          throw error;
        }

        this.message = 'If your email exists in our system, a password reset link has been sent. Please check your inbox.';
        
      } catch (err) {
        console.error('Forgot password error:', err);
        this.error = err.message || 'Failed to send reset link. Please try again.';
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
  max-width: 400px;
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
  padding: 0.75rem 0.75rem 0.75rem 2.5rem;
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
  border-radius: 8px;
  padding: 0.75rem;
  margin-top: 0.5rem;
}

.success-message p {
  color: #16a34a;
  font-size: 0.75rem;
  margin: 0 0 1rem 0;
  font-weight: 500;
}

.dev-helper {
  margin-top: 1rem;
  padding: 1rem;
  background: rgba(59, 130, 246, 0.1);
  border: 1px solid rgba(59, 130, 246, 0.2);
  border-radius: 8px;
  text-align: left;
}

.dev-title {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-weight: 600;
  color: #1d4ed8;
  margin-bottom: 0.5rem;
  font-size: 0.8rem;
}

.dev-instruction {
  color: #374151;
  font-size: 0.75rem;
  margin-bottom: 1rem;
  line-height: 1.4;
}

.dev-button {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: linear-gradient(135deg, #1d4ed8 0%, #3b82f6 100%);
  color: white;
  border: none;
  padding: 0.6rem 1rem;
  border-radius: 6px;
  font-size: 0.75rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-bottom: 1rem;
}

.dev-button:hover:not(:disabled) {
  transform: translateY(-1px);
  box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
}

.dev-button:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.reset-link-display {
  background: rgba(255, 255, 255, 0.8);
  padding: 1rem;
  border-radius: 6px;
  border: 1px solid rgba(59, 130, 246, 0.2);
}

.reset-link-display p {
  color: #374151;
  font-size: 0.75rem;
  margin-bottom: 0.5rem;
  font-weight: 500;
}

.link-box {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.link-input {
  flex: 1;
  padding: 0.5rem;
  border: 1px solid rgba(59, 130, 246, 0.3);
  border-radius: 4px;
  font-size: 0.7rem;
  color: #374151;
  background: white;
}

.copy-btn {
  padding: 0.5rem;
  background: linear-gradient(135deg, #10b981 0%, #34d399 100%);
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}

.copy-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 2px 8px rgba(16, 185, 129, 0.3);
}

.token-info {
  margin: 0.5rem 0;
}

.token-info code {
  background: rgba(59, 130, 246, 0.1);
  padding: 0.2rem 0.4rem;
  border-radius: 3px;
  font-family: 'Courier New', monospace;
  font-size: 0.7rem;
  color: #1d4ed8;
}

.direct-link {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  color: #1d4ed8;
  text-decoration: none;
  font-size: 0.75rem;
  font-weight: 600;
  transition: all 0.3s ease;
  padding: 0.5rem;
  border-radius: 4px;
  background: rgba(59, 130, 246, 0.1);
}

.direct-link:hover {
  background: rgba(59, 130, 246, 0.2);
  transform: translateY(-1px);
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
