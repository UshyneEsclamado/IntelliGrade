<template>
    <div class="login-container">
      <h1>Welcome to IntelliGrade</h1>
      <form>
        <input type="text" placeholder="Username" />
        <input type="password" placeholder="Password" />
        <button type="submit">Login</button>
      </form>
      <p class="signup-text">
        Don’t have an account?
        <router-link to="/signup">Create one</router-link>
      </p>
    </div>
  </template>
  
  <style scoped>
  .login-container {
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
  .signup-text {
    margin-top: 12px;
  }
  </style>
  