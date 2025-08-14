<template>
  <div class="intro">
    <!-- Wave background -->
    <div class="wave"></div>

    <!-- Logo -->
    <img src="@/assets/New IntelliGrade Logo Way BG.png" alt="IntelliGrade Logo" class="logo" />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

onMounted(() => {
  setTimeout(() => {
    router.push('/login')
  }, 2500) // 2.5 seconds before redirect
})
</script>

<style scoped>
.intro {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #3d8d7a; /* your background color */
  overflow: hidden;
}

/* Wave effect */
.wave {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 200%;
  height: 150%;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 45% 55% 35% 65%;
  animation: waveMove 6s ease-in-out infinite alternate;
  z-index: 0;
}

@keyframes waveMove {
  0% { transform: translateX(0) translateY(0) rotate(0deg); }
  100% { transform: translateX(-50px) translateY(-20px) rotate(5deg); }
}

/* Logo styling */
.logo {
  position: relative;
  z-index: 1;
  width: 300px; /* bigger logo */
  animation: zoomIn 2s ease forwards;
}

@keyframes zoomIn {
  0% { transform: scale(0.5); opacity: 0; }
  50% { transform: scale(1); opacity: 1; }
  100% { transform: scale(1.1); }
}
</style>
