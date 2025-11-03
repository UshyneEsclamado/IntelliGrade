<template>
  <div class="dashboard-container">
    <aside class="sidebar">
      <div class="user-info">
        <div class="profile-pic-container">
          <img 
            v-if="profileData.profile_pic" 
            :src="profileData.profile_pic" 
            :alt="profileData.full_name" 
            class="profile-pic"
            @error="handleImageError"
          >
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
        <router-link 
          to="/teacher/dashboard" 
          class="nav-item"
          :class="{ 'is-active': $route.path === '/teacher/dashboard' || $route.name === 'TeacherDashboardHome' }"
        >
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M10,20V14H14V20H19V12H22L12,3L2,12H5V20H10Z" />
          </svg>
          <span>Home</span>
        </router-link>

        <router-link 
          to="/teacher/subjects" 
          class="nav-item"
          :class="{ 'is-active': $route.path.startsWith('/teacher/subjects') || $route.name === 'TeacherSubjects' }"
        >
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M19,3A2,2 0 0,1 21,5V19A2,2 0 0,1 19,21H5A2,2 0 0,1 3,19V5A2,2 0 0,1 5,3H19M19,19V5H5V19H19M16.5,16.25L19,14L16.5,11.75V13.5H10V14.5H16.5V16.25M7.5,7.75L5,10L7.5,12.25V10.5H14V9.5H7.5V7.75Z" />
          </svg>
          <span>My Subjects</span>
        </router-link>

        <router-link 
          to="/teacher/analytics" 
          class="nav-item"
          :class="{ 'is-active': $route.path === '/teacher/analytics' || $route.name === 'TeacherAnalytics' }"
        >
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M22,21H2V3H4V19H6V17H10V19H12V16H16V19H18V17H22V21M2,2H4V4H2V2M5,2H7V4H5V2M8,2H10V4H8V2M11,2H13V4H11V2M14,2H16V4H14V2M17,2H19V4H17V2M20,2H22V4H20V2Z" />
          </svg>
          <span>Analytics</span>
        </router-link>
        
        <router-link 
          to="/teacher/messages" 
          class="nav-item"
          :class="{ 'is-active': $route.path === '/teacher/messages' || $route.name === 'TeacherMessages' }"
        >
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M22 6c0-1.1-.9-2-2-2H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6zM4 6h16v.5l-8 5-8-5V6zm0 13.5V8l8 5 8-5v11.5H4z"/>
          </svg>
          <span>Messages</span>
        </router-link>
        
        <router-link 
          to="/teacher/settings" 
          class="nav-item"
          :class="{ 'is-active': $route.path === '/teacher/settings' || $route.name === 'TeacherSettings' }"
        >
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

    <!-- Floating Help & Support Button -->
    <button class="floating-help-btn" @click="toggleHelpMenu" title="Help & Support">
      <svg v-if="!isHelpMenuOpen" width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
        <path d="M11,18H13V16H11V18M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,20C7.59,20 4,16.41 4,12C4,7.59 7.59,4 12,4C16.41,4 20,7.59 20,12C20,16.41 16.41,20 12,20M12,6A4,4 0 0,0 8,10H10A2,2 0 0,1 12,8A2,2 0 0,1 14,10C14,12 11,11.75 11,15H13C13,12.75 16,12.5 16,10A4,4 0 0,0 12,6Z" />
      </svg>
      <svg v-else width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
        <path d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z" />
      </svg>
    </button>

    <!-- Help Menu -->
    <transition name="help-menu">
      <div v-if="isHelpMenuOpen" class="help-menu">
        <div class="help-menu-header">
          <h3>Help & Support</h3>
          <p>How can we assist you today?</p>
        </div>
        <div class="help-menu-items">
          <a href="#" class="help-menu-item" @click.prevent="openGuide">
            <div class="help-item-icon">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M19,2L14,6.5V17.5L19,13V2M6.5,5C4.55,5 2.45,5.4 1,6.5V21.16C1,21.41 1.25,21.66 1.5,21.66C1.6,21.66 1.65,21.59 1.75,21.59C3.1,20.94 5.05,20.5 6.5,20.5C8.45,20.5 10.55,20.9 12,22C13.35,21.15 15.8,20.5 17.5,20.5C19.15,20.5 20.85,20.81 22.25,21.56C22.35,21.61 22.4,21.59 22.5,21.59C22.75,21.59 23,21.34 23,21.09V6.5C22.4,6.05 21.75,5.75 21,5.5V7.5L21,13V19C19.9,18.65 18.7,18.5 17.5,18.5C15.8,18.5 13.35,19.15 12,20V13L12,8.5V6.5C10.55,5.4 8.45,5 6.5,5Z" />
              </svg>
            </div>
            <div class="help-item-content">
              <h4>Teacher's Guide</h4>
              <p>Learn how to use IntelliGrade effectively</p>
            </div>
          </a>
          <a href="#" class="help-menu-item" @click.prevent="openFAQ">
            <div class="help-item-icon">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M18,15H6L2,19V3A1,1 0 0,1 3,2H18A1,1 0 0,1 19,3V14A1,1 0 0,1 18,15M23,9V23L19,19H8A1,1 0 0,1 7,18V17H20V8H21A1,1 0 0,1 22,9Z" />
              </svg>
            </div>
            <div class="help-item-content">
              <h4>FAQ</h4>
              <p>Find answers to common questions</p>
            </div>
          </a>
          <a href="#" class="help-menu-item" @click.prevent="contactSupport">
            <div class="help-item-icon">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M20,8L12,13L4,8V6L12,11L20,6M20,4H4C2.89,4 2,4.89 2,6V18A2,2 0 0,0 4,20H20A2,2 0 0,0 22,18V6C22,4.89 21.1,4 20,4Z" />
              </svg>
            </div>
            <div class="help-item-content">
              <h4>Contact Support</h4>
              <p>Get help from our support team</p>
            </div>
          </a>
          <a href="#" class="help-menu-item" @click.prevent="reportIssue">
            <div class="help-item-icon">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M13,14H11V10H13M13,18H11V16H13M1,21H23L12,2L1,21Z" />
              </svg>
            </div>
            <div class="help-item-content">
              <h4>Report an Issue</h4>
              <p>Let us know about any problems</p>
            </div>
          </a>
        </div>
      </div>
    </transition>

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

    <!-- Logging Out Overlay -->
    <div v-if="isLoggingOut" class="logging-out-overlay">
      <div class="logging-out-content">
        <div class="spinner"></div>
        <p>Logging out...</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue';
