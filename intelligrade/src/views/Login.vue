<template>
  <div class="auth-container">
    <div class="auth-box">
      <h1>Login</h1>
      <form>
        <input type="email" placeholder="Email" />
        <input type="password" placeholder="Password" />
        <button type="submit">Login</button>
      </form>
      <p class="auth-text">
        Don’t have an account?
        <router-link to="/signup">Sign Up</router-link>
      </p>
    </div>
  </div>
</template>

<style scoped>
.auth-container {
  background-color: #3d8d7a;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.auth-box {
  background: white;
  padding: 40px;
  border-radius: 10px;
  box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.2);
  width: 400px;
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
