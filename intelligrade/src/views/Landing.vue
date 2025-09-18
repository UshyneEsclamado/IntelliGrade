<template>
  <div class="landing-wrapper">
    <!-- Animated background elements -->
    <div class="background-shapes">
      <div class="shape shape-1"></div>
      <div class="shape shape-2"></div>
      <div class="shape shape-3"></div>
      <div class="shape shape-4"></div>
    </div>

    <!-- Floating educational elements -->
    <div class="floating-elements">
      <div class="floating-element element-1">
        <svg width="25" height="25" viewBox="0 0 24 24" fill="rgba(74, 155, 142, 0.2)">
          <path d="M19 3H5C3.9 3 3 3.9 3 5V19C3 20.1 3.9 21 5 21H19C20.1 21 21 20.1 21 19V5C21 3.9 20.1 3 19 3M19 19H5V5H19V19M17 17H7V15H17V17M17 13H7V11H17V13M17 9H7V7H17V9Z"/>
        </svg>
      </div>
      <div class="floating-element element-2">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="rgba(74, 155, 142, 0.2)">
          <path d="M12 3L1 9L12 15L21 10.09V17H23V9L12 3M5 13.18V17.18L12 21L19 17.18V13.18L12 17L5 13.18Z"/>
        </svg>
      </div>
      <div class="floating-element element-3">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="rgba(74, 155, 142, 0.2)">
          <path d="M12,17.27L18.18,21L16.54,13.97L22,9.24L14.81,8.62L12,2L9.19,8.62L2,9.24L7.45,13.97L5.82,21L12,17.27Z"/>
        </svg>
      </div>
      <div class="floating-element element-4">
        <svg width="26" height="26" viewBox="0 0 24 24" fill="rgba(74, 155, 142, 0.2)">
          <path d="M9.5,3A6.5,6.5 0 0,1 16,9.5C16,11.11 15.41,12.59 14.44,13.73L14.71,14H15.5L20.5,19L19,20.5L14,15.5V14.71L13.73,14.44C12.59,15.41 11.11,16 9.5,16A6.5,6.5 0 0,1 3,9.5A6.5,6.5 0 0,1 9.5,3M9.5,5C7,5 5,7 5,9.5C5,12 7,14 9.5,14C12,14 14,12 14,9.5C14,7 12,5 9.5,5Z"/>
        </svg>
      </div>
      <div class="floating-element element-5">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="rgba(74, 155, 142, 0.2)">
          <path d="M19,19H5V8H19M16,1V3H8V1H6V3H5C3.89,3 3,3.89 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5C21,3.89 20.1,3 19,3H18V1M17,12H12V17H17V12Z"/>
        </svg>
      </div>
      <div class="floating-element element-6">
        <svg width="30" height="30" viewBox="0 0 24 24" fill="rgba(74, 155, 142, 0.2)">
          <path d="M20,2H4A2,2 0 0,0 2,4V16A2,2 0 0,0 4,18H18L22,22V4A2,2 0 0,0 20,2M6,9H18V11H6M4,6H20V8H4M6,12H16V14H6"/>
        </svg>
      </div>
    </div>

    <nav class="navbar">
      <div class="navbar-left">
        <div class="navbar-logo">
          <img 
            src="@/assets/New IntelliGrade Logo Way BG 3.png"
            alt="IntelliGrade Logo" 
            class="logo-image"
          />
        </div>
        <span class="navbar-title">IntelliGrade</span>
      </div>
      <div class="navbar-links">
        <a href="#home" :class="{ active: activeSection === 'home' }" @click="scrollToSection('home')">Home</a>
        <a href="#about" :class="{ active: activeSection === 'about' }" @click="scrollToSection('about')">About Us</a>
        <router-link to="/login" class="sign-in-btn">Sign In</router-link>
      </div>
    </nav>

    <section id="home" class="hero-section">
      <h1 class="hero-title">IntelliGrade</h1>
      <p class="hero-desc">A modern, intelligent grading and academic management platform for students and teachers.</p>
      <button @click="scrollToSection('about')" class="cta-button">Learn More</button>
      <div class="scroll-indicator" @click="scrollToSection('about')">
        <div class="scroll-arrow"></div>
      </div>
    </section>

    <section id="about" class="about-section">
      <h2>About Us</h2>
      <p>
        IntelliGrade is designed to simplify and enhance the academic experience for both students and educators. Our platform offers smart grading, analytics, and seamless communication tools to help you stay organized and succeed in your academic journey.
      </p>
      <ul class="about-list">
        <li v-for="(feature, index) in features" :key="index" class="about-item" :style="{ animationDelay: `${index * 0.1}s` }">
          <div class="feature-icon">
            <svg v-if="index === 0" width="20" height="20" viewBox="0 0 24 24" fill="white">
              <path d="M9,11H7V9H9V11M13,11H11V9H13V11M17,11H15V9H17V11M19,3H18V1H16V1H6V3H5C3.89,3 3,3.9 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5C21,3.9 20.1,3 19,3M19,19H5V8H19V19M9,15H7V13H9V15M13,15H11V13H13V15M17,15H15V13H17V15M9,17H7V19H9V17M13,19H11V17H13V19M17,19H15V17H17V19Z"/>
            </svg>
            <svg v-else-if="index === 1" width="20" height="20" viewBox="0 0 24 24" fill="white">
              <path d="M16,18H18V6H16M6.5,18H7.5V6H6.5M9.5,18H10.5V6H9.5M13,18H14V6H13M2,20H22V18H2M4,4V6H20V4H4Z"/>
            </svg>
            <svg v-else-if="index === 2" width="20" height="20" viewBox="0 0 24 24" fill="white">
              <path d="M20,2H4A2,2 0 0,0 2,4V16A2,2 0 0,0 4,18H18L22,22V4A2,2 0 0,0 20,2M6,9H18V11H6M4,6H20V8H4M6,12H16V14H6"/>
            </svg>
            <svg v-else width="20" height="20" viewBox="0 0 24 24" fill="white">
              <path d="M12,1L3,5V11C3,16.55 6.84,21.74 12,23C17.16,21.74 21,16.55 21,11V5L12,1M10,17L6,13L7.41,11.59L10,14.17L16.59,7.58L18,9L10,17Z"/>
            </svg>
          </div>
          <span>{{ feature }}</span>
        </li>
      </ul>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const activeSection = ref('home')
