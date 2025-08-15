<template>
  <div class="auth-wrapper">
    <div class="auth-box">
      <h1>Login</h1>
      <form @submit.prevent="handleLogin">
        <input 
          type="email" 
          placeholder="Email" 
          v-model="email"
        />
        <input 
          type="password" 
          placeholder="Password" 
          v-model="password"
        />
        <button type="submit" class="login-btn">Login</button>
      </form>

      <!-- Show error if fields are empty or login fails -->
      <p v-if="error" class="error-message">{{ error }}</p>

      <p class="forgot-password">
        <a href="#" @click.prevent="handleForgotPassword">Forgot password?</a>
      </p>

      <!-- Redirect to Role Selection -->
      <router-link to="/role-selection" class="create-account-btn">
        Create New Account
      </router-link>
    </div>
  </div>
</template>

<script>
import { supabase } from "../supabase.js";

export default {
  data() {
    return {
      email: "",
      password: "",
      error: ""
    };
  },
  methods: {
    async handleLogin() {
      this.error = "";
      if (!this.email || !this.password) {
        this.error = "Email and password are required";
        return;
      }

      const { data: user, error } = await supabase.auth.signInWithPassword({
        email: this.email,
        password: this.password
      });

      if (error) {
        this.error = error.message;
      } else {
        const { data, error: profileError } = await supabase
          .from("profiles")
          .select("role")
          .eq("id", user.user.id)
          .single();

        if (profileError) {
          this.error = profileError.message;
        } else {
          if (data.role === "teacher") {
            this.$router.push("/teacher-home");
          } else if (data.role === "student") {
            this.$router.push("/student-home");
          }
        }
      }
    },

    async handleForgotPassword() {
      this.error = "";
      if (!this.email) {
        this.error = "Please enter your email to reset password";
        return;
      }

      const { data, error } = await supabase.auth.resetPasswordForEmail(this.email, {
        redirectTo: window.location.origin + "/login" // redirect after reset
      });

      if (error) {
        this.error = error.message;
      } else {
        alert("Password reset email sent! Please check your inbox.");
      }
    }
  }
};
</script>

<style scoped>
/* Keep your original styles */
.auth-wrapper {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: #3d8d7a;
  display: flex;
  justify-content: center;
  align-items: center;
}

.auth-box {
  background: #FBFFE4;
  padding: 40px;
  border-radius: 10px;
  box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.2);
  width: 100%;
  max-width: 500px;
  text-align: center;
}

h1 {
  color: #3d8d7a;
  margin-bottom: 20px;
}

form {
  display: flex;
  flex-direction: column;
}

input {
  margin: 10px 0;
  padding: 12px;
  font-size: 16px;
  border-radius: 5px;
  border: 1px solid #ccc;
  outline: none;
}

input:focus {
  border-color: #3d8d7a;
  box-shadow: 0 0 5px rgba(61, 141, 122, 0.5);
}

.login-btn {
  background-color: #3d8d7a;
  color: white;
  padding: 12px;
  font-size: 16px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.login-btn:hover {
  background-color: #357a66;
}

.forgot-password {
  margin: 15px 0;
}

.forgot-password a {
  text-decoration: none;
  color: #3d8d7a;
  font-size: 14px;
}

.forgot-password a:hover {
  text-decoration: underline;
}

.create-account-btn {
  display: inline-block;
  background-color: #39645a;
  color: white;
  padding: 12px;
  font-size: 16px;
  border-radius: 5px;
  cursor: pointer;
  text-decoration: none;
}

.create-account-btn:hover {
  background-color: #A3D1C6;
}

.error-message {
  color: red;
  margin: 10px 0;
  font-size: 14px;
  font-weight: bold;
}
</style>
