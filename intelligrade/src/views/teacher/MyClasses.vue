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
          <!-- Three-dot menu button -->
          <div class="class-menu" @click.stop="toggleMenu(c.id)">
            <button class="menu-button" :class="{ active: activeMenu === c.id }">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <circle cx="12" cy="12" r="2"></circle>
                <circle cx="12" cy="5" r="2"></circle>
                <circle cx="12" cy="19" r="2"></circle>
              </svg>
            </button>
            
            <!-- Dropdown menu -->
            <div v-if="activeMenu === c.id" class="dropdown-menu">
              <button class="menu-item primary" @click="editClass(c)">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path>
                  <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>
                </svg>
                Edit Class
              </button>
              
              <button class="menu-item" @click="manageStudents(c)">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"></path>
                  <circle cx="9" cy="7" r="4"></circle>
                  <path d="M22 21v-2a4 4 0 0 0-3-3.87"></path>
                  <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                </svg>
                Add Students
              </button>
              
              <button class="menu-item" @click="duplicateClass(c)">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                  <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                </svg>
                Duplicate Class
              </button>
              
              <div class="menu-divider"></div>
              
              <button class="menu-item danger" @click="confirmDelete(c)">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <polyline points="3,6 5,6 21,6"></polyline>
                  <path d="M19,6v14a2,2 0 0,1 -2,2H7a2,2 0 0,1 -2,-2V6m3,0V4a2,2 0 0,1 2,-2h4a2,2 0 0,1 2,2v2"></path>
                  <line x1="10" y1="11" x2="10" y2="17"></line>
                  <line x1="14" y1="11" x2="14" y2="17"></line>
                </svg>
                Delete Class
              </button>
            </div>
          </div>

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
                {{ c.studentCount || 0 }} Students
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

    <!-- Delete Confirmation Modal -->
    <div v-if="showDeleteModal" class="modal-overlay" @click.self="cancelDelete">
      <div class="modal-content delete-modal">
        <svg class="warning-icon" width="64" height="64" viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 2L1 21h22L12 2zm0 3.83L19.31 19H4.69L12 5.83zM11 16h2v2h-2v-2zm0-6h2v4h-2v-4z"/>
        </svg>
        <h3>Delete Class?</h3>
        <p>Are you sure you want to delete <strong>"{{ classToDelete?.name }}"</strong>?</p>
        <p class="warning-text">This action cannot be undone. All associated data will be permanently removed.</p>
        
        <div class="modal-actions">
          <button @click="cancelDelete" class="cancel-btn">Cancel</button>
          <button @click="deleteClass" class="delete-btn" :disabled="deleting">
            <svg v-if="deleting" class="spinner-icon" width="16" height="16" viewBox="0 0 24 24">
              <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" fill="none" opacity="0.25"/>
              <path d="M4 12a8 8 0 0 1 8-8" stroke="currentColor" stroke-width="4" fill="none"/>
            </svg>
            {{ deleting ? 'Deleting...' : 'Delete Class' }}
          </button>
        </div>
      </div>
    </div>

    <!-- Success Message -->
    <div v-if="successMessage" class="success-toast">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
      </svg>
      {{ successMessage }}
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch, onUnmounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { supabase } from '../../supabase';

const router = useRouter();
const route = useRoute();
const classes = ref([]);
const loading = ref(true);
const error = ref('');
const activeMenu = ref(null);
const showDeleteModal = ref(false);
const classToDelete = ref(null);
const deleting = ref(false);
const successMessage = ref('');

// Close menu when clicking outside
const handleClickOutside = (event) => {
  if (!event.target.closest('.class-menu')) {
    activeMenu.value = null;
  }
};

// FIXED FETCH CLASSES FUNCTION
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
    const { data: classesData, error: fetchError } = await supabase
      .from('classes')
      .select('*')
      .eq('teacher_id', user.id)
      .order('created_at', { ascending: false });

    if (fetchError) throw fetchError;

    // For each class, count the students
    const processedClasses = [];
    for (const classItem of classesData || []) {
      // Count students for this class
      const { count: studentCount, error: countError } = await supabase
        .from('students')
        .select('*', { count: 'exact' })
        .eq('class_id', classItem.id);

      if (countError) {
        console.error('Error counting students:', countError);
      }

      processedClasses.push({
        ...classItem,
        studentCount: studentCount || 0,  // Use studentCount instead of students
        assessments: classItem.assessments || 0
      });
    }

    classes.value = processedClasses;
    
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

// Menu functions
const toggleMenu = (classId) => {
  activeMenu.value = activeMenu.value === classId ? null : classId;
};

const editClass = (classData) => {
  activeMenu.value = null;
  // Now can navigate to a simple edit page for name/subject only
  router.push({ name: 'EditClass', params: { id: classData.id } });
};

const manageStudents = (classData) => {
  activeMenu.value = null;
  // Navigate to dedicated student management page
  router.push({ name: 'ClassStudents', params: { id: classData.id } });
};

const duplicateClass = async (classData) => {
  activeMenu.value = null;
  
  try {
    const { data: { user } } = await supabase.auth.getUser();
    if (!user) return;

    // Create a duplicate with "(Copy)" suffix
    const duplicatedClass = {
      name: `${classData.name} (Copy)`,
      subject: classData.subject,
      teacher_id: user.id,
      student_count: 0,
      assessments: 0,
      created_at: new Date().toISOString()
    };

    const { error: duplicateError } = await supabase
      .from('classes')
      .insert([duplicatedClass]);

    if (duplicateError) throw duplicateError;

    showSuccessMessage('Class duplicated successfully!');
    fetchClasses();
  } catch (err) {
    console.error('Error duplicating class:', err);
    error.value = 'Failed to duplicate class. Please try again.';
  }
};

