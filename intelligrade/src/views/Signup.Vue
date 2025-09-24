<template>
  <div class="auth-wrapper">
    <div class="geometric-shapes"></div>
    <div class="floating-elements">
      <!-- Educational floating elements with proper animations -->
      <!-- LEFT SIDE - Around Logo/Tagline -->
      <!-- Document symbols -->
      <div class="floating-element element-1">
        <svg width="35" height="35" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M19 3H5C3.9 3 3 3.9 3 5V19C3 20.1 3.9 21 5 21H19C20.1 21 21 20.1 21 19V5C21 3.9 20.1 3 19 3M19 19H5V5H19V19M17 17H7V15H17V17M17 13H7V11H17V13M17 9H7V7H17V9Z"/>
        </svg>
      </div>
      
      <!-- Education/School symbols -->
      <div class="floating-element element-2">
        <svg width="33" height="33" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M12 3L1 9L12 15L21 10.09V17H23V9L12 3M5 13.18V17.18L12 21L19 17.18V13.18L12 17L5 13.18Z"/>
        </svg>
      </div>
      
      <!-- Search symbols -->
      <div class="floating-element element-3">
        <svg width="30" height="30" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M9.5,3A6.5,6.5 0 0,1 16,9.5C16,11.11 15.41,12.59 14.44,13.73L14.71,14H15.5L20.5,19L19,20.5L14,15.5V14.71L13.73,14.44C12.59,15.41 11.11,16 9.5,16A6.5,6.5 0 0,1 3,9.5A6.5,6.5 0 0,1 9.5,3M9.5,5C7,5 5,7 5,9.5C5,12 7,14 9.5,14C12,14 14,12 14,9.5C14,7 12,5 9.5,5Z"/>
        </svg>
      </div>
      
      <!-- Star symbols -->
      <div class="floating-element element-4">
        <svg width="38" height="38" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M12,17.27L18.18,21L16.54,13.97L22,9.24L14.81,8.62L12,2L9.19,8.62L2,9.24L7.45,13.97L5.82,21L12,17.27Z"/>
        </svg>
      </div>
      
      <!-- Calendar symbols -->
      <div class="floating-element element-5">
        <svg width="33" height="33" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M19,19H5V8H19M16,1V3H8V1H6V3H5C3.89,3 3,3.89 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5C21,3.89 20.1,3 19,3H18V1M17,12H12V17H17V12Z"/>
        </svg>
      </div>
      
      <!-- Chat/Message symbols -->
      <div class="floating-element element-6">
        <svg width="36" height="36" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M20,2H4A2,2 0 0,0 2,4V16A2,2 0 0,0 4,18H18L22,22V4A2,2 0 0,0 20,2M6,9H18V11H6M4,6H20V8H4M6,12H16V14H6"/>
        </svg>
      </div>

      <!-- RIGHT SIDE - Around Signup Form -->
      <!-- Document symbols (duplicate) -->
      <div class="floating-element element-13">
        <svg width="32" height="32" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M19 3H5C3.9 3 3 3.9 3 5V19C3 20.1 3.9 21 5 21H19C20.1 21 21 20.1 21 19V5C21 3.9 20.1 3 19 3M19 19H5V5H19V19M17 17H7V15H17V17M17 13H7V11H17V13M17 9H7V7H17V9Z"/>
        </svg>
      </div>
      
      <!-- Education/School symbols (duplicate) -->
      <div class="floating-element element-14">
        <svg width="29" height="29" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M12 3L1 9L12 15L21 10.09V17H23V9L12 3M5 13.18V17.18L12 21L19 17.18V13.18L12 17L5 13.18Z"/>
        </svg>
      </div>
      
      <!-- Search symbols (duplicate) -->
      <div class="floating-element element-15">
        <svg width="34" height="34" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M9.5,3A6.5,6.5 0 0,1 16,9.5C16,11.11 15.41,12.59 14.44,13.73L14.71,14H15.5L20.5,19L19,20.5L14,15.5V14.71L13.73,14.44C12.59,15.41 11.11,16 9.5,16A6.5,6.5 0 0,1 3,9.5A6.5,6.5 0 0,1 9.5,3M9.5,5C7,5 5,7 5,9.5C5,12 7,14 9.5,14C12,14 14,12 14,9.5C14,7 12,5 9.5,5Z"/>
        </svg>
      </div>
      
      <!-- Star symbols (duplicate) -->
      <div class="floating-element element-16">
        <svg width="31" height="31" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M12,17.27L18.18,21L16.54,13.97L22,9.24L14.81,8.62L12,2L9.19,8.62L2,9.24L7.45,13.97L5.82,21L12,17.27Z"/>
        </svg>
      </div>
      
      <!-- Calculator symbols -->
      <div class="floating-element element-8">
        <svg width="34" height="34" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M9,11H7V9H9V11M13,11H11V9H13V11M17,11H15V9H17V11M19,3H18V1H16V1H6V3H5C3.89,3 3,3.9 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5C21,3.9 20.1,3 19,3M19,19H5V8H19V19M9,15H7V13H9V15M13,15H11V13H13V15M17,15H15V13H17V15M9,17H7V19H9V17M13,19H11V17H13V19M17,19H15V17H17V19Z"/>
        </svg>
      </div>
      
      <!-- User symbols -->
      <div class="floating-element element-9">
        <svg width="29" height="29" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M7.07,18.28C7.5,17.38 10.12,16.5 12,16.5C13.88,16.5 16.5,17.38 16.93,18.28C15.57,19.36 13.86,20 12,20C10.14,20 8.43,19.36 7.07,18.28M18.36,16.83C16.93,15.09 13.46,14.5 12,14.5C10.54,14.5 7.07,15.09 5.64,16.83C4.62,15.5 4,13.82 4,12C4,7.59 7.59,4 12,4C16.41,4 20,7.59 20,12C20,13.82 19.38,15.5 18.36,16.83M12,6C10.06,6 8.5,7.56 8.5,9.5C8.5,11.44 10.06,13 12,13C13.94,13 15.5,11.44 15.5,9.5C15.5,7.56 13.94,6 12,6M12,11A1.5,1.5 0 0,1 10.5,9.5A1.5,1.5 0 0,1 12,8A1.5,1.5 0 0,1 13.5,9.5A1.5,1.5 0 0,1 12,11Z"/>
        </svg>
      </div>
    </div>
    
    <div class="auth-container">
      <!-- IntelliGrade Logo Space - Left Side -->
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
            <p class="brand-tagline">Empower your teaching with AI-powered grading solutions</p>
          </div>
        </div>
      </div>
      
      <!-- Signup Box - Right Side -->
      <div class="auth-box">
        <div class="logo-section">
          <div class="user-icon">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M17,14H19V17H22V19H19V22H17V19H14V17H17V14M12,3A4,4 0 0,1 16,7A4,4 0 0,1 12,11A4,4 0 0,1 8,7A4,4 0 0,1 12,3M12,13C16.42,13 20,14.79 20,17V20H4V17C4,14.79 7.58,13 12,13Z"/>
            </svg>
          </div>
          <h1>Join IntelliGrade</h1>
          <p class="subtitle">Create your teacher account</p>
        </div>

        <form @submit.prevent="handleSignup" class="signup-form">
          <!-- Error Display -->
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
            <div v-else class="loading-spinner"></div>
            {{ isLoading ? 'Creating Account...' : 'Create Account' }}
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
import { supabase } from '../supabase'

