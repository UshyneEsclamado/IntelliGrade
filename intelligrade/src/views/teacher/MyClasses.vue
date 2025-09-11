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

      <div v-if="loading" class="loading-state">
        <div class="spinner"></div>
        <p>Loading your classes...</p>
      </div>

      <div v-else-if="error" class="error-state">
        <p>{{ error }}</p>
        <button @click="fetchClasses" class="retry-btn">Retry</button>
      </div>

      <section v-else class="classes-grid">
        <div v-if="classes.length === 0" class="empty-state">
          <svg width="64" height="64" viewBox="0 0 24 24" fill="currentColor" class="empty-icon">
            <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/>
          </svg>
          <h3>No Classes Yet</h3>
          <p>Create your first class to get started!</p>
        </div>
        
        <div v-else class="card-box class-card" v-for="c in classes" :key="c.id">
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
                {{ c.students || 0 }} Students
              </p>
              <p>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                  <polyline points="14 2 14 8 20 8"></polyline>
                  <line x1="16" y1="13" x2="8" y2="13"></line>
                  <line x1="16" y1="17" x2="8" y2="17"></line>
                  <polyline points="10 9 9 9 8 9"></polyline>
                </svg>
                {{ c.assessments || 0 }} Assessments
              </p>
            </div>
          </router-link>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { supabase } from '../../supabase';

const router = useRouter();
const route = useRoute();
const classes = ref([]);
const loading = ref(true);
const error = ref('');

// Fetch classes from Supabase
const fetchClasses = async () => {
  try {
    loading.value = true;
    error.value = '';
    
    // Get current user
    const { data: { user } } = await supabase.auth.getUser();
    if (!user) {
      router.push('/login');
      return;
    }

    // Fetch classes for current user
    const { data, error: fetchError } = await supabase
      .from('classes')
      .select('*')
      .eq('teacher_id', user.id)
      .order('created_at', { ascending: false });

    if (fetchError) throw fetchError;

    classes.value = data || [];
  } catch (err) {
    console.error('Error fetching classes:', err);
    error.value = 'Failed to load classes. Please try again.';
  } finally {
    loading.value = false;
  }
};

const goToCreateClass = () => {
  router.push({ name: 'CreateClass' });
};

// Watch for route changes (when coming back from create class)
watch(() => route.query.createdAt, (newVal) => {
  if (newVal) {
    fetchClasses();
  }
});

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

.loading-state {
  text-align: center;
  padding: 4rem 2rem;
}

.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid rgba(61, 141, 122, 0.2);
  border-left: 4px solid #3D8D7A;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 1rem;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.error-state {
  text-align: center;
  padding: 4rem 2rem;
  color: #b00020;
}

.retry-btn {
  background: #3D8D7A;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  cursor: pointer;
  margin-top: 1rem;
}

.empty-state {
  grid-column: 1 / -1;
  text-align: center;
  padding: 4rem 2rem;
  color: #666;
}

.empty-icon {
  color: #A3D1C6;
  margin-bottom: 1rem;
}

.empty-state h3 {
  color: #3D8D7A;
  margin-bottom: 0.5rem;
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