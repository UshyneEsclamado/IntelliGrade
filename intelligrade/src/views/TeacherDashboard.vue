<template>
  <div class="dashboard-container">
    <aside class="sidebar">
      <div class="user-info">
        <div class="profile-pic-container">
          <img v-if="profileData.profile" :src="profileData.profile" :alt="profileData.full_name" class="profile-pic">
          <div v-else class="profile-pic-placeholder">
            <svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12,4A4,4 0 0,1 16,8A4,4 0 0,1 12,12A4,4 0 0,1 8,8A4,4 0 0,1 12,4M12,14C16.42,14 20,15.79 20,18V20H4V18C4,15.79 7.58,14 12,14Z" />
            </svg>
          </div>
        </div>
        <div class="user-details">
          <h3>{{ profileData.full_name || 'Loading...' }}</h3>
          <p class="role">Teacher</p>
          <p v-if="profileData.bio" class="bio">{{ profileData.bio }}</p>
        </div>
      </div>

      <nav class="nav-links">
        <router-link to="/teacher/dashboard" class="nav-item">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M10,20V14H14V20H19V12H22L12,3L2,12H5V20H10Z" /></svg>
          <span>Home</span>
        </router-link>

        <router-link to="/teacher/subjects" class="nav-item">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M19,3H5C3.9,3 3,3.9 3,5V19C3,20.1 3.9,21 5,21H19C20.1,21 21,20.1 21,19V5C21,3.9 20.1,3 19,3M5,19V5H19V19H5M12,7A2,2 0 0,1 14,9A2,2 0 0,1 12,11A2,2 0 0,1 10,9A2,2 0 0,1 12,7M16,15H8V14C8,12.67 10.67,12 12,12C13.33,12 16,12.67 16,14V15Z" />
          </svg>
          <span>My Subjects</span>
        </router-link>

        <router-link to="/teacher/create-quiz" class="nav-item">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12,20A8,8 0 0,1 4,12A8,8 0 0,1 12,4A8,8 0 0,1 20,12A8,8 0 0,1 12,20M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M13,7H11V11H7V13H11V17H13V13H17V11H13V7Z" />
          </svg>
          <span>Create Quiz</span>
        </router-link>
        
        <router-link to="/teacher/messages" class="nav-item">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" class="messages-icon">
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
      <button @click="handleLogout" class="logout-btn">
        <span>Logout</span>
      </button>
    </aside>

    <main class="main-content">
      <router-view></router-view>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { supabase } from '../supabase';
import { useRouter } from 'vue-router';
import { useDarkMode } from '../composables/useDarkMode';

const router = useRouter();
const profileData = ref({
  full_name: '',
  bio: '',
  profile: ''
});
const { isDarkMode } = useDarkMode();

const fetchUserProfile = async () => {
  try {
    const { data: { user } } = await supabase.auth.getUser();
    if (!user) {
      router.push('/login');
      return;
    }

    // Fetch all profile fields including profile picture and bio
    const { data: profile, error } = await supabase
      .from('profiles')
      .select('full_name, bio, profile')
      .eq('id', user.id)
      .single();

    if (error) {
      console.warn('Profile not found, using defaults:', error);
      // Set default values if profile doesn't exist
      profileData.value = {
        full_name: user.email || 'User',
        bio: '',
        profile: ''
      };
      return;
    }

    profileData.value = {
      full_name: profile.full_name || user.email || 'User',
      bio: profile.bio || '',
      profile: profile.profile || ''
    };
  } catch (err) {
    console.error('Error fetching user profile:', err);
    // Don't redirect to login on profile fetch error, just use defaults
    const { data: { user } } = await supabase.auth.getUser();
    if (user) {
      profileData.value = {
        full_name: user.email || 'User',
        bio: '',
        profile: ''
      };
    } else {
      router.push('/login');
    }
  }
};

const handleLogout = async () => {
  try {
    const { error } = await supabase.auth.signOut();
    if (error) {
      throw error;
    }
    router.push('/login');
  } catch (err) {
    console.error('Logout error:', err);
  }
};

onMounted(() => {
  fetchUserProfile();
});
</script>

<style scoped>
/*
 * Imported fonts
 */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/*
 * Styles for the dashboard layout (sidebar, main content)
 * Updated for full screen coverage with beautiful design
 */
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
  background: linear-gradient(135deg, #FBFFE4 0%, #B3D8A8 50%, #A3D1C6 100%);
}

.dashboard-container::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: 
    radial-gradient(circle at 20% 80%, rgba(61, 141, 122, 0.1) 0%, transparent 50%),
    radial-gradient(circle at 80% 20%, rgba(179, 216, 168, 0.15) 0%, transparent 50%),
    radial-gradient(circle at 50% 50%, rgba(163, 209, 198, 0.08) 0%, transparent 50%);
  z-index: 0;
  pointer-events: none;
}

