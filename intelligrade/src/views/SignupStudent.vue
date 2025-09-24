<template>
  <div class="auth-wrapper">
    <div class="geometric-shapes"></div>
    <div class="floating-elements">
      <!-- Educational floating elements with proper animations -->
    </div>

    <div class="auth-container">
      <div class="logo-space">
        <div class="intelligrade-branding">
          <div class="logo-container">
            <div class="logo-image-container">
              <img 
                src="@/assets/New IntelliGrade Logo Way BG 3.png"
                alt="IntelliGrade Logo" 
                class="logo-image"
              />
            </div>
            <p class="brand-tagline">Empowering students with smart assessment tools and personalized learning insights</p>
          </div>
        </div>
      </div>

      <div class="auth-box">
        <div class="logo-section">
          <div class="user-icon">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M17,14H19V17H22V19H19V22H17V19H14V17H17V14M12,3A4,4 0 0,1 16,7A4,4 0 0,1 12,11A4,4 0 0,1 8,7A4,4 0 0,1 12,3M12,13C16.42,13 20,14.79 20,17V20H4V17C4,14.79 7.58,13 12,13Z"/>
            </svg>
          </div>
          <h1>Student Sign Up</h1>
          <p class="subtitle">Join your class and start learning with IntelliGrade</p>
        </div>

        <form @submit.prevent="handleSignup" class="signup-form">
          <div v-if="error" class="error-display">
            <div class="error-icon">⚠️</div>
            <p>{{ error }}</p>
          </div>

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
            <label>Student ID</label>
            <div class="input-wrapper">
              <svg class="input-icon" width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
                <path d="M2,3H8L10,5H19A1,1 0 0,1 20,6V18A1,1 0 0,1 19,19H5C3.89,19 3,18.1 3,17V4A1,1 0 0,1 4,3H2V1.5H4A2.5,2.5 0 0,1 6.5,4V17C6.5,17.28 6.72,17.5 7,17.5H18.5V19H7A2,2 0 0,1 5,17V4C5,3.45 4.55,3 4,3H2V3Z"/>
              </svg>
              <input 
                type="text" 
                placeholder="Enter your student ID" 
                v-model="studentId"
                required
              />
            </div>
          </div>

          <!-- Grade Level Dropdown with the same design as inputs -->
          <div class="form-group">
            <label>Grade Level</label>
            <div class="input-wrapper">
              <svg class="input-icon" width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12,4A4,4 0 0,1 16,8A4,4 0 0,1 12,12A4,4 0 0,1 8,8A4,4 0 0,1 12,4M12,14C16.42,14 20,15.79 20,18V20H4V18C4,15.79 7.58,14 12,14Z"/>
              </svg>
              <!-- Drop down styled like an input field -->
              <select v-model="gradeLevel" required class="styled-select">
                <option value="7">Grade 7</option>
                <option value="8">Grade 8</option>
                <option value="9">Grade 9</option>
                <option value="10">Grade 10</option>
                <option value="11">Grade 11</option>
                <option value="12">Grade 12</option>
              </select>
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
            <div v-else class="loading-spinner"></div>
            {{ isLoading ? 'Creating Account...' : 'Join IntelliGrade' }}
          </button>
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
import { supabase } from "../supabase.js";