const features = ref([
  'Automated grading and feedback',
  'Real-time progress tracking',
  'Easy communication between students and teachers',
  'Secure and user-friendly interface'
])

function scrollToSection(sectionId) {
  const element = document.getElementById(sectionId)
  if (element) {
    element.scrollIntoView({ behavior: 'smooth', block: 'start' })
    activeSection.value = sectionId
  }
}

function handleScroll() {
  const aboutElement = document.getElementById('about')
  const homeElement = document.getElementById('home')
  if (aboutElement && window.scrollY + 200 >= aboutElement.offsetTop) {
    activeSection.value = 'about'
  } else if (homeElement && window.scrollY === 0) {
    activeSection.value = 'home'
  }
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
  
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  }

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1'
        entry.target.style.transform = 'translateY(0)'
      }
    })
  }, observerOptions)

  setTimeout(() => {
    const aboutItems = document.querySelectorAll('.about-item')
    aboutItems.forEach(item => {
      item.style.opacity = '0'
      item.style.transform = 'translateY(20px)'
      item.style.transition = 'all 0.6s ease'
      observer.observe(item)
    })
  }, 100)

  const homeElement = document.getElementById('home')
  if (homeElement) {
    homeElement.scrollIntoView({ behavior: 'smooth', block: 'start' })
  }
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
.landing-wrapper {
  min-height: 100vh;
  width: 100vw;
  background: linear-gradient(135deg, #39645a 0%, #B3D8A8 50%, #39645a 100%);
  font-family: 'Inter', sans-serif;
  overflow-x: hidden;
  position: relative;
}

/* Animated background shapes */
.background-shapes {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 0;
  overflow: hidden;
}

.shape {
  position: absolute;
  opacity: 0.1;
  animation: floatShape 20s ease-in-out infinite;
}

.shape-1 {
  top: 10%;
  left: 10%;
  width: 100px;
  height: 100px;
  background: linear-gradient(45deg, #4A9B8E, #B3D8A8);
  border-radius: 50%;
  animation-delay: 0s;
}

.shape-2 {
  top: 20%;
  right: 20%;
  width: 150px;
  height: 150px;
  background: linear-gradient(45deg, #B3D8A8, #4A9B8E);
  border-radius: 30%;
  animation-delay: 5s;
}

.shape-3 {
  bottom: 30%;
  left: 15%;
  width: 120px;
  height: 120px;
  background: linear-gradient(45deg, #4A9B8E, #ffffff);
  border-radius: 20%;
  animation-delay: 10s;
}

.shape-4 {
  bottom: 20%;
  right: 10%;
  width: 80px;
  height: 80px;
  background: linear-gradient(45deg, #B3D8A8, #ffffff);
  border-radius: 50%;
  animation-delay: 15s;
}

/* Floating educational elements */
.floating-elements {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 1;
}

.floating-element {
  position: absolute;
  animation: educationalFloat 12s ease-in-out infinite;
  opacity: 0.15;
  filter: drop-shadow(0 2px 6px rgba(74, 155, 142, 0.1));
  transition: all 0.4s ease;
}

.floating-element:hover {
  opacity: 0.25;
  transform: scale(1.1) !important;
}

.element-1 { top: 15%; left: 8%; animation-delay: 0s; }
.element-2 { top: 25%; right: 12%; animation-delay: 2s; }
.element-3 { top: 60%; left: 5%; animation-delay: 4s; }
.element-4 { top: 45%; right: 8%; animation-delay: 6s; }
.element-5 { bottom: 25%; left: 10%; animation-delay: 8s; }
.element-6 { bottom: 35%; right: 15%; animation-delay: 10s; }

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem 6vw;
  background: white; /* Changed from #B3D8A8 to white */
  box-shadow: 0 4px 24px 0 rgba(179, 216, 168, 0.3);
  border-bottom: 1.5px solid rgba(255, 255, 255, 0.3);
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  backdrop-filter: blur(20px);
  animation: slideDown 0.8s ease-out;
}

.navbar-left {
  display: flex;
  align-items: center;
  gap: 1rem;
  animation: fadeInLeft 1s ease-out;
}

.navbar-logo {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  background: transparent;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: none;
  transition: all 0.3s ease;
  overflow: hidden;
}

.navbar-logo:hover {
  transform: scale(1.05) rotate(5deg);
  box-shadow: 0 8px 25px rgba(179, 216, 168, 0.4);
}

.logo-image {
  width: 40px;
  height: 40px;
  object-fit: contain;
  transition: all 0.3s ease;
}

.navbar-title {
  font-size: 1.6rem;
  font-weight: 800;
  color: #39645a; /* Changed from white to dark green */
  letter-spacing: -0.5px;
  animation: fadeInTitle 1.2s ease-out;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.navbar-links {
  display: flex;
  align-items: center;
  gap: 2.2rem;
  animation: fadeInRight 1s ease-out;
}

.navbar-links a {
  color: #39645a; /* Changed from white to dark green */
  font-weight: 600;
  text-decoration: none;
  font-size: 1.1rem;
  padding: 0.25rem 0.5rem;
  border-bottom: 2px solid transparent;
  transition: all 0.3s ease;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  text-shadow: none;
}

.navbar-links a::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(57, 100, 90, 0.1), transparent);
  transition: left 0.5s ease;
}

.navbar-links a:hover::before {
  left: 100%;
}

.navbar-links a.active,
.navbar-links a:hover {
  border-bottom: 2px solid #B3D8A8;
  color: #2d4a39;
  transform: translateY(-2px);
}

.sign-in-btn {
  background: #39645a !important; /* Changed from white to dark green */
  color: white !important; /* Changed from #2d4a39 to white */
  font-weight: 700;
  border-radius: 10px;
  padding: 0.6rem 1.5rem;
  text-decoration: none;
  margin-left: 1.5rem;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
  transition: all 0.3s ease;
  border: none !important;
  position: relative;
  overflow: hidden;
  text-shadow: none;
}

.sign-in-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
  transition: left 0.6s ease;
}

.sign-in-btn:hover::before {
  left: 100%;
}

.sign-in-btn:hover {
  background: #2d4a39 !important;
  color: white !important;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
  transform: translateY(-2px) scale(1.02);
}

.hero-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  width: 100%;
  padding: 0 2rem;
  text-align: center;
  position: relative;
  box-sizing: border-box;
  margin: 0;
  left: 0;
  right: 0;
  scroll-snap-align: start;
}

.hero-title {
  font-size: 4rem;
  font-weight: 900;
  color: white;
  margin-bottom: 1rem;
  letter-spacing: -1px;
  animation: fadeInUp 1s ease-out 0.3s both, titleGlow 3s ease-in-out infinite;
  text-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

.hero-desc {
  font-size: 1.3rem;
  color: rgba(255, 255, 255, 0.9);
  max-width: 700px;
  margin: 0 auto 3rem;
  line-height: 1.6;
  animation: fadeInUp 1s ease-out 0.6s both, textFloat 6s ease-in-out infinite;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
}

.cta-button {
  background: white; /* Changed to white */
  color: #39645a; /* Changed to dark green */
  font-weight: 700;
  font-size: 1.1rem;
  border-radius: 12px;
  padding: 1rem 2rem;
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.2);
  transition: all 0.3s ease;
  border: none;
  cursor: pointer;
  animation: fadeInUp 1s ease-out 0.9s both, buttonPulse 2s ease-in-out infinite;
  position: relative;
  overflow: hidden;
}

.cta-button::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(57, 100, 90, 0.1), transparent);
  transition: left 0.6s ease;
}