import { supabase } from '../supabase.js';
import { useRouter } from 'vue-router';
import { useTeacherAuth } from '../composables/useTeacherAuth.js';

const router = useRouter();

// Use the teacher auth composable - ONLY DECLARE ONCE
const { 
  teacherProfile, 
  teacherInfo, 
  isLoading,
  isAuthenticated,
  initializeAuth, 
  setupAuthListener
} = useTeacherAuth();

const isLogoutModalVisible = ref(false);
const isHelpMenuOpen = ref(false);
const isLoggingOut = ref(false);

// Computed profile data from the composable
const profileData = computed(() => {
  if (!teacherInfo.value || !teacherProfile.value) {
    return {
      full_name: isLoading.value ? 'Loading...' : 'Teacher',
      email: '',
      department: '',
      employee_id: '',
      role: 'teacher',
      profile_pic: null
    };
  }

  return {
    full_name: teacherProfile.value.full_name || 'Teacher',
    email: teacherProfile.value.email || '',
    department: teacherInfo.value.department || '',
    employee_id: teacherInfo.value.employee_id || '',
    role: teacherProfile.value.role || 'teacher',
    profile_pic: teacherInfo.value.profile_pic || null
  };
});

// Handle image loading errors
const handleImageError = (event: Event) => {
  console.warn('❌ Failed to load profile image, falling back to placeholder');
  console.log('Failed image src:', (event.target as HTMLImageElement)?.src);
  // Note: With computed profileData, we can't directly modify it
  // The composable should handle image error fallbacks
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
  isLoggingOut.value = true;
  
  // Set a timeout to force redirect after 2 seconds max
  const redirectTimeout = setTimeout(() => {
    localStorage.clear();
    window.location.replace('/login');
  }, 2000);
  
  try {
    console.log('Starting logout process...');
    
    // Sign out from Supabase
    await supabase.auth.signOut();
    
    // Clear local storage
    localStorage.clear();
    
    console.log('User logged out successfully, redirecting...');
    
    // Clear the timeout since we're done
    clearTimeout(redirectTimeout);
    
    // Small delay before redirect for smooth UX
    setTimeout(() => {
      window.location.replace('/login');
    }, 500);
    
  } catch (err) {
    console.error('Error during logout:', err);
    // Clear timeout and force logout anyway
    clearTimeout(redirectTimeout);
    localStorage.clear();
    setTimeout(() => {
      window.location.replace('/login');
    }, 500);
  }
};

