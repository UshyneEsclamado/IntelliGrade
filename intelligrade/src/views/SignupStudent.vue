<template>
  <div class="auth-wrapper">
    <div class="auth-box">
      <h1>Create Student Account</h1>
      <form @submit.prevent="handleSignup">
        <input type="text" placeholder="Full Name" v-model="fullName" />
        <input type="email" placeholder="Email" v-model="email" />
        <input type="password" placeholder="Password" v-model="password" />
        <input type="text" placeholder="Student ID" v-model="studentId" />
        <input type="text" placeholder="Course/Year" v-model="courseYear" />
        <button type="submit" class="signup-btn">Sign Up</button>
      </form>

      <!-- Error message -->
      <p v-if="error" class="error-message">{{ error }}</p>

      <p class="auth-text">
        Already have an account?
        <router-link to="/login" class="login-btn-link">Login</router-link>
      </p>
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
      courseYear: "",
      error: ""
    };
  },
  methods: {
    async handleSignup() {
      // Validate required fields
      if (!this.fullName || !this.email || !this.password) {
        this.error = "Full Name, Email, and Password are required";
        return;
      }

      // Sign up with Supabase
      const { data: user, error } = await supabase.auth.signUp({
        email: this.email,
        password: this.password
      });

      if (error) {
        this.error = error.message;
      } else {
        // Insert additional student info into profiles table
        const { error: profileError } = await supabase.from("profiles").insert([
          {
            id: user.user.id,
            full_name: this.fullName,
            role: "student",
            student_id: this.studentId,
            course_year: this.courseYear
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
/* Keep your original styles */
.auth-wrapper { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background-color: #3d8d7a; display: flex; justify-content: center; align-items: center; }
.auth-box { background: #FBFFE4; padding: 40px; border-radius: 10px; box-shadow: 0px 4px 20px rgba(0,0,0,0.2); width: 100%; max-width: 500px; text-align: center; }
h1 { color: #3d8d7a; margin-bottom: 20px; }
form { display: flex; flex-direction: column; }
input { margin: 10px 0; padding: 12px; font-size: 16px; border-radius: 5px; border: 1px solid #ccc; outline: none; }
input::placeholder { color: #6c757d; font-weight: normal; }
input:focus { border-color: #3d8d7a; box-shadow: 0 0 5px rgba(61,141,122,0.5); }
.signup-btn { background-color: #3d8d7a; color: white; padding: 12px; font-size: 16px; border: none; border-radius: 5px; cursor: pointer; }
.signup-btn:hover { background-color: #357a66; }
.auth-text { text-align: center; margin-top: 15px; color: #3d8d7a; font-weight: bold; }
.error-message { color: red; margin: 10px 0; font-size: 14px; font-weight: bold; }
</style>