.cta-button:hover::before {
  left: 100%;
}

.cta-button:hover {
  background: #f8f9fa;
  color: #2d4a39;
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.3);
  transform: translateY(-3px) scale(1.05);
}

.scroll-indicator {
  position: absolute;
  bottom: 2rem;
  left: 50%;
  transform: translateX(-50%);
  animation: bounce 2s infinite, scroll-pulse 2.5s infinite alternate, fadeInUp 1.5s ease-out;
  cursor: pointer;
}

.scroll-arrow {
  width: 24px;
  height: 24px;
  border: 3px solid white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  transition: all 0.3s ease;
}

.scroll-arrow:hover {
  transform: scale(1.1);
  background: rgba(255, 255, 255, 1);
}

.scroll-arrow::after {
  content: '↓';
  color: #39645a;
  font-size: 14px;
  font-weight: bold;
}

.about-section {
  background: linear-gradient(135deg, #39645a 0%, #B3D8A8 50%, #39645a 100%);
  min-height: 100vh;
  padding: 6rem 2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  position: relative;
}

.about-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #B3D8A8, #ffffff, #B3D8A8);
  animation: gradientShift 3s ease-in-out infinite;
}

.about-section h2 {
  font-size: 3rem;
  color: white;
  font-weight: 800;
  margin-bottom: 2rem;
  letter-spacing: -0.5px;
  animation: fadeInUp 1s ease-out, titleGlow 4s ease-in-out infinite;
  text-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
}

