<template>
  <div class="intro">
    <!-- Moving wave background -->
    <div class="wave wave1"></div>
    <div class="wave wave2"></div>

    <!-- Big Logo -->
    <img src="@/assets/DIGI_CHECK_LOGO-removebg-preview.png" alt="DigiCheck Logo" class="logo" />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

onMounted(() => {
  setTimeout(() => {
    document.querySelector('.intro').classList.add('fade-out')
    setTimeout(() => router.push('/landing'), 1000) // Wait for fade animation
  }, 2500)
})
</script>

<style scoped>
.intro {
  position: fixed; /* Full screen */
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #357a66; /* Matching login bg color */
  overflow: hidden;
  transition: opacity 1s ease, transform 1s ease;
}

.fade-out {
  opacity: 0;
  transform: scale(1.05);
}

/* Wave layers */
.wave {
  position: absolute;
  bottom: -30%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: rgba(255, 255, 255, 0.1); /* Lighter waves for effect */
  border-radius: 45% 55% 35% 65%;
  animation: waveMove 6s ease-in-out infinite alternate;
  z-index: 0;
}

.wave2 {
  animation-delay: 2s;
  background: rgba(255, 255, 255, 0.15);
}

@keyframes waveMove {
  0% { transform: translateX(0) translateY(0) rotate(0deg) scale(1); }
  100% { transform: translateX(-50px) translateY(-20px) rotate(5deg) scale(1.05); }
}

/* Bigger logo */
.logo {
  position: relative;
  z-index: 1;
  width: 450px; /* Bigger for recognizability */
  max-width: 90%;
  animation: zoomIn 2s ease forwards;
}

@keyframes zoomIn {
  0% { transform: scale(0.5); opacity: 0; }
  50% { transform: scale(1); opacity: 1; }
  100% { transform: scale(1.15); }
}
</style>
