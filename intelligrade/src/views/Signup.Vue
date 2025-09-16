<template>
  <div class="auth-wrapper">
    <div class="geometric-shapes"></div>
    <div class="floating-elements">
      <div class="floating-circle circle-1"></div>
      <div class="floating-circle circle-2"></div>
      <div class="floating-circle circle-3"></div>
    </div>
    
    <div class="auth-container">
      <!-- Logo Space - Left Side -->
      <div class="logo-space">
        <div class="logo-placeholder">
          <div class="logo-icon">
            <svg width="180" height="180" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 2C13.1 2 14 2.9 14 4C14 5.1 13.1 6 12 6C10.9 6 10 5.1 10 4C10 2.9 10.9 2 12 2ZM19 7V9L15 13L11 9L7 11V9L11 7L15 11L19 7ZM5 13L9 17L15 11L21 17H3L5 13ZM9 19V21H15V19H9Z"/>
            </svg>
          </div>
          <h2>IntelliGrade</h2>
          <p>Empower your teaching with AI</p>
        </div>
      </div>
      
      <!-- Signup Box - Right Side -->
      <div class="auth-box">
        <div class="logo-section">
          <div class="user-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor">
              <path d="M17,14H19V17H22V19H19V22H17V19H14V17H17V14M12,3A4,4 0 0,1 16,7A4,4 0 0,1 12,11A4,4 0 0,1 8,7A4,4 0 0,1 12,3M12,13C16.42,13 20,14.79 20,17V20H4V17C4,14.79 7.58,13 12,13Z"/>
            </svg>
          </div>
          <h1>Join IntelliGrade</h1>
          <p class="subtitle">Create your teacher account</p>
        </div>

        <form @submit.prevent="handleSignup" class="signup-form">
          <div class="form-group">
            <label>Full Name</label>
            <div class="input-wrapper">
              <svg class="input-icon" width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12,4A4,4 0 0,1 16,8A4,4 0 0,1 12,12A4,4 0 0,1 8,8A4,4 0 0,1 12,4M12,14C16.42,14 20,15.79 20,18V20H4V18C4,15.79 7.58,14 12,14Z"/>
              </svg>
              <input 
                type="text" 
                placeholder="Enter your full name" 
                v-model="fullName"
                required
              />
            </div>
          </div>

          <div class="form-group">
            <label>Email</label>
            <div class="input-wrapper">
              <svg class="input-icon" width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
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

          <div class="form-group">
            <label>Password</label>
            <div class="input-wrapper">
              <svg class="input-icon" width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12,17A2,2 0 0,0 14,15C14,13.89 13.1,13 12,13A2,2 0 0,0 10,15A2,2 0 0,0 12,17M18,8A2,2 0 0,1 20,10V20A2,2 0 0,1 18,22H6A2,2 0 0,1 4,20V10C4,8.89 4.9,8 6,8H7V6A5,5 0 0,1 12,1A5,5 0 0,1 17,6V8H18M12,3A3,3 0 0,0 9,6V8H15V6A3,3 0 0,0 12,3Z"/>
              </svg>
              <input 
                type="password" 
                placeholder="Create a password" 
                v-model="password"
                required
              />
            </div>
          </div>

          <div class="form-group">
            <label>Confirm Password</label>
            <div class="input-wrapper">
              <svg class="input-icon" width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12,17A2,2 0 0,0 14,15C14,13.89 13.1,13 12,13A2,2 0 0,0 10,15A2,2 0 0,0 12,17M18,8A2,2 0 0,1 20,10V20A2,2 0 0,1 18,22H6A2,2 0 0,1 4,20V10C4,8.89 4.9,8 6,8H7V6A5,5 0 0,1 12,1A5,5 0 0,1 17,6V8H18M12,3A3,3 0 0,0 9,6V8H15V6A3,3 0 0,0 12,3Z"/>
              </svg>
              <input 
                type="password" 
                placeholder="Confirm your password" 
                v-model="confirmPassword"
                required
              />
            </div>
          </div>

          <button 
            type="submit" 
            class="signup-btn"
            :disabled="isLoading"
          >
            <svg v-if="!isLoading" width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
              <path d="M19,13H13V19H11V13H5V11H11V5H13V11H19V13Z"/>
            </svg>
            {{ isLoading ? 'Creating Account...' : 'Create Account' }}
          </button>

          <div v-if="error" class="error-message">{{ error }}</div>
        </form>

        <div class="login-section">
          <span class="login-text">Already have an account? </span>
          <router-link to="/login" class="login-link">Login here</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { supabase } from '../supabase'