const toggleHelpMenu = () => {
  isHelpMenuOpen.value = !isHelpMenuOpen.value;
};

const openGuide = () => {
  alert('Teacher\'s Guide: Opening documentation...');
  isHelpMenuOpen.value = false;
};

const openFAQ = () => {
  alert('FAQ: Opening frequently asked questions...');
  isHelpMenuOpen.value = false;
};

const contactSupport = () => {
  alert('Contact Support: Opening support form...');
  isHelpMenuOpen.value = false;
};

const reportIssue = () => {
  alert('Report Issue: Opening issue report form...');
  isHelpMenuOpen.value = false;
};

// Listen for profile updates from Settings component
const handleProfileUpdate = async (event: CustomEvent) => {
  console.log('📢 Received profile update event in TeacherDashboard:', event.detail);
  const { nameChanged, photoChanged, newName, newPhoto } = event.detail || {};
  
  if (nameChanged && teacherProfile.value) {
    console.log(`✏️ Name changed to: ${newName}`);
    // Update the profile data immediately
    teacherProfile.value.full_name = newName;
  }
  
  if (photoChanged && teacherInfo.value) {
    console.log('📸 Profile photo changed');
    // Update the profile photo immediately
    teacherInfo.value.profile_pic = newPhoto;
  }
  
  // Also reload to ensure consistency
  await initializeAuth();
  
  console.log('✅ TeacherDashboard profile updated:', profileData.value);
};

onMounted(async () => {
  console.log('\n🚀 TeacherDashboard mounted\n');
  initializeDarkMode();
  
  // Initialize authentication once for the entire teacher dashboard
  const authResult = await initializeAuth();
  if (authResult.success) {
    setupAuthListener();
    console.log('Teacher dashboard initialized successfully');
  } else {
    console.error('Failed to initialize teacher dashboard');
    router.push('/login');
  }
  
  // Listen for profile updates from Settings component
  window.addEventListener('teacherProfileUpdated', handleProfileUpdate as EventListener);
});

// Cleanup on unmount
import { onUnmounted } from 'vue';

