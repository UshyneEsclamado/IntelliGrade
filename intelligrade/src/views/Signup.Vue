<template>
  <div class="auth-wrapper">
    <div class="auth-box">
      <h1>Create Account</h1>
      <form @submit.prevent="handleSignup">
        <input type="text" placeholder="Name" v-model="name" />
        <input type="email" placeholder="Email" v-model="email" />
        <input type="password" placeholder="Password" v-model="password" />
        <button type="submit" class="signup-btn">Sign Up</button>
      </form>

      <!-- Error message -->
      <p v-if="error" class="error-message">{{ error }}</p>

      <p class="auth-text">
        Already have an account?
        <router-link to="/login" class="login-link">Login</router-link>
      </p>
    </div>
  </div>
</template>

<script>
import { supabase } from "../supabase.js";

export default {
  data() {
    return {
      name: "",
      email: "",
      password: "",
      error: ""
    };
  },
  methods: {
    async handleSignup() {
      // Validate required fields
      if (!this.name || !this.email || !this.password) {
        this.error = "Name, Email, and Password are required";
        return;
      }

      // Sign up with Supabase Auth
      const { data: user, error } = await supabase.auth.signUp({
        email: this.email,
        password: this.password
      });

      if (error) {
        this.error = error.message;
      } else {
        // Insert teacher info into profiles table
        const { error: profileError } = await supabase.from("profiles").insert([
          {
            id: user.user.id,
            full_name: this.name,
            role: "teacher"
          }
        ]);

        if (profileError) {
          this.error = profileError.message;
        } else {
          alert("Signup successful! Please check your email to confirm.");
          this.$router.push("/login");
        }
      }
    }
  }
};
</script>

<style scoped>
/* Wrapper */
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

/* Auth box */
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

/* Form */
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
  transition: border-color 0.3s, box-shadow 0.3s;
}

input:focus {
  border-color: #3d8d7a;
  box-shadow: 0 0 5px rgba(61, 141, 122, 0.5);
}

/* Buttons */
.signup-btn {
  background-color: #3d8d7a;
  color: white;
  padding: 12px;
  font-size: 16px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 10px;
}

.signup-btn:hover {
  background-color: #357a66;
}

/* Text & links */
.auth-text {
  margin-top: 15px;
  color: #3d8d7a;
  font-weight: bold;
}

.login-link {
  color: #3d8d7a;
  font-weight: bold;
  text-decoration: none;
}

.login-link:hover {
  text-decoration: underline;
}

/* Error message */
.error-message {
  color: red;
  margin: 10px 0;
  font-size: 14px;
  font-weight: bold;
}
</style>
