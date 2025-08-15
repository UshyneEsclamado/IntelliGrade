<template>
  <div class="auth-wrapper">
    <div class="auth-box">
      <h1>Create Student Account</h1>
      <form>
        <input type="text" placeholder="Full Name" />
        <input type="email" placeholder="Email" />
        <input type="password" placeholder="Password" />
        <input type="text" placeholder="Student ID" />
        <input type="text" placeholder="Course/Year" />
        <button type="submit" class="signup-btn">Sign Up</button>
      </form>
      <p class="auth-text">
        Already have an account?
        <router-link to="/login" class="login-btn-link">Login</router-link>
      </p>
    </div>
  </div>
</template>

<style scoped>
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

/* Match placeholder style from login */
input::placeholder {
  color: #6c757d; /* same faded gray look */
  font-weight: normal;
}

input:focus {
  border-color: #3d8d7a;
  box-shadow: 0 0 5px rgba(61, 141, 122, 0.5);
}

.signup-btn {
  background-color: #3d8d7a;
  color: white;
  padding: 12px;
  font-size: 16px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.signup-btn:hover {
  background-color: #357a66;
}

.auth-text {
  text-align: center;
  margin-top: 15px;
  color: #3d8d7a; 
  font-weight: bold;
}
</style>
