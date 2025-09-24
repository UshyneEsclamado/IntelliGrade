<template>
  <div class="verification-container">
    <div v-if="isLoading" class="loading-state">
      <div class="logo-container">
        <img src="@/assets/New IntelliGrade Logo Way BG 3.png" alt="IntelliGrade" class="logo">
      </div>
      <h2>Verifying your email...</h2>
      <div class="spinner"></div>
    </div>
    <div v-else-if="verified" class="success-state">
      <div class="logo-container">
        <img src="@/assets/New IntelliGrade Logo Way BG 3.png" alt="IntelliGrade" class="logo">
      </div>
      <h2>✅ Email Verified Successfully!</h2>
      <p>Welcome to IntelliGrade! Your account has been created and verified.</p>
      <router-link to="/login" class="login-btn">Go to Login</router-link>
    </div>
    <div v-else class="error-state">
      <div class="logo-container">
        <img src="@/assets/New IntelliGrade Logo Way BG 3.png" alt="IntelliGrade" class="logo">
      </div>
      <h2>❌ Verification Failed</h2>
      <p>{{ error }}</p>
      <router-link to="/signup-student" class="retry-btn">Try Again</router-link>
    </div>
  </div>
</template>

<script>
import { supabase } from '../supabase.js';

export default {
  data() {
    return {
      isLoading: true,
      verified: false,
      error: null
    }
  },
  async mounted() {
    await this.handleEmailVerification();
  },
  methods: {
    async handleEmailVerification() {
      try {
        const { data: { session }, error } = await supabase.auth.getSession();
        
        if (error) throw error;
        
        if (session && session.user.email_confirmed_at) {
          const userData = session.user.user_metadata;
          
          const { error: profileError } = await supabase
            .from('profiles')
            .insert([{
              id: session.user.id,
              auth_user_id: session.user.id,
              full_name: userData.full_name,
              email: session.user.email,
              role: userData.role,
              student_id: userData.student_id || null,
              grade_level: userData.grade_level || null,
              email_verified: true,
              password_changed_at: new Date().toISOString()
            }]);

          if (profileError) throw profileError;
          
          this.verified = true;
        } else {
          throw new Error('Email verification incomplete');
        }
        
      } catch (err) {
        console.error('Verification error:', err);
        this.error = err.message;
      } finally {
        this.isLoading = false;
      }
    }
  }
}
</script>

<style scoped>
.verification-container {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #A3D1C6 0%, #B3D8A8 50%, #FBFFE4 100%);
  padding: 2rem;
}

.loading-state, .success-state, .error-state {
  background: white;
  padding: 3rem;
  border-radius: 15px;
  text-align: center;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
  max-width: 500px;
}

.logo-container {
  margin-bottom: 2rem;
}

.logo {
  width: 120px;
  height: 120px;
  object-fit: contain;
}

.login-btn, .retry-btn {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: white;
  padding: 0.75rem 2rem;
  border-radius: 8px;
  text-decoration: none;
  display: inline-block;
  margin-top: 1rem;
  font-weight: 600;
}

.spinner {
  border: 3px solid #f3f3f3;
  border-top: 3px solid #3D8D7A;
  border-radius: 50%;
  width: 30px;
  height: 30px;
  animation: spin 1s linear infinite;
  margin: 1rem auto;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

h2 {
  color: #3D8D7A;
  margin-bottom: 1rem;
}

p {
  color: #666;
  margin-bottom: 1rem;
}
</style>