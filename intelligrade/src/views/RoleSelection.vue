<template>
  <div class="auth-wrapper">
    <div class="geometric-shapes"></div>
    <div class="floating-elements">
      <div class="floating-circle circle-1"></div>
      <div class="floating-circle circle-2"></div>
      <div class="floating-circle circle-3"></div>
    </div>
    <div class="auth-box">
      <div class="logo-section">
        <div class="user-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12,5A3.5,3.5 0 0,0 8.5,8.5A3.5,3.5 0 0,0 12,12A3.5,3.5 0 0,0 15.5,8.5A3.5,3.5 0 0,0 12,5M12,7A1.5,1.5 0 0,1 13.5,8.5A1.5,1.5 0 0,1 12,10A1.5,1.5 0 0,1 10.5,8.5A1.5,1.5 0 0,1 12,7M5.5,8A2.5,2.5 0 0,0 3,10.5C3,11.44 3.53,12.25 4.29,12.68C4.65,12.88 5.06,13 5.5,13C5.94,13 6.35,12.88 6.71,12.68C7.08,12.47 7.39,12.17 7.62,11.81C6.89,10.86 6.5,9.7 6.5,8.5C6.5,8.41 6.5,8.31 6.5,8.22C6.2,8.08 5.86,8 5.5,8M18.5,8C18.14,8 17.8,8.08 17.5,8.22C17.5,8.31 17.5,8.41 17.5,8.5C17.5,9.7 17.11,10.86 16.38,11.81C16.5,12 16.63,12.15 16.78,12.3C16.94,12.45 17.1,12.58 17.29,12.68C17.65,12.88 18.06,13 18.5,13C18.94,13 19.35,12.88 19.71,12.68C20.47,12.25 21,11.44 21,10.5A2.5,2.5 0 0,0 18.5,8M12,14C9.66,14 5,15.17 5,17.5V19H19V17.5C19,15.17 14.34,14 12,14M4.71,14.55C2.78,14.78 0,15.76 0,17.5V19H3V17.07C3,16.06 3.69,15.22 4.71,14.55M19.29,14.55C20.31,15.22 21,16.06 21,17.07V19H24V17.5C24,15.76 21.22,14.78 19.29,14.55M12,16C13.53,16 15.24,16.5 16.23,17H7.77C8.76,16.5 10.47,16 12,16Z"/>
          </svg>
        </div>
        <h1>Select Your Role</h1>
        <p class="subtitle">Choose how you want to join</p>
      </div>

      <div class="buttons">
        <router-link to="/signup-student" class="role-btn student-btn">
          <svg class="btn-icon" width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 3L1 9L12 15L21 10.09V17H23V9M5 13.18V17.18L12 21L19 17.18V13.18L12 17L5 13.18Z"/>
          </svg>
          Student
        </router-link>
        
        <router-link to="/signup" class="role-btn teacher-btn">
          <svg class="btn-icon" width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M20,17A2,2 0 0,0 22,15V4A2,2 0 0,0 20,2H9.46C9.81,2.61 10,3.3 10,4H20V15H11V17M15,7V9H9V22H7V16H5V22H3V14H1.5V9A2,2 0 0,1 3.5,7H15M8,4A2,2 0 0,1 6,6A2,2 0 0,1 4,4A2,2 0 0,1 6,2A2,2 0 0,1 8,4Z"/>
          </svg>
          Teacher
        </router-link>
      </div>

      <div class="login-section">
        <router-link to="/login" class="login-link">
          Already have an account? Sign in
        </router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Existing base styles */
* { margin: 0; padding: 0; box-sizing: border-box; }