onUnmounted(() => {
  window.removeEventListener('teacherProfileUpdated', handleProfileUpdate as EventListener);
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
  font-size: 1.15rem;
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

/* SIDEBAR - EXACT STUDENT DASHBOARD MATCH */
.sidebar {
  width: 300px;
  background: var(--card-background);
  backdrop-filter: blur(20px);
  border-right: 1px solid var(--border-color);
  display: flex;
  flex-direction: column;
  padding: 1.5rem 1rem;
  box-shadow: 
    0 8px 32px var(--shadow-medium),
    0 0 0 1px var(--border-color);
  overflow-y: hidden;
  flex-shrink: 0;
  position: relative;
  z-index: 1;
}

/* USER INFO - EXACT STUDENT DASHBOARD MATCH */
.user-info {
  margin-bottom: 1.5rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid var(--border-color);
  background: var(--bg-accent);
  border-radius: 16px;
  padding: 1.5rem 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.profile-pic-container {
  margin-bottom: 0.75rem;
}

.profile-pic {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  object-fit: cover;
  box-shadow: 0 4px 16px var(--shadow-strong);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.profile-pic:hover {
  transform: translateY(-1px) scale(1.02);
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.15);
}

.profile-pic-placeholder {
  width: 60px;
  height: 60px;
  background: var(--accent-color);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  box-shadow: 0 4px 16px var(--shadow-strong);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.profile-pic-placeholder:hover {
  transform: translateY(-1px) scale(1.02);
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.15);
}

.profile-pic-placeholder svg {
  width: 32px;
  height: 32px;
}

.user-details {
  width: 100%;
}

.user-info h3 {
  font-size: 1.35rem;
  font-weight: 700;
  color: var(--accent-color);
  margin-bottom: 0.5rem;
  word-break: break-word;
  line-height: 1.2;
  min-height: 1.5rem;
}

.user-info .role {
  font-size: 0.85rem;
  color: var(--text-muted);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  background: var(--bg-accent);
  padding: 0.25rem 0.5rem;
  border-radius: 8px;
  display: inline-block;
  margin-bottom: 0.5rem;
  border: 1px solid var(--border-color);
}

/* NAVIGATION LINKS - EXACT STUDENT DASHBOARD MATCH */
.nav-links {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  justify-content: center;
}

.nav-item {
  display: flex;
  align-items: center;
  padding: 0.75rem 1rem;
  border-radius: 12px;
  color: var(--accent-color);
  text-decoration: none;
  font-weight: 600;
  font-size: 1rem;
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
  margin-right: 0.75rem;
  width: 18px;
  height: 18px;
  fill: #3D8D7A;
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
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.08);
  border-color: rgba(61, 141, 122, 0.15);
}

.nav-item:hover::before {
  left: 0;
}

.nav-item.is-active,
.nav-item.router-link-exact-active {
  background: rgba(95, 179, 160, 0.12);
  border-color: rgba(95, 179, 160, 0.3);
  box-shadow: 0 2px 8px rgba(95, 179, 160, 0.1);
  color: var(--accent-color);
  transform: none;
}

.nav-item.is-active svg,
.nav-item.router-link-exact-active svg {
  fill: var(--accent-color);
}

.nav-item.is-active span,
.nav-item.router-link-exact-active span {
  color: var(--accent-color);
  font-weight: 600;
}

/* Dark mode active state */
:root.dark .nav-item.is-active,
:root.dark .nav-item.router-link-exact-active {
  background: rgba(95, 179, 160, 0.15);
  border-color: rgba(95, 179, 160, 0.35);
  box-shadow: 0 2px 8px rgba(95, 179, 160, 0.15);
}

/* LOGOUT BUTTON - EXACT STUDENT DASHBOARD MATCH */
.logout-btn {
  display: flex;
  align-items: center;
  padding: 0.75rem 1rem;
  border-radius: 12px;
  color: var(--text-inverse);
  text-decoration: none;
  font-weight: 600;
  font-size: 1rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  background: var(--accent-color);
  border: 1px solid var(--accent-color);
  cursor: pointer;
  width: 100%;
  text-align: left;
  position: relative;
  overflow: hidden;
  margin-top: 0.5rem;
  box-shadow: none;
  line-height: 1;
  gap: 0.75rem;
  justify-content: flex-start;
  box-sizing: border-box;
}

.logout-btn svg {
  width: 18px;
  height: 18px;
  margin-right: 0.75rem;
}

.logout-btn:hover {
  background: var(--accent-hover);
  color: var(--text-inverse);
  border-color: var(--accent-hover);
  transform: none;
  box-shadow: 0 2px 8px rgba(24, 60, 46, 0.1);
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
  border-radius: 20px;
  padding: 2.5rem;
  max-width: 420px;
  width: 90%;
  box-shadow: 
    0 8px 40px rgba(0, 0, 0, 0.12),
    0 0 0 1px rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.08);
  animation: modalSlideIn 0.3s ease-out;
  text-align: center;
}

/* Dark mode styles for modal */
:root.dark .modal-container {
  background: rgba(30, 35, 34, 0.95);
  border: 1px solid rgba(95, 179, 160, 0.2);
  box-shadow: 
    0 8px 40px rgba(0, 0, 0, 0.3),
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
  background: linear-gradient(135deg, #5FB3A0 0%, #A3D1C6 100%);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 1.5rem;
  color: white;
  box-shadow: 0 4px 20px rgba(95, 179, 160, 0.3);
}

.modal-icon svg {
  width: 40px;
  height: 40px;
}

.modal-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 0.75rem;
  letter-spacing: -0.01em;
}

.modal-message {
  font-size: 1rem;
  color: var(--text-secondary);
  line-height: 1.5;
  margin-bottom: 0;
}

.modal-actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
  margin-top: 2rem;
}

