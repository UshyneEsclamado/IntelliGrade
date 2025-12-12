<template>
  <div class="landing-wrapper">
    <!-- Educational Themed Animation Background -->
    <div class="educational-animation">
      <div class="floating-academic-elements">
        <div class="academic-element book element-1">
          <div class="book-pages"></div>
        </div>
        <div class="academic-element graduation-cap element-2">
          <div class="cap-top"></div>
          <div class="cap-tassel"></div>
        </div>
        <div class="academic-element pencil element-3">
          <div class="pencil-tip"></div>
        </div>
        <div class="academic-element lightbulb element-4">
          <div class="bulb-glow"></div>
        </div>
        <div class="academic-element calculator element-5">
          <div class="calc-screen"></div>
        </div>
        <div class="academic-element diploma element-6">
          <div class="diploma-ribbon"></div>
        </div>
        <div class="academic-element atom element-7">
          <div class="electron-orbit orbit-1"></div>
          <div class="electron-orbit orbit-2"></div>
          <div class="electron-orbit orbit-3"></div>
        </div>
        <div class="academic-element trophy element-8">
          <div class="trophy-glow"></div>
        </div>
      </div>
      <div class="knowledge-particles">
        <div class="knowledge-dot dot-1"></div>
        <div class="knowledge-dot dot-2"></div>
        <div class="knowledge-dot dot-3"></div>
        <div class="knowledge-dot dot-4"></div>
        <div class="knowledge-dot dot-5"></div>
        <div class="knowledge-dot dot-6"></div>
        <div class="knowledge-dot dot-7"></div>
        <div class="knowledge-dot dot-8"></div>
      </div>
      <div class="academic-grid-overlay"></div>
    </div>
    
    <!-- Floating particles for subtle animation -->
    <div class="particles">
      <div class="particle particle-1"></div>
      <div class="particle particle-2"></div>
      <div class="particle particle-3"></div>
      <div class="particle particle-4"></div>
      <div class="particle particle-5"></div>
    </div>

    <!-- Enhanced navbar with better glassmorphism -->
    <nav class="navbar">
      <div class="navbar-left">
        <div class="navbar-logo">
          <img 
            src="@/assets/LOGO WAY BG.png"
            alt="IntelliGrade Logo" 
            class="logo-image"
          />
          <div class="logo-shine"></div>
        </div>
        <span class="navbar-title">DigiCheck</span>
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
        <h1 class="hero-title">DigiCheck</h1>
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
  background: linear-gradient(135deg, #B3D8A8 0%, #A3D1C6 30%, #B3D8A8 70%, #3D8D7A 100%);
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  overflow-x: hidden;
  position: relative;
}

/* Educational Themed Animation Background */
.educational-animation {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  z-index: 0;
  pointer-events: none;
}

.floating-academic-elements {
  position: absolute;
  width: 100%;
  height: 100%;
}

.academic-element {
  position: absolute;
  opacity: 0.9;
  animation-timing-function: ease-in-out;
  animation-iteration-count: infinite;
  z-index: 2;
}

/* Book Animation */
.book {
  width: 40px;
  height: 30px;
  background: linear-gradient(135deg, rgba(179, 216, 168, 0.8), rgba(163, 209, 198, 0.7));
  border-radius: 3px;
  animation: bookFloat 20s infinite;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.3);
}

.book-pages {
  width: 36px;
  height: 26px;
  background: rgba(255, 255, 255, 0.8);
  border-radius: 2px;
  margin: 2px;
  position: relative;
}

.book-pages::after {
  content: '';
  position: absolute;
  width: 30px;
  height: 2px;
  background: rgba(61, 141, 122, 0.3);
  top: 6px;
  left: 3px;
  box-shadow: 0 4px 0 rgba(61, 141, 122, 0.2), 0 8px 0 rgba(61, 141, 122, 0.2);
}

/* Graduation Cap Animation */
.graduation-cap {
  width: 50px;
  height: 35px;
  animation: capFloat 22s infinite;
}

.cap-top {
  width: 50px;
  height: 8px;
  background: linear-gradient(135deg, rgba(61, 141, 122, 0.8), rgba(179, 216, 168, 0.7));
  border-radius: 25px;
  position: relative;
  box-shadow: 0 2px 6px rgba(61, 141, 122, 0.4);
}