.about-section p {
  color: rgba(255, 255, 255, 0.9);
  font-size: 1.2rem;
  margin-bottom: 3rem;
  max-width: 800px;
  line-height: 1.8;
  animation: fadeInUp 1s ease-out 0.3s both;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.about-list {
  list-style: none;
  padding: 0;
  margin: 0 auto;
  max-width: 600px;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  width: 100%;
}

.about-item {
  color: white;
  font-size: 1.1rem;
  background: rgba(255, 255, 255, 0.15);
  border-radius: 16px;
  padding: 1.5rem;
  font-weight: 600;
  border-left: 4px solid rgba(255, 255, 255, 0.3);
  transition: all 0.4s ease;
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: center;
  gap: 1rem;
  backdrop-filter: blur(10px);
}

.about-item::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(255, 255, 255, 0.1) 100%);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.about-item::after {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.1), transparent);
  transform: rotate(45deg);
  transition: all 0.6s ease;
  opacity: 0;
}

.about-item:hover {
  transform: translateY(-8px) scale(1.02);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.2);
  border-left-color: rgba(255, 255, 255, 0.6);
  background: rgba(255, 255, 255, 0.2);
}

.about-item:hover::before {
  opacity: 1;
}

.about-item:hover::after {
  left: 100%;
  opacity: 1;
}