export default {
  name: 'TeacherSignup',
  data() {
    return {
      fullName: '',
      email: '',
      password: '',
      confirmPassword: '',
      showPassword: false,
      showConfirmPassword: false,
      isLoading: false,
      error: null,
      role: 'teacher',
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
    }
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

    toggleConfirmPasswordVisibility() {
      this.showConfirmPassword = !this.showConfirmPassword;
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

      // Basic format check
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

      // Check for disposable email services
      const disposableDomains = [
        '10minutemail.com', 'guerrillamail.com', 'mailinator.com',
        'tempmail.org', 'throwaway.email'
      ];

      if (disposableDomains.includes(domain)) {
        this.emailValidation = {
          isValid: true,
          warning: 'Temporary email detected',
          suggestion: 'Consider using a permanent email address'
        };
        return;
      }

      this.emailValidation = { isValid: true, warning: '', suggestion: '' };
    },

    async sendVerificationEmail(userId, email) {
      const token = this.generateVerificationToken();
      const expiresAt = new Date();
      expiresAt.setHours(expiresAt.getHours() + 24);

      // Store verification token
      await supabase
        .from("profiles")
        .update({
          verification_token: token,
          token_expires_at: expiresAt.toISOString()
        })
        .eq("id", userId);

      // Here you would integrate with your email service
      console.log(`Verification email sent to ${email} with token: ${token}`);
      
      // For now, just show success message
      this.error = "Account created! Please check your email for verification link.";
    },

    generateVerificationToken() {
      return Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15);
    },

    async handleSignup() {
      // Validation
      if (!this.fullName || !this.email || !this.password || !this.confirmPassword) {
        this.error = 'Please fill in all fields.';
        return;
      }

      if (this.password !== this.confirmPassword) {
        this.error = 'Passwords do not match.';
        return;
      }

      if (this.passwordStrength.score < 6) {
        this.error = 'Password does not meet security requirements.';
        return;
      }

      this.isLoading = true;
      this.error = null;

      try {
        const { data: authData, error: authError } = await supabase.auth.signUp({
          email: this.email,
          password: this.password,
        });

        if (authError) {
          throw authError;
        }

        const user = authData.user;
        
        // Insert into profiles table
        const { error: profileError } = await supabase
          .from('profiles')
          .insert([{
            id: user.id,
            auth_user_id: user.id,
            full_name: this.fullName,
            email: this.email,
            role: this.role,
            email_verified: false,
            password_changed_at: new Date().toISOString()
          }]);

        if (profileError) {
          throw profileError;
        }

        // Send verification email
        await this.sendVerificationEmail(user.id, this.email);

        // Don't redirect immediately - wait for email verification
        
      } catch (err) {
        console.error('Signup error:', err);
        this.error = err.message || 'An unexpected error occurred during signup.';
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