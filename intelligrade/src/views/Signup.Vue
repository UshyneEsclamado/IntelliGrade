<template>
  <div class="auth-wrapper">
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
      </form>

      <div class="login-section">
        <span class="login-text">Already have an account? </span>
        <router-link to="/login" class="login-link">Login here</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Signup',
  data() {
    return {
      fullName: '',
      email: '',
      password: '',
      confirmPassword: '',
      isLoading: false
    }
  },
  methods: {
    async handleSignup() {
      if (!this.fullName || !this.email || !this.password || !this.confirmPassword) {
        alert('Please fill in all fields');
        return;
      }
      
      if (this.password !== this.confirmPassword) {
        alert('Passwords do not match');
        return;
      }
      
      this.isLoading = true;
      
      try {
        console.log('Signup attempt:', {
          fullName: this.fullName,
          email: this.email,
          password: this.password
        });
        
        await new Promise(resolve => setTimeout(resolve, 2000));
        
        // Handle successful signup
        // this.$router.push('/login');
        
      } catch (error) {
        console.error('Signup error:', error);
        alert('Signup failed. Please try again.');
      } finally {
        this.isLoading = false;
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
  padding: 32px;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  text-align: center;
  width: 100%;
  max-width: 380px;
}

.logo-section {
  margin-bottom: 28px;
}

.user-icon {
  width: 50px;
  height: 50px;
  background: rgba(61, 141, 122, 0.2);
  border-radius: 50%;
  margin: 0 auto 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #3D8D7A;
}

h1 {
  color: #3D8D7A;
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 6px;
  letter-spacing: -0.5px;
}

.subtitle {
  color: #3D8D7A;
  font-size: 13px;
  opacity: 0.8;
  font-weight: 400;
}

.signup-form {
  text-align: left;
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 16px;
}

.form-group label {
  display: block;
  color: #3D8D7A;
  font-size: 12px;
  font-weight: 500;
  margin-bottom: 6px;
  letter-spacing: 0.2px;
}

.input-wrapper {
  position: relative;
  display: flex;
  align-items: center;
}

.input-icon {
  position: absolute;
  left: 10px;
  color: #6B7280;
  z-index: 1;
}

input {
  width: 100%;
  padding: 10px 10px 10px 32px;
  font-size: 13px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 8px;
  outline: none;
  background: rgba(255, 255, 255, 0.9);
  color: #374151;
  transition: all 0.3s ease;
  font-weight: 400;
}

input:focus {
  border-color: #3D8D7A;
  background: white;
  box-shadow: 0 0 0 2px rgba(61, 141, 122, 0.1);
}

input::placeholder {
  color: #9CA3AF;
  font-size: 12px;
  font-weight: 400;
}

.signup-btn {
  width: 100%;
  background: #3D8D7A;
  color: white;
  padding: 11px 16px;
  font-size: 13px;
  font-weight: 500;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  letter-spacing: 0.3px;
}

.signup-btn:hover:not(:disabled) {
  background: #2d6b5a;
  transform: translateY(-1px);
}

.signup-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.login-section {
  font-size: 12px;
  color: #3D8D7A;
  line-height: 1.4;
}

.login-text {
  color: #3D8D7A;
  opacity: 0.8;
  font-weight: 400;
}

.login-link {
  color: #3D8D7A;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s ease;
  border-bottom: 1px solid transparent;
}

.login-link:hover {
  opacity: 0.8;
  border-bottom-color: #3D8D7A;
}

@media (max-width: 480px) {
  .auth-box {
    padding: 24px 20px;
    margin: 16px;
    max-width: 340px;
  }

  .user-icon {
    width: 44px;
    height: 44px;
  }

  h1 {
    font-size: 18px;
  }

  .subtitle {
    font-size: 12px;
  }

  input {
    padding: 9px 9px 9px 30px;
    font-size: 12px;
  }

  .input-icon {
    left: 9px;
  }

  .form-group label {
    font-size: 11px;
  }

  .signup-btn {
    font-size: 12px;
    padding: 10px 16px;
  }

  .login-section {
    font-size: 11px;
  }
}
</style>