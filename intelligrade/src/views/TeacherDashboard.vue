<template>
  <div class="dashboard-container">
    <aside class="sidebar">
      <div class="user-info">
        <div class="profile-pic-container">
          <img v-if="profileData.profile_pic" :src="profileData.profile_pic" :alt="profileData.full_name" class="profile-pic">
          <div v-else class="profile-pic-placeholder">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12,4A4,4 0 0,1 16,8A4,4 0 0,1 12,12A4,4 0 0,1 8,8A4,4 0 0,1 12,4M12,14C16.42,14 20,15.79 20,18V20H4V18C4,15.79 7.58,14 12,14Z" />
            </svg>
          </div>
        </div>
        <div class="user-details">
          <h3>{{ profileData.full_name }}</h3>
          <p class="role">TEACHER</p>
        </div>
      </div>

      <nav class="nav-links">
        <router-link to="/teacher/dashboard" class="nav-item">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M10,20V14H14V20H19V12H22L12,3L2,12H5V20H10Z" />
          </svg>
          <span>Home</span>
        </router-link>

        <router-link to="/teacher/subjects" class="nav-item">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M19,3A2,2 0 0,1 21,5V19A2,2 0 0,1 19,21H5A2,2 0 0,1 3,19V5A2,2 0 0,1 5,3H19M19,19V5H5V19H19M16.5,16.25L19,14L16.5,11.75V13.5H10V14.5H16.5V16.25M7.5,7.75L5,10L7.5,12.25V10.5H14V9.5H7.5V7.75Z" />
          </svg>
          <span>My Subjects</span>
        </router-link>

        <router-link to="/teacher/analytics" class="nav-item">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M22,21H2V3H4V19H6V17H10V19H12V16H16V19H18V17H22V21M2,2H4V4H2V2M5,2H7V4H5V2M8,2H10V4H8V2M11,2H13V4H11V2M14,2H16V4H14V2M17,2H19V4H17V2M20,2H22V4H20V2Z" />
          </svg>
          <span>Analytics</span>
        </router-link>
        
        <router-link to="/teacher/messages" class="nav-item">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M22 6c0-1.1-.9-2-2-2H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6zM4 6h16v.5l-8 5-8-5V6zm0 13.5V8l8 5 8-5v11.5H4z"/>
          </svg>
          <span>Messages</span>
        </router-link>
        
        <router-link to="/teacher/settings" class="nav-item">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12,15.5A3.5,3.5 0 0,1 8.5,12A3.5,3.5 0 0,1 12,8.5A3.5,3.5 0 0,1 15.5,12A3.5,3.5 0 0,1 12,15.5M19.43,12.97C19.47,12.65 19.5,12.33 19.5,12C19.5,11.67 19.47,11.34 19.43,11.03L21.54,9.37C21.73,9.22 21.78,8.95 21.67,8.75L19.67,5.27C19.56,5.08 19.3,5.03 19.1,5.12L16.9,6C16.5,5.65 16.08,5.36 15.61,5.1L15.2,2.83C15.15,2.56 14.9,2.33 14.62,2.33L9.38,2.33C9.1,2.33 8.85,2.56 8.8,2.83L8.39,5.09C7.92,5.34 7.5,5.65 7.1,6L4.9,5.12C4.7,5.03 4.44,5.08 4.33,5.27L2.33,8.75C2.22,8.95 2.27,9.22 2.46,9.37L4.57,11.03C4.53,11.34 4.5,11.67 4.5,12C4.5,12.33 4.53,12.65 4.57,12.97L2.46,14.63C2.27,14.78 2.22,15.05 2.33,15.25L4.33,18.73C4.44,18.92 4.7,18.97 4.9,18.88L7.1,18C7.5,18.35 7.92,18.64 8.39,18.9L8.8,21.17C8.85,21.44 9.1,21.67 9.38,21.67L14.62,21.67C14.9,21.67 15.15,21.44 15.2,21.17L15.61,18.91C16.08,18.66 16.5,18.35 16.9,18L19.1,18.88C19.3,18.97 19.56,18.92 19.67,18.73L21.67,15.25C21.78,15.05 21.73,14.78 21.54,14.63L19.43,12.97Z" />
          </svg>
          <span>Settings</span>
        </router-link>
      </nav>
      
      <button @click="showLogoutModal" class="logout-btn">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
          <path d="M16,17V14H9V10H16V7L21,12L16,17M14,2A2,2 0 0,1 16,4V6H14V4H5V20H14V18H16V20A2,2 0 0,1 14,22H5A2,2 0 0,1 3,20V4A2,2 0 0,1 5,2H14Z" />
        </svg>
        <span>Logout</span>
      </button>
    </aside>

    <main class="main-content">
      <router-view></router-view>
    </main>

    <!-- Logout Confirmation Modal -->
    <div v-if="isLogoutModalVisible" class="modal-overlay" @click="hideLogoutModal">
      <div class="modal-container" @click.stop>
        <div class="modal-header">
          <div class="modal-icon">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor">
              <path d="M9,12L11,14.4L15,9.6M12,2A10,10 0 0,1 22,12A10,10 0 0,1 12,22A10,10 0 0,1 2,12A10,10 0 0,1 12,2Z" />
            </svg>
          </div>
          <h3 class="modal-title">Confirm Logout</h3>
          <p class="modal-message">Are you sure you want to logout from your account?</p>
        </div>
        
        <div class="modal-actions">
          <button @click="hideLogoutModal" class="btn-cancel">
            Cancel
          </button>
          <button @click="confirmLogout" class="btn-confirm">
            Yes, Logout
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { supabase } from '../supabase.js';
import { useRouter } from 'vue-router';