.cap-tassel {
  width: 2px;
  height: 15px;
  background: rgba(61, 141, 122, 0.9);
  position: absolute;
  right: 10px;
  top: 8px;
  animation: tasselSway 3s ease-in-out infinite;
}

/* Pencil Animation */
.pencil {
  width: 8px;
  height: 60px;
  background: linear-gradient(to bottom, rgba(179, 216, 168, 0.8), rgba(163, 209, 198, 0.7));
  border-radius: 4px 4px 0 0;
  animation: pencilWrite 18s infinite;
  box-shadow: 0 2px 4px rgba(61, 141, 122, 0.3);
}

.pencil-tip {
  width: 6px;
  height: 8px;
  background: rgba(61, 141, 122, 0.9);
  margin: 0 auto;
  clip-path: polygon(50% 100%, 0% 0%, 100% 0%);
}

/* Lightbulb Animation */
.lightbulb {
  width: 30px;
  height: 40px;
  animation: lightPulse 16s infinite;
}

.bulb-glow {
  width: 30px;
  height: 30px;
  background: radial-gradient(circle, rgba(179, 216, 168, 0.8), rgba(163, 209, 198, 0.6));
  border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%;
  position: relative;
  box-shadow: 0 0 10px rgba(179, 216, 168, 0.5);
}

.bulb-glow::after {
  content: '';
  position: absolute;
  width: 20px;
  height: 10px;
  background: rgba(61, 141, 122, 0.7);
  bottom: -10px;
  left: 5px;
  border-radius: 2px;
}

/* Calculator Animation */
.calculator {
  width: 35px;
  height: 45px;
  background: linear-gradient(135deg, rgba(61, 141, 122, 0.8), rgba(179, 216, 168, 0.7));
  border-radius: 4px;
  animation: calcBounce 24s infinite;
  box-shadow: 0 2px 6px rgba(61, 141, 122, 0.3);
}

.calc-screen {
  width: 28px;
  height: 12px;
  background: rgba(255, 255, 255, 0.9);
  margin: 4px auto;
  border-radius: 2px;
}

/* Diploma Animation */
.diploma {
  width: 50px;
  height: 35px;
  background: rgba(255, 255, 255, 0.8);
  border-radius: 3px;
  animation: diplomaRoll 26s infinite;
  position: relative;
}

.diploma-ribbon {
  width: 8px;
  height: 20px;
  background: rgba(61, 141, 122, 0.4);
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}

/* Atom Animation */
.atom {
  width: 50px;
  height: 50px;
  position: relative;
  animation: atomSpin 15s infinite;
}

.electron-orbit {
  position: absolute;
  border: 1px solid rgba(61, 141, 122, 0.3);
  border-radius: 50%;
  animation: orbitRotate 8s linear infinite;
}

.orbit-1 {
  width: 50px;
  height: 50px;
  animation-duration: 8s;
}

.orbit-2 {
  width: 35px;
  height: 35px;
  top: 7.5px;
  left: 7.5px;
  animation-duration: 6s;
  animation-direction: reverse;
}

.orbit-3 {
  width: 20px;
  height: 20px;
  top: 15px;
  left: 15px;
  animation-duration: 4s;
}

.orbit-1::after, .orbit-2::after, .orbit-3::after {
  content: '';
  position: absolute;
  width: 4px;
  height: 4px;
  background: rgba(179, 216, 168, 0.6);
  border-radius: 50%;
  top: -2px;
  left: 50%;
  transform: translateX(-50%);
}

/* Trophy Animation */
.trophy {
  width: 40px;
  height: 45px;
  animation: trophyShine 28s infinite;
}

.trophy-glow {
  width: 30px;
  height: 25px;
  background: linear-gradient(135deg, rgba(179, 216, 168, 0.5), rgba(61, 141, 122, 0.3));
  border-radius: 15px 15px 5px 5px;
  margin: 0 auto;
  position: relative;
}

.trophy-glow::after {
  content: '';
  position: absolute;
  width: 35px;
  height: 8px;
  background: rgba(61, 141, 122, 0.4);
  bottom: -8px;
  left: -2.5px;
  border-radius: 0 0 4px 4px;
}

