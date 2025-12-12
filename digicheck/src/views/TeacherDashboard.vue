<template>
  <div class="teacher-layout">
    <!-- The router-view renders the child route component -->
    <router-view :key="$route.fullPath" />
  </div>
</template>

<script>
export default {
  name: 'TeacherDashboard'
}
</script>

<style scoped>
.teacher-layout {
  min-height: 100vh;
  width: 100%;
}
</style>
