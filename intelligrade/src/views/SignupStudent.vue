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
                :type="showPassword ? 'text' : 'password'" 
                placeholder="Create a password" 
                v-model="password"
                required
              />
              <button 
                type="button" 
                class="password-toggle"
                @click="togglePasswordVisibility"
                tabindex="-1"
              >
                <svg v-if="!showPassword" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12,9A3,3 0 0,0 9,12A3,3 0 0,0 12,15A3,3 0 0,0 15,12A3,3 0 0,0 12,9M12,17A5,5 0 0,1 7,12A5,5 0 0,1 12,7A5,5 0 0,1 17,12A5,5 0 0,1 12,17M12,4.5C7,4.5 2.73,7.61 1,12C2.73,16.39 7,19.5 12,19.5C17,19.5 21.27,16.39 23,12C21.27,7.61 17,4.5 12,4.5Z"/>
                </svg>
                <svg v-else width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M11.83,9L15,12.16C15,12.11 15,12.05 15,12A3,3 0 0,0 12,9C11.94,9 11.89,9 11.83,9M7.53,9.8L9.08,11.35C9.03,11.56 9,11.77 9,12A3,3 0 0,0 12,15C12.22,15 12.44,14.97 12.65,14.92L14.2,16.47C13.53,16.8 12.79,17 12,17A5,5 0 0,1 7,12C7,11.21 7.2,10.47 7.53,9.8M2,4.27L4.28,6.55L4.73,7C3.08,8.3 1.78,10 1,12C2.73,16.39 7,19.5 12,19.5C13.55,19.5 15.03,19.2 16.38,18.66L16.81,19.09L19.73,22L21,20.73L3.27,3M12,7A5,5 0 0,1 17,12C17,12.64 16.87,13.26 16.64,13.82L19.57,16.75C21.07,15.5 22.27,13.86 23,12C21.27,7.61 17,4.5 12,4.5C10.6,4.5 9.26,4.75 8,5.2L10.17,7.35C10.76,7.13 11.37,7 12,7Z"/>
                </svg>
              </button>
            </div>
            <!-- Password Strength Indicator -->
            <div v-if="password.length > 0" class="password-strength">
              <div class="strength-bar">
                <div 
                  class="strength-fill" 
                  :class="'strength-' + passwordStrength"
                  :style="{ width: (passwordStrength / 4) * 100 + '%' }"
                ></div>
              </div>
              <div class="strength-text">
                <span v-if="passwordStrength === 0" class="weak">Very Weak</span>
                <span v-else-if="passwordStrength === 1" class="weak">Weak</span>
                <span v-else-if="passwordStrength === 2" class="fair">Fair</span>
                <span v-else-if="passwordStrength === 3" class="good">Good</span>
                <span v-else class="strong">Strong</span>
              </div>
            </div>
            <!-- Password Error Messages -->
            <div v-if="passwordErrors.length > 0 && password.length > 0" class="password-errors">
              <ul>
                <li v-for="error in passwordErrors" :key="error" class="error-item">{{ error }}</li>
              </ul>
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
      error: "",
      isLoading: false,
      showPassword: false,
      passwordStrength: 0,
      passwordErrors: []
    };
  },
  watch: {
    password(newPassword) {
      this.validatePassword(newPassword);
    }
  },
  methods: {
    togglePasswordVisibility() {
      this.showPassword = !this.showPassword;
    },
    
    validatePassword(password) {
      this.passwordErrors = [];
      let strength = 0;

      if (password.length < 10) {
        this.passwordErrors.push("Password must be at least 10 characters long");
      } else {
        strength += 1;
      }

      if (!/[A-Z]/.test(password)) {
        this.passwordErrors.push("Password must contain at least one uppercase letter");
      } else {
        strength += 1;
      }

      if (!/[0-9]/.test(password)) {
        this.passwordErrors.push("Password must contain at least one number");
      } else {
        strength += 1;
      }

      if (!/[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(password)) {
        this.passwordErrors.push("Password must contain at least one symbol");
      } else {
        strength += 1;
      }

      this.passwordStrength = strength;
    },

    async handleSignup() {
      if (!this.fullName || !this.email || !this.password || !this.studentId || !this.gradeLevel) {
        this.error = "Please fill in all fields.";
        return;
      }

      this.isLoading = true;
      this.error = "";

      try {
        // Step 1: Sign up the user with email and password
        const { data: authData, error: authError } = await supabase.auth.signUp({
          email: this.email,
          password: this.password,
        });

        if (authError) {
          throw authError;
        }

        const user = authData.user;
        
        // Step 2: Insert into profiles table with new structure
        const { error: profileError } = await supabase
          .from('profiles')
          .insert([{
            id: user.id,
            auth_user_id: user.id,
            full_name: this.fullName,
            email: this.email,
            role: 'student',
          }]);

        if (profileError) {
          throw profileError;
        }

        // Step 3: Insert student-specific details into student_details table
        const { error: studentError } = await supabase
          .from('student_details')
          .insert([{
            profile_id: user.id,
            student_id: this.studentId,
            grade_level: parseInt(this.gradeLevel), // Convert to integer
            enrollment_status: 'active'
          }]);

        if (studentError) {
          throw studentError;
        }

        // Step 4: Redirect to the student dashboard on success
        this.$router.push("/student-dashboard");
        
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
  align-items: flex-start;
  justify-content: center;
  padding: 0.5rem;
  font-family: 'Inter', sans-serif;
  overflow-y: scroll;
  overflow-x: hidden;
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
  gap: 2rem;
  width: 100%;
  max-width: 1100px;
  min-height: 100vh;
  z-index: 10;
  position: relative;
  padding: 1rem 0;
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
  padding: 1.25rem;
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
  overflow-y: visible;
}

.logo-section {
  margin-bottom: 0.75rem;
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
  margin-bottom: 0.75rem;
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
    min-height: auto;
    padding: 1rem 0;
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
    align-items: flex-start;
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
  padding: 0.65rem 0.65rem 0.65rem 2.1rem;
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
  padding: 0.65rem;
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
  margin-top: 0.4rem;
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

/* Password Security Styles */
.password-toggle {
  position: absolute;
  right: 0.75rem;
  background: none;
  border: none;
  color: rgba(61, 141, 122, 0.6);
  cursor: pointer;
  padding: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  z-index: 2;
  border-radius: 4px;
  width: 32px;
  height: 32px;
}

.password-toggle:hover {
  color: #3D8D7A;
  background-color: rgba(61, 141, 122, 0.1);
}

.password-strength {
  margin-top: 0.5rem;
}

.strength-bar {
  width: 100%;
  height: 4px;
  background-color: rgba(61, 141, 122, 0.15);
  border-radius: 2px;
  overflow: hidden;
  margin-bottom: 0.3rem;
}

.strength-fill {
  height: 100%;
  border-radius: 2px;
  transition: all 0.4s ease;
}

.strength-0 {
  background: linear-gradient(90deg, #ef4444, #f87171);
  width: 25%;
}

.strength-1 {
  background: linear-gradient(90deg, #f59e0b, #fbbf24);
  width: 50%;
}

.strength-2 {
  background: linear-gradient(90deg, #eab308, #facc15);
  width: 75%;
}

.strength-3 {
  background: linear-gradient(90deg, #22c55e, #4ade80);
  width: 100%;
}

.strength-4 {
  background: linear-gradient(90deg, #16a34a, #22c55e);
  width: 100%;
}

.strength-text {
  display: flex;
  justify-content: flex-end;
  font-size: 0.75rem;
  font-weight: 600;
}

.strength-text .weak {
  color: #dc2626;
}

.strength-text .fair {
  color: #d97706;
}

.strength-text .good {
  color: #16a34a;
}

.strength-text .strong {
  color: #15803d;
}

.password-errors {
  margin-top: 0.4rem;
}

.password-errors ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.password-errors .error-item {
  color: #dc2626;
  font-size: 0.7rem;
  font-weight: 500;
  margin-bottom: 0.2rem;
  padding: 0.3rem 0.5rem;
  background: rgba(239, 68, 68, 0.1);
  border-radius: 4px;
  border-left: 3px solid #ef4444;
  display: flex;
  align-items: center;
}

.password-errors .error-item::before {
  content: "⚠";
  margin-right: 0.4rem;
  color: #dc2626;
  font-weight: bold;
}

/* Responsive adjustments for password toggle */
@media (max-width: 768px) {
  .password-toggle {
    width: 28px;
    height: 28px;
    right: 0.6rem;
  }
  
  .password-toggle svg {
    width: 14px;
    height: 14px;
  }
}

@media (max-width: 480px) {
  .password-toggle {
    width: 24px;
    height: 24px;
    right: 0.5rem;
  }
  
  .password-toggle svg {
    width: 12px;
    height: 12px;
  }
  
  .strength-text {
    font-size: 0.7rem;
  }
  
  .password-errors .error-item {
    font-size: 0.65rem;
    padding: 0.25rem 0.4rem;
  }
}
</style>