.sidebar {
  width: 300px;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border-right: 1px solid rgba(61, 141, 122, 0.1);
  display: flex;
  flex-direction: column;
  padding: 2.5rem 1.5rem;
  box-shadow: 
    0 8px 32px rgba(61, 141, 122, 0.1),
    0 0 0 1px rgba(255, 255, 255, 0.2);
  overflow-y: auto;
  flex-shrink: 0;
  position: relative;
  z-index: 1;
}

.user-info {
  margin-bottom: 2.5rem;
  padding-bottom: 2rem;
  border-bottom: 1px solid rgba(61, 141, 122, 0.15);
  background: rgba(251, 255, 228, 0.3);
  border-radius: 20px;
  padding: 2rem 1.5rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.profile-pic-container {
  margin-bottom: 1rem;
}

.profile-pic {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid #3D8D7A;
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.3);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.profile-pic:hover {
  transform: translateY(-2px) scale(1.05);
  box-shadow: 0 12px 40px rgba(61, 141, 122, 0.4);
}

.profile-pic-placeholder {
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.3);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.profile-pic-placeholder:hover {
  transform: translateY(-2px) scale(1.05);
  box-shadow: 0 12px 40px rgba(61, 141, 122, 0.4);
}

.profile-pic-placeholder svg {
  width: 48px;
  height: 48px;
}

.user-details {
  width: 100%;
}

.user-info h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #3D8D7A;
  margin-bottom: 0.5rem;
  text-shadow: 0 1px 2px rgba(61, 141, 122, 0.1);
}

.user-info .role {
  font-size: 0.875rem;
  color: #777;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  background: rgba(61, 141, 122, 0.1);
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  display: inline-block;
  margin-bottom: 0.5rem;
}

.user-info .bio {
  font-size: 0.875rem;
  color: #666;
  font-style: italic;
  line-height: 1.4;
  margin-top: 0.5rem;
  padding: 0.5rem;
  background: rgba(61, 141, 122, 0.05);
  border-radius: 8px;
  border-left: 3px solid #3D8D7A;
}

.nav-links {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.nav-item {
  display: flex;
  align-items: center;
  padding: 1rem 1.25rem;
  border-radius: 16px;
  color: #3D8D7A;
  text-decoration: none;
  font-weight: 600;
  font-size: 0.95rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  background: rgba(251, 255, 228, 0.5);
  border: 1px solid rgba(61, 141, 122, 0.1);
  cursor: pointer;
  width: 100%;
  text-align: left;
  position: relative;
  overflow: hidden;
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
  margin-right: 1rem;
  width: 22px;
  height: 22px;
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
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(61, 141, 122, 0.15);
  border-color: rgba(61, 141, 122, 0.2);
}

.nav-item:hover::before {
  left: 0;
}

.nav-item:hover svg {
  transform: scale(1.1);
}

.nav-item.router-link-exact-active {
  background: linear-gradient(135deg, rgba(61, 141, 122, 0.1) 0%, rgba(163, 209, 198, 0.15) 100%);
  border-color: rgba(61, 141, 122, 0.2);
  box-shadow: 0 4px 16px rgba(61, 141, 122, 0.1);
}

.nav-item.router-link-exact-active svg {
  fill: #3D8D7A;
  transform: scale(1.1);
}

.logout-btn {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: white;
  padding: 1rem 1.5rem;
  border: none;
  border-radius: 16px;
  cursor: pointer;
  font-weight: 600;
  font-size: 0.95rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  margin-top: 0.75rem;
  margin-bottom: 0.75rem;
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.2);
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  line-height: 1; 
  width: 100%;
}

.logout-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #A3D1C6 0%, #3D8D7A 100%);
  transition: left 0.3s ease;
  z-index: 0;
}

.logout-btn span {
  position: relative;
  z-index: 1;
  display: inline-block; 
}

.logout-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 16px 48px rgba(61, 141, 122, 0.3);
}

.logout-btn:hover::before {
  left: 0;
}

.main-content {
  flex: 1;
  overflow-y: auto;
  background: transparent;
  min-width: 0;
  position: relative;
  z-index: 1;
}

/*
 * Responsive styles for the layout
 */
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
    border-bottom: 1px solid rgba(61, 141, 122, 0.1);
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
    background: rgba(251, 255, 228, 0.5);
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
  
  .user-info .bio {
    display: none; /* Hide bio on mobile to save space */
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
}
</style>

<style>
/* These global styles should be added to your main CSS file or App.vue */
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