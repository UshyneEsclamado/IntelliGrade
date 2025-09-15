<template>
  <div class="landing-wrapper">
    <nav class="navbar">
      <div class="navbar-left">
        <div class="navbar-logo">IG</div>
        <span class="navbar-title">IntelliGrade</span>
      </div>
      <div class="navbar-links">
        <a href="#home" :class="{ active: activeSection === 'home' }" @click="scrollToSection('home')">Home</a>
        <a href="#about" :class="{ active: activeSection === 'about' }" @click="scrollToSection('about')">About Us</a>
        <router-link to="/login" class="sign-in-btn">Sign In</router-link>
      </div>
    </nav>

    <section id="home" class="hero-section">
  <!-- IG logo removed as per user request -->
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
      element.scrollIntoView({ behavior: 'smooth', block: 'start' }) // Ensure the section aligns at the top
      activeSection.value = sectionId
    }
}

function handleScroll() {
  const aboutElement = document.getElementById('about')
  const homeElement = document.getElementById('home')
    if (aboutElement && window.scrollY + 200 >= aboutElement.offsetTop) {
      activeSection.value = 'about'
    } else if (homeElement && window.scrollY === 0) {
      activeSection.value = 'home' // Check if at the very top to reset home
    }
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
  
  // Setup intersection observer for animations
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

  // Observe about section items
  setTimeout(() => {
    const aboutItems = document.querySelectorAll('.about-item')
    aboutItems.forEach(item => {
      item.style.opacity = '0'
      item.style.transform = 'translateY(20px)'
      item.style.transition = 'all 0.6s ease'
      observer.observe(item)
    })
  }, 100)
    // Ensure home section is properly centered
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
  background: linear-gradient(135deg, #f0fdf4 0%, #ecfdf5 50%, #f7fee7 100%);
  font-family: 'Inter', sans-serif;
  overflow-x: hidden;
}
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem 6vw;
  background: rgba(255,255,255,0.95);
  box-shadow: 0 4px 24px 0 rgba(61, 141, 122, 0.08);
  border-bottom: 1.5px solid #b7e4d8;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  backdrop-filter: blur(10px);
}

.navbar-left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.navbar-logo {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: bold;
  font-size: 1.2rem;
}

.navbar-title {
  font-size: 1.6rem;
  font-weight: 800;
  color: #33806b;
  letter-spacing: -0.5px;
}

.navbar-links {
  display: flex;
  align-items: center;
  gap: 2.2rem;
}

.navbar-links a {
  color: #33806b;
  font-weight: 600;
  text-decoration: none;
  font-size: 1.1rem;
  padding: 0.25rem 0.5rem;
  border-bottom: 2px solid transparent;
  transition: border 0.3s, color 0.3s;
  cursor: pointer;
}

.navbar-links a.active,
.navbar-links a:hover {
  border-bottom: 2px solid #33806b;
  color: #2d7060;
}


/* Light green Sign In button */
.sign-in-btn {
  background: linear-gradient(135deg, #b7e4d8 0%, #d1fae5 100%) !important;
  color: #33806b !important;
  font-weight: 700;
  border-radius: 10px;
  padding: 0.6rem 1.5rem;
  text-decoration: none;
  margin-left: 1.5rem;
  box-shadow: 0 4px 16px rgba(61, 141, 122, 0.12);
  transition: all 0.3s ease;
  border: none !important;
}

.sign-in-btn:hover {
  background: linear-gradient(135deg, #a7f3d0 0%, #b7e4d8 100%) !important;
  color: #256d4a !important;
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.18);
  transform: translateY(-2px);
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
  scroll-snap-align: start;  /* Ensures that it aligns properly during scroll */
}

.hero-logo {
  width: 120px;
  height: 120px;
  margin-bottom: 2rem;
  border-radius: 20px;
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.12);
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: bold;
  font-size: 2.5rem;
  animation: float 3s ease-in-out infinite;
}

@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-10px); }
}

.hero-title {
  font-size: 4rem;
  font-weight: 900;
  color: #33806b;
  margin-bottom: 1rem;
  letter-spacing: -1px;
  animation: fadeInUp 1s ease-out 0.3s both;
}

.hero-desc {
  font-size: 1.3rem;
  color: #5e8c7a;
  max-width: 700px;
  margin: 0 auto 3rem;
  line-height: 1.6;
  animation: fadeInUp 1s ease-out 0.6s both;
}

.cta-button {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: white;
  font-weight: 700;
  font-size: 1.1rem;
  border-radius: 12px;
  padding: 1rem 2rem;
  box-shadow: 0 6px 24px rgba(61, 141, 122, 0.15);
  transition: all 0.3s ease;
  border: none;
  cursor: pointer;
  animation: fadeInUp 1s ease-out 0.9s both;
}

.cta-button:hover {
  background: linear-gradient(135deg, #33806b 0%, #4dbb98 100%);
  box-shadow: 0 12px 40px rgba(61, 141, 122, 0.25);
  transform: translateY(-3px);
}

.scroll-indicator {
  position: absolute;
  bottom: 2rem;
  left: 50%;
  transform: translateX(-50%);
  animation: bounce 2s infinite, scroll-pulse 2.5s infinite alternate;
  cursor: pointer;
}

.scroll-arrow {
  width: 24px;
  height: 24px;
  border: 3px solid #33806b;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(10px);
}

.scroll-arrow::after {
  content: '↓';
  color: #33806b;
  font-size: 14px;
  font-weight: bold;
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

.about-section {
  background: rgba(255,255,255,0.95);
  min-height: 100vh;
  padding: 6rem 2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  box-shadow: 0 -8px 32px rgba(61, 141, 122, 0.08);
}

.about-section h2 {
  font-size: 3rem;
  color: #33806b;
  font-weight: 800;
  margin-bottom: 2rem;
  letter-spacing: -0.5px;
}

.about-section p {
  color: #5e8c7a;
  font-size: 1.2rem;
  margin-bottom: 3rem;
  max-width: 800px;
  line-height: 1.8;
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
  color: #33806b;
  font-size: 1.1rem;
  background: rgba(163, 209, 198, 0.15);
  border-radius: 16px;
  padding: 1.5rem;
  font-weight: 600;
  border-left: 4px solid #A3D1C6;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.about-item::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, rgba(61, 141, 122, 0.05) 0%, rgba(163, 209, 198, 0.1) 100%);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.about-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.15);
}

.about-item:hover::before {
  opacity: 1;
}

.about-item span {
  position: relative;
  z-index: 1;
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
  
  .hero-logo {
    width: 100px;
    height: 100px;
    font-size: 2rem;
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
  
  .hero-logo {
    width: 80px;
    height: 80px;
    font-size: 1.5rem;
  }
}
</style>