const router = useRouter();
const profileData = ref({
  full_name: 'Loading...',
  email: '',
  department: '',
  employee_id: '',
  role: 'teacher',
  profile_pic: null
});
const isLogoutModalVisible = ref(false);

const fetchUserProfile = async () => {
  try {
    const { data: { user }, error: authError } = await supabase.auth.getUser();
    
    if (authError || !user) {
      console.error('Auth error:', authError);
      router.push('/login');
      return;
    }

    console.log('Authenticated user:', user.id, user.email);

    // First, get profile data and verify role
    const { data: profile, error: profileError } = await supabase
      .from('profiles')
      .select('id, full_name, email, role')
      .eq('auth_user_id', user.id)
      .single();

    if (profileError) {
      console.warn('Profile fetch error:', profileError);
      router.push('/login');
      return;
    }

    const userData = { 
      user_id: profile.id,
      role: profile.role, 
      full_name: profile.full_name, 
      email: profile.email 
    };
    
    // Verify user is a teacher
    if (userData.role !== 'teacher') {
      console.warn('Access denied: User is not a teacher');
      router.push('/login');
      return;
    }

    console.log('User data from function:', userData);

    // Get additional teacher details
    const { data: teacherDetails, error: teacherError } = await supabase
      .from('teachers')
      .select('employee_id, department')
      .eq('id', userData.user_id)
      .single();

    if (teacherError) {
      console.warn('Teacher details fetch error:', teacherError);
    }

    console.log('Teacher details:', teacherDetails);
    
    // Set profile data
    profileData.value = {
      full_name: userData.full_name || 'Teacher',
      email: userData.email || '',
      department: teacherDetails?.department || '',
      employee_id: teacherDetails?.employee_id || '',
      role: userData.role,
      profile_pic: null // You can add profile pic URL field to your database later
    };
    
    console.log('Final profile data set:', profileData.value);
    
  } catch (err) {
    console.error('Unexpected error fetching user profile:', err);
    profileData.value = {
      full_name: 'Teacher',
      email: '',
      department: '',
      employee_id: '',
      role: 'teacher',
      profile_pic: null
    };
  }
};

const initializeDarkMode = () => {
  const savedTheme = localStorage.getItem('darkMode');
  if (savedTheme === 'true') {
    document.documentElement.classList.add('dark');
    document.body.classList.add('dark-mode');
  } else {
    document.documentElement.classList.remove('dark');
    document.body.classList.remove('dark-mode');
  }
};

const showLogoutModal = () => {
  isLogoutModalVisible.value = true;
};

const hideLogoutModal = () => {
  isLogoutModalVisible.value = false;
};

const confirmLogout = async () => {
  isLogoutModalVisible.value = false;
  
  try {
    const { error } = await supabase.auth.signOut();
    if (error) {
      throw error;
    }
    
    localStorage.removeItem('userProfile');
    localStorage.removeItem('darkMode');
    
    console.log('User logged out successfully');
    router.push('/login');
  } catch (err) {
    console.error('Logout error:', err);
    router.push('/login');
  }
};

