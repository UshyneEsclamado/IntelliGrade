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

    <!-- Enhanced About section with complete content -->
  <section id="about" :class="['about-section', { active: activeSection === 'about' }]">
      <div class="about-container">
        <div class="about-header">
          <div class="section-badge">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12,1L3,5V11C3,16.55 6.84,21.74 12,23C17.16,21.74 21,16.55 21,11V5L12,1M10,17L6,13L7.41,11.59L10,14.17L16.59,7.58L18,9L10,17Z"/>
            </svg>
            <span>About IntelliGrade</span>
          </div>
          <h2>Empowering Academic Excellence</h2>
          <p class="about-intro">IntelliGrade is a modern academic management platform designed to streamline grading, enhance learning outcomes, and simplify communication between students and teachers.</p>
        </div>

        <!-- Mission & Vision Section -->
        <div class="mission-vision-container">
          <div class="mission-vision-card">
            <div class="mv-icon-wrapper">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12,2L1,21H23M12,6L19.53,19H4.47M11,10V14H13V10M11,16V18H13V16"/>
              </svg>
            </div>
            <h3>Our Mission</h3>
            <p>To empower academic excellence through intelligent technology and user-friendly tools that transform how education is managed and delivered.</p>
          </div>
          <div class="mission-vision-card">
            <div class="mv-icon-wrapper">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12,9A3,3 0 0,0 9,12A3,3 0 0,0 12,15A3,3 0 0,0 15,12A3,3 0 0,0 12,9M12,17A5,5 0 0,1 7,12A5,5 0 0,1 12,7A5,5 0 0,1 17,12A5,5 0 0,1 12,17M12,4.5C7,4.5 2.73,7.61 1,12C2.73,16.39 7,19.5 12,19.5C17,19.5 21.27,16.39 23,12C21.27,7.61 17,4.5 12,4.5Z"/>
              </svg>
            </div>
            <h3>Our Vision</h3>
            <p>To become the leading platform that modernizes education management worldwide, helping schools and educators focus on what matters most—student success.</p>
          </div>
        </div>

        <!-- Key Features Section -->
        <div class="features-header">
          <h3>Why Choose IntelliGrade?</h3>
          <p>Discover the powerful features designed to enhance your academic experience</p>
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
                <path d="M20,2H4A2,2 0 0,0 2,4V16A2,2 0 0,0 4,18H18L22,22V4A2,2 0 0,0 20,2M6,9H18V11H6M4,6H20V8H4M6,12H16V14H6"/>
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

        <!-- Who Is It For Section -->
        <div class="audience-section">
          <h3>Built For Everyone in Education</h3>
          <div class="audience-grid">
            <div class="audience-card">
              <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12,3L1,9L12,15L21,10.09V17H23V9M5,13.18V17.18L12,21L19,17.18V13.18L12,17L5,13.18Z"/>
              </svg>
              <h4>Students</h4>
              <p>Track progress, submit work, and communicate with teachers seamlessly</p>
            </div>
            <div class="audience-card">
              <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,4A8,8 0 0,1 20,12A8,8 0 0,1 12,20A8,8 0 0,1 4,12A8,8 0 0,1 12,4M12.5,7V12.25L17,14.92L16.25,16.15L11,13V7H12.5Z"/>
              </svg>
              <h4>Teachers</h4>
              <p>Automate grading, analyze performance, and manage classes efficiently</p>
            </div>
            <div class="audience-card">
              <svg width="32" height="32" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12,5.5A3.5,3.5 0 0,1 15.5,9A3.5,3.5 0 0,1 12,12.5A3.5,3.5 0 0,1 8.5,9A3.5,3.5 0 0,1 12,5.5M5,8C5.56,8 6.08,8.15 6.53,8.42C6.38,9.85 6.8,11.27 7.66,12.38C7.16,13.34 6.16,14 5,14A3,3 0 0,1 2,11A3,3 0 0,1 5,8M19,8A3,3 0 0,1 22,11A3,3 0 0,1 19,14C17.84,14 16.84,13.34 16.34,12.38C17.2,11.27 17.62,9.85 17.47,8.42C17.92,8.15 18.44,8 19,8M5.5,18.25C5.5,16.18 8.41,14.5 12,14.5C15.59,14.5 18.5,16.18 18.5,18.25V20H5.5V18.25M0,20V18.5C0,17.11 1.89,15.94 4.45,15.6C3.86,16.28 3.5,17.22 3.5,18.25V20H0M24,20H20.5V18.25C20.5,17.22 20.14,16.28 19.55,15.6C22.11,15.94 24,17.11 24,18.5V20Z"/>
              </svg>
              <h4>Schools</h4>
              <p>Streamline operations, ensure security, and drive institutional excellence</p>
            </div>
          </div>
        </div>

        <!-- Commitment Statement -->
        <div class="commitment-section">
          <div class="commitment-content">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12,1L8,5H11V14H13V5H16M18,23H6C4.89,23 4,22.1 4,21V9A2,2 0 0,1 6,7H9V9H6V21H18V9H15V7H18A2,2 0 0,1 20,9V21A2,2 0 0,1 18,23Z"/>
            </svg>
            <h3>Our Commitment</h3>
            <p>At IntelliGrade, we are committed to innovation, security, and exceptional user experience. We continuously enhance our platform to meet the evolving needs of modern education, ensuring that every feature we build puts student success and educator efficiency at the forefront.</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

