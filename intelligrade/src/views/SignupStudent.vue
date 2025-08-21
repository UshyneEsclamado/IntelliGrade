<template>
  <div class="auth-wrapper">
    <div class="floating-elements">
      <div class="floating-circle circle-1"></div>
      <div class="floating-circle circle-2"></div>
      <div class="floating-circle circle-3"></div>
    </div>
    
    <div class="auth-box">
      <div class="logo-section">
        <div class="user-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12,3L1,9L12,15L21,10.09V17H23V9M5,13.18V17.18L12,21L19,17.18V13.18L12,17L5,13.18Z"/>
          </svg>
        </div>
        <h1>Create Student Account</h1>
        <p class="subtitle">Join our learning community</p>
      </div>

      <form @submit.prevent="handleSignup" class="signup-form">
        <div class="form-group">
          <label>Full Name</label>
          <div class="input-wrapper">
            <svg class="input-icon" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12,4A4,4 0 0,1 16,8A4,4 0 0,1 12,12A4,4 0 0,1 8,8A4,4 0 0,1 12,4M12,14C16.42,14 20,15.79 20,18V20H4V18C4,15.79 7.58,14 12,14Z"/>
            </svg>
            <input type="text" placeholder="Enter your full name" v-model="fullName" required />
          </div>
        </div>

        <div class="form-group">
          <label>Email</label>
          <div class="input-wrapper">
            <svg class="input-icon" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M20,8L12,13L4,8V6L12,11L20,6M20,4H4C2.89,4 2,4.89 2,6V18A2,2 0 0,0 4,20H20A2,2 0 0,0 22,18V6C22,5.89 21.1,4 20,4Z"/>
            </svg>
            <input type="email" placeholder="Enter your email" v-model="email" required />
          </div>
        </div>

        <div class="form-group">
          <label>Password</label>
          <div class="input-wrapper">
            <svg class="input-icon" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12,17A2,2 0 0,0 14,15C14,13.89 13.1,13 12,13A2,2 0 0,0 10,15A2,2 0 0,0 12,17M18,8A2,2 0 0,1 20,10V20A2,2 0 0,1 18,22H6A2,2 0 0,1 4,20V10C4,8.89 4.9,8 6,8H7V6A5,5 0 0,1 12,1A5,5 0 0,1 17,6V8H18M12,3A3,3 0 0,0 9,6V8H15V6A3,3 0 0,0 12,3Z"/>
            </svg>
            <input type="password" placeholder="Create a password" v-model="password" required />
          </div>
        </div>

        <div class="form-group">
          <label>Student ID</label>
          <div class="input-wrapper">
            <svg class="input-icon" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M20,4H4A2,2 0 0,0 2,6V18A2,2 0 0,0 4,20H20A2,2 0 0,0 22,18V6A2,2 0 0,0 20,4M20,18H4V6H20V18Z"/>
            </svg>
            <input type="text" placeholder="Enter your student ID" v-model="studentId" required />
          </div>
        </div>

        <div class="form-group">
          <label>Course/Year</label>
          <div class="input-wrapper">
            <svg class="input-icon" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12,3L1,9L12,15L21,10.09V17H23V9M5,13.18V17.18L12,21L19,17.18V13.18L12,17L5,13.18Z"/>
            </svg>
            <input type="text" placeholder="Enter your course and year" v-model="courseYear" required />
          </div>
        </div>

        <p v-if="error" class="error-message">{{ error }}</p>

        <button type="submit" class="signup-btn" :disabled="isLoading">
          <svg v-if="!isLoading" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
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

    <div class="geometric-shapes"></div>
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
      courseYear: "",
      error: "",
      isLoading: false
    };
  },
  methods: {
    async handleSignup() {
      if (!this.fullName || !this.email || !this.password || !this.studentId || !this.courseYear) {
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

        // Step 2: Insert additional user profile data into the "profiles" table
        const user = authData.user;
        const { error: profileError } = await supabase
          .from("profiles")
          .insert([
            {
              id: user.id,
              full_name: this.fullName,
              role: "student", // Automatically set the role to 'student'
              student_id: this.studentId,
              course_year: this.courseYear,
            },
          ]);

        if (profileError) {
          // If profile insertion fails, you might want to handle it or show an error
          throw profileError;
        }

        // Step 3: Redirect to the student dashboard on success
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
/* Change fixed to absolute to enable scrolling */
.auth-wrapper {
  position: absolute; 
  inset: 0;
  background: linear-gradient(135deg, #3D8D7A, #A3D1C6);
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  padding: 20px;
  font-family: 'Inter', sans-serif;
  overflow-y: auto; 
}

.auth-box {
  background: rgba(251, 255, 228, 0.95);
  backdrop-filter: blur(10px);
  padding: 35px;
  border-radius: 20px;
  box-shadow: 0 20px 40px rgba(61, 141, 122, 0.2);
  width: 100%;
  max-width: 500px;
  text-align: center;
  position: relative;
  margin: 80px auto;
  z-index: 1;
}

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

.login-section {
  margin-top: 20px;
  font-size: 16px;
  color: #3D8D7A;
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

.floating-circle {
  position: absolute;
  border-radius: 50%;
  opacity: 0.15;
  animation: float 8s ease-in-out infinite;
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255,255,255,0.1);
}

.circle-1 { 
  width: 100px; 
  height: 100px; 
  background: linear-gradient(45deg, #B3D8A8, transparent);
  top: 15%; 
  left: 10%; 
  animation-delay: 0s; 
}

.circle-2 { 
  width: 140px; 
  height: 140px; 
  background: linear-gradient(-45deg, #FBFFE4, transparent);
  bottom: 20%; 
  right: 15%; 
  animation-delay: 2s; 
}

.circle-3 { 
  width: 120px; 
  height: 120px; 
  background: linear-gradient(135deg, #A3D1C6, transparent);
  top: 45%; 
  left: 65%; 
  animation-delay: 4s; 
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

@keyframes float {
  0%, 100% { 
    transform: translateY(0) rotate(0deg) scale(1); 
  }
  50% { 
    transform: translateY(-20px) rotate(180deg) scale(1.05); 
  }
}

@media (max-height: 700px) {
  .auth-wrapper {
    align-items: flex-start;
    padding: 20px;
  }
  
  .auth-box {
    margin: 20px auto;
  }
}

@media (max-width: 768px) {
  .auth-box {
    padding: 30px;
    max-width: 400px;
    margin: 15px;
  }
  
  .signup-form {
    max-width: 340px;
  }

  .user-icon {
    width: 70px;
    height: 70px;
  }

  .user-icon svg {
    width: 28px;
    height: 28px;
  }

  h1 {
    font-size: 24px;
  }

  .subtitle {
    font-size: 14px;
  }

  input {
    padding: 12px 12px 12px 40px;
    font-size: 14px;
  }

  .input-icon {
    width: 18px !important;
    height: 18px !important;
  }

  .signup-btn {
    font-size: 15px;
    padding: 12px;
  }

  .login-section {
    font-size: 14px;
  }
}
</style>