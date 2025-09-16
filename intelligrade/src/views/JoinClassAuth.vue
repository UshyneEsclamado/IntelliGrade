<template>
  <div class="auth-wrapper">
    <div class="geometric-shapes"></div>
    <div class="floating-elements">
      <div class="floating-circle circle-1"></div>
      <div class="floating-circle circle-2"></div>
      <div class="floating-circle circle-3"></div>
    </div>
    
    <div class="auth-container">
      <div class="auth-box">
        <!-- Header Section -->
        <div class="logo-section">
          <div class="class-icon">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12,3L1,9L12,15L21,10.09V17H23V9M5,13.18V17.18L12,21L19,17.18V13.18L12,17L5,13.18Z"/>
            </svg>
          </div>
          <h1>Join a Class</h1>
          <p class="subtitle">Choose your account option to continue</p>
        </div>

        <!-- Account Status Selection -->
        <div v-if="!showAuthForm" class="account-selection">
          <div class="selection-card" @click="selectAccountOption(true)">
            <div class="card-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12,4A4,4 0 0,1 16,8A4,4 0 0,1 12,12A4,4 0 0,1 8,8A4,4 0 0,1 12,4M12,14C16.42,14 20,15.79 20,18V20H4V18C4,15.79 7.58,14 12,14Z"/>
              </svg>
            </div>
            <h3>I already have an account</h3>
            <p>Login with your existing credentials</p>
            <div class="card-arrow">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M4,11V13H16L10.5,18.5L11.92,19.92L19.84,12L11.92,4.08L10.5,5.5L16,11H4Z"/>
              </svg>
            </div>
          </div>

          <div class="selection-card" @click="selectAccountOption(false)">
            <div class="card-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M15,14C12.33,14 7,15.33 7,18V20H23V18C23,15.33 17.67,14 15,14M6,10V7H4V10H1V12H4V15H6V12H9V10M15,12A4,4 0 0,0 19,8A4,4 0 0,0 15,4A4,4 0 0,0 11,8A4,4 0 0,0 15,12Z"/>
              </svg>
            </div>
            <h3>I don't have an account</h3>
            <p>Create a new student account</p>
            <div class="card-arrow">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M4,11V13H16L10.5,18.5L11.92,19.92L19.84,12L11.92,4.08L10.5,5.5L16,11H4Z"/>
              </svg>
            </div>
          </div>
        </div>

        <!-- Login Form -->
        <div v-if="showAuthForm && hasAccount" class="auth-form-container">
          <div class="form-header">
            <button class="back-btn" @click="goBack">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z"/>
              </svg>
            </button>
            <h2>Login to Your Account</h2>
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
              class="auth-btn"
              :disabled="isLoading"
            >
              <svg v-if="!isLoading" width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                <path d="M10,17V14H3V10H10V7L15,12L10,17M10,2H19A2,2 0 0,1 21,4V20A2,2 0 0,1 19,22H10A2,2 0 0,1 8,20V18H10V20H19V4H10V6H8V4A2,2 0 0,1 10,2Z"/>
              </svg>
              {{ isLoading ? 'Logging in...' : 'Continue' }}
            </button>
          </form>

          <div class="forgot-section">
            <a href="#" @click.prevent="forgotPassword">Forgot your password?</a>
          </div>
        </div>

        <!-- Signup Form -->
        <div v-if="showAuthForm && !hasAccount" class="auth-form-container">
          <div class="form-header">
            <button class="back-btn" @click="goBack">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M20,11V13H8L13.5,18.5L12.08,19.92L4.16,12L12.08,4.08L13.5,5.5L8,11H20Z"/>
              </svg>
            </button>
            <h2>Create Student Account</h2>
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
              class="auth-btn"
              :disabled="isLoading"
            >
              <svg v-if="!isLoading" width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                <path d="M15,14C12.33,14 7,15.33 7,18V20H23V18C23,15.33 17.67,14 15,14M6,10V7H4V10H1V12H4V15H6V12H9V10M15,12A4,4 0 0,0 19,8A4,4 0 0,0 15,4A4,4 0 0,0 11,8A4,4 0 0,0 15,12Z"/>
              </svg>
              {{ isLoading ? 'Creating Account...' : 'Create Account & Continue' }}
            </button>
          </form>
        </div>

        <!-- Back to Login Link -->
        <div v-if="!showAuthForm" class="back-to-login">
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
import { supabase } from "../supabase.js";