// Define component name to fix Vue linting rule
defineOptions({
  name: 'LandingPage'
})

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
        (entry.target as HTMLElement).style.opacity = '1';
        (entry.target as HTMLElement).style.transform = 'translateY(0) scale(1)'
      }
    })
  }, observerOptions)

  setTimeout(() => {
    const featureCards = document.querySelectorAll('.feature-card')
    featureCards.forEach(card => {
      const cardElement = card as HTMLElement;
      cardElement.style.opacity = '0';
      cardElement.style.transform = 'translateY(30px) scale(0.95)';
      cardElement.style.transition = 'all 0.8s ease';
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
.landing-wrapper {
  min-height: 100vh;
  width: 100vw;
  background: linear-gradient(135deg, #39645a 0%, #B3D8A8 50%, #39645a 100%);
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  overflow-x: hidden;
  position: relative;
}

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
  flex-shrink: 0;
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
  white-space: nowrap;
}

.navbar-links {
  display: flex;
  align-items: center;
  gap: 2.2rem;
  animation: fadeInRight 1.2s ease-out;
}

.navbar-links a {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  font-size: 1.05rem;
  font-weight: 600;
  color: #355c4c;
  padding: 0.65rem 1.8rem;
  border-radius: 10px;
  background: #f8faf9;
  border: 1.5px solid #e0ede5;
  box-shadow: 0 2px 6px rgba(53, 92, 76, 0.08);
  outline: none;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  white-space: nowrap;
  cursor: pointer;
  transition: all 0.25s ease;
  text-decoration: none;
}

.navbar-links a:hover,
.navbar-links a.active {
  background: #ffffff;
  border-color: #20c997;
  color: #2d4a39;
  box-shadow: 0 3px 12px rgba(32, 201, 151, 0.12);
  transform: translateY(-1px);
}

.link-underline {
  position: absolute;
  bottom: -1px;
  left: 50%;
  transform: translateX(-50%);
  width: 0;
  height: 2px;
  background: #20c997;
  transition: width 0.3s ease;
}

.navbar-links a:hover .link-underline,
.navbar-links a.active .link-underline {
  width: 80%;
}

.sign-in-btn {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: linear-gradient(135deg, #355c4c 0%, #218c5a 100%) !important;
  color: white !important;
  font-weight: 700;
  font-size: 1.05rem;
  border-radius: 10px;
  padding: 0.65rem 1.8rem;
  text-decoration: none;
  box-shadow: 0 4px 16px rgba(53, 92, 76, 0.2);
  transition: all 0.25s ease;
  border: none !important;
  position: relative;
  overflow: hidden;
  white-space: nowrap;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-left: 0.5rem;
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
  background: linear-gradient(135deg, #218c5a 0%, #20c997 100%) !important;
  box-shadow: 0 6px 20px rgba(32, 201, 151, 0.25);
  transform: translateY(-1px);
}

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

.about-section {
  background: linear-gradient(135deg, #39645a 0%, #B3D8A8 50%, #39645a 100%);
  min-height: 100vh;
  padding: 12rem 2rem 3rem; /* Increased top padding for desktop */
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  box-sizing: border-box;
  overflow: visible;
}

.about-section.active {
  overflow-y: auto;
  max-height: 100vh;
  scrollbar-width: thin;
  scrollbar-color: #20c997 #e0ede5;
}

.about-section.active::-webkit-scrollbar {
  width: 8px;
}
.about-section.active::-webkit-scrollbar-thumb {
  background: #20c997;
  border-radius: 8px;
}
.about-section.active::-webkit-scrollbar-track {
  background: #e0ede5;
  border-radius: 8px;
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
  margin-bottom: 2rem;
}

.section-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(255, 255, 255, 0.25);
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 25px;
  padding: 0.5rem 1.2rem;
  color: #2d4a39;
  font-size: 0.85rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  backdrop-filter: blur(15px);
  animation: fadeInUp 1s ease-out;
  text-shadow: 0 1px 3px rgba(179, 216, 168, 0.3);
}

.about-section h2 {
  font-size: 3.2rem;
  color: #2d4a39;
  font-weight: 900;
  margin-bottom: 1.5rem;
  letter-spacing: -1px;
  animation: fadeInUp 1s ease-out 0.2s both;
  text-shadow: 0 3px 12px rgba(179, 216, 168, 0.3);
  line-height: 1.2;
}

.about-intro {
  font-size: 1.1rem;
  max-width: 700px;
  margin: 1rem auto 0;
  line-height: 1.6;
  color: #2d4a39;
  text-shadow: 0 1px 3px rgba(179, 216, 168, 0.3);
}

.mission-vision-container {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
  margin-bottom: 2.5rem;
  max-width: 1000px;
  margin-left: auto;
  margin-right: auto;
}

.mission-vision-card {
  background: rgba(255, 255, 255, 0.95);
  border: 2px solid rgba(179, 216, 168, 0.3);
  border-radius: 16px;
  padding: 2rem 1.5rem;
  text-align: center;
  transition: all 0.3s ease;
  backdrop-filter: blur(10px);
}

.mission-vision-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 35px rgba(57, 100, 90, 0.15);
  border-color: rgba(74, 155, 142, 0.4);
}

.mv-icon-wrapper {
  width: 64px;
  height: 64px;
  margin: 0 auto 1.5rem;
  background: linear-gradient(135deg, #4A9B8E 0%, #B3D8A8 100%);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  box-shadow: 0 6px 20px rgba(74, 155, 142, 0.3);
}

.mission-vision-card h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #2d4a39;
  margin-bottom: 1rem;
}

.mission-vision-card p {
  font-size: 1.05rem;
  color: #355c4c;
  line-height: 1.7;
  margin: 0;
}

.features-header {
  text-align: center;
  margin-top: 2.5rem;
  margin-bottom: 2.5rem;
}

.features-header h3 {
  font-size: 2rem;
  font-weight: 700;
  color: #2d4a39;
  margin-bottom: 0.8rem;
  text-shadow: 0 2px 8px rgba(179, 216, 168, 0.3);
}

.features-header p {
  font-size: 1.1rem;
  color: #355c4c;
  margin: 0;
  text-shadow: 0 1px 4px rgba(179, 216, 168, 0.2);
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 2rem;
  max-width: 1000px;
  margin: 1.5rem auto 4rem; /* Add top margin to push cards lower */
}

.feature-card {
  background: rgba(255, 255, 255, 0.95);
  border: 2px solid rgba(179, 216, 168, 0.3);
  border-radius: 16px;
  padding: 2.5rem 2rem;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
  backdrop-filter: blur(10px);
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.feature-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #4A9B8E, #B3D8A8);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.card-shine {
  display: none;
}

.feature-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 40px rgba(57, 100, 90, 0.15);
  border-color: rgba(74, 155, 142, 0.4);
}

.feature-card:hover::before {
  opacity: 1;
}

.feature-icon {
  width: 56px;
  height: 56px;
  border-radius: 12px;
  background: linear-gradient(135deg, #4A9B8E 0%, #B3D8A8 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.5rem;
  transition: all 0.3s ease;
  color: white;
  position: relative;
  overflow: visible;
  flex-shrink: 0;
  box-shadow: 0 4px 12px rgba(74, 155, 142, 0.25);
}

.icon-glow {
  display: none;
}

.feature-card:hover .feature-icon {
  transform: scale(1.08);
  box-shadow: 0 6px 18px rgba(74, 155, 142, 0.35);
}

.feature-content {
  flex: 1;
}

.feature-content h3 {
  color: #2d4a39;
  font-size: 1.35rem;
  font-weight: 700;
  margin-bottom: 0.8rem;
  position: relative;
  z-index: 2;
  line-height: 1.3;
}

.feature-content p {
  color: #355c4c;
  font-size: 1rem;
  line-height: 1.7;
  margin: 0;
  position: relative;
  z-index: 2;
  font-weight: 400;
  opacity: 0.9;
}

.audience-section {
  margin-top: 4rem;
  margin-bottom: 4rem;
}

.audience-section h3 {
  text-align: center;
  font-size: 2rem;
  font-weight: 700;
  color: #2d4a39;
  margin-bottom: 2.5rem;
  text-shadow: 0 2px 8px rgba(179, 216, 168, 0.3);
}

.audience-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
  max-width: 1000px;
  margin: 0 auto;
}

.audience-card {
  background: rgba(255, 255, 255, 0.95);
  border: 2px solid rgba(179, 216, 168, 0.3);
  border-radius: 16px;
  padding: 2.5rem 1.5rem;
  text-align: center;
  transition: all 0.3s ease;
  backdrop-filter: blur(10px);
}

.audience-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 35px rgba(57, 100, 90, 0.15);
  border-color: rgba(74, 155, 142, 0.4);
}

.audience-card svg {
  color: #4A9B8E;
  margin-bottom: 1.2rem;
}

.audience-card h4 {
  font-size: 1.3rem;
  font-weight: 700;
  color: #2d4a39;
  margin-bottom: 0.8rem;
}

.audience-card p {
  font-size: 1rem;
  color: #355c4c;
  line-height: 1.6;
  margin: 0;
}

.commitment-section {
  max-width: 800px;
  margin: 4rem auto 0;
}

.commitment-content {
  background: rgba(255, 255, 255, 0.95);
  border: 2px solid rgba(179, 216, 168, 0.3);
  border-radius: 16px;
  padding: 3rem 2.5rem;
  text-align: center;
  position: relative;
  backdrop-filter: blur(10px);
}

.commitment-content svg {
  color: #4A9B8E;
  margin-bottom: 1.5rem;
}

.commitment-content h3 {
  font-size: 1.8rem;
  font-weight: 700;
  color: #2d4a39;
  margin-bottom: 1rem;
}

.commitment-content p {
  font-size: 1.1rem;
  color: #355c4c;
  line-height: 1.8;
  margin: 0;
}

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
    opacity: 0.18;
  }
  25% {
    transform: scale(1.05) rotate(2deg);
    opacity: 0.22;
  }
  50% {
    transform: scale(0.95) rotate(-1deg);
    opacity: 0.16;
  }
  75% {
    transform: scale(1.02) rotate(1deg);
    opacity: 0.20;
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

@media (max-width: 768px) {
  .navbar {
    padding: 1rem 4vw;
    flex-wrap: wrap;
    justify-content: center;
    gap: 1rem;
  }
  
  .navbar-left {
    gap: 0.8rem;
    flex: 0 0 auto;
  }
  
  .navbar-logo {
    width: 48px;
    height: 48px;
  }
  
  .logo-image {
    width: 38px;
    height: 38px;
  }
  
  .navbar-title {
    font-size: 1.5rem;
  }
  
  .navbar-links {
    gap: 0.9rem;
    flex-wrap: wrap;
    justify-content: center;
    width: 100%;
    flex: 1 1 100%;
  }
  
  .navbar-links a {
    font-size: 0.98rem;
    padding: 0.6rem 1.5rem;
    flex: 0 1 auto;
  }
  
  .sign-in-btn {
    font-size: 0.98rem !important;
    padding: 0.6rem 1.6rem !important;
  }
  
  .hero-section {
    min-height: 100vh;
    padding: 0 1.5rem;
  }
  
  .hero-title {
    font-size: 3.5rem;
    letter-spacing: -1.5px;
  }
  
  .hero-desc {
    font-size: 1.15rem;
    padding: 0 1rem;
  }
  
  .hero-badge {
    font-size: 0.85rem;
    padding: 0.55rem 1.3rem;
  }
  
  .about-section {
    padding: 23rem 1.5rem 2.5rem; /* Increased top padding for mobile/tablet */
    min-height: auto;
  }
  
  .about-section h2 {
    font-size: 2.5rem;
  }
  
  .about-intro {
    font-size: 1.05rem;
  }
  
  .section-badge {
    font-size: 0.8rem;
    padding: 0.45rem 1.1rem;
  }
  
  .mission-vision-container {
    grid-template-columns: 1fr;
    gap: 1.2rem;
    margin-bottom: 2rem;
  }
  
  .mission-vision-card {
    padding: 1.8rem 1.3rem;
  }
  
  .mv-icon-wrapper {
    width: 56px;
    height: 56px;
    margin-bottom: 1.2rem;
  }
  
  .mission-vision-card h3 {
    font-size: 1.3rem;
  }
  
  .mission-vision-card p {
    font-size: 1rem;
  }
  
  .features-header {
    margin-bottom: 2rem;
  }
  
  .features-header h3 {
    font-size: 1.8rem;
  }
  
  .features-header p {
    font-size: 1.05rem;
  }
  
  .features-grid {
    grid-template-columns: 1fr;
    gap: 1.2rem;
    margin-bottom: 2rem;
    max-width: 500px;
  }
  
  .feature-card {
    padding: 1.8rem 1.3rem;
  }
  
  .feature-icon {
    width: 52px;
    height: 52px;
  }
  
  .feature-content h3 {
    font-size: 1.25rem;
  }
  
  .feature-content p {
    font-size: 0.98rem;
  }
  
  .audience-section {
    margin-top: 2rem;
    margin-bottom: 2rem;
  }
  
  .audience-section h3 {
    font-size: 1.8rem;
    margin-bottom: 1.5rem;
  }
  
  .audience-grid {
    grid-template-columns: 1fr;
    gap: 1.2rem;
    max-width: 500px;
    margin: 0 auto;
  }
  
  .audience-card {
    padding: 1.8rem 1.3rem;
  }
  
  .audience-card h4 {
    font-size: 1.2rem;
  }
  
  .audience-card p {
    font-size: 0.98rem;
  }
  
  .commitment-section {
    margin-top: 2rem;
  }
  
  .commitment-content {
    padding: 2rem 1.5rem;
  }
  
  .commitment-content h3 {
    font-size: 1.6rem;
  }
  
  .commitment-content p {
    font-size: 1.05rem;
  }
  
  .bg-logo-image {
    width: 650px;
    height: 650px;
    opacity: 0.15;
  }
  
  .scroll-indicator {
    bottom: 2.5rem;
  }
  
  .shape-1,
  .shape-2,
  .shape-3,
  .shape-4,
  .shape-5,
  .shape-6 {
    opacity: 0.06;
  }
  
  .floating-element {
    opacity: 0.1;
  }
}

@media (max-width: 480px) {
  .navbar {
    padding: 0.9rem 3vw;
    gap: 0.8rem;
  }
  
  .navbar-left {
    gap: 0.7rem;
  }
  
  .navbar-logo {
    width: 42px;
    height: 42px;
  }
  
  .logo-image {
    width: 34px;
    height: 34px;
  }
  
  .navbar-title {
    font-size: 1.3rem;
  }
  
  .navbar-links {
    gap: 0.7rem;
  }
  
  .navbar-links a {
    font-size: 0.9rem;
    padding: 0.55rem 1.2rem;
  }
  
  .sign-in-btn {
    font-size: 0.9rem !important;
    padding: 0.55rem 1.4rem !important;
  }
  
  .hero-section {
    min-height: 100vh;
    padding: 0 1.2rem;
  }
  
  .hero-title {
    font-size: 2.8rem;
    letter-spacing: -1px;
  }
  
  .hero-desc {
    font-size: 1.05rem;
    padding: 0 0.8rem;
  }
  
  .hero-badge {
    font-size: 0.8rem;
    padding: 0.5rem 1.1rem;
  }
  
  .about-section {
    padding: 22rem 1.2rem 2rem; /* Increased top padding for small screens */
    min-height: auto;
  }
  
  .about-section h2 {
    font-size: 2.2rem;
  }
  
  .about-intro {
    font-size: 1rem;
  }
  
  .section-badge {
    font-size: 0.75rem;
    padding: 0.4rem 1rem;
  }
  
  .mission-vision-container {
    gap: 1rem;
    margin-bottom: 1.5rem;
  }
  
  .mission-vision-card {
    padding: 1.6rem 1.2rem;
  }
  
  .mv-icon-wrapper {
    width: 52px;
    height: 52px;
  }
  
  .mission-vision-card h3 {
    font-size: 1.2rem;
  }
  
  .mission-vision-card p {
    font-size: 0.95rem;
  }
  
  .features-header {
    margin-bottom: 1.5rem;
  }
  
  .features-header h3 {
    font-size: 1.6rem;
  }
  
  .features-header p {
    font-size: 1rem;
  }
  
  .features-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
    margin-bottom: 1.5rem;
    max-width: 100%;
  }
  
  .feature-card {
    padding: 1.6rem 1.2rem;
  }
  
  .feature-icon {
    width: 50px;
    height: 50px;
    margin-bottom: 1.2rem;
  }
  
  .feature-content h3 {
    font-size: 1.15rem;
  }
  
  .feature-content p {
    font-size: 0.95rem;
  }
  
  .audience-section {
    margin-top: 1.5rem;
    margin-bottom: 1.5rem;
  }
  
  .audience-section h3 {
    font-size: 1.6rem;
    margin-bottom: 1.2rem;
  }
  
  .audience-grid {
    gap: 1rem;
    max-width: 100%;
  }
  
  .audience-card {
    padding: 1.6rem 1.2rem;
  }
  
  .audience-card svg {
    width: 28px;
    height: 28px;
  }
  
  .audience-card h4 {
    font-size: 1.15rem;
  }
  
  .audience-card p {
    font-size: 0.95rem;
  }
  
  .commitment-section {
    margin-top: 1.5rem;
  }
  
  .commitment-content {
    padding: 1.8rem 1.3rem;
  }
  
  .commitment-content svg {
    width: 36px;
    height: 36px;
  }
  
  .commitment-content h3 {
    font-size: 1.45rem;
  }
  
  .commitment-content p {
    font-size: 1rem;
  }
  
  .bg-logo-image {
    width: 500px;
    height: 500px;
    opacity: 0.12;
    filter: blur(0.8px);
  }
  
  .scroll-indicator {
    bottom: 2rem;
  }
  
  .scroll-arrow {
    width: 22px;
    height: 22px;
  }
  
  .shape-1,
  .shape-2,
  .shape-3,
  .shape-4,
  .shape-5,
  .shape-6 {
    opacity: 0.05;
  }
  
  .floating-element {
    opacity: 0.08;
  }
}

@media (max-width: 360px) {
  .navbar {
    padding: 0.8rem 2.5vw;
  }
  
  .navbar-logo {
    width: 38px;
    height: 38px;
  }
  
  .logo-image {
    width: 30px;
    height: 30px;
  }
  
  .navbar-title {
    font-size: 1.15rem;
  }
  
  .navbar-links a {
    font-size: 0.85rem;
    padding: 0.5rem 1rem;
  }
  
  .sign-in-btn {
    font-size: 0.85rem !important;
    padding: 0.5rem 1.2rem !important;
  }
  
  .hero-section {
    min-height: 100vh;
    padding: 0 1rem;
  }
  
  .hero-title {
    font-size: 2.4rem;
  }
  
  .hero-desc {
    font-size: 0.98rem;
  }
  
  .hero-badge {
    font-size: 0.75rem;
    padding: 0.45rem 1rem;
  }
  
  .about-section {
    padding: 21rem 1rem 1.5rem; /* Increased top padding for very small screens */
  }
  
  .about-section h2 {
    font-size: 2rem;
  }
  
  .about-intro {
    font-size: 0.95rem;
  }
  
  .section-badge {
    font-size: 0.7rem;
    padding: 0.35rem 0.9rem;
  }
  
  .mission-vision-card {
    padding: 1.5rem 1rem;
  }
  
  .mv-icon-wrapper {
    width: 48px;
    height: 48px;
  }
  
  .mission-vision-card h3 {
    font-size: 1.1rem;
  }
  
  .mission-vision-card p {
    font-size: 0.9rem;
  }
  
  .features-header h3 {
    font-size: 1.5rem;
  }
  
  .features-header p {
    font-size: 0.95rem;
  }
  
  .audience-section h3 {
    font-size: 1.5rem;
  }
  
  .commitment-content {
    padding: 1.6rem 1.2rem;
  }
  
  .commitment-content h3 {
    font-size: 1.35rem;
  }
  
  .commitment-content p {
    font-size: 0.95rem;
  }
  
  .feature-card {
    padding: 1.5rem 1rem;
  }
  
  .feature-icon {
    width: 48px;
    height: 48px;
  }
  
  .feature-content h3 {
    font-size: 1.1rem;
  }
  
  .feature-content p {
    font-size: 0.92rem;
  }
  
  .bg-logo-image {
    width: 380px;
    height: 380px;
    opacity: 0.1;
  }
  
  .shape-1,
  .shape-2,
  .shape-3,
  .shape-4,
  .shape-5,
  .shape-6 {
    opacity: 0.04;
  }
  
  .floating-element {
    opacity: 0.06;
  }
}
</style>