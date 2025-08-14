<template>
  <div class="auth-wrapper">
    <div class="auth-box">
      <h1>Create Account</h1>
      <form>
        <input type="text" placeholder="Username" />
        <input type="email" placeholder="Email" />
        <input type="password" placeholder="Password" />
        <button type="submit">Sign Up</button>
      </form>
      <p class="auth-text">
        Already have an account?
        <router-link to="/login">Login</router-link>
      </p>
    </div>
  </div>
</template>

<style scoped>
.auth-wrapper {
  position: fixed; /* Force full-screen */
  top: 0;
  left: 0;
  width: 100vw; /* Full width */
  height: 100vh; /* Full height */
  background-color: #3d8d7a;
  display: flex;
  justify-content: center;
  align-items: center;
}

.auth-box {
  background: white;
  padding: 40px;
  border-radius: 10px;
  box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.2);
  width: 100%;
  max-width: 500px; /* Wider for desktop */
}

h1 {
  text-align: center;
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
}

button {
  background-color: #3d8d7a;
  color: white;
  padding: 12px;
  font-size: 16px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #357a66;
}

.auth-text {
  text-align: center;
  margin-top: 15px;
}
</style>