export default {
  name: "JoinClassAuth",
  props: {
    classCode: String,
    sectionCode: String
  },
  data() {
    return {
      showAuthForm: false,
      hasAccount: true,
      email: "",
      password: "",
      fullName: "",
      confirmPassword: "",
      isLoading: false,
      error: null,
    };
  },
  methods: {
    selectAccountOption(hasAccount) {
      this.hasAccount = hasAccount;
      this.showAuthForm = true;
    },

    goBack() {
      this.showAuthForm = false;
      this.email = "";
      this.password = "";
      this.fullName = "";
      this.confirmPassword = "";
      this.error = null;
    },

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
          // Check if coming from section link (has both classCode and sectionCode)
          if (this.classCode && this.sectionCode) {
            // Go directly to section code input
            this.$router.push({
              name: 'SectionCode',
              query: { 
                classCode: this.classCode, 
                sectionCode: this.sectionCode 
              }
            });
          }
          // Check if coming from class link (has only classCode)
          else if (this.classCode) {
            // Go to section selection
            this.$router.push({
              name: 'SectionSelection',
              query: { classCode: this.classCode }
            });
          }
          // Default: manual entry flow (no URL parameters)
          else {
            this.$router.push("/join-class/enter-code");
          }
        } else {
          // Only students can join classes
          this.error = "Only student accounts can join classes.";
        }
      } catch (err) {
        console.error("Login error:", err);
        this.error = err.message || "Login failed. Please check your credentials.";
      } finally {
        this.isLoading = false;
      }
    },

    async handleSignup() {
      if (!this.fullName || !this.email || !this.password || !this.confirmPassword) {
        this.error = "Please fill in all fields.";
        return;
      }

      if (this.password !== this.confirmPassword) {
        this.error = "Passwords do not match.";
        return;
      }

      if (this.password.length < 6) {
        this.error = "Password must be at least 6 characters long.";
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

        // Create profile for the new user
        const { error: profileError } = await supabase
          .from("profiles")
          .insert([
            {
              id: authData.user.id,
              full_name: this.fullName,
              email: this.email,
              role: "student",
            },
          ]);

        if (profileError) {
          throw profileError;
        }

        // Same routing logic as login
        // Check if coming from section link (has both classCode and sectionCode)
        if (this.classCode && this.sectionCode) {
          // Go directly to section code input
          this.$router.push({
            name: 'SectionCode',
            query: { 
              classCode: this.classCode, 
              sectionCode: this.sectionCode 
            }
          });
        }
        // Check if coming from class link (has only classCode)
        else if (this.classCode) {
          // Go to section selection
          this.$router.push({
            name: 'SectionSelection',
            query: { classCode: this.classCode }
          });
        }
        // Default: manual entry flow (no URL parameters)
        else {
          this.$router.push("/join-class/enter-code");
        }
      } catch (err) {
        console.error("Signup error:", err);
        this.error = err.message || "Signup failed. Please try again.";
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
/* Base styles - inherited from login component */
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
  width: 100%;
  max-width: 600px;
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
  text-align: center;
  position: relative;
}

.logo-section {
  margin-bottom: 40px;
}

.class-icon {
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

/* Account Selection Cards */
.account-selection {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-bottom: 30px;
}

.selection-card {
  background: rgba(255, 255, 255, 0.8);
  border: 2px solid rgba(61, 141, 122, 0.15);
  border-radius: 16px;
  padding: 25px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  text-align: left;
  gap: 20px;
  position: relative;
}

.selection-card:hover {
  border-color: rgba(61, 141, 122, 0.3);
  background: rgba(255, 255, 255, 0.95);
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(61, 141, 122, 0.1);
}

.card-icon {
  width: 50px;
  height: 50px;
  background: rgba(61, 141, 122, 0.08);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #3D8D7A;
  flex-shrink: 0;
}

.selection-card h3 {
  color: #3D8D7A;
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 5px;
}

.selection-card p {
  color: rgba(61, 141, 122, 0.7);
  font-size: 14px;
  margin: 0;
}

.card-arrow {
  position: absolute;
  right: 25px;
  color: rgba(61, 141, 122, 0.4);
  transition: all 0.3s ease;
}

.selection-card:hover .card-arrow {
  color: #3D8D7A;
  transform: translateX(3px);
}

/* Form Styles */
.auth-form-container {
  text-align: left;
}

.form-header {
  display: flex;
  align-items: center;
  margin-bottom: 30px;
  gap: 15px;
}

.back-btn {
  background: rgba(61, 141, 122, 0.1);
  border: none;
  border-radius: 10px;
  padding: 10px;
  cursor: pointer;
  color: #3D8D7A;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}

.back-btn:hover {
  background: rgba(61, 141, 122, 0.15);
  transform: translateX(-2px);
}

.form-header h2 {
  color: #3D8D7A;
  font-size: 24px;
  font-weight: 600;
  margin: 0;
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

.auth-btn {
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

.auth-btn:hover:not(:disabled) {
  transform: translateY(-3px);
  box-shadow: 0 12px 30px rgba(61, 141, 122, 0.25);
}

.auth-btn:active:not(:disabled) {
  transform: translateY(-1px);
}

.auth-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.forgot-section {
  margin: 25px 0;
  text-align: center;
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

.back-to-login {
  text-align: center;
  margin-top: 25px;
}

.back-link {
  color: rgba(61, 141, 122, 0.7);
  text-decoration: none;
  font-size: 16px;
  font-weight: 500;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  transition: all 0.3s ease;
  padding: 8px 16px;
  border-radius: 8px;
}

.back-link:hover {
  color: #3D8D7A;
  background: rgba(61, 141, 122, 0.05);
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

@media (max-width: 768px) {
  .auth-wrapper {
    padding: 25px;
  }
  
  .auth-box {
    padding: 40px 35px;
  }

  .class-icon {
    width: 80px;
    height: 80px;
  }

  h1 {
    font-size: 28px;
  }

  .subtitle {
    font-size: 16px;
  }

  .selection-card {
    padding: 20px;
    gap: 15px;
    flex-direction: column;
    text-align: center;
  }

  .card-icon {
    width: 45px;
    height: 45px;
  }

  .selection-card h3 {
    font-size: 17px;
  }

  .selection-card p {
    font-size: 13px;
  }

  .card-arrow {
    position: static;
    margin-top: 10px;
  }

  .form-header h2 {
    font-size: 22px;
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

  .auth-btn {
    font-size: 16px;
    padding: 16px;
  }

  .forgot-section a,
  .back-link {
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