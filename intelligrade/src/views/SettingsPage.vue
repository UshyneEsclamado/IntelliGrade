<template>
  <div class="page-container">
    <div class="main-wrapper">
      <div class="hero-header card-box">
        <div class="header-content">
          <div class="header-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M12,15.5A3.5,3.5 0 0,1 8.5,12A3.5,3.5 0 0,1 12,8.5A3.5,3.5 0 0,1 15.5,12A3.5,3.5 0 0,1 12,15.5M19.43,12.97C19.47,12.65 19.5,12.33 19.5,12C19.5,11.67 19.47,11.34 19.43,11.03L21.54,9.37C21.73,9.22 21.78,8.95 21.67,8.75L19.67,5.27C19.56,5.08 19.3,5.03 19.1,5.12L16.9,6C16.5,5.65 16.08,5.36 15.61,5.1L15.2,2.83C15.15,2.56 14.9,2.33 14.62,2.33L9.38,2.33C9.1,2.33 8.85,2.56 8.8,2.83L8.39,5.09C7.92,5.34 7.5,5.65 7.1,6L4.9,5.12C4.7,5.03 4.44,5.08 4.33,5.27L2.33,8.75C2.22,8.95 2.27,9.22 2.46,9.37L4.57,11.03C4.53,11.34 4.5,11.67 4.5,12C4.5,12.33 4.53,12.65 4.57,12.97L2.46,14.63C2.27,14.78 2.22,15.05 2.33,15.25L4.33,18.73C4.44,18.92 4.7,18.97 4.9,18.88L7.1,18C7.5,18.35 7.92,18.64 8.39,18.9L8.8,21.17C8.85,21.44 9.1,21.67 9.38,21.67L14.62,21.67C14.9,21.67 15.15,21.44 15.2,21.17L15.61,18.91C16.08,18.66 16.5,18.35 16.9,18L19.1,18.88C19.3,18.97 19.56,18.92 19.67,18.73L21.67,15.25C21.78,15.05 21.73,14.78 21.54,14.63L19.43,12.97Z" />
            </svg>
          </div>
          <h1 class="page-title">Settings</h1>
          <p class="page-subtitle">Manage your account, profile, and app preferences.</p>
        </div>
      </div>
      
      <section class="settings-grid">
        <div class="card-box settings-card">
          <h2><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="section-icon"><path d="M12,4A4,4 0 0,1 16,8A4,4 0 0,1 12,12A4,4 0 0,1 8,8A4,4 0 0,1 12,4M12,14C16.42,14 20,15.79 20,18V20H4V18C4,15.79 7.58,14 12,14Z" /></svg> Account & Profile</h2>
          <p class="section-subtitle">Update your personal information and profile settings.</p>
          <ul class="settings-list">
            <li>
              <div class="setting-item">
                <span>Change Password</span>
                <button class="action-btn">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>
                </button>
              </div>
            </li>
            <li>
              <div class="setting-item">
                <span>Update Profile Info</span>
                <button @click="openModal" class="action-btn">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>
                </button>
              </div>
            </li>
          </ul>
        </div>
        
        <div class="card-box settings-card">
          <h2><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="section-icon"><path d="M17 3a2.85 2.85 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"/></svg> App Preferences</h2>
          <p class="section-subtitle">Customize the app's look and feel.</p>
          <ul class="settings-list">
            <li>
              <div class="setting-item">
                <span>Dark Mode</span>
                <label class="switch">
                  <input type="checkbox" checked>
                  <span class="slider round"></span>
                </label>
              </div>
            </li>
            <li>
              <div class="setting-item">
                <span>Notifications</span>
                <label class="switch">
                  <input type="checkbox">
                  <span class="slider round"></span>
                </label>
              </div>
            </li>
          </ul>
        </div>

        <div class="card-box settings-card">
          <h2><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="section-icon"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" /></svg> Privacy & Legal</h2>
          <p class="section-subtitle">Understand our policies and manage your data.</p>
          <ul class="settings-list">
            <li>
              <div class="setting-item">
                <span>Privacy Policy</span>
                <a href="#" class="action-btn">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" /><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" /></svg>
                </a>
              </div>
            </li>
            <li>
              <div class="setting-item">
                <span>Terms of Service</span>
                <a href="#" class="action-btn">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71" /><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71" /></svg>
                </a>
              </div>
            </li>
          </ul>
        </div>

        <div class="card-box settings-card danger-zone">
          <h2><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="section-icon"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg> Danger Zone</h2>
          <p class="section-subtitle">Sensitive actions that cannot be undone.</p>
          <ul class="settings-list">
            <li>
              <div class="setting-item">
                <span class="danger-text">Delete Account</span>
                <button class="action-btn danger-btn">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 6l3 0l0 15a2 2 0 0 0 2 2l8 0a2 2 0 0 0 2 -2l0 -15l3 0"/><path d="M14 10l0 5"/><path d="M10 10l0 5"/><path d="M18 6l-12 0"/><path d="M10 3l4 0l0 3l-4 0l0 -3z"/></svg>
                </button>
              </div>
            </li>
          </ul>
        </div>
      </section>
      
      <section class="about-section">
        <div class="about-card card-box">
          <h2>IntelliGrade</h2>
          <p class="copyright-text">© 2025 IntelliGrade. All Rights Reserved.</p>
        </div>
      </section>

    </div>
  </div>

  <UserProfileModal 
    :isOpen="isModalOpen"
    :initialData="profileData"
    :userId="userId"
    @close="isModalOpen = false"
    @profileUpdated="handleProfileUpdate"
  />
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { supabase } from '../supabase';
import UserProfileModal from '../components/UserProfileModal.vue';

