<template>
  <div class="auth-wrapper">
    <div class="geometric-shapes"></div>
    <div class="floating-elements">
      <div class="floating-circle circle-1"></div>
      <div class="floating-circle circle-2"></div>
      <div class="floating-circle circle-3"></div>
    </div>
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
          <svg v-if="!isLoading" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
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
          this.$router.push("/teacher/dashboard"); // This line is correct
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
/* All CSS styles from the original code are unchanged and should be kept as is. */
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

.login-form {
  margin: 25px auto;
  max-width: 380px; 
}

.form-group {
  margin-bottom: 16px;
  text-align: left;
}

.input-wrapper {
  position: relative;
  display: flex;
  align-items: center;
  margin: 0 auto;
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

@media (max-width: 768px) {
  .auth-box {
    padding: 30px;
    max-width: 400px;
    margin: 15px;
  }
  
  .login-form {
    max-width: 340px;
  }
}

@media (max-height: 700px) {
  .auth-wrapper {
    align-items: flex-start;
  }
  
  .auth-box {
    margin: 20px auto;
  }
}

* { margin: 0; padding: 0; box-sizing: border-box; }

.floating-circle {
  position: absolute;
  border-radius: 50%;
  opacity: 0.1;
  animation: float 8s ease-in-out infinite;
}

.circle-1 { 
  width: 80px; 
  height: 80px; 
  background: #B3D8A8; 
  top: 10%; 
  left: 15%; 
  animation-delay: 0s; 
}

.circle-2 { 
  width: 120px; 
  height: 120px; 
  background: #FBFFE4; 
  bottom: 15%; 
  right: 20%; 
  animation-delay: 2s; 
}

.circle-3 { 
  width: 100px; 
  height: 100px; 
  background: #A3D1C6; 
  top: 50%; 
  left: 60%; 
  animation-delay: 4s; 
}

@keyframes float {
  0%, 100% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-20px) rotate(180deg); }
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

.logo-section {
  margin-bottom: 40px;
}

.user-icon {
  width: 80px;
  height: 80px;
  margin: 0 auto 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #3D8D7A;
  box-shadow: 0 8px 16px rgba(61, 141, 122, 0.1);
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

.login-form {
  text-align: left;
  margin: 30px 0;
}

.form-group {
  margin-bottom: 20px;
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
  left: 16px;
  width: 24px !important;
  height: 24px !important;
  color: rgba(61, 141, 122, 0.6);
}

input {
  width: 100%;
  padding: 14px 14px 14px 45px;
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

input::placeholder {
  color: rgba(61, 141, 122, 0.5);
  font-size: 15px;
}

.login-btn {
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
  margin-top: 16px;
}

.login-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(61, 141, 122, 0.2);
}

.login-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.forgot-section {
  margin: 20px 0;
}

.forgot-section a {
  color: #3D8D7A;
  font-size: 16px;
  text-decoration: none;
  font-weight: 500;
  transition: all 0.3s ease;
  padding-bottom: 2px;
  border-bottom: 2px solid transparent;
}

.forgot-section a:hover {
  border-bottom-color: #3D8D7A;
}

.signup-section {
  font-size: 16px;
  color: #3D8D7A;
  margin-top: 20px;
}

.signup-link {
  color: #3D8D7A;
  text-decoration: none;
  font-weight: 600;
  margin-left: 4px;
  transition: all 0.3s ease;
  padding-bottom: 2px;
  border-bottom: 2px solid transparent;
}

.signup-link:hover {
  border-bottom-color: #3D8D7A;
}

@media (max-width: 768px) {
  .auth-box {
    padding: 25px 20px;
    margin: 15px;
    max-width: 340px;
  }

  .user-icon {
    width: 80px;
    height: 80px;
  }

  .user-icon svg {
    width: 32px;
    height: 32px;
  }

  h1 {
    font-size: 28px;
  }

  .subtitle {
    font-size: 16px;
  }

  input {
    padding: 14px 14px 14px 45px;
    font-size: 15px;
  }

  .input-icon {
    width: 20px !important;
    height: 20px !important;
  }

  .login-btn {
    font-size: 16px;
    padding: 14px;
  }

  .forgot-section a,
  .signup-section {
    font-size: 14px;
  }
}

@media (max-height: 700px) {
  .auth-wrapper {
    align-items: flex-start;
  }
  
  .auth-box {
    margin: 20px auto;
  }
}
</style>