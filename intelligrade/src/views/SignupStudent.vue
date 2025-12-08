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
      
      <!-- Calculator symbols -->
      <div class="floating-element element-8">
        <svg width="34" height="34" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M9,11H7V9H9V11M13,11H11V9H13V11M17,11H15V9H17V11M19,3H18V1H16V1H6V3H5C3.89,3 3,3.9 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5C21,3.9 20.1,3 19,3H18V1M17,12H12V17H17V12Z"/>
        </svg>
      </div>
      
      <!-- User symbols -->
      <div class="floating-element element-9">
        <svg width="29" height="29" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M7.07,18.28C7.5,17.38 10.12,16.5 12,16.5C13.88,16.5 16.5,17.38 16.93,18.28C15.57,19.36 13.86,20 12,20C10.14,20 8.43,19.36 7.07,18.28M18.36,16.83C16.93,15.09 13.46,14.5 12,14.5C10.54,14.5 7.07,15.09 5.64,16.83C4.62,15.5 4,13.82 4,12C4,7.59 7.59,4 12,4C16.41,4 20,7.59 20,12C20,13.82 19.38,15.5 18.36,16.83M12,6C10.06,6 8.5,7.56 8.5,9.5C8.5,11.44 10.06,13 12,13C13.94,13 15.5,11.44 15.5,9.5C15.5,7.56 13.94,6 12,6M12,11A1.5,1.5 0 0,1 10.5,9.5A1.5,1.5 0 0,1 12,8A1.5,1.5 0 0,1 13.5,9.5A1.5,1.5 0 0,1 12,11Z"/>
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
    </div>

    <div class="auth-container">
      <div class="logo-space logo-align">
        <div class="intelligrade-branding">
          <div class="logo-container">
            <div class="logo-image-container large-logo">
              <img 
                 src="@/assets/DIGI CHECK LOGO WAY BG.png"
                alt="DigiCheck Logo" 
                class="logo-image large-logo-img"
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
          <p class="subtitle">Join your class and start learning with DigiCheck</p>
        </div>

        <div v-if="signupSuccess" class="success-display">
          <div class="success-icon">✅</div>
          <p>{{ successMessage }}</p>
        </div>

        <form @submit.prevent="handleSignup" class="signup-form" v-if="!signupSuccess">
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
            <!-- ✅ SAFE: Password Strength Indicator with proper checks -->
            <div v-if="password && password.length > 0" class="password-strength">
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
            <!-- ✅ SAFE: Password Error Messages with proper checks -->
            <div v-if="passwordErrors && passwordErrors.length > 0 && password && password.length > 0" class="password-errors">
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
            {{ isLoading ? 'Creating Account...' : 'Join DigiCheck' }}
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

<script lang="ts">
import { supabase } from "../supabase.js";