export default {
  data() {
    return {
      fullName: "",
      email: "",
      password: "",
      studentId: "",
      gradeLevel: "",
      showPassword: false,
      error: "",
      isLoading: false,
      passwordStrength: {
        score: 0,
        checks: {
          length: false,
          uppercase: false,
          lowercase: false,
          number: false,
          symbol: false,
          noCommon: false
        }
      },
      emailValidation: {
        isValid: false,
        warning: '',
        suggestion: ''
      }
    };
  },
  watch: {
    password: {
      handler(newPassword) {
        this.checkPasswordStrength(newPassword);
      },
      immediate: true
    },
    email: {
      handler(newEmail) {
        this.validateEmailRealTime(newEmail);
      },
      immediate: true
    }
  },
  methods: {
    togglePasswordVisibility() {
      this.showPassword = !this.showPassword;
    },

    checkPasswordStrength(password) {
      const checks = {
        length: password.length >= 10,
        uppercase: /[A-Z]/.test(password),
        lowercase: /[a-z]/.test(password),
        number: /\d/.test(password),
        symbol: /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(password),
        noCommon: !['password', '123456789', 'qwerty', 'admin', 'password123'].some(common => 
          password.toLowerCase().includes(common)
        )
      };
      
      const score = Object.values(checks).filter(Boolean).length;
      this.passwordStrength = { score, checks };
    },

    getPasswordStrengthText() {
      if (this.passwordStrength.score < 3) return 'Weak';
      if (this.passwordStrength.score < 5) return 'Medium';
      return 'Strong';
    },

    getPasswordStrengthColor() {
      if (this.passwordStrength.score < 3) return '#dc2626';
      if (this.passwordStrength.score < 5) return '#f59e0b';
      return '#10b981';
    },

    validateEmailRealTime(email) {
      if (!email) {
        this.emailValidation = { isValid: false, warning: '', suggestion: '' };
        return;
      }

      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(email)) {
        this.emailValidation = { 
          isValid: false, 
          warning: 'Invalid email format', 
          suggestion: '' 
        };
        return;
      }

      // Check for common typos
      const commonDomains = {
        'gmial.com': 'gmail.com',
        'gmai.com': 'gmail.com',
        'yahooo.com': 'yahoo.com',
        'hotmial.com': 'hotmail.com',
        'outlok.com': 'outlook.com'
      };

      const domain = email.split('@')[1];
      if (commonDomains[domain]) {
        this.emailValidation = {
          isValid: true,
          warning: 'Possible typo detected',
          suggestion: `Did you mean ${email.replace(domain, commonDomains[domain])}?`
        };
        return;
      }

      this.emailValidation = { isValid: true, warning: '', suggestion: '' };
    },

    async handleSignup() {
      if (!this.fullName || !this.email || !this.password || !this.studentId || !this.gradeLevel) {
        this.error = "Please fill in all fields.";
        return;
      }

      if (this.passwordStrength.score < 6) {
        this.error = 'Password does not meet security requirements.';
        return;
      }

      this.isLoading = true;
      this.error = "";

      try {
        // Use Supabase Auth with email confirmation
        const { data: authData, error: authError } = await supabase.auth.signUp({
          email: this.email,
          password: this.password,
          options: {
            emailRedirectTo: `${window.location.origin}/email-verified`,
            data: {
              full_name: this.fullName,
              role: 'student',
              student_id: this.studentId,
              grade_level: this.gradeLevel
            }
          }
        });

        if (authError) {
          throw authError;
        }

        // Show success message - don't redirect yet
        this.error = "Account created! Please check your email and click the verification link to complete registration.";
        
        // Clear form
        this.fullName = "";
        this.email = "";
        this.password = "";
        this.studentId = "";
        this.gradeLevel = "";
        
      } catch (err) {
        console.error("Signup error:", err);
        this.error = err.message || "An unexpected error occurred during signup.";
      } finally {
        this.isLoading = false;
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
    radial-gradient(circle at 10% 80%, rgba(255,255,255,0.12) 0, transparent 50px),
    radial-gradient(circle at 90% 70%, rgba(255,255,255,0.12) 0, transparent 70px);
  animation: moveBackground 30s linear infinite;
}

.geometric-shapes::after {
  content: '';
  position: absolute;
  inset: 0;
  background:
    radial-gradient(circle at 15% 25%, rgba(255,255,255,0.15) 0, transparent 200px),
    radial-gradient(circle at 85% 75%, rgba(255,255,255,0.15) 0, transparent 200px),
    radial-gradient(circle at 50% 50%, rgba(255,255,255,0.08) 0, transparent 300px);
  animation: floatShapes 20s ease-in-out infinite;
}

/* Educational floating elements with proper animations */
.floating-element {
  position: absolute;
  animation: educationalFloat 15s ease-in-out infinite;
  opacity: 0.6;
  filter: drop-shadow(0 4px 12px rgba(74, 155, 142, 0.25));
  z-index: 1;
  transition: all 0.4s ease;
}

.floating-element:hover {
  opacity: 1;
  transform: scale(1.3) !important;
  filter: drop-shadow(0 6px 20px rgba(74, 155, 142, 0.4));
}

/* LEFT SIDE - Around Logo/Tagline */
.element-1 { top: 15%; left: 10%; animation-delay: 1s; }   /* Document - top left */
.element-2 { top: 30%; left: 5%; animation-delay: 3s; }    /* School - middle left */
.element-3 { top: 8%; left: 20%; animation-delay: 5s; }    /* Search - top left area */
.element-4 { top: 50%; left: 15%; animation-delay: 7s; }   /* Star - middle left */
.element-5 { bottom: 25%; left: 8%; animation-delay: 9s; } /* Calendar - bottom left */
.element-6 { top: 70%; left: 22%; animation-delay: 11s; }  /* Chat - lower left */
.element-8 { top: 45%; left: 3%; animation-delay: 13s; }   /* Calculator - middle left */
.element-9 { bottom: 45%; left: 18%; animation-delay: 15s; } /* User - avoiding tagline */

/* RIGHT SIDE - Around Signup Form */
.element-13 { top: 10%; right: 8%; animation-delay: 0s; }      /* Document - top right */
.element-14 { top: 35%; right: 3%; animation-delay: 2s; }      /* School - middle right */
.element-15 { bottom: 45%; right: 6%; animation-delay: 4s; }   /* Search - bottom right */
.element-16 { top: 20%; right: 15%; animation-delay: 6s; }     /* Star - top right area */

.auth-container {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 2.5rem;
  width: 100%;
  max-width: 1100px;
  height: 90vh;
  z-index: 10;
  position: relative;
}

.logo-space {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  max-width: 450px;
  height: 100%;
}

.intelligrade-branding {
  text-align: center;
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
}

.intelligrade-branding:hover {
  transform: translateY(-5px);
}

.logo-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.logo-image-container {
  width: 300px;
  height: 300px;
  display: flex;
  align-items: center;
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
          border-bottom-color: rgba(61, 141, 122, 0.5);
          color: #26796a;
        }
  width: 280px;
  height: 280px;
  object-fit: contain;
  animation: gentleFloat 8s ease-in-out infinite;
  background: transparent;
}

.brand-tagline {
  color: rgba(74, 155, 142, 0.8);
  font-size: 1rem;
  line-height: 1.5;
  font-weight: 500;
  letter-spacing: 0.3px;
  font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  text-shadow: 0 2px 8px rgba(74, 155, 142, 0.1);
  max-width: 350px;
  margin: 0 auto;
  animation: slideInFade 2s ease-out;
  text-align: center;
  position: relative;
  z-index: 15;
  background: rgba(255, 255, 255, 0.1);
  padding: 0.5rem 1rem;
  border-radius: 10px;
  backdrop-filter: blur(10px);
}

.auth-box {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  padding: 1.5rem;
  border-radius: 18px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  box-shadow: 
    0 25px 50px rgba(61, 141, 122, 0.1),
    0 10px 30px rgba(0, 0, 0, 0.05),
    inset 0 1px 0 rgba(255, 255, 255, 0.9);
  width: 100%;
  max-width: 400px;
  text-align: center;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: fit-content;
  max-height: 90vh;
  overflow-y: auto;
}

.logo-section {
  margin-bottom: 1rem;
}

.user-icon {
  width: 45px;
  height: 45px;
  margin: 0 auto 0.75rem;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(61, 141, 122, 0.1);
  border-radius: 50%;
  color: #3D8D7A;
  box-shadow: 0 8px 20px rgba(61, 141, 122, 0.15);
}

h1 {
  color: #3D8D7A;
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 0.3rem;
  letter-spacing: -0.5px;
}

.subtitle {
  color: #3D8D7A;
  font-size: 0.8rem;
  opacity: 0.8;
  font-weight: 500;
}

.signup-form {
  text-align: left;
  margin: 1rem 0 0.75rem 0;
}

.form-group {
  margin-bottom: 0.9rem;
}

.form-group label {
  display: block;
  color: #3D8D7A;
  font-size: 0.8rem;
  font-weight: 600;
  margin-bottom: 0.3rem;
  letter-spacing: 0.2px;
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
  z-index: 1;
}

input {
  width: 100%;
  padding: 0.7rem 0.7rem 0.7rem 2.25rem;
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

.error-display {
  background: rgba(239, 68, 68, 0.1);
  border: 2px solid rgba(239, 68, 68, 0.2);
  border-radius: 9px;
  padding: 0.6rem;
  display: flex;
  align-items: center;
  gap: 0.4rem;
  margin-bottom: 0.75rem;
}

.error-icon {
  font-size: 0.9rem;
  flex-shrink: 0;
}

.error-display p {
  color: #dc2626;
  font-size: 0.75rem;
  margin: 0;
  font-weight: 500;
}

.signup-btn {
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

.signup-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(61, 141, 122, 0.3);
}

.signup-btn:active:not(:disabled) {
  transform: translateY(-1px);
}

.signup-btn:disabled {
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

.login-section {
  font-size: 0.75rem;
  color: #3D8D7A;
  margin-top: 0.6rem;
  opacity: 0.8;
  text-align: center;
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
  padding-bottom: 2px;
  border-bottom: 2px solid transparent;
}

.login-link:hover {
  border-bottom-color: rgba(61, 141, 122, 0.5);
}

/* Enhanced animations */
@keyframes educationalFloat {
  0%, 100% { 
    transform: translateY(0px) translateX(0px) rotate(0deg); 
    opacity: 0.6;
  }
  20% { 
    transform: translateY(-20px) translateX(15px) rotate(72deg); 
    opacity: 0.9;
  }
  40% { 
    transform: translateY(-10px) translateX(-18px) rotate(144deg); 
    opacity: 1;
  }
  60% { 
    transform: translateY(-25px) translateX(8px) rotate(216deg); 
    opacity: 0.8;
  }
  80% { 
    transform: translateY(-5px) translateX(-12px) rotate(288deg); 
    opacity: 0.7;
  }
}

@keyframes moveBackground {
  0% {
    transform: translate(0, 0) rotate(0deg);
  }
  100% {
    transform: translate(-60px, -60px) rotate(2deg);
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

@keyframes gentleFloat {
  0%, 100% {
    transform: translateY(0px) scale(1);
  }
  50% {
    transform: translateY(-20px) scale(1.02);
  }
}

@keyframes slideInFade {
  0% {
    opacity: 0;
    transform: translateY(30px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Responsive Design */
@media (max-width: 1200px) {
  .auth-container {
    flex-direction: column;
    gap: 1.25rem;
    height: auto;
    max-height: 95vh;
  }
  
  .logo-space {
    order: -1;
    max-width: 100%;
  }
  
  .logo-image-container {
    width: 250px;
    height: 250px;
  }
  
  .logo-image {
    width: 230px;
    height: 230px;
  }
  
  .brand-tagline {
    font-size: 0.9rem;
  }

  .auth-box {
    max-width: 100%;
    max-height: none;
  }
}

@media (max-width: 768px) {
  .auth-wrapper {
    padding: 0.75rem;
    overflow-y: auto;
  }
  
  .auth-box {
    padding: 1.25rem;
    max-width: 100%;
    height: auto;
    max-height: none;
  }

  .user-icon {
    width: 40px;
    height: 40px;
  }

  h1 {
    font-size: 1.3rem;
  }

  .subtitle {
    font-size: 0.75rem;
  }

  input {
    padding: 0.6rem 0.6rem 0.6rem 2rem;
    font-size: 0.8rem;
  }

  .input-icon {
    left: 0.65rem;
    width: 12px !important;
    height: 12px !important;
  }

  .signup-btn {
    font-size: 0.8rem;
    padding: 0.65rem;
  }

  .login-section {
    font-size: 0.7rem;
  }
  
  .logo-image-container {
    width: 200px;
    height: 200px;
  }
  
  .logo-image {
    width: 180px;
    height: 180px;
  }
  
  .brand-tagline {
    font-size: 0.8rem;
    max-width: 280px;
  }

  /* Hide some duplicate elements on mobile to reduce clutter */
  .element-13, .element-14, .element-15, .element-16 {
    display: none;
  }
}

@media (max-width: 480px) {
  .logo-image-container {
    width: 160px;
    height: 160px;
  }
  
  .logo-image {
    width: 140px;
    height: 140px;
  }
  
  .brand-tagline {
    font-size: 0.75rem;
    max-width: 240px;
  }
  
  .element-8, .element-9, .element-13, .element-14, .element-15, .element-16 {
    display: none;
  }

  .auth-container {
    gap: 1rem;
  }

  .auth-box {
    padding: 1rem;
  }

  .form-group {
    margin-bottom: 0.8rem;
  }
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
  z-index: 1;
}

input, select {
  width: 100%;
  padding: 0.7rem 0.7rem 0.7rem 2.25rem;
  font-size: 0.85rem;
  border: 2px solid rgba(61, 141, 122, 0.2);
  border-radius: 9px;
  outline: none;
  background: rgba(255, 255, 255, 0.8);
  color: #3D8D7A;
  transition: all 0.3s ease;
  font-weight: 500;
}

input:focus, select:focus {
  border-color: rgba(61, 141, 122, 0.5);
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
  background: white;
}

input::placeholder, select::placeholder {
  color: rgba(61, 141, 122, 0.4);
  font-size: 0.8rem;
  font-weight: 400;
}

/* Same button styles */
.signup-btn {
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

.signup-btn:disabled {
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

.password-toggle {
  position: absolute;
  right: 0.75rem;
  background: none;
  border: none;
  cursor: pointer;
  color: rgba(61, 141, 122, 0.5);
  padding: 0;
  display: flex;
  align-items: center;
  z-index: 2;
}

.password-toggle:hover {
  color: rgba(61, 141, 122, 0.8);
}

.password-strength {
  margin-top: 0.5rem;
  padding: 0.5rem;
  background: rgba(61, 141, 122, 0.05);
  border-radius: 6px;
  font-size: 0.75rem;
}

.strength-meter {
  display: flex;
  gap: 0.25rem;
  margin: 0.25rem 0;
}

.strength-bar {
  height: 4px;
  flex: 1;
  background: rgba(61, 141, 122, 0.1);
  border-radius: 2px;
}

.strength-bar.active {
  background: var(--strength-color);
}

.strength-checks {
  list-style: none;
  padding: 0;
  margin: 0.5rem 0 0 0;
}

.strength-checks li {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  margin: 0.1rem 0;
}

.email-warning {
  margin-top: 0.3rem;
  padding: 0.4rem;
  background: rgba(251, 191, 36, 0.1);
  border: 1px solid rgba(251, 191, 36, 0.3);
  border-radius: 6px;
  font-size: 0.7rem;
  color: #92400e;
}

.email-suggestion {
  color: #1d4ed8;
  cursor: pointer;
  text-decoration: underline;
}
</style>