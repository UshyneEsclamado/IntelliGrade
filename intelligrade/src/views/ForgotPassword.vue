<template>
  <div class="forgot-password-wrapper">
    <h2>Forgot your password?</h2>
    <form @submit.prevent="submitEmail">
      <label for="email">Enter your email address:</label>
      <input v-model="email" type="email" id="email" required />
      <button type="submit" :disabled="loading">Send Reset Link</button>
    </form>
    <div v-if="message" class="message">{{ message }}</div>
    <div v-if="error" class="error">{{ error }}</div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'ForgotPassword',
  data() {
    return {
      email: '',
      loading: false,
      message: '',
      error: ''
    };
  },
  methods: {
    async submitEmail() {
      this.loading = true;
      this.message = '';
      this.error = '';
      try {
        await axios.post('/api/auth/forgot-password', { email: this.email });
        this.message = 'If your email exists in our system, a reset link has been sent.';
      } catch (err) {
        this.error = err.response?.data?.detail || 'Failed to send reset link.';
      } finally {
        this.loading = false;
      }
    }
  }
};
</script>

<style scoped>
.forgot-password-wrapper {
  max-width: 400px;
  margin: 60px auto;
  padding: 2rem;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}
label {
  display: block;
  margin-bottom: 0.5rem;
}
input[type="email"] {
  width: 100%;
  padding: 0.5rem;
  margin-bottom: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}
button {
  width: 100%;
  padding: 0.7rem;
  background: #4A9B8E;
  color: #fff;
  border: none;
  border-radius: 4px;
  font-weight: bold;
  cursor: pointer;
}
button:disabled {
  background: #b2dfdb;
  cursor: not-allowed;
}
.message {
  color: #388e3c;
  margin-top: 1rem;
}
.error {
  color: #d32f2f;
  margin-top: 1rem;
}
</style>