/* Element Positioning */
.element-1 { top: 15%; left: 10%; animation-delay: 0s; }
.element-2 { top: 25%; right: 15%; animation-delay: -3s; }
.element-3 { top: 60%; left: 8%; animation-delay: -6s; }
.element-4 { top: 75%; right: 20%; animation-delay: -9s; }
.element-5 { top: 40%; left: 70%; animation-delay: -12s; }
.element-6 { bottom: 25%; right: 25%; animation-delay: -15s; }
.element-7 { top: 10%; left: 85%; animation-delay: -18s; }
.element-8 { top: 85%; left: 75%; animation-delay: -21s; }

/* Knowledge Particles */
.knowledge-particles {
  position: absolute;
  width: 100%;
  height: 100%;
}

.knowledge-dot {
  position: absolute;
  width: 12px;
  height: 12px;
  background: rgba(179, 216, 168, 0.8);
  border-radius: 50%;
  animation: knowledgeFloat 12s ease-in-out infinite;
  box-shadow: 0 0 6px rgba(179, 216, 168, 0.6);
}

.dot-1 { top: 20%; left: 25%; animation-delay: 0s; }
.dot-2 { top: 30%; left: 60%; animation-delay: -1.5s; }
.dot-3 { top: 50%; left: 15%; animation-delay: -3s; }
.dot-4 { top: 70%; left: 80%; animation-delay: -4.5s; }
.dot-5 { top: 80%; left: 40%; animation-delay: -6s; }
.dot-6 { top: 45%; left: 85%; animation-delay: -7.5s; }
.dot-7 { top: 15%; left: 50%; animation-delay: -9s; }
.dot-8 { top: 65%; left: 30%; animation-delay: -10.5s; }

/* Academic Grid Overlay */
.academic-grid-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: 
    linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
  background-size: 80px 80px;
  animation: gridSlide 50s linear infinite;
}

/* Floating Particles */
.particles {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 1;
}

.particle {
  position: absolute;
  width: 6px;
  height: 6px;
  background: rgba(255, 255, 255, 0.4);
  border-radius: 50%;
  animation: float 15s ease-in-out infinite;
}

.particle-1 {
  top: 20%;
  left: 20%;
  animation-delay: 0s;
}

.particle-2 {
  top: 40%;
  left: 80%;
  animation-delay: -3s;
}

.particle-3 {
  top: 80%;
  left: 30%;
  animation-delay: -6s;
}

.particle-4 {
  top: 10%;
  left: 70%;
  animation-delay: -9s;
}

.particle-5 {
  top: 70%;
  left: 10%;
  animation-delay: -12s;
}

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
  gap: 0.3rem;
  animation: fadeInLeft 1.2s ease-out;
}

.navbar-logo {
  width: 64px;
  height: 64px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.4s ease;
  position: relative;
  flex-shrink: 0;
  margin-top: -2px;
}

.navbar-logo:hover {
  transform: scale(1.08);
}

.logo-image {
  width: 60px;
  height: 60px;
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
  color: #2D5A4A;
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
  font-weight: 500;
  color: #2D5A4A;
  padding: 0.6rem 1.5rem;
  border-radius: 8px;
  background: transparent;
  border: 1.5px solid #A3D1C6;
  outline: none;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  white-space: nowrap;
  cursor: pointer;
  transition: all 0.3s ease;
  text-decoration: none;
}

.navbar-links a:hover,
.navbar-links a.active {
  background: rgba(61, 141, 122, 0.1);
  border-color: #3D8D7A;
  color: #3D8D7A;
  transform: translateY(-1px);
}

.link-underline {
  display: none;
}

.sign-in-btn {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: #3D8D7A !important;
  color: #fff !important;
  font-weight: 600;
  font-size: 1.05rem;
  border-radius: 8px;
  padding: 0.6rem 1.5rem;
  text-decoration: none;
  border: 1.5px solid #3D8D7A !important;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.2);
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
  white-space: nowrap;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-left: 0.5rem;
}

.sign-in-btn:hover {
  background: #2D5A4A !important;
  border-color: #2D5A4A !important;
  color: #fff !important;
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(61, 141, 122, 0.3);
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
  background: linear-gradient(135deg, rgba(179, 216, 168, 0.15) 0%, rgba(163, 209, 198, 0.10) 50%, rgba(61, 141, 122, 0.05) 100%);
  backdrop-filter: blur(20px);
}