const setupAuthListener = () => {
  supabase.auth.onAuthStateChange(async (event, session) => {
    console.log('Auth state changed:', event, session?.user?.email);
    
    if (event === 'SIGNED_OUT' || !session) {
      router.push('/login');
    } else if (event === 'SIGNED_IN' || event === 'TOKEN_REFRESHED') {
      await fetchUserProfile();
    }
  });
};

onMounted(async () => {
  initializeDarkMode();
  setupAuthListener();
  await fetchUserProfile();
});
</script>

<style scoped>
/* Imported fonts */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* Dashboard layout - perfectly fitted */
.dashboard-container {
  display: flex;
  height: 100vh;
  width: 100vw;
  margin: 0;
  padding: 0;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  font-family: 'Inter', sans-serif;
  background: var(--bg-primary);
}

.dashboard-container::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: 
    radial-gradient(circle at 20% 80%, rgba(61, 141, 122, 0.02) 0%, transparent 50%),
    radial-gradient(circle at 80% 20%, rgba(179, 216, 168, 0.03) 0%, transparent 50%),
    radial-gradient(circle at 50% 50%, rgba(163, 209, 198, 0.01) 0%, transparent 50%);
  z-index: 0;
  pointer-events: none;
}

/* PERFECTLY FITTED SIDEBAR */
.sidebar {
  width: 300px;
  height: 100vh;
  background: var(--card-background);
  backdrop-filter: blur(20px);
  border-right: 1px solid var(--border-color);
  display: flex;
  flex-direction: column;
  padding: 1.75rem 1.25rem;
  box-shadow: 
    0 8px 32px var(--shadow-medium),
    0 0 0 1px var(--border-color);
  overflow: hidden;
  flex-shrink: 0;
  position: relative;
  z-index: 1;
  justify-content: space-between;
}

/* COMPACT USER INFO */
.user-info {
  background: var(--bg-accent);
  border-radius: 16px;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  flex-shrink: 0;
  margin-bottom: 0;
}

.profile-pic-container {
  margin-bottom: 0.75rem;
}

.profile-pic {
  width: 65px;
  height: 65px;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid var(--accent-color);
  box-shadow: 0 8px 32px var(--shadow-strong);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.profile-pic:hover {
  transform: translateY(-2px) scale(1.05);
  box-shadow: 0 12px 40px var(--shadow-strong);
}

.profile-pic-placeholder {
  width: 65px;
  height: 65px;
  background: var(--accent-color);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  box-shadow: 0 8px 32px var(--shadow-strong);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.profile-pic-placeholder:hover {
  transform: translateY(-2px) scale(1.05);
  box-shadow: 0 12px 40px var(--shadow-strong);
}

.profile-pic-placeholder svg {
  width: 36px;
  height: 36px;
}

.user-details {
  width: 100%;
}

.user-info h3 {
  font-size: 1.3rem;
  font-weight: 700;
  color: var(--accent-color);
  margin-bottom: 0.4rem;
  text-shadow: 0 1px 2px var(--shadow-light);
}

.user-info .role {
  font-size: 0.8rem;
  color: var(--text-muted);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  background: var(--bg-accent);
  padding: 0.2rem 0.6rem;
  border-radius: 12px;
  display: inline-block;
  margin-bottom: 0;
}

/* PERFECTLY DISTRIBUTED NAVIGATION */
.nav-links {
  display: flex;
  flex-direction: column;
  flex: 1;
  justify-content: space-between;
  padding: 1.25rem 0;
  min-height: 280px; /* Ensure minimum height for proper distribution */
}

.nav-item {
  display: flex;
  align-items: center;
  padding: 1rem 1.2rem;
  border-radius: 14px;
  color: var(--accent-color);
  text-decoration: none;
  font-weight: 600;
  font-size: 0.9rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  background: var(--bg-accent);
  border: 1px solid var(--border-color);
  cursor: pointer;
  width: 100%;
  text-align: left;
  position: relative;
  overflow: hidden;
  margin: 0;
  box-shadow: none;
  line-height: 1;
  flex-shrink: 0;
}

.nav-item::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, rgba(179, 216, 168, 0.3) 0%, rgba(163, 209, 198, 0.2) 100%);
  transition: left 0.3s ease;
  z-index: 0;
}