/* Auth wrapper styles */
.auth-wrapper {
  position: fixed;
  inset: 0;
  background: linear-gradient(135deg, #3D8D7A, #A3D1C6);
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  padding: 20px;
  font-family: 'Inter', sans-serif;
}

/* Geometric background styles */
.geometric-shapes {
  position: fixed;
  inset: 0;
  z-index: 0;
  overflow: hidden;
  background: linear-gradient(135deg, #3D8D7A, #A3D1C6);
}

.geometric-shapes::before {
  content: '';
  position: absolute;
  width: 100%;
  height: 100%;
  background: 
    linear-gradient(45deg, transparent 48%, rgba(255,255,255,0.1) 50%, transparent 52%) 0 0 / 60px 60px,
    linear-gradient(-45deg, transparent 48%, rgba(255,255,255,0.1) 50%, transparent 52%) 0 0 / 60px 60px,
    radial-gradient(circle at 20% 30%, rgba(255,255,255,0.1) 0, transparent 50px),
    radial-gradient(circle at 80% 20%, rgba(255,255,255,0.1) 0, transparent 70px),
    radial-gradient(circle at 10% 80%, rgba(255,255,255,0.1) 0, transparent 60px),
    radial-gradient(circle at 90% 70%, rgba(255,255,255,0.1) 0, transparent 80px);
  animation: moveBackground 30s linear infinite;
}

.geometric-shapes::after {
  content: '';
  position: absolute;
  inset: 0;
  background:
    radial-gradient(circle at 10% 20%, rgba(255,255,255,0.2) 0, transparent 200px),
    radial-gradient(circle at 90% 80%, rgba(255,255,255,0.2) 0, transparent 200px),
    radial-gradient(circle at 50% 50%, rgba(255,255,255,0.1) 0, transparent 300px);
  animation: floatShapes 20s ease-in-out infinite;
}

/* Floating elements styles */
.floating-elements {
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 0;
}

.floating-circle {
  position: absolute;
  border-radius: 50%;
  opacity: 0.15;
  animation: float 8s ease-in-out infinite;
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255,255,255,0.1);
}

.circle-1 { 
  width: 100px; 
  height: 100px; 
  background: linear-gradient(45deg, #B3D8A8, transparent);
  top: 15%; 
  left: 10%; 
  animation-delay: 0s; 
}

.circle-2 { 
  width: 140px; 
  height: 140px; 
  background: linear-gradient(-45deg, #FBFFE4, transparent);
  bottom: 20%; 
  right: 15%; 
  animation-delay: 2s; 
}

.circle-3 { 
  width: 120px; 
  height: 120px; 
  background: linear-gradient(135deg, #A3D1C6, transparent);
  top: 45%; 
  left: 65%; 
  animation-delay: 4s; 
}

/* Update animations */
@keyframes moveBackground {
  0% {
    transform: translate(0, 0) rotate(0deg);
  }
  100% {
    transform: translate(-60px, -60px) rotate(5deg);
  }
}

@keyframes floatShapes {
  0%, 100% {
    transform: translate(0, 0);
  }
  50% {
    transform: translate(20px, 20px);
  }
}

@keyframes float {
  0%, 100% { 
    transform: translateY(0) rotate(0deg) scale(1); 
  }
  50% { 
    transform: translateY(-20px) rotate(180deg) scale(1.1); 
  }
}

/* Auth box styles */
.auth-box {
  background: rgba(251, 255, 228, 0.92);
  backdrop-filter: blur(12px);
  padding: 35px;
  border-radius: 20px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  box-shadow: 
    0 20px 40px rgba(61, 141, 122, 0.2),
    0 0 100px rgba(255, 255, 255, 0.1);
  width: 100%;
  max-width: 400px;
  text-align: center;
  position: relative;
  overflow: hidden;
  margin: auto;
  z-index: 1;
}

/* Logo section styles */
.logo-section {
  margin-bottom: 30px;
}

.user-icon {
  width: 80px;
  height: 80px;
  background: rgba(61, 141, 122, 0.1);
  border-radius: 50%;
  margin: 0 auto 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #3D8D7A;
  box-shadow: 0 8px 16px rgba(61, 141, 122, 0.1);
}

.user-icon svg {
  width: 32px;
  height: 32px;
}

h1 {
  color: #3D8D7A;
  font-size: 28px;
  font-weight: 700;
  margin-bottom: 8px;
  letter-spacing: -0.5px;
}

.subtitle {
  color: #3D8D7A;
  font-size: 16px;
  opacity: 0.85;
  font-weight: 500;
}

/* Button styles */
.buttons {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin: 30px auto;
  max-width: 340px;
}

.role-btn {
  width: 100%;
  background: linear-gradient(135deg, #3D8D7A, #A3D1C6);
  color: #FBFFE4;
  padding: 14px;
  font-size: 16px;
  font-weight: 600;
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
  text-decoration: none;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  backdrop-filter: blur(4px);
}

.student-btn {
  background: linear-gradient(135deg, #3D8D7A 0%, #B3D8A8 100%);
}

.teacher-btn {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
}

.role-btn:hover {
  transform: translateY(-2px);
  box-shadow: 
    0 10px 20px rgba(61, 141, 122, 0.2),
    0 0 30px rgba(255,255,255,0.1);
}

.btn-icon {
  width: 24px;
  height: 24px;
}

/* Login section styles */
.login-section {
  margin-top: 20px;
}

.login-link {
  color: #3D8D7A;
  font-size: 16px;
  text-decoration: none;
  font-weight: 500;
  transition: all 0.3s ease;
  padding-bottom: 2px;
  border-bottom: 2px solid transparent;
}

.login-link:hover {
  border-bottom-color: #3D8D7A;
}

/* Responsive styles */
@media (max-width: 768px) {
  .auth-box {
    padding: 25px 20px;
    margin: 15px;
    max-width: 340px;
  }

  .user-icon {
    width: 70px;
    height: 70px;
  }

  .user-icon svg {
    width: 28px;
    height: 28px;
  }

  h1 {
    font-size: 24px;
  }

  .subtitle {
    font-size: 14px;
  }

  .role-btn {
    font-size: 15px;
    padding: 12px;
  }

  .btn-icon {
    width: 20px;
    height: 20px;
  }

  .login-link {
    font-size: 14px;
  }
}
</style>