.hero-content {
  max-width: 800px;
  z-index: 10;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.25) 0%, rgba(255, 255, 255, 0.15) 100%);
  backdrop-filter: blur(25px);
  border-radius: 24px;
  padding: 3rem 2rem;
  border: 2px solid rgba(255, 255, 255, 0.3);
  box-shadow: 
    0 8px 32px rgba(61, 141, 122, 0.1),
    0 4px 16px rgba(179, 216, 168, 0.1),
    inset 0 1px 0 rgba(255, 255, 255, 0.4);
  position: relative;
  overflow: hidden;
}

.hero-content::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, transparent 0%, rgba(179, 216, 168, 0.05) 50%, transparent 100%);
  pointer-events: none;
  border-radius: 24px;
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(255, 255, 255, 0.9);
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 25px;
  padding: 0.6rem 1.5rem;
  color: #2D5A4A;
  font-size: 0.9rem;
  font-weight: 700;
  margin-bottom: 2rem;
  backdrop-filter: blur(15px);
  animation: fadeInUp 1s ease-out 0.2s both;
  text-align: center;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.hero-badge svg {
  color: #3D8D7A;
}

.hero-title {
  font-size: 4.5rem;
  font-weight: 900;
  color: #ffffff;
  margin-bottom: 1.5rem;
  letter-spacing: -2px;
  animation: fadeInUp 1s ease-out 0.4s both, titleGlow 4s ease-in-out infinite;
  text-shadow: 0 4px 20px rgba(0, 0, 0, 0.8), 0 2px 8px rgba(0, 0, 0, 0.5);
  line-height: 1.1;
  text-align: center;
}

.hero-desc {
  font-size: 1.25rem;
  color: #ffffff;
  max-width: 600px;
  margin: 0 auto;
  line-height: 1.7;
  animation: fadeInUp 1s ease-out 0.6s both;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.7), 0 1px 4px rgba(0, 0, 0, 0.5);
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
  color: #2D5A4A;
  font-size: 14px;
  font-weight: bold;
}

