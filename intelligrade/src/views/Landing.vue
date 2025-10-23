.navbar-links {
  display: flex;
  flex-direction: row;
  gap: 2.2rem;
  align-items: center;
}
.navbar-links a,
.sign-in-btn {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  font-size: 1.08rem;
  font-weight: 600;
  color: #355c4c;
  padding: 0.7rem 2.1rem;
  border-radius: 12px;
  background: #f6faf7;
  border: 1.5px solid #dbeee2;
  box-shadow: 0 2px 8px rgba(53,92,76,0.07);
  outline: none;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  white-space: nowrap;
  cursor: pointer;
  transition: box-shadow 0.2s, background 0.2s, color 0.2s, border 0.2s, transform 0.2s;
}
  .sign-in-btn {
    font-size: 1rem;
    padding: 0.6rem 1.2rem;
    border-radius: 10px;
  }
}
@media (max-width: 480px) {
  .navbar-links {
    gap: 0.7rem;
  }
  .navbar-links a,
  .sign-in-btn {
    font-size: 0.95rem;
    padding: 0.5rem 0.8rem;
    border-radius: 9px;
  }
}
<template>
  <div class="landing-wrapper">
    <!-- Enhanced animated background elements -->
    <div class="background-shapes">
      <div class="shape shape-1"></div>
      <div class="shape shape-2"></div>
      <div class="shape shape-3"></div>
      <div class="shape shape-4"></div>
      <div class="shape shape-5"></div>
      <div class="shape shape-6"></div>
    </div>

    <!-- Background logo with blur effect -->
    <div class="background-logo">
      <img 
        src="@/assets/New IntelliGrade Logo Way BG.png"
        alt="Background Logo" 
        class="bg-logo-image"
      />
    </div>

    <!-- Enhanced floating educational elements -->
    <div class="floating-elements">
      <div class="floating-element element-1">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="rgba(74, 155, 142, 0.3)">
          <path d="M19 3H5C3.9 3 3 3.9 3 5V19C3 20.1 3.9 21 5 21H19C20.1 21 21 20.1 21 19V5C21 3.9 20.1 3 19 3M19 19H5V5H19V19M17 17H7V15H17V17M17 13H7V11H17V13M17 9H7V7H17V9Z"/>
        </svg>
        <div class="element-glow"></div>
      </div>
      <div class="floating-element element-2">
        <svg width="32" height="32" viewBox="0 0 24 24" fill="rgba(74, 155, 142, 0.3)">
          <path d="M12 3L1 9L12 15L21 10.09V17H23V9L12 3M5 13.18V17.18L12 21L19 17.18V13.18L12 17L5 13.18Z"/>
        </svg>
        <div class="element-glow"></div>
      </div>
      <div class="floating-element element-3">
        <svg width="26" height="26" viewBox="0 0 24 24" fill="rgba(74, 155, 142, 0.3)">
          <path d="M12,17.27L18.18,21L16.54,13.97L22,9.24L14.81,8.62L12,2L9.19,8.62L2,9.24L7.45,13.97L5.82,21L12,17.27Z"/>
        </svg>
        <div class="element-glow"></div>
      </div>
      <div class="floating-element element-4">
        <svg width="30" height="30" viewBox="0 0 24 24" fill="rgba(74, 155, 142, 0.3)">
          <path d="M9.5,3A6.5,6.5 0 0,1 16,9.5C16,11.11 15.41,12.59 14.44,13.73L14.71,14H15.5L20.5,19L19,20.5L14,15.5V14.71L13.73,14.44C12.59,15.41 11.11,16 9.5,16A6.5,6.5 0 0,1 3,9.5A6.5,6.5 0 0,1 9.5,3M9.5,5C7,5 5,7 5,9.5C5,12 7,14 9.5,14C12,14 14,12 14,9.5C14,7 12,5 9.5,5Z"/>
        </svg>
        <div class="element-glow"></div>
      </div>
      <div class="floating-element element-5">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="rgba(74, 155, 142, 0.3)">
          <path d="M19,19H5V8H19M16,1V3H8V1H6V3H5C3.89,3 3,3.89 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5C21,3.89 20.1,3 19,3H18V1M17,12H12V17H17V12Z"/>
        </svg>
        <div class="element-glow"></div>
      </div>
      <div class="floating-element element-6">
        <svg width="34" height="34" viewBox="0 0 24 24" fill="rgba(74, 155, 142, 0.3)">
          <path d="M20,2H4A2,2 0 0,0 2,4V16A2,2 0 0,0 4,18H18L22,22V4A2,2 0 0,0 20,2M6,9H18V11H6M4,6H20V8H4M6,12H16V14H6"/>
        </svg>
        <div class="element-glow"></div>
      </div>
    </div>

    <!-- Enhanced navbar with better glassmorphism -->
    <nav class="navbar">
      <div class="navbar-left">
        <div class="navbar-logo">
          <img 
            src="@/assets/New IntelliGrade Logo Way BG 3.png"
            alt="IntelliGrade Logo" 
            class="logo-image"
          />
          <div class="logo-shine"></div>
        </div>
        <span class="navbar-title">IntelliGrade</span>
      </div>
      <div class="navbar-links">
        <a href="#home" :class="{ active: activeSection === 'home' }" @click="scrollToSection('home')">
          <span>Home</span>
          <div class="link-underline"></div>
        </a>
        <a href="#about" :class="{ active: activeSection === 'about' }" @click="scrollToSection('about')">
          <span>About Us</span>
          <div class="link-underline"></div>
        </a>
        <router-link to="/login" class="sign-in-btn">
          <span>Sign In</span>
          <div class="btn-shine"></div>
        </router-link>
      </div>
    </nav>

    <!-- Enhanced hero section -->
    <section id="home" class="hero-section">
      <div class="hero-content">
        <div class="hero-badge">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12,17.27L18.18,21L16.54,13.97L22,9.24L14.81,8.62L12,2L9.19,8.62L2,9.24L7.45,13.97L5.82,21L12,17.27Z"/>
          </svg>
          <span>Modern Academic Management</span>
        </div>
        <h1 class="hero-title">IntelliGrade</h1>
        <p class="hero-desc">A modern, intelligent grading and academic management platform for students and teachers.</p>
      </div>

      <div class="scroll-indicator" @click="scrollToSection('about')">
        <div class="scroll-arrow"></div>
      </div>
    </section>

    <!-- Compact about section -->
    <section id="about" class="about-section">
      <div class="about-container">
        <div class="about-header">
          <div class="section-badge">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12,1L3,5V11C3,16.55 6.84,21.74 12,23C17.16,21.74 21,16.55 21,11V5L12,1M10,17L6,13L7.41,11.59L10,14.17L16.59,7.58L18,9L10,17Z"/>
            </svg>
            <span>Why Choose Us</span>
          </div>
          <h2>Empowering Academic Excellence</h2>
          <p>Experience the future of education management with our intuitive platform designed to enhance learning outcomes and streamline academic processes.</p>
        </div>

        <div class="features-grid">
          <div v-for="(feature, index) in features" :key="index" 
               class="feature-card" 
               :style="{ animationDelay: `${index * 0.1}s` }">
            <div class="feature-icon">
              <svg v-if="index === 0" width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M19 3H14.82C14.4 1.84 13.3 1 12 1S9.6 1.84 9.18 3H5C3.9 3 3 3.9 3 5V19C3 20.1 3.9 21 5 21H19C20.1 21 21 20.1 21 19V5C21 3.9 20.1 3 19 3M12 3C12.55 3 13 3.45 13 4S12.55 5 12 5 11 4.55 11 4 11.45 3 12 3M7 7H17V9H7V7M7 11H17V13H7V11M7 15H13V17H7V15Z"/>
              </svg>
              <svg v-else-if="index === 1" width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M16,6L18.29,8.29L13.41,13.17L9.41,9.17L2,16.59L3.41,18L9.41,12L13.41,16L19.71,9.71L22,12V6H16Z"/>
              </svg>
              <svg v-else-if="index === 2" width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12,2A2,2 0 0,1 14,4A2,2 0 0,1 12,6A2,2 0 0,1 10,4A2,2 0 0,1 12,2M21,9V7L15,1H5C3.89,1 3,1.89 3,3V7H9V9H3V19A2,2 0 0,0 5,21H10V23H12V21H17A2,2 0 0,0 19,19V9H21M5,19V7H7V19H5M10,19H9V7H10V19M17,19H12V7H17V19Z"/>
              </svg>
              <svg v-else width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12,1L3,5V11C3,16.55 6.84,21.74 12,23C17.16,21.74 21,16.55 21,11V5L12,1M10,17L6,13L7.41,11.59L10,14.17L16.59,7.58L18,9L10,17Z"/>
              </svg>
              <div class="icon-glow"></div>
            </div>
            <div class="feature-content">
              <h3>{{ feature.title }}</h3>
              <p>{{ feature.description }}</p>
            </div>
            <div class="card-shine"></div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const activeSection = ref('home')
