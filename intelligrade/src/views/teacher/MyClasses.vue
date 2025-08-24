<template>
  <div class="page-container">
    <div class="main-wrapper">
      <div class="hero-header card-box">
        <div class="header-content">
          <h1>My Classes</h1>
          <p>View and manage your classes, students, and assessments.</p>
        </div>
        <button class="create-class-btn" @click="goToCreateClass">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="12" y1="5" x2="12" y2="19"></line>
            <line x1="5" y1="12" x2="19" y2="12"></line>
          </svg>
          Create New Class
        </button>
      </div>

      <section class="classes-grid">
        <div class="card-box class-card" v-for="c in classes" :key="c.id">
          <router-link :to="{ name: 'ClassDetails', params: { id: c.id } }" class="class-link">
            <h2 class="class-name">{{ c.name }}</h2>
            <p class="class-subject">{{ c.subject }}</p>
            <div class="class-stats">
              <p>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                  <circle cx="9" cy="7" r="4"></circle>
                  <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                  <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                </svg>
                {{ c.students }} Students
              </p>
              <p>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                  <polyline points="14 2 14 8 20 8"></polyline>
                  <line x1="16" y1="13" x2="8" y2="13"></line>
                  <line x1="16" y1="17" x2="8" y2="17"></line>
                  <polyline points="10 9 9 9 8 9"></polyline>
                </svg>
                {{ c.assessments }} Assessments
              </p>
            </div>
          </router-link>
        </div>
      </section>

    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const classes = ref([]);

const fetchClasses = () => {
  classes.value = [
    { id: 1, name: 'Grade 10 - Rizal', subject: 'Mathematics', students: 30, assessments: 5 },
    { id: 2, name: 'Grade 9 - Bonifacio', subject: 'Science', students: 28, assessments: 4 },
  ];
};

const goToCreateClass = () => {
  router.push({ name: 'CreateClass' });
};

onMounted(() => {
  fetchClasses();
});
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

.page-container {
  padding: 2rem 5%;
  font-family: 'Inter', sans-serif;
  min-height: 100vh;
}

.main-wrapper {
  max-width: 1400px;
  margin: 0 auto;
}

.card-box {
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(61, 141, 122, 0.1);
  border-radius: 24px;
  padding: 2.5rem;
  box-shadow: 
    0 8px 32px rgba(61, 141, 122, 0.1),
    0 0 0 1px rgba(255, 255, 255, 0.2);
}

.hero-header {
  margin-bottom: 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1.5rem;
}

.header-content {
  flex: 1;
}

.hero-header h1 {
  font-size: 2.5rem;
  font-weight: 800;
  color: #3D8D7A;
  margin: 0;
}

.hero-header p {
  font-size: 1.1rem;
  color: #666;
  margin: 0;
}

.create-class-btn {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: #fff;
  border: none;
  padding: 1rem 2rem;
  border-radius: 16px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.2);
  display: flex;
  align-items: center;
  gap: 0.5rem;
  white-space: nowrap;
}

.create-class-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 16px 48px rgba(61, 141, 122, 0.3);
}

.create-class-btn svg {
  color: #fff;
}

.classes-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.class-card {
  position: relative;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.class-link {
  text-decoration: none;
  color: inherit;
  display: block;
}

.class-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 24px rgba(61, 141, 122, 0.2);
}

.class-name {
  font-size: 1.5rem;
  font-weight: 700;
  color: #3D8D7A;
  margin-bottom: 0.5rem;
}

.class-subject {
  font-size: 1rem;
  color: #777;
  font-weight: 500;
  margin-bottom: 1.5rem;
}

.class-stats {
  display: flex;
  gap: 1.5rem;
}

.class-stats p {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #555;
  font-size: 0.9rem;
  font-weight: 600;
}

.class-stats svg {
  color: #A3D1C6;
}
</style>