<template>
    <div class="signup-container">
      <h1>Create Account</h1>
      <form>
        <input type="text" placeholder="Username" />
        <input type="email" placeholder="Email" />
        <input type="password" placeholder="Password" />
        <button type="submit">Sign Up</button>
      </form>
      <p class="login-text">
        Already have an account?
        <router-link to="/login">Login</router-link>
      </p>
    </div>
  </template>
  
  <style scoped>
  .signup-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
  }
  form {
    display: flex;
    flex-direction: column;
    width: 250px;
  }
  input, button {
    margin: 8px 0;
    padding: 10px;
  }
  .login-text {
    margin-top: 12px;
  }
  </style>
  