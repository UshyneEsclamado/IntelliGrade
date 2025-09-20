<template>
  <div class="auth-wrapper">
    <div class="geometric-shapes"></div>
    <div class="floating-elements">
      <!-- Educational floating elements with proper animations -->
      <!-- LEFT SIDE - Around Center -->
      <!-- Document symbols -->
      <div class="floating-element element-1">
        <svg width="35" height="35" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M19 3H5C3.9 3 3 3.9 3 5V19C3 20.1 3.9 21 5 21H19C20.1 21 21 20.1 21 19V5C21 3.9 20.1 3 19 3M19 19H5V5H19V19M17 17H7V15H17V17M17 13H7V11H17V13M17 9H7V7H17V9Z"/>
        </svg>
      </div>
      
      <!-- Education/School symbols -->
      <div class="floating-element element-2">
        <svg width="33" height="33" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M12 3L1 9L12 15L21 10.09V17H23V9L12 3M5 13.18V17.18L12 21L19 17.18V13.18L12 17L5 13.18Z"/>
        </svg>
      </div>
      
      <!-- Search symbols -->
      <div class="floating-element element-3">
        <svg width="30" height="30" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M9.5,3A6.5,6.5 0 0,1 16,9.5C16,11.11 15.41,12.59 14.44,13.73L14.71,14H15.5L20.5,19L19,20.5L14,15.5V14.71L13.73,14.44C12.59,15.41 11.11,16 9.5,16A6.5,6.5 0 0,1 3,9.5A6.5,6.5 0 0,1 9.5,3M9.5,5C7,5 5,7 5,9.5C5,12 7,14 9.5,14C12,14 14,12 14,9.5C14,7 12,5 9.5,5Z"/>
        </svg>
      </div>
      
      <!-- Star symbols -->
      <div class="floating-element element-4">
        <svg width="38" height="38" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M12,17.27L18.18,21L16.54,13.97L22,9.24L14.81,8.62L12,2L9.19,8.62L2,9.24L7.45,13.97L5.82,21L12,17.27Z"/>
        </svg>
      </div>
      
      <!-- Calendar symbols -->
      <div class="floating-element element-5">
        <svg width="33" height="33" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M19,19H5V8H19M16,1V3H8V1H6V3H5C3.89,3 3,3.89 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5C21,3.89 20.1,3 19,3H18V1M17,12H12V17H17V12Z"/>
        </svg>
      </div>
      
      <!-- Chat/Message symbols -->
      <div class="floating-element element-6">
        <svg width="36" height="36" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M20,2H4A2,2 0 0,0 2,4V16A2,2 0 0,0 4,18H18L22,22V4A2,2 0 0,0 20,2M6,9H18V11H6M4,6H20V8H4M6,12H16V14H6"/>
        </svg>
      </div>

      <!-- RIGHT SIDE - Around Logo -->
      <!-- Document symbols (duplicate) -->
      <div class="floating-element element-13">
        <svg width="32" height="32" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M19 3H5C3.9 3 3 3.9 3 5V19C3 20.1 3.9 21 5 21H19C20.1 21 21 20.1 21 19V5C21 3.9 20.1 3 19 3M19 19H5V5H19V19M17 17H7V15H17V17M17 13H7V11H17V13M17 9H7V7H17V9Z"/>
        </svg>
      </div>
      
      <!-- Education/School symbols (duplicate) -->
      <div class="floating-element element-14">
        <svg width="29" height="29" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M12 3L1 9L12 15L21 10.09V17H23V9L12 3M5 13.18V17.18L12 21L19 17.18V13.18L12 17L5 13.18Z"/>
        </svg>
      </div>
      
      <!-- Search symbols (duplicate) -->
      <div class="floating-element element-15">
        <svg width="34" height="34" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M9.5,3A6.5,6.5 0 0,1 16,9.5C16,11.11 15.41,12.59 14.44,13.73L14.71,14H15.5L20.5,19L19,20.5L14,15.5V14.71L13.73,14.44C12.59,15.41 11.11,16 9.5,16A6.5,6.5 0 0,1 3,9.5A6.5,6.5 0 0,1 9.5,3M9.5,5C7,5 5,7 5,9.5C5,12 7,14 9.5,14C12,14 14,12 14,9.5C14,7 12,5 9.5,5Z"/>
        </svg>
      </div>
      
      <!-- Star symbols (duplicate) -->
      <div class="floating-element element-16">
        <svg width="31" height="31" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M12,17.27L18.18,21L16.54,13.97L22,9.24L14.81,8.62L12,2L9.19,8.62L2,9.24L7.45,13.97L5.82,21L12,17.27Z"/>
        </svg>
      </div>
      
      <!-- Calculator symbols -->
      <div class="floating-element element-8">
        <svg width="34" height="34" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M9,11H7V9H9V11M13,11H11V9H13V11M17,11H15V9H17V11M19,3H18V1H16V1H6V3H5C3.89,3 3,3.9 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5C21,3.9 20.1,3 19,3M19,19H5V8H19V19M9,15H7V13H9V15M13,15H11V13H13V15M17,15H15V13H17V15M9,17H7V19H9V17M13,19H11V17H13V19M17,19H15V17H17V19Z"/>
        </svg>
      </div>
      
      <!-- User symbols -->
      <div class="floating-element element-9">
        <svg width="29" height="29" viewBox="0 0 24 24" fill="#4A9B8E">
          <path d="M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M7.07,18.28C7.5,17.38 10.12,16.5 12,16.5C13.88,16.5 16.5,17.38 16.93,18.28C15.57,19.36 13.86,20 12,20C10.14,20 8.43,19.36 7.07,18.28M18.36,16.83C16.93,15.09 13.46,14.5 12,14.5C10.54,14.5 7.07,15.09 5.64,16.83C4.62,15.5 4,13.82 4,12C4,7.59 7.59,4 12,4C16.41,4 20,7.59 20,12C20,13.82 19.38,15.5 18.36,16.83M12,6C10.06,6 8.5,7.56 8.5,9.5C8.5,11.44 10.06,13 12,13C13.94,13 15.5,11.44 15.5,9.5C15.5,7.56 13.94,6 12,6M12,11A1.5,1.5 0 0,1 10.5,9.5A1.5,1.5 0 0,1 12,8A1.5,1.5 0 0,1 13.5,9.5A1.5,1.5 0 0,1 12,11Z"/>
        </svg>
      </div>
    </div>
    
    <div class="auth-container">
      <!-- Centered Role Selection Box -->
      <div class="auth-box">
        <div class="logo-section">
          <img src="../assets/New IntelliGrade Logo.png" alt="IntelliGrade Logo" class="logo" />
          <h1>Select Your Role</h1>
          <p class="subtitle">Choose how you want to join IntelliGrade</p>
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
  </div>