const confirmDelete = (classData) => {
  activeMenu.value = null;
  classToDelete.value = classData;
  showDeleteModal.value = true;
};

const cancelDelete = () => {
  showDeleteModal.value = false;
  classToDelete.value = null;
};

const deleteClass = async () => {
  if (!classToDelete.value) return;
  
  deleting.value = true;
  
  try {
    const { error: deleteError } = await supabase
      .from('classes')
      .delete()
      .eq('id', classToDelete.value.id);

    if (deleteError) throw deleteError;

    showSuccessMessage('Class deleted successfully!');
    fetchClasses();
    cancelDelete();
  } catch (err) {
    console.error('Error deleting class:', err);
    error.value = 'Failed to delete class. Please try again.';
  } finally {
    deleting.value = false;
  }
};

const showSuccessMessage = (message) => {
  successMessage.value = message;
  setTimeout(() => {
    successMessage.value = '';
  }, 3000);
};

// Watch for route changes (when coming back from create class)
watch(() => route.query.createdAt, (newVal) => {
  if (newVal) {
    fetchClasses();
  }
});

onMounted(() => {
  fetchClasses();
  document.addEventListener('click', handleClickOutside);
});

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside);
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

/* Class Menu Styles */
.class-menu {
  position: absolute;
  top: 1rem;
  right: 1rem;
  z-index: 10;
}

.menu-button {
  background: rgba(255, 255, 255, 0.9);
  border: 1px solid rgba(61, 141, 122, 0.1);
  border-radius: 8px;
  padding: 0.5rem;
  cursor: pointer;
  transition: all 0.3s;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.menu-button:hover,
.menu-button.active {
  background: #3D8D7A;
  color: white;
  transform: scale(1.1);
}

.dropdown-menu {
  position: absolute;
  top: 100%;
  right: 0;
  background: white;
  border: 1px solid rgba(61, 141, 122, 0.1);
  border-radius: 12px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
  min-width: 180px;
  z-index: 100;
  overflow: hidden;
  animation: slideDown 0.2s ease-out;
}

@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.menu-item {
  width: 100%;
  background: none;
  border: none;
  padding: 0.75rem 1rem;
  text-align: left;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-size: 0.9rem;
  font-weight: 500;
  color: #333;
}

.menu-item:hover {
  background: #f8f9fa;
}

.menu-item.primary {
  color: #3D8D7A;
  font-weight: 600;
}

.menu-item.primary:hover {
  background: rgba(61, 141, 122, 0.1);
}

.menu-item.danger {
  color: #dc3545;
}

.menu-item.danger:hover {
  background: rgba(220, 53, 69, 0.1);
}

.menu-divider {
  height: 1px;
  background: #e9ecef;
  margin: 0.5rem 0;
}

.class-name {
  font-size: 1.5rem;
  font-weight: 700;
  color: #3D8D7A;
  margin-bottom: 0.5rem;
  margin-right: 3rem; /* Space for menu button */
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

/* Modal Styles */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  backdrop-filter: blur(4px);
}

.modal-content {
  background: #fff;
  border-radius: 24px;
  padding: 3rem;
  text-align: center;
  box-shadow: 0 16px 64px rgba(0, 0, 0, 0.3);
  max-width: 500px;
  width: 90%;
  transform: scale(0.9);
  animation: modalScale 0.3s forwards;
}

@keyframes modalScale {
  to {
    transform: scale(1);
  }
}

.delete-modal .warning-icon {
  color: #dc3545;
  margin-bottom: 1.5rem;
}

.delete-modal h3 {
  color: #dc3545;
  font-size: 1.75rem;
  font-weight: 700;
  margin-bottom: 1rem;
}

.delete-modal p {
  color: #666;
  margin-bottom: 1rem;
}

.warning-text {
  color: #dc3545;
  font-size: 0.9rem;
  font-weight: 500;
}

.modal-actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
  margin-top: 2rem;
}

.cancel-btn {
  background: #6c757d;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 12px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.cancel-btn:hover {
  background: #5a6268;
  transform: translateY(-1px);
}

.delete-btn {
  background: #dc3545;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 12px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.delete-btn:hover:not(:disabled) {
  background: #c82333;
  transform: translateY(-1px);
}

.delete-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.spinner-icon {
  animation: spin 1s linear infinite;
}

/* Success Toast */
.success-toast {
  position: fixed;
  top: 2rem;
  right: 2rem;
  background: #28a745;
  color: white;
  padding: 1rem 1.5rem;
  border-radius: 12px;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-weight: 600;
  z-index: 1000;
  animation: slideInRight 0.3s ease-out, fadeOut 0.3s ease-out 2.7s;
}

@keyframes slideInRight {
  from {
    transform: translateX(100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

@keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}

/* Responsive Design */
@media (max-width: 768px) {
  .page-container {
    padding: 1rem 3%;
  }
  
  .card-box {
    padding: 1.5rem;
  }
  
  .hero-header {
    flex-direction: column;
    align-items: stretch;
  }
  
  .hero-header h1 {
    font-size: 2rem;
  }
  
  .create-class-btn {
    justify-content: center;
  }
  
  .classes-grid {
    grid-template-columns: 1fr;
  }
  
  .class-name {
    font-size: 1.25rem;
  }
  
  .modal-content {
    padding: 2rem 1.5rem;
  }
  
  .modal-actions {
    flex-direction: column;
  }
  
  .success-toast {
    right: 1rem;
    left: 1rem;
  }
}
</style>