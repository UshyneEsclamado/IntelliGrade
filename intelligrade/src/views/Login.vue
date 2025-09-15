<template>
  <div class="auth-wrapper">
    <div class="geometric-shapes"></div>
    <div class="floating-elements">
      <div class="floating-circle circle-1"></div>
      <div class="floating-circle circle-2"></div>
      <div class="floating-circle circle-3"></div>
    </div>
    
    <div class="auth-container">
      <!-- Login Box - Left Side -->
      <div class="auth-box">
        <div class="logo-section">
          <div class="user-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor">
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
            <svg v-if="!isLoading" width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
              <path d="M10,17V14H3V10H10V7L15,12L10,17M10,2H19A2,2 0 0,1 21,4V20A2,2 0 0,1 19,22H10A2,2 0 0,1 8,20V18H10V20H19V4H10V6H8V4A2,2 0 0,1 10,2Z"/>
            </svg>
            {{ isLoading ? 'Logging in...' : 'Login' }}
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
      
      <!-- Logo Space - Right Side -->
      <div class="logo-space">
        <div class="logo-placeholder">
          <div class="logo-icon">
            <svg width="120" height="120" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12,2A3,3 0 0,1 15,5V11A3,3 0 0,1 12,14A3,3 0 0,1 9,11V5A3,3 0 0,1 12,2M19,11C19,14.53 16.39,17.44 13,17.93V21H11V17.93C7.61,17.44 5,14.53 5,11H7A5,5 0 0,0 12,16A5,5 0 0,0 17,11H19Z"/>
            </svg>
          </div>
          <h2>Your Logo Here</h2>
          <p>Brand tagline or description</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { supabase } from "../supabase.js";

export default {
  name: "Login",
  data() {
    return {
      email: "",
      password: "",
      isLoading: false,
      error: null,
    };
  },
  methods: {
    async handleLogin() {
      if (!this.email || !this.password) {
        this.error = "Please enter both email and password.";
        return;
      }

      this.isLoading = true;
      this.error = null;

      try {
        const { data: authData, error: authError } = await supabase.auth.signInWithPassword({
          email: this.email,
          password: this.password,
        });

        if (authError) {
          throw authError;
        }

        const { data: profileData, error: profileError } = await supabase
          .from("profiles")
          .select("role")
          .eq("id", authData.user.id)
          .single();

        if (profileError) {
          throw profileError;
        }

        if (profileData.role === "student") {
          this.$router.push("/student-dashboard");
        } else if (profileData.role === "teacher") {
          this.$router.push("/teacher/dashboard");
        } else {
          this.$router.push("/");
        }
      } catch (err) {
        console.error("Login error:", err);
        this.error = err.message || "Login failed. Please check your credentials.";
      } finally {
        this.isLoading = false;
      }
    },

    forgotPassword() {
      this.$router.push("/forgot-password");
    },
  },
};
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
  width: 140px;
  height: 140px;
  margin: 0 auto 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.9);
  border-radius: 50%;
  color: #3D8D7A;
  box-shadow: 0 15px 30px rgba(61, 141, 122, 0.1);
}

.logo-placeholder h2 {
  color: #3D8D7A;
  font-size: 24px;
  font-weight: 600;
  margin-bottom: 8px;
}

.logo-placeholder p {
  color: #3D8D7A;
  font-size: 16px;
  opacity: 0.8;
}

.logo-section {
  margin-bottom: 45px;
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

.login-form {
  text-align: left;
  margin: 35px 0;
}

.form-group {
  margin-bottom: 25px;
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

.login-btn {
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

.login-btn:hover:not(:disabled) {
  transform: translateY(-3px);
  box-shadow: 0 12px 30px rgba(61, 141, 122, 0.25);
}

.login-btn:active:not(:disabled) {
  transform: translateY(-1px);
}

.login-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.forgot-section {
  margin: 25px 0;
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

.signup-section {
  font-size: 16px;
  color: #3D8D7A;
  margin-top: 25px;
  opacity: 0.8;
}

.signup-link {
  color: #3D8D7A;
  text-decoration: none;
  font-weight: 600;
  margin-left: 4px;
  transition: all 0.3s ease;
  padding-bottom: 3px;
  border-bottom: 2px solid transparent;
}

.signup-link:hover {
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
    width: 100px;
    height: 100px;
  }
  
  .logo-placeholder h2 {
    font-size: 20px;
  }
  
  .logo-placeholder p {
    font-size: 14px;
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
    padding: 16px 16px 16px 48px;
    font-size: 15px;
  }

  .input-icon {
    left: 16px;
    width: 16px !important;
    height: 16px !important;
  }

  .login-btn {
    font-size: 16px;
    padding: 16px;
  }

  .forgot-section a,
  .signup-section {
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