.btn-cancel,
.btn-confirm {
  padding: 0.75rem 1.75rem;
  border: none;
  border-radius: 12px;
  font-weight: 600;
  font-size: 0.95rem;
  cursor: pointer;
  transition: all 0.2s ease;
  min-width: 110px;
  outline: none;
}

.btn-cancel {
  background: rgba(95, 179, 160, 0.1);
  color: var(--accent-color);
  border: 1.5px solid rgba(95, 179, 160, 0.3);
}

.btn-cancel:hover {
  background: rgba(95, 179, 160, 0.15);
  border-color: var(--accent-color);
}

.btn-confirm {
  background: var(--accent-color);
  color: white;
  box-shadow: 0 2px 8px rgba(95, 179, 160, 0.25);
}

.btn-confirm:hover {
  background: var(--accent-hover);
  box-shadow: 0 4px 12px rgba(95, 179, 160, 0.3);
}

/* Dark mode styles for modal buttons */
:root.dark .btn-cancel {
  background: rgba(95, 179, 160, 0.1);
  color: var(--accent-color);
  border: 1.5px solid rgba(95, 179, 160, 0.3);
}

:root.dark .btn-cancel:hover {
  background: rgba(95, 179, 160, 0.18);
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

/* Floating Help Button */
.floating-help-btn {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  width: 60px;
  height: 60px;
  background: var(--accent-color);
  border: none;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 4px 16px var(--shadow-strong);
  color: white;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  z-index: 999;
}

.floating-help-btn:hover {
  transform: scale(1.1);
  box-shadow: 0 6px 24px var(--shadow-strong);
  background: var(--accent-hover);
}

.floating-help-btn:active {
  transform: scale(0.95);
}

/* Help Menu */
.help-menu {
  position: fixed;
  bottom: 6rem;
  right: 2rem;
  width: 320px;
  background: var(--card-background);
  border-radius: 16px;
  box-shadow: 0 8px 32px var(--shadow-strong);
  border: 1px solid var(--border-color);
  overflow: hidden;
  z-index: 998;
}

.help-menu-header {
  padding: 1.5rem;
  background: var(--bg-accent);
  border-bottom: 1px solid var(--border-color);
}

.help-menu-header h3 {
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--accent-color);
  margin-bottom: 0.5rem;
}

.help-menu-header p {
  font-size: 0.875rem;
  color: var(--text-muted);
  margin: 0;
}

.help-menu-items {
  padding: 0.5rem;
}

.help-menu-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  border-radius: 12px;
  text-decoration: none;
  transition: all 0.2s ease;
  cursor: pointer;
  margin-bottom: 0.5rem;
}

.help-menu-item:last-child {
  margin-bottom: 0;
}