.about-section {
  background: linear-gradient(135deg, #FBFFE4 0%, #B3D8A8 50%, #A3D1C6 100%);
  min-height: 100vh;
  padding: 12rem 2rem 3rem;
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
  scrollbar-color: #3D8D7A #e0ede5;
}

.about-section.active::-webkit-scrollbar {
  width: 8px;
}
.about-section.active::-webkit-scrollbar-thumb {
  background: #3D8D7A;
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
  background: linear-gradient(90deg, transparent, #3D8D7A, transparent);
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
  background: rgba(255, 255, 255, 0.8);
  border: 1px solid rgba(61, 141, 122, 0.3);
  border-radius: 25px;
  padding: 0.5rem 1.2rem;
  color: #3D8D7A;
  font-size: 0.85rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  backdrop-filter: blur(15px);
  animation: fadeInUp 1s ease-out;
}

.section-badge svg {
  color: #3D8D7A;
}

.about-section h2 {
  font-size: 3.2rem;
  color: #2D5A4A;
  font-weight: 900;
  margin-bottom: 1.5rem;
  letter-spacing: -1px;
  animation: fadeInUp 1s ease-out 0.2s both;
  line-height: 1.2;
  text-shadow: 0 2px 8px rgba(61, 141, 122, 0.2);
}

.about-intro {
  font-size: 1.1rem;
  max-width: 700px;
  margin: 1rem auto 0;
  line-height: 1.6;
  color: #355C4C;
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
  background: rgba(255, 255, 255, 0.9);
  border: 2px solid rgba(179, 216, 168, 0.3);
  border-radius: 16px;
  padding: 2rem 1.5rem;
  text-align: center;
  transition: all 0.3s ease;
  backdrop-filter: blur(10px);
}

.mission-vision-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 35px rgba(61, 141, 122, 0.15);
  border-color: rgba(61, 141, 122, 0.4);
  background: rgba(255, 255, 255, 0.95);
}

.mv-icon-wrapper {
  width: 64px;
  height: 64px;
  margin: 0 auto 1.5rem;
  background: linear-gradient(135deg, #3D8D7A 0%, #B3D8A8 100%);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  box-shadow: 0 6px 20px rgba(61, 141, 122, 0.3);
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

/* Educational Animation Keyframes */
@keyframes bookFloat {
  0%, 100% { 
    transform: translateY(0px) rotate(0deg); 
    opacity: 0.7; 
  }
  25% { 
    transform: translateY(-15px) rotate(2deg); 
    opacity: 0.9; 
  }
  50% { 
    transform: translateY(-8px) rotate(-1deg); 
    opacity: 0.6; 
  }
  75% { 
    transform: translateY(-20px) rotate(1deg); 
    opacity: 0.8; 
  }
}

@keyframes capFloat {
  0%, 100% { 
    transform: translateY(0px) rotate(0deg); 
    opacity: 0.7; 
  }
  50% { 
    transform: translateY(-25px) rotate(5deg); 
    opacity: 0.9; 
  }
}

@keyframes tasselSway {
  0%, 100% { 
    transform: rotate(0deg); 
  }
  50% { 
    transform: rotate(15deg); 
  }
}

@keyframes pencilWrite {
  0%, 100% { 
    transform: translateY(0px) rotate(0deg); 
    opacity: 0.7; 
  }
  25% { 
    transform: translateY(-10px) rotate(-2deg); 
    opacity: 0.8; 
  }
  50% { 
    transform: translateY(-20px) rotate(1deg); 
    opacity: 0.9; 
  }
  75% { 
    transform: translateY(-5px) rotate(-1deg); 
    opacity: 0.6; 
  }
}

@keyframes lightPulse {
  0%, 100% { 
    transform: translateY(0px) scale(1); 
    opacity: 0.6; 
    filter: brightness(1); 
  }
  50% { 
    transform: translateY(-15px) scale(1.1); 
    opacity: 0.9; 
    filter: brightness(1.3); 
  }
}

@keyframes calcBounce {
  0%, 100% { 
    transform: translateY(0px); 
    opacity: 0.7; 
  }
  25% { 
    transform: translateY(-12px); 
    opacity: 0.8; 
  }
  50% { 
    transform: translateY(-25px); 
    opacity: 0.9; 
  }
  75% { 
    transform: translateY(-8px); 
    opacity: 0.7; 
  }
}

@keyframes diplomaRoll {
  0%, 100% { 
    transform: translateY(0px) rotate(0deg); 
    opacity: 0.7; 
  }
  50% { 
    transform: translateY(-20px) rotate(10deg); 
    opacity: 0.9; 
  }
}

@keyframes atomSpin {
  0%, 100% { 
    transform: translateY(0px) rotate(0deg); 
    opacity: 0.7; 
  }
  50% { 
    transform: translateY(-18px) rotate(180deg); 
    opacity: 0.9; 
  }
}

@keyframes orbitRotate {
  0% { 
    transform: rotate(0deg); 
  }
  100% { 
    transform: rotate(360deg); 
  }
}

@keyframes trophyShine {
  0%, 100% { 
    transform: translateY(0px) scale(1); 
    opacity: 0.7; 
    filter: brightness(1); 
  }
  50% { 
    transform: translateY(-22px) scale(1.05); 
    opacity: 0.9; 
    filter: brightness(1.2); 
  }
}

@keyframes knowledgeFloat {
  0%, 100% { 
    transform: translateY(0px) scale(1); 
    opacity: 0.4; 
  }
  50% { 
    transform: translateY(-30px) scale(1.2); 
    opacity: 0.7; 
  }
}

@keyframes gridSlide {
  0% { 
    transform: translateX(0) translateY(0); 
  }
  100% { 
    transform: translateX(80px) translateY(80px); 
  }
}

@keyframes float {
  0%, 100% {
    transform: translateY(0px) translateX(0px) scale(1);
    opacity: 0.4;
  }
  25% {
    transform: translateY(-20px) translateX(10px) scale(1.2);
    opacity: 0.7;
  }
  50% {
    transform: translateY(-10px) translateX(-15px) scale(0.8);
    opacity: 0.5;
  }
  75% {
    transform: translateY(-25px) translateX(5px) scale(1.1);
    opacity: 0.6;
  }
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
    width: 44px;
    height: 44px;
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
  
  .scroll-indicator {
    bottom: 2.5rem;
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
    width: 38px;
    height: 38px;
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
  
  .scroll-indicator {
    bottom: 2rem;
  }
  
  .scroll-arrow {
    width: 22px;
    height: 22px;
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
}
</style>