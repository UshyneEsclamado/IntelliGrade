<template>
    <div class="intro">
      <img src="@/assets/New IntelliGrade Logo.png" alt="IntelliGrade Logo" class="logo" />
    </div>
  </template>
  
  <script setup>
  import { onMounted } from 'vue'
  import { useRouter } from 'vue-router'
  
  const router = useRouter()
  
  onMounted(() => {
    setTimeout(() => {
      router.push('/login')
    }, 2500) // 2.5 seconds
  })
  </script>
  
  <style scoped>
  .intro {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background: white;
  }
  
  .logo {
    width: 180px;
    animation: moveZoom 2s ease forwards;
  }
  
  @keyframes moveZoom {
    0% { transform: translateY(20px) scale(0.8); opacity: 0; }
    50% { transform: translateY(0) scale(1); opacity: 1; }
    100% { transform: translateY(-10px) scale(1.1); opacity: 1; }
  }
  </style>
  