export default {
  name: 'Signup',
  data() {
    return {
      fullName: '',
      email: '',
      password: '',
      confirmPassword: '',
      isLoading: false,
      error: null,
      role: 'teacher'
    }
  },
  methods: {
    async handleSignup() {
      if (!this.fullName || !this.email || !this.password || !this.confirmPassword) {
        this.error = 'Please fill in all fields.'
        return
      }
      if (this.password !== this.confirmPassword) {
        this.error = 'Passwords do not match.'
        return
      }
      
      this.isLoading = true
      this.error = null

      try {
        const { data: authData, error: authError } = await supabase.auth.signUp({
          email: this.email,
          password: this.password,
        })

        if (authError) {
          throw authError
        }

        const user = authData.user;
        const { error: profileError } = await supabase
          .from('profiles')
          .insert([{
            id: user.id,
            full_name: this.fullName,
            role: this.role,
          }])

        if (profileError) {
          throw profileError
        }

        // FIX: Redirect to the correct dashboard based on role
        this.$router.push('/teacher/dashboard')
        
      } catch (err) {
        console.error('Signup error:', err);
        this.error = err.message || 'An unexpected error occurred during signup.';
      } finally {
        this.isLoading = false
      }
    }
  }
}
</script>

<style scoped>
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
  gap: 80px;
  width: 100%;
  max-width: 1200px;
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
  max-width: 480px;
  text-align: center;
  position: relative;
}

.logo-space {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  max-width: 400px;
}

.logo-placeholder {
  text-align: center;
  opacity: 0.7;
  transition: all 0.3s ease;
}

.logo-placeholder:hover {
  opacity: 1;
  transform: translateY(-2px);
}

.logo-icon {
  width: 200px;
  height: 200px;
  margin: 0 auto 30px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.95);
  border-radius: 50%;
  color: #3D8D7A;
  box-shadow: 0 20px 40px rgba(61, 141, 122, 0.15);
}

.logo-placeholder h2 {
  color: #3D8D7A;
  font-size: 32px;
  font-weight: 700;
  margin-bottom: 16px;
  text-shadow: 0 2px 4px rgba(61, 141, 122, 0.1);
}

.logo-placeholder p {
  color: #3D8D7A;
  font-size: 20px;
  opacity: 0.95;
  line-height: 1.6;
  font-weight: 500;
}

.logo-section {
  margin-bottom: 40px;
}

.user-icon {
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

.signup-form {
  text-align: left;
  margin: 35px 0;
}

.form-group {
  margin-bottom: 22px;
}

.form-group label {
  display: block;
  color: #3D8D7A;
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 10px;
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
  padding: 16px 16px 16px 50px;
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

.signup-btn {
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

.signup-btn:hover:not(:disabled) {
  transform: translateY(-3px);
  box-shadow: 0 12px 30px rgba(61, 141, 122, 0.25);
}

.signup-btn:active:not(:disabled) {
  transform: translateY(-1px);
}

.signup-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.error-message {
  background: rgba(220, 53, 69, 0.1);
  color: #dc3545;
  padding: 12px 16px;
  border-radius: 12px;
  font-size: 14px;
  margin-top: 15px;
  border: 1px solid rgba(220, 53, 69, 0.2);
}

.login-section {
  margin-top: 25px;
  font-size: 16px;
  color: #3D8D7A;
}

.login-text {
  color: #3D8D7A;
  opacity: 0.8;
  font-weight: 500;
}

.login-link {
  color: #3D8D7A;
  text-decoration: none;
  font-weight: 600;
  margin-left: 4px;
  transition: all 0.3s ease;
  padding-bottom: 3px;
  border-bottom: 2px solid transparent;
}

.login-link:hover {
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

@media (max-width: 1024px) {
  .auth-container {
    flex-direction: column;
    gap: 50px;
  }
  
  .logo-space {
    order: -1;
  }
  
  .logo-icon {
    width: 150px;
    height: 150px;
  }
  
  .logo-placeholder h2 {
    font-size: 26px;
  }
  
  .logo-placeholder p {
    font-size: 18px;
  }
}

@media (max-width: 768px) {
  .auth-wrapper {
    padding: 25px;
  }
  
  .auth-box {
    padding: 40px 35px;
    max-width: 400px;
  }

  .user-icon {
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
    padding: 14px 14px 14px 48px;
    font-size: 15px;
  }

  .input-icon {
    left: 16px;
    width: 16px !important;
    height: 16px !important;
  }

  .signup-btn {
    font-size: 16px;
    padding: 16px;
  }

  .login-section {
    font-size: 15px;
  }
}

@media (max-height: 700px) {
  .auth-wrapper {
    align-items: flex-start;
    padding-top: 30px;
  }
}
</style>