export default {
  data() {
    return {
      fullName: "",
      email: "",
      password: "",
      studentId: "",
      gradeLevel: "7",
      error: "",
      isLoading: false,
      showPassword: false,
      passwordStrength: 0,
      passwordErrors: [],
      signupSuccess: false,
      successMessage: ""
    };
  },
  watch: {
    password(newPassword) {
      if (newPassword !== undefined && newPassword !== null) {
        this.validatePassword(newPassword);
      }
    }
  },
  methods: {
    togglePasswordVisibility() {
      this.showPassword = !this.showPassword;
    },
    
    validatePassword(password) {
      this.passwordErrors = [];
      let strength = 0;
      
      // Add safety check
      if (!password || password === undefined || password === null) {
        this.passwordStrength = 0;
        return;
      }

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
      this.error = "";

      console.log('=== STUDENT SIGNUP STARTED ===');

      // Validation checks
      if (!this.fullName || !this.email || !this.password || !this.studentId || !this.gradeLevel) {
        this.error = "Please fill in all fields.";
        return;
      }

      if (this.passwordErrors.length > 0) {
        this.error = 'Your password does not meet the security policy. Please fix the issues listed below the password field.';
        return;
      }

      const gradeNum = parseInt(this.gradeLevel);
      if (gradeNum < 7 || gradeNum > 10) {
        this.error = "Grade level must be between 7 and 10.";
        return;
      }

      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(this.email)) {
        this.error = "Please enter a valid email address.";
        return;
      }

      this.isLoading = true;

      try {
       console.log('📝 Signup Data Being Sent:');
console.log('Student ID:', this.studentId.trim());
console.log('Grade Level:', parseInt(this.gradeLevel, 10));
console.log('Full metadata:', {
  full_name: this.fullName.trim(),
  role: 'student',
  student_id: this.studentId.trim(),
  grade_level: parseInt(this.gradeLevel, 10)
});

        // Check if student ID is already taken
        const { data: existingStudent, error: checkError } = await supabase
          .from('students')
          .select('student_id')
          .eq('student_id', this.studentId.trim())
          .maybeSingle();

        if (existingStudent) {
          throw new Error('This Student ID is already registered. Please use a different Student ID.');
        }

        // Check if email is already taken
        const { data: existingProfile, error: profileError } = await supabase
          .from('profiles')
          .select('email')
          .eq('email', this.email.toLowerCase().trim())
          .maybeSingle();

        if (existingProfile) {
          throw new Error('An account with this email already exists. Please try logging in instead.');
        }

        console.log('✅ Validation passed, creating auth user...');
        
        // Create the Supabase auth user with properly structured metadata
    const { data: authData, error: authError } = await supabase.auth.signUp({
  email: this.email.toLowerCase().trim(),
  password: this.password,
  options: {
    emailRedirectTo: `${window.location.origin}/email-verified`,
    data: {
      full_name: this.fullName.trim(),
      role: 'student',
      student_id: this.studentId.trim(),
      grade_level: parseInt(this.gradeLevel, 10) 
    }
  }
});
        if (authError) {
          console.error('❌ Auth signup error:', authError);
          
          // Handle specific Supabase errors
          if (authError.message?.includes('User already registered')) {
            throw new Error('An account with this email already exists. Please try logging in instead.');
          } else if (authError.message?.includes('Email rate limit exceeded')) {
            throw new Error('Too many signup attempts. Please wait a few minutes and try again.');
          } else if (authError.message?.includes('Invalid email')) {
            throw new Error('Please enter a valid email address.');
          } else if (authError.message?.includes('Password')) {
            throw new Error('Password must be at least 6 characters long.');
          } else if (authError.message?.includes('Signup is disabled')) {
            throw new Error('Account registration is currently disabled. Please contact support.');
          } else {
            throw new Error(authError.message || 'Failed to create account. Please try again.');
          }
        }

        if (!authData.user) {
          console.error('❌ No user data returned from signup');
          throw new Error("Signup failed. No user data returned. Please try again.");
        }

        console.log('✅ Auth user created:', authData.user.id);
        console.log('User metadata sent:', authData.user.user_metadata);

        // Wait longer for the database trigger to complete
        console.log('⏳ Waiting for database trigger to create profile and student record...');
        await new Promise(resolve => setTimeout(resolve, 3000));

        // Verify that the profile was created
        console.log('🔍 Verifying profile creation...');
        const { data: profileCheck, error: profileCheckError } = await supabase
          .from('profiles')
          .select('id, role, full_name')
          .eq('auth_user_id', authData.user.id)
          .single();

        if (profileCheckError || !profileCheck) {
          console.error('❌ Profile not created:', profileCheckError);
          
          // Try to manually create the profile if trigger failed
          console.log('⚠️ Trigger failed, attempting manual profile creation...');
          const { data: manualProfile, error: manualProfileError } = await supabase
            .from('profiles')
            .insert({
              auth_user_id: authData.user.id,
              full_name: this.fullName.trim(),
              email: this.email.toLowerCase().trim(),
              role: 'student',
              email_verified: authData.user.email_confirmed_at != null
            })
            .select()
            .single();

          if (manualProfileError) {
            console.error('❌ Manual profile creation failed:', manualProfileError);
            throw new Error('Failed to create your profile. Please contact support with error: ' + manualProfileError.message);
          }

          console.log('✅ Manual profile created:', manualProfile);

          // Now create the student record
          console.log('Creating student record...');
          const { data: studentRecord, error: studentError } = await supabase
            .from('students')
            .insert({
              profile_id: manualProfile.id,
              student_id: this.studentId.trim(),
              full_name: this.fullName.trim(),
              email: this.email.toLowerCase().trim(),
              grade_level: gradeNum,
              is_active: true
            })
            .select()
            .single();

          if (studentError) {
            console.error('❌ Student record creation failed:', studentError);
            throw new Error('Failed to create student record. Please contact support with error: ' + studentError.message);
          }

          console.log('✅ Student record created:', studentRecord);
        } else {
          console.log('✅ Profile found:', profileCheck);

          // Verify student record was created
          console.log('🔍 Verifying student record...');
          const { data: studentCheck, error: studentCheckError } = await supabase
            .from('students')
            .select('id, student_id, grade_level')
            .eq('profile_id', profileCheck.id)
            .single();

          if (studentCheckError || !studentCheck) {
            console.error('❌ Student record not created:', studentCheckError);
            
            // Try manual creation
            console.log('⚠️ Attempting manual student record creation...');
            const { data: manualStudent, error: manualStudentError } = await supabase
              .from('students')
              .insert({
                profile_id: profileCheck.id,
                student_id: this.studentId.trim(),
                full_name: this.fullName.trim(),
                email: this.email.toLowerCase().trim(),
                grade_level: gradeNum,
                is_active: true
              })
              .select()
              .single();

            if (manualStudentError) {
              console.error('❌ Manual student creation failed:', manualStudentError);
              throw new Error('Failed to create student record. Please contact support.');
            }

            console.log('✅ Manual student record created:', manualStudent);
          } else {
            console.log('✅ Student record found:', studentCheck);
          }
        }

        console.log('✅ SIGNUP SUCCESSFUL!');

        // Show success message
        this.signupSuccess = true;
        
        if (!authData.session) {
          console.log('📧 Email confirmation required');
          this.successMessage = `🎉 Student account created successfully! 

Please check your email (${this.email}) and click the confirmation link to verify your account. 

After verification, you'll be able to log in with your credentials.

Note: The email might take a few minutes to arrive. Don't forget to check your spam folder!`;
        } else {
          console.log('✅ Account created and automatically verified');
          this.successMessage = `🎉 Student account created successfully! 

Your account has been verified and you can now log in.`;
        }

        // Clear sensitive data
        this.password = '';
        this.passwordStrength = 0;
        this.passwordErrors = [];
        
        // Redirect after 6 seconds
        setTimeout(() => {
          this.$router.push('/login');
        }, 6000);
        
      } catch (err) {
        console.error("❌ Student Signup error:", err);
        
        // User-friendly error messages
        if (err.message?.includes('already registered') || 
            err.message?.includes('already exists')) {
          this.error = 'An account with this email already exists. Please try logging in instead.';
        } else if (err.message?.includes('Student ID')) {
          this.error = err.message;
        } else if (err.message?.includes('rate limit')) {
          this.error = 'Too many signup attempts. Please wait a few minutes and try again.';
        } else if (err.message?.includes('contact support')) {
          this.error = err.message;
        } else {
          this.error = err.message || "An unexpected error occurred during signup. Please try again.";
        }
      } finally {
        this.isLoading = false;
        console.log('=== Signup process completed ===');
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

.logo-space.logo-align {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  max-width: 450px;
  height: 100%;
  /* Align logo vertically with wordings */
  margin-top: 0;
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
  justify-content: center;
  object-fit: contain;
  animation: gentleFloat 8s ease-in-out infinite;
  background: transparent;
}

.logo-image-container.large-logo {
  width: 340px;
  height: 340px;
  display: flex;
  align-items: center;
  justify-content: center;
  filter: drop-shadow(0 15px 40px rgba(74, 155, 142, 0.3));
  transition: all 0.4s ease;
  margin-bottom: 0.75rem;
}

.logo-image-container.large-logo:hover {
  filter: drop-shadow(0 20px 50px rgba(74, 155, 142, 0.4));
  transform: scale(1.05);
}

.logo-image.large-logo-img {
  width: 320px;
  height: 320px;
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

.success-display {
  background: rgba(34, 197, 94, 0.1);
  border: 2px solid rgba(34, 197, 94, 0.2);
  border-radius: 9px;
  padding: 1rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 1rem;
  text-align: left;
}

.success-icon {
  font-size: 1.2rem;
  flex-shrink: 0;
}

.success-display p {
  color: #16a34a;
  font-size: 0.85rem;
  margin: 0;
  font-weight: 500;
  line-height: 1.4;
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
  
  .logo-image-container.large-logo {
    width: 200px;
    height: 200px;
    margin-bottom: 0.3rem;
  }
  .logo-image.large-logo-img {
    width: 180px;
    height: 180px;
  }
  .brand-tagline {
    font-size: 0.8rem;
    max-width: 280px;
    margin-bottom: 0.2rem;
  }

  /* Hide some duplicate elements on mobile to reduce clutter */
  .element-13, .element-14, .element-15, .element-16 {
    display: none;
  }
}

@media (max-width: 480px) {
  .logo-image-container.large-logo {
    width: 160px;
    height: 160px;
    margin-bottom: 0.15rem;
  }
  .logo-image.large-logo-img {
    width: 140px;
    height: 140px;
  }
  .brand-tagline {
    font-size: 0.75rem;
    max-width: 240px;
    margin-bottom: 0.1rem;
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