.feature-icon {
  width: 40px;
  height: 40px;
  border-radius: 10px;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.2) 0%, rgba(255, 255, 255, 0.3) 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  transition: all 0.3s ease;
  backdrop-filter: blur(10px);
}

.about-item:hover .feature-icon {
  transform: rotate(10deg) scale(1.1);
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.3) 0%, rgba(255, 255, 255, 0.4) 100%);
}

.about-item span {
  position: relative;
  z-index: 1;
  flex: 1;
}

/* Enhanced Animations */
@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-100%);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeInLeft {
  from {
    opacity: 0;
    transform: translateX(-30px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes fadeInRight {
  from {
    opacity: 0;
    transform: translateX(30px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes fadeInTitle {
  from {
    opacity: 0;
    transform: translateY(20px) scale(0.9);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

@keyframes titleGlow {
  0%, 100% {
    text-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
  }
  50% {
    text-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
  }
}

@keyframes textFloat {
  0%, 100% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(-5px);
  }
}

@keyframes buttonPulse {
  0%, 100% {
    box-shadow: 0 6px 24px rgba(0, 0, 0, 0.2);
  }
  50% {
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);
  }
}

@keyframes floatShape {
  0%, 100% {
    transform: translateY(0px) translateX(0px) rotate(0deg);
  }
  25% {
    transform: translateY(-20px) translateX(10px) rotate(90deg);
  }
  50% {
    transform: translateY(-10px) translateX(-15px) rotate(180deg);
  }
  75% {
    transform: translateY(-30px) translateX(5px) rotate(270deg);
  }
}

@keyframes educationalFloat {
  0%, 100% { 
    transform: translateY(0px) translateX(0px) rotate(0deg); 
    opacity: 0.15;
  }
  25% { 
    transform: translateY(-15px) translateX(10px) rotate(90deg); 
    opacity: 0.2;
  }
  50% { 
    transform: translateY(-8px) translateX(-12px) rotate(180deg); 
    opacity: 0.25;
  }
  75% { 
    transform: translateY(-20px) translateX(6px) rotate(270deg); 
    opacity: 0.2;
  }
}

@keyframes gradientShift {
  0%, 100% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
}

@keyframes bounce {
  0%, 20%, 50%, 80%, 100% { transform: translateX(-50%) translateY(0); }
  40% { transform: translateX(-50%) translateY(-10px); }
  60% { transform: translateX(-50%) translateY(-5px); }
}

@keyframes scroll-pulse {
  0% {
    filter: drop-shadow(0 0 0px #a7f3d0);
    opacity: 1;
  }
  50% {
    filter: drop-shadow(0 0 8px #a7f3d0);
    opacity: 0.8;
  }
  100% {
    filter: drop-shadow(0 0 0px #a7f3d0);
    opacity: 1;
  }
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Mobile Responsiveness */
@media (max-width: 768px) {
  .navbar {
    padding: 1rem;
    flex-direction: column;
    gap: 1rem;
  }
  
  .navbar-links {
    gap: 1.5rem;
  }
  
  .hero-section {
    padding: 8rem 1rem 4rem;
  }
  
  .hero-title {
    font-size: 2.8rem;
  }
  
  .hero-desc {
    font-size: 1.1rem;
  }
  
  .about-section {
    padding: 4rem 1rem;
  }
  
  .about-section h2 {
    font-size: 2.2rem;
  }
  
  .about-list {
    grid-template-columns: 1fr;
    max-width: 100%;
  }

  .about-item {
    flex-direction: column;
    text-align: center;
    gap: 0.8rem;
  }

  /* Hide some floating elements on mobile */
  .element-4, .element-5, .element-6 {
    display: none;
  }
}

@media (max-width: 480px) {
  .navbar-links {
    flex-direction: column;
    gap: 0.8rem;
  }
  
  .sign-in-btn {
    margin-left: 0;
    margin-top: 0.5rem;
  }
  
  .hero-title {
    font-size: 2.2rem;
  }

  .logo-image {
    width: 35px;
    height: 35px;
  }

  .navbar-logo {
    width: 40px;
    height: 40px;
  }

  .navbar-title {
    font-size: 1.4rem;
  }
}
</style>