.help-menu-item:hover {
  background: var(--bg-accent);
}

.help-item-icon {
  width: 40px;
  height: 40px;
  background: var(--accent-color);
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
}

.help-item-content {
  flex: 1;
}

.help-item-content h4 {
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 0.25rem;
}

.help-item-content p {
  font-size: 0.813rem;
  color: var(--text-muted);
  margin: 0;
}

/* Help Menu Transitions */
.help-menu-enter-active,
.help-menu-leave-active {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.help-menu-enter-from {
  opacity: 0;
  transform: translateY(20px) scale(0.95);
}

.help-menu-leave-to {
  opacity: 0;
  transform: translateY(20px) scale(0.95);
}

/* Responsive adjustments for floating button */
@media (max-width: 768px) {
  .floating-help-btn {
    bottom: 1.5rem;
    right: 1.5rem;
    width: 56px;
    height: 56px;
  }
  
  .help-menu {
    bottom: 5rem;
    right: 1.5rem;
    left: 1.5rem;
    width: auto;
  }
}

@media (max-width: 480px) {
  .floating-help-btn {
    bottom: 1rem;
    right: 1rem;
    width: 52px;
    height: 52px;
  }
  
  .help-menu {
    bottom: 4.5rem;
    right: 1rem;
    left: 1rem;
  }
}

/* Logging Out Overlay */
.logging-out-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.8);
  backdrop-filter: blur(10px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10000;
  animation: fadeIn 0.3s ease-out;
}

.logging-out-content {
  text-align: center;
  color: white;
}

.spinner {
  width: 60px;
  height: 60px;
  margin: 0 auto 1.5rem;
  border: 4px solid rgba(255, 255, 255, 0.2);
  border-top: 4px solid var(--accent-color);
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.logging-out-content p {
  font-size: 1.25rem;
  font-weight: 600;
  color: white;
  margin: 0;
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
  overflow: hidden;
}

#app {
  height: 100%;
  width: 100%;
}

/* CSS Variables for consistent theming */
:root {
  /* Light mode colors */
  --bg-primary: #f8faf9;
  --bg-secondary: #fefefe;
  --bg-accent: #f3f7f4;
  --bg-accent-hover: #e9f5ee;
  
  --card-background: #ffffff;
  --card-background-hover: #f8faf9;
  
  --accent-color: #33806b;
  --accent-hover: #2d6a57;
  --accent-light: #5FB3A0;
  --accent-lighter: #A3D1C6;
  
  --text-primary: #1a1a1a;
  --text-secondary: #3d8d7a;
  --text-muted: #7a9c8f;
  --text-inverse: #ffffff;
  
  --border-color: rgba(61, 141, 122, 0.12);
  --border-hover: rgba(61, 141, 122, 0.2);
  
  --shadow-light: rgba(61, 141, 122, 0.05);
  --shadow-medium: rgba(61, 141, 122, 0.1);
  --shadow-strong: rgba(61, 141, 122, 0.2);
}

/* Dark mode colors */
:root.dark {
  --bg-primary: #181c20;
  --bg-secondary: #23272b;
  --bg-accent: #23272b;
  --bg-accent-hover: #23272b;
  
  --card-background: #23272b;
  --card-background-hover: #181c20;
  
  --accent-color: #5FB3A0;
  --accent-hover: #33806b;
  --accent-light: #7BC4B5;
  --accent-lighter: #A3D1C6;
  
  --text-primary: #f0f0f0;
  --text-secondary: #A3D1C6;
  --text-muted: #7a9c8f;
  --text-inverse: #ffffff;
  
  --border-color: rgba(95, 179, 160, 0.15);
  --border-hover: rgba(95, 179, 160, 0.25);
  
  --shadow-light: rgba(0, 0, 0, 0.1);
  --shadow-medium: rgba(0, 0, 0, 0.2);
  --shadow-strong: rgba(0, 0, 0, 0.3);
}
</style>