</template>

<script>
export default {
  name: "RoleSelection"
};
</script>

<style scoped>
/* Existing base styles */
* { margin: 0; padding: 0; box-sizing: border-box; }

/* Auth wrapper styles */
.auth-wrapper {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  width: 100vw;
  height: 100vh;
  background: transparent !important;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1rem;
  font-family: 'Inter', sans-serif;
  overflow: hidden;
}

/* Geometric background styles */
.geometric-shapes {
  position: fixed;
  inset: 0;
  z-index: 0;
  overflow: hidden;
  background: linear-gradient(135deg, #A3D1C6 0%, #B3D8A8 50%, #FBFFE4 100%);
}

.geometric-shapes::before {
  content: '';
  position: absolute;
  width: 100%;
  height: 100%;
  background: 
    linear-gradient(45deg, transparent 48%, rgba(255,255,255,0.08) 50%, transparent 52%) 0 0 / 60px 60px,
    linear-gradient(-45deg, transparent 48%, rgba(255,255,255,0.08) 50%, transparent 52%) 0 0 / 60px 60px,
    radial-gradient(circle at 20% 30%, rgba(255,255,255,0.12) 0, transparent 40px),
    radial-gradient(circle at 80% 20%, rgba(255,255,255,0.12) 0, transparent 60px),
    radial-gradient(circle at 10% 80%, rgba(255,255,255,0.12) 0, transparent 50px),
    radial-gradient(circle at 90% 70%, rgba(255,255,255,0.12) 0, transparent 70px);
  animation: moveBackground 30s linear infinite;
}

.geometric-shapes::after {
  content: '';
  position: absolute;
  inset: 0;
  background:
    radial-gradient(circle at 15% 25%, rgba(255,255,255,0.15) 0, transparent 200px),
    radial-gradient(circle at 85% 75%, rgba(255,255,255,0.15) 0, transparent 200px),
    radial-gradient(circle at 50% 50%, rgba(255,255,255,0.08) 0, transparent 300px);
  animation: floatShapes 20s ease-in-out infinite;
}

/* Floating elements styles */
.floating-elements {
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 0;
  overflow: hidden;
}

/* Educational floating elements with proper animations */
.floating-element {
  position: absolute;
  animation: educationalFloat 15s ease-in-out infinite;
  opacity: 0.6;
  filter: drop-shadow(0 4px 12px rgba(74, 155, 142, 0.25));
  z-index: 1;
  transition: all 0.4s ease;
}

.floating-element:hover {
  opacity: 1;
  transform: scale(1.3) !important;
  filter: drop-shadow(0 6px 20px rgba(74, 155, 142, 0.4));
}

/* Element positioning */
.element-1 { top: 10%; left: 8%; animation-delay: 0s; }
.element-2 { top: 35%; left: 3%; animation-delay: 2s; }
.element-3 { bottom: 45%; left: 6%; animation-delay: 4s; }
.element-4 { top: 20%; left: 15%; animation-delay: 6s; }
.element-5 { bottom: 20%; left: 10%; animation-delay: 8s; }
.element-6 { top: 60%; left: 2%; animation-delay: 10s; }

.element-8 { bottom: 8%; left: 18%; animation-delay: 12s; }
.element-9 { top: 48%; left: 12%; animation-delay: 14s; }
.element-13 { top: 15%; right: 10%; animation-delay: 1s; }
.element-14 { top: 30%; right: 5%; animation-delay: 3s; }
.element-15 { top: 8%; right: 20%; animation-delay: 5s; }
.element-16 { top: 50%; right: 15%; animation-delay: 7s; }

/* Update animations */
@keyframes moveBackground {
  0% {
    transform: translate(0, 0) rotate(0deg);
  }
  100% {
    transform: translate(-60px, -60px) rotate(2deg);
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

@keyframes educationalFloat {
  0%, 100% { 
    transform: translateY(0) translateX(0) rotate(0deg); 
    opacity: 0.6; 
  }
  25% { 
    transform: translateY(-12px) translateX(6px) rotate(3deg); 
    opacity: 0.8; 
  }
  50% { 
    transform: translateY(-20px) translateX(-3px) rotate(-2deg); 
    opacity: 0.7; 
  }
  75% { 
    transform: translateY(-8px) translateX(9px) rotate(4deg); 
    opacity: 0.9; 
  }
}

@keyframes gentleFloat {
  0%, 100% {
    transform: translateY(0px) scale(1);
  }
  50% {
    transform: translateY(-20px) scale(1.02);
  }
}

@keyframes slideInFade {
  0% {
    opacity: 0;
    transform: translateY(30px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes logoGlow {
  0% { transform: scale(1) rotate(0deg); }
  100% { transform: scale(1.1) rotate(2deg); }
}

.auth-container {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 90vh;
  z-index: 10;
  position: relative;
}

/* Auth box styles */
.auth-box {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  padding: 1.5rem;
  border-radius: 18px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  box-shadow: 
    0 25px 50px rgba(61, 141, 122, 0.1),
    0 10px 30px rgba(0, 0, 0, 0.05),
    inset 0 1px 0 rgba(255, 255, 255, 0.9);
  width: 100%;
  max-width: 380px;
  text-align: center;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: fit-content;
  z-index: 1;
  transition: all 0.4s ease;
}

.auth-box:hover {
  transform: translateY(-2px);
  box-shadow: 
    0 35px 70px rgba(61, 141, 122, 0.15),
    0 20px 50px rgba(0, 0, 0, 0.08),
    inset 0 2px 0 rgba(255, 255, 255, 0.95),
    inset 0 -1px 0 rgba(61, 141, 122, 0.15);
}

.logo-space {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  max-width: 450px;
  height: 100%;
}

.intelligrade-branding {
  text-align: center;
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
}

.intelligrade-branding:hover {
  transform: translateY(-5px);
}

.logo-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.logo-image-container {
  width: 300px;
  height: 300px;
  display: flex;
  align-items: center;
  justify-content: center;
  filter: drop-shadow(0 15px 40px rgba(74, 155, 142, 0.3));
  transition: all 0.4s ease;
  margin-bottom: 0.75rem;
}

.logo-image-container:hover {
  filter: drop-shadow(0 20px 50px rgba(74, 155, 142, 0.4));
  transform: scale(1.05);
}

.logo-image {
  width: 280px;
  height: 280px;
  object-fit: contain;
  animation: gentleFloat 8s ease-in-out infinite;
  background: transparent;
}

.brand-tagline {
  color: rgba(74, 155, 142, 0.8);
  font-size: 1rem;
  line-height: 1.5;
  font-weight: 500;
  letter-spacing: 0.3px;
  font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  text-shadow: 0 2px 8px rgba(74, 155, 142, 0.1);
  max-width: 350px;
  margin: 0 auto;
  animation: slideInFade 2s ease-out;
  text-align: center;
  position: relative;
  z-index: 15;
  background: rgba(255, 255, 255, 0.1);
  padding: 0.5rem 1rem;
  border-radius: 10px;
  backdrop-filter: blur(10px);
}

/* Logo section styles */
.logo-section {
  margin-bottom: 1rem;
}

.logo {
  width: 100px;
  height: auto;
  margin: 0 auto 0.75rem;
  display: block;
  filter: 
    drop-shadow(0 10px 30px rgba(61, 141, 122, 0.2))
    drop-shadow(0 4px 15px rgba(61, 141, 122, 0.1));
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  position: relative;
}

.logo:hover {
  transform: scale(1.08) rotateY(8deg) perspective(500px);
  filter: 
    drop-shadow(0 20px 50px rgba(61, 141, 122, 0.3))
    drop-shadow(0 8px 25px rgba(61, 141, 122, 0.2))
    drop-shadow(0 0 0 rgba(255, 255, 255, 0.8));
}

.logo::before {
  content: '';
  position: absolute;
  top: -10px;
  left: -10px;
  right: -10px;
  bottom: -10px;
  background: linear-gradient(45deg, rgba(163, 209, 198, 0.1), rgba(179, 216, 168, 0.1));
  border-radius: 50%;
  opacity: 0;
  transition: opacity 0.4s ease;
  z-index: -1;
}

.logo:hover::before {
  opacity: 1;
  animation: logoGlow 2s ease-in-out infinite alternate;
}

h1 {
  color: #3D8D7A;
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 0.3rem;
  letter-spacing: -0.5px;
  background: linear-gradient(135deg, #3D8D7A 0%, #4A9B8E 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  text-shadow: 0 4px 12px rgba(61, 141, 122, 0.2);
  position: relative;
}

h1::after {
  content: '';
  position: absolute;
  bottom: -8px;
  left: 50%;
  transform: translateX(-50%);
  width: 60px;
  height: 3px;
  background: linear-gradient(90deg, #3D8D7A, #A3D1C6);
  border-radius: 2px;
  opacity: 0.7;
}

.subtitle {
  color: #3D8D7A;
  font-size: 0.8rem;
  opacity: 0.8;
  font-weight: 500;
  line-height: 1.5;
  margin-bottom: 10px;
}

/* Button styles */
.buttons {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  margin: 1rem auto;
  max-width: 380px;
}

.role-btn {
  width: 100%;
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: white;
  padding: 0.75rem 1rem;
  font-size: 0.9rem;
  font-weight: 600;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  text-decoration: none;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  box-shadow: 
    0 8px 30px rgba(61, 141, 122, 0.25),
    0 2px 10px rgba(61, 141, 122, 0.1),
    inset 0 1px 0 rgba(255, 255, 255, 0.2);
  position: relative;
  overflow: hidden;
}

.role-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
  transition: left 0.6s ease;
}

.role-btn:hover::before {
  left: 100%;
}

.student-btn {
  background: linear-gradient(135deg, #3D8D7A 0%, #B3D8A8 100%);
  box-shadow: 
    0 8px 30px rgba(61, 141, 122, 0.25),
    0 2px 10px rgba(179, 216, 168, 0.15),
    inset 0 1px 0 rgba(255, 255, 255, 0.2);
}

.teacher-btn {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  box-shadow: 
    0 8px 30px rgba(61, 141, 122, 0.25),
    0 2px 10px rgba(163, 209, 198, 0.15),
    inset 0 1px 0 rgba(255, 255, 255, 0.2);
}

.role-btn:hover {
  transform: translateY(-4px) scale(1.02);
  box-shadow: 
    0 15px 40px rgba(61, 141, 122, 0.35),
    0 5px 15px rgba(61, 141, 122, 0.2),
    inset 0 1px 0 rgba(255, 255, 255, 0.3);
}

.role-btn:active {
  transform: translateY(-2px) scale(1.01);
  transition: all 0.2s ease;
}

.btn-icon {
  width: 18px;
  height: 18px;
  transition: transform 0.3s ease;
}

.role-btn:hover .btn-icon {
  transform: scale(1.1) rotate(5deg);
}

/* Login section styles */
.login-section {
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid rgba(61, 141, 122, 0.15);
}

.login-link {
  color: #3D8D7A;
  font-size: 0.8rem;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s ease;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  border: 2px solid transparent;
  background: rgba(61, 141, 122, 0.05);
  display: inline-block;
  position: relative;
  overflow: hidden;
  border-bottom: 2px solid transparent;
}

.login-link::before {
  display: none;
}

.login-link:hover::before {
  display: none;
}

.login-link:hover {
  color: #267c6e;
  background: rgba(61, 141, 122, 0.07);
  border-bottom-color: rgba(61, 141, 122, 0.5);
  text-decoration: none;
  box-shadow: none;
  transform: none;
}

/* Responsive Design */
@media (max-width: 1200px) {
  .auth-container {
    flex-direction: column;
    gap: 1.25rem;
    height: auto;
    max-height: 95vh;
  }
  
  .logo-space {
    order: -1;
    max-width: 100%;
  }
  
  .logo-image-container {
    width: 250px;
    height: 250px;
  }
  
  .logo-image {
    width: 230px;
    height: 230px;
  }
  
  .brand-tagline {
    font-size: 0.9rem;
  }

  .auth-box {
    max-width: 100%;
    max-height: none;
  }
}

/* Responsive styles */
@media (max-width: 768px) {
  .auth-wrapper {
    padding: 0.75rem;
    overflow-y: auto;
  }
  
  .auth-box {
    padding: 1.25rem;
    max-width: 350px;
    height: auto;
    max-height: none;
    margin: 15px;
  }

  .logo {
    width: 80px;
    margin-bottom: 0.5rem;
  }

  .floating-element {
    opacity: 0.4;
  }

  .floating-element svg {
    transform: scale(0.8);
  }

  h1 {
    font-size: 1.3rem;
  }

  .subtitle {
    font-size: 0.75rem;
  }

  .role-btn {
    font-size: 0.85rem;
    padding: 0.65rem;
  }

  .btn-icon {
    width: 16px;
    height: 16px;
  }

  .login-link {
    font-size: 0.75rem;
  }

  /* Hide some duplicate elements on mobile to reduce clutter */
  .element-13, .element-14, .element-15, .element-16 {
    display: none;
  }
}

@media (max-width: 480px) {
  .element-8, .element-9, .element-13, .element-14, .element-15, .element-16 {
    display: none;
  }

  .auth-box {
    padding: 1rem;
    max-width: 320px;
    margin: 10px;
  }

  .logo {
    width: 70px;
    margin-bottom: 0.5rem;
  }

  h1 {
    font-size: 1.2rem;
  }

  .subtitle {
    font-size: 0.7rem;
  }

  .role-btn {
    font-size: 0.8rem;
    padding: 0.6rem;
  }

  .btn-icon {
    width: 14px;
    height: 14px;
  }

  .login-link {
    font-size: 0.7rem;
  }
}
</style>