const isModalOpen = ref(false);
const userId = ref(null);
const profileData = ref({
  full_name: '',
  bio: '',
  avatar_url: '',
});

const openModal = () => {
  isModalOpen.value = true;
};

const handleProfileUpdate = (updates) => {
  profileData.value.full_name = updates.full_name;
  profileData.value.bio = updates.bio;
  profileData.value.avatar_url = updates.avatar_url;
};

const fetchUserProfile = async () => {
  try {
    const { data: { user } } = await supabase.auth.getUser();
    if (user) {
      userId.value = user.id;
      const { data: profile, error } = await supabase
        .from('profiles')
        .select('full_name, bio, avatar_url')
        .eq('id', user.id)
        .single();
      
      if (error) throw error;
      
      profileData.value = {
        full_name: profile.full_name,
        bio: profile.bio,
        avatar_url: profile.avatar_url,
      };
    }
  } catch (error) {
    console.error('Error fetching profile:', error.message);
  }
};

onMounted(() => {
  fetchUserProfile();
});
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

.page-container {
  padding: 2rem 5%;
  font-family: 'Inter', sans-serif;
  min-height: 100vh;
  position: relative;
  overflow-x: hidden;
  background: linear-gradient(135deg, #f8fffe 0%, #f0f7f4 100%);
}

.main-wrapper {
  max-width: 1400px;
  margin: 0 auto;
  position: relative;
  z-index: 1;
}

.card-box {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(61, 141, 122, 0.08);
  border-radius: 28px;
  padding: 2.5rem;
  box-shadow: 
    0 20px 60px rgba(61, 141, 122, 0.05),
    0 8px 32px rgba(61, 141, 122, 0.03),
    0 0 0 1px rgba(255, 255, 255, 0.3);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.hero-header {
  margin-bottom: 2rem;
  text-align: center;
}

.header-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}

.header-icon {
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  border-radius: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.2);
  animation: pulse 3s ease-in-out infinite;
}

.hero-header .page-title {
  font-size: 2.5rem; /* Reduced font size */
  font-weight: 800;
  color: #3D8D7A;
  margin: 0;
  letter-spacing: -0.02em;
}

.hero-header .page-subtitle {
  font-size: 1.2rem;
  color: #666;
  margin: 0;
  max-width: 600px;
}

.settings-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.settings-card {
  padding: 2.5rem;
}

.settings-card h2 {
  font-size: 1.8rem;
  font-weight: 700;
  color: #3D8D7A;
  margin-bottom: 0.5rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.section-icon {
  stroke: #3D8D7A;
}

.settings-card.danger-zone h2 {
  color: #d9534f;
}

.settings-card.danger-zone .section-subtitle,
.settings-card.danger-zone .setting-item {
  color: #d9534f;
}

.settings-card.danger-zone .action-btn.danger-btn {
  background-color: #f2dede;
  color: #d9534f;
}

.settings-card.danger-zone .action-btn.danger-btn:hover {
  background-color: #d9534f;
  color: white;
}

.section-subtitle {
  color: #777;
  font-size: 1rem;
  font-weight: 500;
  margin-bottom: 2rem;
}

.settings-list {
  list-style-type: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.setting-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 1.1rem;
  font-weight: 500;
  color: #555;
  border-bottom: 1px solid rgba(61, 141, 122, 0.1);
  padding-bottom: 1rem;
}

.setting-item:last-child {
  border-bottom: none;
  padding-bottom: 0;
}

.action-btn {
  background: rgba(61, 141, 122, 0.1);
  border: none;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #3D8D7A;
  cursor: pointer;
  transition: all 0.2s ease;
}

.action-btn:hover {
  background: rgba(61, 141, 122, 0.2);
  transform: scale(1.1);
}

.action-btn svg {
  stroke: currentColor;
}

/* Toggle Switch Styles */
.switch {
  position: relative;
  display: inline-block;
  width: 50px;
  height: 28px;
}

.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  transition: .4s;
}

.slider:before {
  position: absolute;
  content: "";
  height: 20px;
  width: 20px;
  left: 4px;
  bottom: 4px;
  background-color: white;
  transition: .4s;
}

input:checked + .slider {
  background-color: #3D8D7A;
}

input:focus + .slider {
  box-shadow: 0 0 1px #3D8D7A;
}

input:checked + .slider:before {
  transform: translateX(22px);
}

.slider.round {
  border-radius: 28px;
}

.slider.round:before {
  border-radius: 50%;
}

.about-section {
  margin-top: 2rem;
  text-align: center;
}

.about-card {
  padding: 2rem;
  max-width: 600px;
  margin: 0 auto;
}

.about-card h2 {
  font-size: 1.5rem;
  color: #3D8D7A;
  margin-bottom: 1rem;
  display: block;
}

.about-card p {
  color: #666;
  font-size: 1rem;
  line-height: 1.5;
}

/* Responsive */
@media (max-width: 1024px) {
  .settings-grid {
    grid-template-columns: 1fr;
  }
}
</style>