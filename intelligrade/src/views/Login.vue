<template>
  <div class="auth-wrapper">
    <div class="auth-box">
      <div class="logo-section">
        <div class="user-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 2C13.1 2 14 2.9 14 4C14 5.1 13.1 6 12 6C10.9 6 10 5.1 10 4C10 2.9 10.9 2 12 2ZM21 9V7L15 1H5C3.89 1 3 1.89 3 3V21C3 22.11 3.89 23 5 23H19C20.11 23 21 22.11 21 21V9M12 7C14.21 7 16 8.79 16 11C16 13.21 14.21 15 12 15C9.79 15 8 13.21 8 11C8 8.79 9.79 7 12 7ZM6 19.5V18.5C6 16.84 8.69 16 12 16C15.31 16 18 16.84 18 18.5V19.5H6Z"/>
          </svg>
        </div>
        <h1>Welcome Back</h1>
        <p class="subtitle">Please login to your account</p>
      </div>

      <form @submit.prevent="handleLogin" class="login-form">
        <div class="form-group">
          <label>Email</label>
          <div class="input-wrapper">
            <svg class="input-icon" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
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
            <svg class="input-icon" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12,17A2,2 0 0,0 14,15C14,13.89 13.1,13 12,13A2,2 0 0,0 10,15A2,2 0 0,0 12,17M18,8A2,2 0 0,1 20,10V20A2,2 0 0,1 18,22H6A2,2 0 0,1 4,20V10C4,8.89 4.9,8 6,8H7V6A5,5 0 0,1 12,1A5,5 0 0,1 17,6V8H18M12,3A3,3 0 0,0 9,6V8H15V6A3,3 0 0,0 12,3Z"/>
            </svg>
            <input 
              :type="showPassword ? 'text' : 'password'" 
              placeholder="Enter your password" 
              v-model="password"
              required
            />
          </div>
        </div>

        <button 
          type="submit" 
          class="login-btn"
          :disabled="isLoading"
        >
          <svg v-if="!isLoading" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
            <path d="M10,17V14H3V10H10V7L15,12L10,17M10,2H19A2,2 0 0,1 21,4V20A2,2 0 0,1 19,22H10A2,2 0 0,1 8,20V18H10V20H19V4H10V6H8V4A2,2 0 0,1 10,2Z"/>
          </svg>
          {{ isLoading ? 'Signing In...' : 'Login' }}
        </button>
      </form>

      <div class="forgot-section">
        <a href="#" @click.prevent="forgotPassword">Forgot your password?</a>
      </div>

      <div class="signup-section">
        <span>Don't have an account? </span>
        <router-link to="/role-selection" class="signup-link">Sign up here</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data() {
    return {
      email: '',
      password: '',
      showPassword: false,
      isLoading: false
    }
  },
  methods: {
    togglePassword() {
      this.showPassword = !this.showPassword;
    },
    
    async handleLogin() {
      if (!this.email || !this.password) return;
      
      this.isLoading = true;
      
      try {
        console.log('Login attempt:', {
          email: this.email,
          password: this.password
        });
        
        await new Promise(resolve => setTimeout(resolve, 2000));
        
        // Handle successful login
        // this.$router.push('/dashboard');
        
      } catch (error) {
        console.error('Login error:', error);
        alert('Login failed. Please try again.');
      } finally {
        this.isLoading = false;
      }
    },
    
    forgotPassword() {
      console.log('Forgot password clicked');
      // this.$router.push('/forgot-password');
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
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: #FBFFE4;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

.auth-box {
  background: #A3D1C6;
  padding: 40px;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  text-align: center;
  width: 100%;
  max-width: 400px;
}

.logo-section {
  margin-bottom: 32px;
}

.user-icon {
  width: 60px;
  height: 60px;
  background: rgba(61, 141, 122, 0.2);
  border-radius: 50%;
  margin: 0 auto 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #3D8D7A;
}

h1 {
  color: #3D8D7A;
  font-size: 24px;
  font-weight: 600;
  margin-bottom: 8px;
}

.subtitle {
  color: #3D8D7A;
  font-size: 14px;
  opacity: 0.8;
}

.login-form {
  text-align: left;
  margin-bottom: 24px;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  color: #3D8D7A;
  font-size: 14px;
  font-weight: 500;
  margin-bottom: 8px;
}

.input-wrapper {
  position: relative;
  display: flex;
  align-items: center;
}

.input-icon {
  position: absolute;
  left: 12px;
  color: #6B7280;
  z-index: 1;
}

input {
  width: 100%;
  padding: 12px 12px 12px 40px;
  font-size: 14px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 8px;
  outline: none;
  background: rgba(255, 255, 255, 0.9);
  color: #374151;
  transition: all 0.3s ease;
}

input:focus {
  border-color: #3D8D7A;
  background: white;
  box-shadow: 0 0 0 2px rgba(61, 141, 122, 0.1);
}

input::placeholder {
  color: #9CA3AF;
  font-size: 13px;
}

.login-btn {
  width: 100%;
  background: #3D8D7A;
  color: white;
  padding: 12px 16px;
  font-size: 14px;
  font-weight: 500;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.login-btn:hover:not(:disabled) {
  background: #2d6b5a;
  transform: translateY(-1px);
}

.login-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.forgot-section {
  margin: 20px 0;
}

.forgot-section a {
  color: #3D8D7A;
  font-size: 13px;
  text-decoration: none;
  opacity: 0.9;
  transition: opacity 0.3s ease;
}

.forgot-section a:hover {
  opacity: 1;
}

.signup-section {
  font-size: 13px;
  color: #3D8D7A;
  opacity: 0.8;
}

.signup-link {
  color: #3D8D7A;
  text-decoration: none;
  font-weight: 500;
  transition: opacity 0.3s ease;
}

.signup-link:hover {
  opacity: 0.8;
}

@media (max-width: 480px) {
  .auth-box {
    padding: 32px 24px;
    margin: 16px;
  }

  .user-icon {
    width: 50px;
    height: 50px;
  }

  h1 {
    font-size: 20px;
  }

  input {
    padding: 10px 10px 10px 36px;
    font-size: 13px;
  }

  .input-icon {
    left: 10px;
  }
}
</style>