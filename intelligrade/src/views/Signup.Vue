<template>
  <div class="auth-wrapper">
    <div class="geometric-shapes"></div>
    <div class="auth-box">
      <div class="logo-section">
        <div class="user-icon">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M17,14H19V17H22V19H19V22H17V19H14V17H17V14M12,3A4,4 0 0,1 16,7A4,4 0 0,1 12,11A4,4 0 0,1 8,7A4,4 0 0,1 12,3M12,13C16.42,13 20,14.79 20,17V20H4V17C4,14.79 7.58,13 12,13Z"/>
          </svg>
        </div>
        <h1>Create Account</h1>
        <p class="subtitle">Join our teaching community</p>
      </div>

      <form @submit.prevent="handleSignup" class="signup-form">
        <div class="form-group">
          <label>Full Name</label>
          <div class="input-wrapper">
            <svg class="input-icon" width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
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

        <div class="form-group">
          <label>Password</label>
          <div class="input-wrapper">
            <svg class="input-icon" width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
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
            <svg class="input-icon" width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
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
          <svg v-if="!isLoading" width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
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
/* Change fixed to absolute to enable scrolling */
.auth-wrapper {
  position: absolute; 
  inset: 0;
  background: transparent !important;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  padding: 20px;
  font-family: 'Inter', sans-serif;
  overflow-y: auto; 
}

/* Geometric Background Styles */
.geometric-shapes {
  position: fixed;
  inset: 0;
  z-index: 0;
  overflow: hidden;
  background: linear-gradient(135deg, #3D8D7A, #A3D1C6);
}

.geometric-shapes::before {
  content: '';
  position: absolute;
  width: 100%;
  height: 100%;
  background: 
    linear-gradient(45deg, transparent 48%, rgba(255,255,255,0.1) 50%, transparent 52%) 0 0 / 60px 60px,
    linear-gradient(-45deg, transparent 48%, rgba(255,255,255,0.1) 50%, transparent 52%) 0 0 / 60px 60px,
    radial-gradient(circle at 20% 30%, rgba(255,255,255,0.1) 0, transparent 50px),
    radial-gradient(circle at 80% 20%, rgba(255,255,255,0.1) 0, transparent 70px),
    radial-gradient(circle at 10% 80%, rgba(255,255,255,0.1) 0, transparent 60px),
    radial-gradient(circle at 90% 70%, rgba(255,255,255,0.1) 0, transparent 80px);
  animation: moveBackground 30s linear infinite;
}

.geometric-shapes::after {
  content: '';
  position: absolute;
  inset: 0;
  background:
    radial-gradient(circle at 10% 20%, rgba(255,255,255,0.2) 0, transparent 200px),
    radial-gradient(circle at 90% 80%, rgba(255,255,255,0.2) 0, transparent 200px),
    radial-gradient(circle at 50% 50%, rgba(255,255,255,0.1) 0, transparent 300px);
  animation: floatShapes 20s ease-in-out infinite;
}

/* Auth box styles update */
.auth-box {
  background: rgba(251, 255, 228, 0.92);
  backdrop-filter: blur(12px);
  padding: 35px;
  border-radius: 20px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  box-shadow: 
    0 20px 40px rgba(61, 141, 122, 0.2),
    0 0 100px rgba(255, 255, 255, 0.1);
  width: 100%;
  max-width: 460px;
  text-align: center;
  position: relative;
  margin: 20px auto;
  z-index: 1;
}

@keyframes moveBackground {
  0% {
    transform: translate(0, 0) rotate(0deg);
  }
  100% {
    transform: translate(-60px, -60px) rotate(5deg);
  }
}

@keyframes floatShapes {
  0%, 100% {
    transform: translate(0, 0);
  }
  50% {
    transform: translate(20px, 20px);
  }
}

/* Update logo section */
.logo-section {
  margin-bottom: 30px;
}

.user-icon {
  width: 80px;
  height: 80px;
  background: rgba(61, 141, 122, 0.1);
  border-radius: 50%;
  margin: 0 auto 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #3D8D7A;
}

.user-icon svg {
  width: 32px;
  height: 32px;
}

h1 {
  color: #3D8D7A;
  font-size: 28px;
  font-weight: 700;
  margin-bottom: 8px;
  letter-spacing: -0.5px;
}

.subtitle {
  color: #3D8D7A;
  font-size: 16px;
  opacity: 0.85;
  font-weight: 500;
}

/* Update form styles */
.signup-form {
  margin: 25px auto;
  max-width: 380px;
}

.form-group {
  margin-bottom: 16px;
  text-align: left;
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
  margin: 0 auto;
}

.input-icon {
  position: absolute;
  left: 12px;
  width: 20px !important;
  height: 20px !important;
  color: rgba(61, 141, 122, 0.6);
}

input {
  width: 100%;
  padding: 12px 12px 12px 45px;
  font-size: 15px;
  border: 2px solid rgba(61, 141, 122, 0.2);
  border-radius: 12px;
  outline: none;
  background: white;
  color: #3D8D7A;
  transition: all 0.3s ease;
}

input:focus {
  border-color: #3D8D7A;
  box-shadow: 0 0 0 4px rgba(61, 141, 122, 0.1);
}

/* Update button styles */
.signup-btn {
  width: 100%;
  background: linear-gradient(135deg, #3D8D7A, #A3D1C6);
  color: #FBFFE4;
  padding: 14px;
  font-size: 16px;
  font-weight: 600;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  margin-top: 20px;
}

.signup-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(61, 141, 122, 0.2);
}

.signup-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

/* Update login section */
.login-section {
  margin-top: 20px;
  font-size: 16px;
  color: #3D8D7A;
}

.login-text {
  color: #3D8D7A;
  opacity: 0.85;
  font-weight: 500;
}

.login-link {
  color: #3D8D7A;
  text-decoration: none;
  font-weight: 600;
  margin-left: 4px;
  transition: all 0.3s ease;
  padding-bottom: 2px;
  border-bottom: 2px solid transparent;
}

.login-link:hover {
  border-bottom-color: #3D8D7A;
}

/* Update responsive styles */
@media (max-width: 768px) {
  .auth-box {
    padding: 30px;
    max-width: 400px;
    margin: 30px auto;
  }
  
  .signup-form {
    max-width: 340px;
  }
}

@media (max-height: 768px) {
  .auth-wrapper {
    align-items: flex-start;
    padding-top: 30px;
  }
  
  .auth-box {
    margin-top: 20px;
  }
}
</style>