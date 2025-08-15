<template>
  <div class="role-wrapper">
    <div class="role-box">
      <h1>Select Your Role</h1>
     <div class="buttons">
  <router-link to="/signup-student" class="role-btn">Student</router-link>
  <router-link to="/signup" class="role-btn">Teacher</router-link>
</div>
    </div>
  </div>
</template>

<style scoped>
.role-wrapper {
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

.role-box {
  background: #FBFFE4;
  padding: 40px;
  border-radius: 10px;
  box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.2);
  text-align: center;
  max-width: 500px;
  width: 100%;
}

h1 {
  color: #3d8d7a;
  margin-bottom: 30px;
}

.buttons {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.role-btn {
  background-color: #3d8d7a;
  color: white;
  padding: 15px;
  font-size: 18px;
  border-radius: 5px;
  text-decoration: none;
  font-weight: bold;
}

.role-btn:hover {
  background-color: #357a66;
}
</style>