.nav-item svg {
  margin-right: 0.9rem;
  width: 20px;
  height: 20px;
  fill: var(--accent-color);
  transition: all 0.3s ease;
  position: relative;
  z-index: 1;
}

.nav-item span {
  position: relative;
  z-index: 1;
}

.nav-item:hover {
  transform: none;
  box-shadow: 0 2px 8px var(--shadow-light);
  border-color: var(--border-color);
}

.nav-item:hover::before {
  left: 0;
}

.nav-item:hover svg {
  transform: none;
}

.nav-item.router-link-exact-active {
  background: rgba(95, 179, 160, 0.12);
  border-color: rgba(95, 179, 160, 0.3);
  box-shadow: 0 2px 8px rgba(95, 179, 160, 0.1);
  color: var(--accent-color);
  transform: none;
}

.nav-item.router-link-exact-active svg {
  fill: var(--accent-color);
  transform: none;
}

.nav-item.router-link-exact-active span {
  color: var(--accent-color);
  font-weight: 600;
}

/* Dark mode active state */
:root.dark .nav-item.router-link-exact-active {
  background: rgba(95, 179, 160, 0.15);
  border-color: rgba(95, 179, 160, 0.35);
  box-shadow: 0 2px 8px rgba(95, 179, 160, 0.15);
}

/* BOTTOM POSITIONED LOGOUT BUTTON */
.logout-btn {
  display: flex;
  align-items: center;
  padding: 1rem 1.2rem;
  border-radius: 14px;
  color: var(--text-inverse);
  text-decoration: none;
  font-weight: 600;
  font-size: 0.9rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  background: var(--accent-color);
  border: 1px solid var(--accent-color);
  cursor: pointer;
  width: 100%;
  text-align: left;
  position: relative;
  overflow: hidden;
  box-shadow: none;
  line-height: 1;
  gap: 0.9rem;
  justify-content: flex-start;
  box-sizing: border-box;
  flex-shrink: 0;
  margin-top: 0; /* No margin needed since we're using space-between */
}

.logout-btn svg {
  width: 20px;
  height: 20px;
  fill: var(--text-inverse);
  transition: all 0.3s ease;
  position: relative;
  z-index: 1;
}

.logout-btn span {
  position: relative;
  z-index: 1;
}

.logout-btn:hover {
  background: var(--accent-hover);
  color: var(--text-inverse);
  border-color: var(--accent-hover);
  transform: none;
  box-shadow: 0 2px 8px var(--shadow-light);
}

.logout-btn:hover svg {
  transform: none;
}

.main-content {
  flex: 1;
  overflow-y: auto;
  background: transparent;
  min-width: 0;
  position: relative;
  z-index: 1;
}

/* Modal Styles */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(8px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  animation: fadeIn 0.3s ease-out;
}

.modal-container {
  background: var(--card-background);
  backdrop-filter: blur(20px);
  border-radius: 24px;
  padding: 2.5rem;
  max-width: 450px;
  width: 90%;
  box-shadow: 
    0 20px 60px var(--shadow-strong),
    0 0 0 1px var(--border-color);
  border: 1px solid var(--border-color);
  animation: modalSlideIn 0.3s ease-out;
  text-align: center;
}

/* Dark mode styles for modal */
:root.dark .modal-container {
  background: rgba(30, 35, 34, 0.95);
  border: 1px solid rgba(95, 179, 160, 0.2);
  box-shadow: 
    0 20px 60px rgba(0, 0, 0, 0.4),
    0 0 0 1px rgba(95, 179, 160, 0.1);
}

:root.dark .modal-title {
  color: var(--text-primary);
}

:root.dark .modal-message {
  color: var(--text-secondary);
}

.modal-header {
  margin-bottom: 2rem;
}

.modal-icon {
  width: 80px;
  height: 80px;
  background: var(--accent-color);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 1.5rem;
  color: white;
  box-shadow: 0 8px 32px var(--shadow-strong);
}

.modal-icon svg {
  width: 48px;
  height: 48px;
}

.modal-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--accent-color);
  margin-bottom: 0.75rem;
}

.modal-message {
  font-size: 1rem;
  color: var(--text-secondary);
  line-height: 1.6;
  margin-bottom: 0;
}

.modal-actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
}

.btn-cancel,
.btn-confirm {
  padding: 0.875rem 2rem;
  border: none;
  border-radius: 16px;
  font-weight: 600;
  font-size: 0.95rem;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  min-width: 120px;
  position: relative;
  overflow: hidden;
}