const features = ref([
  {
    title: 'Smart Grading',
    description: 'Automated grading and feedback'
  },
  {
    title: 'Progress Analytics', 
    description: 'Real-time progress tracking'
  },
  {
    title: 'Seamless Communication',
    description: 'Easy communication between students and teachers'
  },
  {
    title: 'Secure Platform',
    description: 'Secure and user-friendly interface'
  }
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
        entry.target.style.transform = 'translateY(0) scale(1)'
      }
    })
  }, observerOptions)

  setTimeout(() => {
    const featureCards = document.querySelectorAll('.feature-card')
    featureCards.forEach(card => {
      card.style.opacity = '0'
      card.style.transform = 'translateY(30px) scale(0.95)'
      card.style.transition = 'all 0.8s ease'
      observer.observe(card)
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
/* Formal Navbar Button Styles */
.navbar-links {
  display: flex;
  align-items: center;
  gap: 2.2rem;
}
.navbar-links a {
  color: #218c5a;
  font-weight: 600;
  font-size: 1.08rem;
  padding: 0.5rem 1.2rem;
  border-radius: 8px;
  background: none;
  border: none;
  box-shadow: none;
  transition: color 0.3s, box-shadow 0.3s;
  position: relative;
  cursor: pointer;
}
.navbar-links a.active {
  color: #355c4c;
  background: #f5faf7;
  box-shadow: 0 2px 0 #20c997;
}
.navbar-links a:not(.active):hover {
  color: #20c997;
}
.sign-in-btn {
  background: linear-gradient(135deg, #355c4c 0%, #218c5a 100%);
  color: #fff;
  font-weight: 700;
  font-size: 1.08rem;
  border-radius: 12px;
  padding: 0.7rem 2.1rem;
  margin-left: 2.2rem;
  box-shadow: 0 6px 25px rgba(0, 0, 0, 0.13);
  border: none;
  cursor: pointer;
  transition: background 0.3s, box-shadow 0.3s;
}
.sign-in-btn:hover {
  background: linear-gradient(135deg, #218c5a 0%, #20c997 100%);
  box-shadow: 0 8px 30px rgba(32, 201, 151, 0.18);
}
@media (max-width: 600px) {
  .navbar-links {
    gap: 1.2rem;
  }
  .navbar-links a {
    font-size: 0.98rem;
    padding: 0.45rem 0.9rem;
  }
  .sign-in-btn {
    font-size: 0.98rem;
    padding: 0.55rem 1.2rem;
    margin-left: 1.2rem;
  }
}
.landing-wrapper {
  min-height: 100vh;
  width: 100vw;
  background: linear-gradient(135deg, #39645a 0%, #B3D8A8 50%, #39645a 100%);
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  overflow-x: hidden;
  position: relative;
}

/* Enhanced animated background shapes */
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

/* Background logo with blur effect */
.background-logo {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.bg-logo-image {
  width: 800px;
  height: 800px;
  object-fit: contain;
  opacity: 0.18;
  filter: blur(0.5px);
  animation: logoFloat 20s ease-in-out infinite;
  transform-origin: center;
}

.shape {
  position: absolute;
  opacity: 0.08;
  animation: floatShape 25s ease-in-out infinite;
  border-radius: 30% 70% 70% 30% / 30% 30% 70% 70%;
  filter: blur(1px);
}

.shape-1 {
  top: 10%;
  left: 8%;
  width: 120px;
  height: 120px;
  background: linear-gradient(45deg, #4A9B8E, #B3D8A8, #ffffff);
  animation-delay: 0s;
}

.shape-2 {
  top: 15%;
  right: 15%;
  width: 180px;
  height: 180px;
  background: linear-gradient(135deg, #B3D8A8, #4A9B8E, #ffffff);
  animation-delay: 5s;
}

.shape-3 {
  top: 50%;
  left: 5%;
  width: 140px;
  height: 140px;
  background: linear-gradient(225deg, #4A9B8E, #ffffff, #B3D8A8);
  animation-delay: 10s;
}

.shape-4 {
  bottom: 25%;
  right: 8%;
  width: 100px;
  height: 100px;
  background: linear-gradient(315deg, #B3D8A8, #ffffff, #4A9B8E);
  animation-delay: 15s;
}

.shape-5 {
  top: 35%;
  left: 60%;
  width: 90px;
  height: 90px;
  background: linear-gradient(45deg, #ffffff, #4A9B8E);
  animation-delay: 20s;
}

.shape-6 {
  bottom: 40%;
  left: 25%;
  width: 110px;
  height: 110px;
  background: linear-gradient(180deg, #4A9B8E, #B3D8A8);
  animation-delay: 12s;
}

/* Enhanced floating educational elements */
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
  animation: educationalFloat 15s ease-in-out infinite;
  opacity: 0.12;
  transition: all 0.6s ease;
  cursor: pointer;
}

.floating-element:hover {
  opacity: 0.3;
  transform: scale(1.15) !important;
}

.element-glow {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 60px;
  height: 60px;
  background: radial-gradient(circle, rgba(74, 155, 142, 0.1) 0%, transparent 70%);
  transform: translate(-50%, -50%);
  border-radius: 50%;
  animation: pulse 3s ease-in-out infinite;
}

.element-1 { top: 18%; left: 12%; animation-delay: 0s; }
.element-2 { top: 28%; right: 18%; animation-delay: 2.5s; }
.element-3 { top: 65%; left: 8%; animation-delay: 5s; }
.element-4 { top: 48%; right: 12%; animation-delay: 7.5s; }
.element-5 { bottom: 28%; left: 15%; animation-delay: 10s; }
.element-6 { bottom: 38%; right: 20%; animation-delay: 12.5s; }

/* Enhanced navbar */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.2rem 6vw;
  background: rgba(255, 255, 255, 0.95);
  box-shadow: 0 8px 40px rgba(179, 216, 168, 0.15);
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  backdrop-filter: blur(25px);
  animation: slideDown 1s ease-out;
}

.navbar-left {
  display: flex;
  align-items: center;
  gap: 1.2rem;
  animation: fadeInLeft 1.2s ease-out;
}

.navbar-logo {
  width: 52px;
  height: 52px;
  border-radius: 16px;
  background: linear-gradient(135deg, rgba(57, 100, 90, 0.1) 0%, rgba(179, 216, 168, 0.1) 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.4s ease;
  overflow: hidden;
  position: relative;
}

.navbar-logo:hover {
  transform: scale(1.08) rotate(8deg);
  box-shadow: 0 12px 35px rgba(179, 216, 168, 0.3);
}

.logo-image {
  width: 42px;
  height: 42px;
  object-fit: contain;
  transition: all 0.4s ease;
  position: relative;
  z-index: 2;
}

.logo-shine {
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
  transition: left 0.6s ease;
}

.navbar-logo:hover .logo-shine {
  left: 100%;
}

.navbar-title {
  font-size: 1.7rem;
  font-weight: 900;
  color: #39645a;
  letter-spacing: -0.8px;
  animation: fadeInTitle 1.4s ease-out;
  text-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
}

.navbar-links {
  display: flex;
  align-items: center;
  gap: 2.5rem;
  animation: fadeInRight 1.2s ease-out;
}

  .navbar-links {
    flex-direction: row !important;
    gap: 0.7rem;
    width: auto;
    justify-content: flex-start;
    flex-wrap: nowrap;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  transition: all 0.4s ease;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}

.link-underline {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background: linear-gradient(90deg, #B3D8A8, #4A9B8E);
  transition: width 0.4s ease;
}

.navbar-links a:hover .link-underline,
.navbar-links a.active .link-underline {
  width: 100%;
}

.navbar-links a.active,
.navbar-links a:hover {
  color: #2d4a39;
  background: rgba(179, 216, 168, 0.1);
  transform: translateY(-2px);
}

.sign-in-btn {
  background: linear-gradient(135deg, #39645a 0%, #2d4a39 100%) !important;
  color: white !important;
  font-weight: 700;
  border-radius: 12px;
  padding: 0.8rem 2rem;
  text-decoration: none;
  margin-left: 1.5rem;
  box-shadow: 0 6px 25px rgba(0, 0, 0, 0.15);
  transition: all 0.4s ease;
  border: none !important;
  position: relative;
  overflow: hidden;
}

.btn-shine {
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
  transition: left 0.8s ease;
}

.sign-in-btn:hover .btn-shine {
  left: 100%;
}

.sign-in-btn:hover {
  background: linear-gradient(135deg, #2d4a39 0%, #1a2f24 100%) !important;
  box-shadow: 0 12px 45px rgba(0, 0, 0, 0.25);
  transform: translateY(-3px) scale(1.03);
}

/* Enhanced hero section */
.hero-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  width: 100%;
  padding: 0 2rem;
  text-align: center;
  position: relative;
  box-sizing: border-box;
}

.hero-content {
  max-width: 800px;
  z-index: 10;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(255, 255, 255, 0.25);
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 25px;
  padding: 0.6rem 1.5rem;
  color: rgba(255, 255, 255, 0.95);
  font-size: 0.9rem;
  font-weight: 700;
  margin-bottom: 2rem;
  backdrop-filter: blur(15px);
  animation: fadeInUp 1s ease-out 0.2s both;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
  text-align: center;
}

.hero-title {
  font-size: 4.5rem;
  font-weight: 900;
  background: linear-gradient(135deg, #ffffff 0%, rgba(255, 255, 255, 0.95) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 1.5rem;
  letter-spacing: -2px;
  animation: fadeInUp 1s ease-out 0.4s both, titleGlow 4s ease-in-out infinite;
  text-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
  line-height: 1.1;
  filter: drop-shadow(0 2px 8px rgba(0, 0, 0, 0.3));
  text-align: center;
}

.hero-desc {
  font-size: 1.25rem;
  color: rgba(255, 255, 255, 0.95);
  max-width: 600px;
  margin: 0 auto;
  line-height: 1.7;
  animation: fadeInUp 1s ease-out 0.6s both;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.4);
  font-weight: 500;
  text-align: center;
}

.cta-button {
  background: white;
  color: #39645a;
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
  bottom: 3rem;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.8rem;
  animation: bounce 2s infinite, fadeInUp 1.5s ease-out;
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

/* Compact about section */
.about-section {
  background: linear-gradient(135deg, #39645a 0%, #B3D8A8 50%, #39645a 100%);
  min-height: 100vh;
  padding: 6rem 2rem 4rem;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
}

.about-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.5), transparent);
  animation: gradientShift 4s ease-in-out infinite;
}

.about-container {
  max-width: 1200px;
  width: 100%;
}

.about-header {
  text-align: center;
  margin-bottom: 4rem;
}

.section-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(255, 255, 255, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 25px;
  padding: 0.5rem 1.2rem;
  color: rgba(255, 255, 255, 0.95);
  font-size: 0.85rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  backdrop-filter: blur(15px);
  animation: fadeInUp 1s ease-out;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
}

.about-section h2 {
  font-size: 3.2rem;
  color: white;
  font-weight: 900;
  margin-bottom: 1.5rem;
  letter-spacing: -1px;
  animation: fadeInUp 1s ease-out 0.2s both;
  text-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
  line-height: 1.2;
  filter: drop-shadow(0 2px 8px rgba(0, 0, 0, 0.3));
}

.about-section p {
  color: rgba(255, 255, 255, 0.95);
  font-size: 1.15rem;
  margin-bottom: 2rem;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
  line-height: 1.7;
  animation: fadeInUp 1s ease-out 0.4s both;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
  font-weight: 500;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  max-width: 900px;
  margin: 0 auto;
}

.feature-card {
  background: rgba(255, 255, 255, 0.12);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 20px;
  padding: 1.2rem 1rem;
  transition: all 0.5s ease;
  position: relative;
  overflow: hidden;
  backdrop-filter: blur(15px);
  cursor: pointer;
}

.feature-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.03) 0%, rgba(255, 255, 255, 0.08) 100%);
  opacity: 0;
  transition: opacity 0.4s ease;
}

.card-shine {
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.08), transparent);
  transform: rotate(45deg);
  transition: all 0.8s ease;
  opacity: 0;
}

.feature-card:hover {
  transform: translateY(-12px) scale(1.03);
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.25);
  border-color: rgba(255, 255, 255, 0.25);
  background: rgba(255, 255, 255, 0.18);
}

.feature-card:hover::before {
  opacity: 1;
}

.feature-card:hover .card-shine {
  left: 100%;
  opacity: 1;
}

.feature-icon {
  width: 60px;
  height: 60px;
  border-radius: 16px;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.15) 0%, rgba(255, 255, 255, 0.25) 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.5rem;
  transition: all 0.4s ease;
  backdrop-filter: blur(10px);
  color: white;
  position: relative;
  overflow: hidden;
}

.icon-glow {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 80px;
  height: 80px;
  background: radial-gradient(circle, rgba(255, 255, 255, 0.1) 0%, transparent 70%);
  transform: translate(-50%, -50%);
  border-radius: 50%;
  animation: pulse 2s ease-in-out infinite;
  opacity: 0;
  transition: opacity 0.4s ease;
}

.feature-card:hover .feature-icon {
  transform: rotate(12deg) scale(1.1);
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.2) 0%, rgba(255, 255, 255, 0.35) 100%);
}

.feature-card:hover .icon-glow {
  opacity: 1;
}

.feature-content h3 {
  color: #39645a;
  font-size: 1.1rem;
  font-weight: 800;
  margin-bottom: 0.5rem;
  position: relative;
  z-index: 2;
  text-shadow: 0 2px 10px rgba(255,255,255,0.7), 0 2px 6px rgba(0,0,0,0.25);
}

.feature-content p {
  color: #2d4a39;
  font-size: 0.92rem;
  line-height: 1.5;
  margin: 0;
  position: relative;
  z-index: 2;
  text-shadow: 0 1px 8px rgba(255,255,255,0.7), 0 1px 4px rgba(0,0,0,0.2);
  font-weight: 500;
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
    transform: translateX(-40px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes fadeInRight {
  from {
    opacity: 0;
    transform: translateX(40px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes fadeInTitle {
  from {
    opacity: 0;
    transform: translateY(30px) scale(0.9);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

@keyframes titleGlow {
  0%, 100% {
    filter: drop-shadow(0 4px 20px rgba(0, 0, 0, 0.3));
  }
  50% {
    filter: drop-shadow(0 4px 35px rgba(0, 0, 0, 0.5));
  }
}

@keyframes logoFloat {
  0%, 100% {
    transform: scale(1) rotate(0deg);
    opacity: 0.08;
  }
  25% {
    transform: scale(1.05) rotate(2deg);
    opacity: 0.12;
  }
  50% {
    transform: scale(0.95) rotate(-1deg);
    opacity: 0.06;
  }
  75% {
    transform: scale(1.02) rotate(1deg);
    opacity: 0.10;
  }
}

@keyframes floatShape {
  0%, 100% {
    transform: translateY(0px) translateX(0px) rotate(0deg) scale(1);
    border-radius: 30% 70% 70% 30% / 30% 30% 70% 70%;
  }
  25% {
    transform: translateY(-25px) translateX(15px) rotate(90deg) scale(1.1);
    border-radius: 70% 30% 30% 70% / 70% 70% 30% 30%;
  }
  50% {
    transform: translateY(-15px) translateX(-20px) rotate(180deg) scale(0.9);
    border-radius: 50% 50% 50% 50% / 50% 50% 50% 50%;
  }
  75% {
    transform: translateY(-35px) translateX(8px) rotate(270deg) scale(1.05);
    border-radius: 30% 70% 30% 70% / 30% 70% 30% 70%;
  }
}

@keyframes educationalFloat {
  0%, 100% { 
    transform: translateY(0px) translateX(0px) rotate(0deg); 
    opacity: 0.12;
  }
  25% { 
    transform: translateY(-20px) translateX(15px) rotate(90deg); 
    opacity: 0.18;
  }
  50% { 
    transform: translateY(-12px) translateX(-18px) rotate(180deg); 
    opacity: 0.22;
  }
  75% { 
    transform: translateY(-28px) translateX(10px) rotate(270deg); 
    opacity: 0.16;
  }
}

@keyframes pulse {
  0%, 100% {
    transform: translate(-50%, -50%) scale(1);
    opacity: 0.5;
  }
  50% {
    transform: translate(-50%, -50%) scale(1.2);
    opacity: 0.8;
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
  40% { transform: translateX(-50%) translateY(-15px); }
  60% { transform: translateX(-50%) translateY(-8px); }
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(40px);
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
  }
  
  .navbar-links {
    gap: 1.5rem;
  }
  
  .hero-title {
    font-size: 3rem;
    letter-spacing: -1px;
  }
  
  .hero-desc {
    font-size: 1.1rem;
  }
  
  .hero-actions {
    flex-direction: column;
    gap: 1rem;
  }
  
  .about-section {
    padding: 5rem 1rem 3rem;
  }
  
  .about-section h2 {
    font-size: 2.5rem;
  }
  
  .features-grid {
    width: 60px;
    height: 60px;
    border-radius: 16px;
    background: linear-gradient(135deg, #B3D8A8 0%, #4A9B8E 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 1.5rem;
    transition: all 0.4s ease;
    backdrop-filter: blur(6px);
    color: #39645a;
    position: relative;
    overflow: hidden;

  .bg-logo-image {
    width: 600px;
    height: 600px;
    opacity: 0.06;
  }
}

@media (max-width: 480px) {
  .navbar {
    flex-direction: column;
    gap: 1rem;
    padding: 1rem;
  }
  
  .navbar-links {
    flex-direction: column;
    gap: 0.8rem;
  }
  
  .sign-in-btn {
    margin-left: 0;
    margin-top: 0.5rem;
  }
  
  .hero-title {
    font-size: 2.5rem;
  }

  .hero-badge {
    font-size: 0.8rem;
    padding: 0.5rem 1rem;
  }

  .logo-image {
    width: 38px;
    height: 38px;
  }

  .navbar-logo {
    width: 48px;
    height: 48px;
  }

  .navbar-title {
    font-size: 1.5rem;
  }

  .about-section h2 {
    font-size: 2.2rem;
  }

  .feature-icon {
    width: 50px;
    height: 50px;
  }

  .bg-logo-image {
    width: 400px;
    height: 400px;
    opacity: 0.04;
    filter: blur(1px);
  }
}
}
</style>