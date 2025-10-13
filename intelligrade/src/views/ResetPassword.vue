<template>
  <div class="reset-password-wrapper">
    <h2>Reset your password</h2>
    <form @submit.prevent="submitReset">
      <label for="password">New Password:</label>
      <input v-model="password" type="password" id="password" required />
      <button type="submit" :disabled="loading">Reset Password</button>
    </form>
    <div v-if="message" class="message">{{ message }}</div>
    <div v-if="error" class="error">{{ error }}</div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'ResetPassword',
  data() {
    return {
      password: '',
      loading: false,
      message: '',
      error: ''
    };
  },
  computed: {
    token() {
      return this.$route.query.token;
    }
  },
  methods: {
    async submitReset() {
      this.loading = true;
      this.message = '';
      this.error = '';
      try {
        await axios.post('/api/auth/reset-password', {
          token: this.token,
          new_password: this.password
        });
        this.message = 'Your password has been reset. You can now log in.';
      } catch (err) {
        this.error = err.response?.data?.detail || 'Failed to reset password.';
      } finally {
        this.loading = false;
      }
    }
  }
};
</script>

<style scoped>
.reset-password-wrapper {
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
input[type="password"] {
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