.btn-cancel {
  background: var(--bg-accent);
  color: var(--accent-color);
  border: 2px solid var(--border-color);
}

.btn-cancel:hover {
  background: var(--bg-accent-hover);
  border-color: var(--accent-color);
  transform: none;
  box-shadow: 0 2px 8px var(--shadow-light);
}

.btn-confirm {
  background: var(--accent-color);
  color: var(--text-inverse);
  box-shadow: 0 2px 8px var(--shadow-medium);
  transition: background 0.2s, box-shadow 0.2s, transform 0.2s;
}

.btn-confirm:hover {
  background: var(--accent-hover);
  color: var(--text-inverse);
  box-shadow: 0 4px 12px var(--shadow-medium);
  transform: none;
}

/* Dark mode styles for modal buttons */
:root.dark .btn-cancel {
  background: rgba(95, 179, 160, 0.1);
  color: var(--accent-color);
  border: 2px solid rgba(95, 179, 160, 0.3);
}

:root.dark .btn-cancel:hover {
  background: rgba(95, 179, 160, 0.2);
  border-color: var(--accent-color);
}

:root.dark .btn-confirm {
  background: var(--accent-color);
  color: white;
}

/* Animations */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes modalSlideIn {
  from { 
    opacity: 0; 
    transform: translateY(-30px) scale(0.95); 
  }
  to { 
    opacity: 1; 
    transform: translateY(0) scale(1); 
  }
}

/* Responsive styles for the layout */
@media (max-width: 768px) {
  .dashboard-container {
    flex-direction: column;
    position: relative;
    height: 100vh;
  }
  
  .sidebar {
    width: 100%;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    padding: 1.5rem;
    border-right: none;
    border-bottom: 1px solid var(--border-color);
    position: sticky;
    top: 0;
    z-index: 10;
    height: auto;
    backdrop-filter: blur(20px);
  }
  
  .user-info {
    flex-direction: row;
    align-items: center;
    gap: 1rem;
    text-align: left;
    margin-bottom: 0;
    padding: 1rem 1.5rem;
    background: var(--bg-accent);
    border-radius: 16px;
  }
  
  .profile-pic-container {
    margin-bottom: 0;
  }
  
  .profile-pic, .profile-pic-placeholder {
    width: 50px;
    height: 50px;
  }
  
  .profile-pic-placeholder svg {
    width: 28px;
    height: 28px;
  }
  
  .user-info h3 {
    font-size: 1.1rem;
    margin-bottom: 0.25rem;
  }
  
  .user-info .role {
    font-size: 0.75rem;
    padding: 0.2rem 0.5rem;
  }
  
  .nav-links {
    display: none;
  }
  
  .logout-btn {
    margin-top: 0;
    padding: 0.75rem 1.25rem;
    font-size: 0.85rem;
    border-radius: 12px;
  }
  
  .main-content {
    flex: 1;
    overflow-y: auto;
    height: calc(100vh - 100px);
  }

  .modal-container {
    padding: 2rem;
    margin: 1rem;
  }
  
  .modal-actions {
    flex-direction: column;
  }
  
  .btn-cancel,
  .btn-confirm {
    width: 100%;
  }
}

@media (max-width: 480px) {
  .sidebar {
    padding: 1rem;
  }
  
  .user-info {
    padding: 0.75rem 1rem;
    gap: 0.75rem;
  }
  
  .profile-pic, .profile-pic-placeholder {
    width: 40px;
    height: 40px;
  }
  
  .profile-pic-placeholder svg {
    width: 24px;
    height: 24px;
  }
  
  .user-info h3 {
    font-size: 1rem;
  }
  
  .logout-btn {
    padding: 0.6rem 1rem;
    font-size: 0.8rem;
  }

  .modal-container {
    padding: 1.5rem;
  }
  
  .modal-icon {
    width: 60px;
    height: 60px;
  }
  
  .modal-icon svg {
    width: 36px;
    height: 36px;
  }
  
  .modal-title {
    font-size: 1.25rem;
  }
}
</style>

<style>
/* Global styles - same as student dashboard */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html, body {
  height: 100%;
  width: 100%;
  overflow: hidden; /* Prevents scrollbars on the body */
}

#app {
  height: 100%;
  width: 100%;
}
</style>