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
                <button @click="openPasswordModal" class="action-btn">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>
                </button>
              </div>
            </li>
            <li>
              <div class="setting-item">
                <span>Update Profile Info</span>
                <button @click="openProfileModal" class="action-btn">
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
                  <input type="checkbox" v-model="isDarkMode" @change="handleDarkModeToggle">
                  <span class="slider round"></span>
                </label>
              </div>
            </li>
            <li>
              <div class="setting-item">
                <span>Notifications</span>
                <label class="switch">
                  <input type="checkbox" v-model="notificationsEnabled" @change="toggleNotifications">
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
                <button @click="confirmDeleteAccount" class="action-btn danger-btn">
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

  <!-- Profile Update Modal -->
  <div v-if="isProfileModalOpen" class="modal-overlay" @click="closeProfileModal">
    <div class="modal-content" @click.stop>
      <div class="modal-header">
        <h3>Update Profile</h3>
        <button @click="closeProfileModal" class="close-btn">×</button>
      </div>
      <div class="modal-body">
        <!-- Profile Picture Section - FIRST -->
        <div class="form-group">
          <label>Profile Picture</label>
          <div class="avatar-upload-section">
            <div v-if="profileForm.profile || previewImage" class="current-avatar">
              <img 
                :src="previewImage || profileForm.profile" 
                alt="Profile Picture" 
                class="avatar-preview"
              >
            </div>
            <div v-else class="avatar-placeholder">
              <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2z"/>
                <circle cx="12" cy="7" r="4"/>
              </svg>
            </div>
            <input 
              type="file" 
              @change="handleFileSelect"
              accept="image/*"
              class="file-input"
              id="avatar-upload"
            >
            <label for="avatar-upload" class="file-input-label">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3l-2.5-3z"/>
                <circle cx="12" cy="13" r="3"/>
              </svg>
              {{ selectedFile ? 'Change Photo' : 'Choose Photo' }}
            </label>
            <div v-if="selectedFile" class="selected-file">
              Selected: {{ selectedFile.name }}
            </div>
          </div>
        </div>
        
        <!-- Full Name Section - SECOND -->
        <div class="form-group">
          <label>Full Name</label>
          <input 
            type="text" 
            v-model="profileForm.full_name" 
            placeholder="Enter your full name"
            class="form-input"
          >
        </div>
        
        <!-- Bio Section - THIRD -->
        <div class="form-group">
          <label>Bio</label>
          <textarea 
            v-model="profileForm.bio" 
            placeholder="Tell us about yourself"
            class="form-input"
            rows="4"
          ></textarea>
        </div>
        
        <!-- Messages -->
        <div v-if="profileError" class="error-message">{{ profileError }}</div>
        <div v-if="profileSuccess" class="success-message">{{ profileSuccess }}</div>
      </div>
      <div class="modal-footer">
        <button @click="closeProfileModal" class="btn-secondary">Cancel</button>
        <button @click="updateProfile" class="btn-primary" :disabled="isUpdating">
          {{ isUpdating ? 'Updating...' : 'Update Profile' }}
        </button>
      </div>
    </div>
  </div>

  <!-- Password Change Modal -->
  <div v-if="isPasswordModalOpen" class="modal-overlay" @click="closePasswordModal">
    <div class="modal-content" @click.stop>
      <div class="modal-header">
        <h3>Change Password</h3>
        <button @click="closePasswordModal" class="close-btn">×</button>
      </div>
      <div class="modal-body">
        <div class="form-group">
          <label>Current Password</label>
          <input 
            type="password" 
            v-model="passwordForm.currentPassword" 
            placeholder="Enter current password"
            class="form-input"
          >
        </div>
        <div class="form-group">
          <label>New Password</label>
          <input 
            type="password" 
            v-model="passwordForm.newPassword" 
            placeholder="Enter new password"
            class="form-input"
          >
        </div>
        <div class="form-group">
          <label>Confirm New Password</label>
          <input 
            type="password" 
            v-model="passwordForm.confirmPassword" 
            placeholder="Confirm new password"
            class="form-input"
          >
        </div>
        <div v-if="passwordError" class="error-message">{{ passwordError }}</div>
        <div v-if="passwordSuccess" class="success-message">{{ passwordSuccess }}</div>
      </div>
      <div class="modal-footer">
        <button @click="closePasswordModal" class="btn-secondary">Cancel</button>
        <button @click="changePassword" class="btn-primary">Update Password</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { supabase } from '../supabase';
import { useThemeStore } from '../stores/theme';

// Use the Pinia theme store
const themeStore = useThemeStore();

// Computed property for two-way binding with dark mode checkbox
const isDarkMode = computed({
  get: () => themeStore.isDarkMode,
  set: (value) => {
    if (value !== themeStore.isDarkMode) {
      themeStore.toggleDarkMode();
    }
  }
});

const notificationsEnabled = ref(false);

// Modal states
const isProfileModalOpen = ref(false);
const isPasswordModalOpen = ref(false);

// User data
const userId = ref(null);
const profileForm = ref({
  full_name: '',
  bio: '',
  profile: ''
});

// File upload
const selectedFile = ref(null);
const isUpdating = ref(false);
const previewImage = ref(null);

// Password form
const passwordForm = ref({
  currentPassword: '',
  newPassword: '',
  confirmPassword: ''
});

// Messages
const passwordError = ref('');
const passwordSuccess = ref('');
const profileError = ref('');
const profileSuccess = ref('');

// Dark mode toggle function
const handleDarkModeToggle = () => {
  themeStore.toggleDarkMode();
};

// Notifications toggle
const toggleNotifications = () => {
  localStorage.setItem('notifications', notificationsEnabled.value.toString());
  console.log('Notifications:', notificationsEnabled.value ? 'Enabled' : 'Disabled');
};

// File upload handler with preview
const handleFileSelect = (event) => {
  const file = event.target.files[0];
  if (file) {
    // Validate file type
    if (!file.type.startsWith('image/')) {
      profileError.value = 'Please select an image file';
      return;
    }
    // Validate file size (max 5MB)
    if (file.size > 5 * 1024 * 1024) {
      profileError.value = 'File size must be less than 5MB';
      return;
    }
    selectedFile.value = file;
    profileError.value = '';

    // Create preview
    const reader = new FileReader();
    reader.onload = (e) => {
      previewImage.value = e.target.result;
    };
    reader.readAsDataURL(file);
  }
};

// Upload avatar to Supabase storage
const uploadAvatar = async () => {
  if (!selectedFile.value) return null;
  try {
    const { data: { user } } = await supabase.auth.getUser ();
    if (!user) {
      throw new Error('No user logged in');
    }
    const fileExt = selectedFile.value.name.split('.').pop();
    const fileName = `${user.id}/${user.id}-${Date.now()}.${fileExt}`;

    // Upload file to Supabase Storage
    const { data, error } = await supabase.storage
      .from('avatars')
      .upload(fileName, selectedFile.value, { cacheControl: '3600', upsert: true });

    if (error) {
      console.error('Upload error:', error);
      throw new Error(`Upload failed: ${error.message}`);
    }

    // Get the public URL
    const { data: { publicUrl } } = supabase.storage
      .from('avatars')
      .getPublicUrl(fileName);

    return publicUrl;
  } catch (error) {
    console.error('Upload error:', error);
    throw error;
  }
};

// Profile Modal functions
const openProfileModal = async () => {
  isProfileModalOpen.value = true;
  profileError.value = '';
  profileSuccess.value = '';
  selectedFile.value = null;
  previewImage.value = null;
  await fetchUserProfile();
};

const closeProfileModal = () => {
  isProfileModalOpen.value = false;
  selectedFile.value = null;
  previewImage.value = null;
};

// Update profile function
const updateProfile = async () => {
  profileError.value = '';
  profileSuccess.value = '';

  // Basic validation
  if (!profileForm.value.full_name.trim()) {
    profileError.value = 'Full name is required';
    return;
  }

  isUpdating.value = true;

  try {
    const { data: { user } } = await supabase.auth.getUser ();
    if (!user) {
      throw new Error('No user logged in');
    }

    // Upload profile if a new file is selected
    let profileUrl = profileForm.value.profile;
    if (selectedFile.value) {
      profileUrl = await uploadAvatar();  // <-- fixed here
    }

    const profileData = {
      full_name: profileForm.value.full_name.trim(),
      bio: profileForm.value.bio.trim(),
      profile: profileUrl,
      updated_at: new Date().toISOString()
    };

    // Check if profile exists
    const { data: existingProfile } = await supabase
      .from('profiles')
      .select('id')
      .eq('id', user.id)
      .single();

    let result;
    if (existingProfile) {
      // Update existing profile
      result = await supabase
        .from('profiles')
        .update(profileData)
        .eq('id', user.id);
    } else {
      // Create new profile
      result = await supabase
        .from('profiles')
        .insert({ id: user.id, ...profileData });
    }

    if (result.error) {
      console.error('Profile update error:', result.error);
      throw new Error(result.error.message);
    }

    profileSuccess.value = 'Profile updated successfully!';

    // Update the form with the new profile URL if uploaded
    if (profileUrl) {
      profileForm.value.profile = profileUrl;
    }

    // Close modal after success
    setTimeout(() => {
      closeProfileModal();
    }, 2000);

  } catch (error) {
    console.error('Profile update error:', error);
    profileError.value = error.message || 'Failed to update profile';
  } finally {
    isUpdating.value = false;
  }
};

// Password Modal functions
const openPasswordModal = () => {
  isPasswordModalOpen.value = true;
  passwordError.value = '';
  passwordSuccess.value = '';
  passwordForm.value = {
    currentPassword: '',
    newPassword: '',
    confirmPassword: ''
  };
};

const closePasswordModal = () => {
  isPasswordModalOpen.value = false;
};

const changePassword = async () => {
  passwordError.value = '';
  passwordSuccess.value = '';

  if (!passwordForm.value.newPassword || !passwordForm.value.confirmPassword) {
    passwordError.value = 'All fields are required';
    return;
  }
  if (passwordForm.value.newPassword.length < 6) {
    passwordError.value = 'New password must be at least 6 characters';
    return;
  }
  if (passwordForm.value.newPassword !== passwordForm.value.confirmPassword) {
    passwordError.value = 'Passwords do not match';
    return;
  }

  try {
    const { error } = await supabase.auth.updateUser ({ password: passwordForm.value.newPassword });
    if (error) throw error;
    passwordSuccess.value = 'Password updated successfully!';
    setTimeout(() => {
      closePasswordModal();
    }, 2000);
  } catch (error) {
    passwordError.value = error.message;
  }
};

const confirmDeleteAccount = () => {
  if (confirm('Are you sure you want to delete your account? This action cannot be undone.')) {
    if (confirm('This will permanently delete all your data. Are you absolutely sure?')) {
      console.log('Account deletion initiated');
      // Add your account deletion logic here
    }
  }
};

// Fetch user profile data
const fetchUserProfile = async () => {
  try {
    const { data: { user } } = await supabase.auth.getUser();
    if (user) {
      userId.value = user.id;
      const { data: profile } = await supabase
        .from('profiles')
        .select('full_name, bio, profile')
        .eq('id', user.id)
        .single();

      if (profile) {
        profileForm.value = {
          full_name: profile.full_name || '',
          bio: profile.bio || '',
          profile: profile.profile || '',
        };
      }
    }
  } catch (error) {
    console.error('Error fetching profile:', error.message);
    profileError.value = 'Failed to load profile data';
  }
};

onMounted(() => {
  // Load saved notifications preference
  const savedNotifications = localStorage.getItem('notifications');
  if (savedNotifications !== null) {
    notificationsEnabled.value = savedNotifications === 'true';
  }
  // Fetch user profile
  fetchUserProfile();
});
</script>

<style scoped>
/* Light mode variables (default) */
:root {
  --bg-primary: linear-gradient(135deg, #f8fffe 0%, #f0f7f4 100%);
  --bg-secondary: #ffffff;
  --card-background: rgba(255, 255, 255, 0.95);
  --card-border-color: rgba(61, 141, 122, 0.08);
  --primary-text-color: #333333;
  --secondary-text-color: #666666;
  --accent-color: #3D8D7A;
  --accent-hover: #2d6d5a;
  --action-btn-bg: rgba(61, 141, 122, 0.1);
  --action-btn-color: #3D8D7A;
  --background-color: #ffffff;
  --border-color: #e0e0e0;
  --input-bg: #ffffff;
  --input-border: #ddd;
}

/* Dark mode variables */
:root.dark {
  --bg-primary: linear-gradient(135deg, #1a1f1e 0%, #2d3634 100%);
  --bg-secondary: #1e2322;
  --card-background: rgba(30, 35, 34, 0.95);
  --card-border-color: rgba(61, 141, 122, 0.2);
  --primary-text-color: #e0e0e0;
  --secondary-text-color: #a0a8a6;
  --accent-color: #5fb3a0;
  --accent-hover: #4a9b87;
  --action-btn-bg: rgba(95, 179, 160, 0.1);
  --action-btn-color: #5fb3a0;
  --background-color: #2d3634;
  --border-color: rgba(61, 141, 122, 0.3);
  --input-bg: #2d3634;
  --input-border: rgba(61, 141, 122, 0.3);
}

.page-container {
  padding: 2rem 5%;
  font-family: 'Inter', sans-serif;
  min-height: 100vh;
  position: relative;
  overflow-x: hidden;
  background: var(--bg-primary);
  color: var(--primary-text-color);
  transition: all 0.3s ease;
}

.main-wrapper {
  max-width: 1400px;
  margin: 0 auto;
  position: relative;
  z-index: 1;
}

.card-box {
  background: var(--card-background);
  backdrop-filter: blur(20px);
  border: 1px solid var(--card-border-color);
  border-radius: 28px;
  padding: 2.5rem;
  box-shadow: 
    0 20px 60px rgba(61, 141, 122, 0.05),
    0 8px 32px rgba(61, 141, 122, 0.03),
    0 0 0 1px rgba(255, 255, 255, 0.3);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  color: var(--primary-text-color);
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
  background: linear-gradient(135deg, var(--accent-color) 0%, var(--accent-hover) 100%);
  border-radius: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.2);
  animation: pulse 3s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.05);
  }
}

.hero-header .page-title {
  font-size: 2.5rem;
  font-weight: 800;
  color: var(--primary-text-color);
  margin: 0;
  letter-spacing: -0.02em;
}

.hero-header .page-subtitle {
  font-size: 1.2rem;
  color: var(--secondary-text-color);
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
  color: var(--primary-text-color);
  margin-bottom: 0.5rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.section-icon {
  stroke: var(--primary-text-color);
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
  color: var(--secondary-text-color);
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
  color: var(--primary-text-color);
  border-bottom: 1px solid var(--card-border-color);
  padding-bottom: 1rem;
}

.setting-item:last-child {
  border-bottom: none;
  padding-bottom: 0;
}

.action-btn {
  background: var(--action-btn-bg);
  border: none;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--action-btn-color);
  cursor: pointer;
  transition: all 0.2s ease;
  text-decoration: none;
}

.action-btn:hover {
  background: var(--accent-color);
  color: white;
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
  background-color: var(--accent-color);
}

input:focus + .slider {
  box-shadow: 0 0 1px var(--accent-color);
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
  color: var(--accent-color);
  margin-bottom: 1rem;
  display: block;
}

.about-card p {
  color: var(--secondary-text-color);
  font-size: 1rem;
  line-height: 1.5;
}

/* Modal Styles - IMPROVED LAYOUT */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  padding: 20px;
}

.modal-content {
  background: var(--card-background);
  border-radius: 16px;
  padding: 0;
  width: 100%;
  max-width: 500px;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  color: var(--primary-text-color);
}

.modal-header {
  padding: 1.5rem;
  border-bottom: 1px solid var(--card-border-color);
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: sticky;
  top: 0;
  background: var(--card-background);
  border-radius: 16px 16px 0 0;
}

.modal-header h3 {
  margin: 0;
  font-size: 1.5rem;
  color: var(--primary-text-color);
}

.close-btn {
  background: none;
  border: none;
  font-size: 2rem;
  color: var(--secondary-text-color);
  cursor: pointer;
  line-height: 1;
  padding: 0;
  width: 30px;
  height: 30px;
}

.close-btn:hover {
  color: var(--primary-text-color);
}

.modal-body {
  padding: 1.5rem;
  padding-bottom: 0;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
  color: var(--primary-text-color);
}

.form-input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid var(--input-border);
  border-radius: 8px;
  font-size: 1rem;
  transition: border-color 0.2s;
  background-color: var(--input-bg);
  color: var(--primary-text-color);
  box-sizing: border-box;
}

.form-input:focus {
  outline: none;
  border-color: var(--accent-color);
}

.form-input::placeholder {
  color: var(--secondary-text-color);
}

/* Avatar upload styles - IMPROVED */
.avatar-upload-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  background: var(--action-btn-bg);
  border-radius: 12px;
  border: 2px dashed var(--card-border-color);
}

.current-avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  overflow: hidden;
  border: 3px solid var(--accent-color);
}

.avatar-preview {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.avatar-placeholder {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  background: var(--card-background);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--accent-color);
  border: 2px dashed var(--accent-color);
}

.file-input {
  display: none;
}

.file-input-label {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: var(--accent-color);
  color: white;
  border-radius: 8px;
  cursor: pointer;
  font-size: 0.9rem;
  font-weight: 500;
  transition: all 0.2s;
}

.file-input-label:hover {
  background: var(--accent-hover);
  transform: translateY(-1px);
}

.selected-file {
  font-size: 0.9rem;
  color: var(--secondary-text-color);
  text-align: center;
  max-width: 250px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.error-message {
  color: #d9534f;
  margin-top: 1rem;
  padding: 0.75rem;
  background: rgba(217, 83, 79, 0.1);
  border-radius: 8px;
  border: 1px solid rgba(217, 83, 79, 0.3);
}

.success-message {
  color: #5cb85c;
  margin-top: 1rem;
  padding: 0.75rem;
  background: rgba(92, 184, 92, 0.1);
  border-radius: 8px;
  border: 1px solid rgba(92, 184, 92, 0.3);
}

.modal-footer {
  padding: 1.5rem;
  border-top: 1px solid var(--card-border-color);
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
  position: sticky;
  bottom: 0;
  background: var(--card-background);
  border-radius: 0 0 16px 16px;
}

.btn-primary, .btn-secondary {
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
  border: none;
}

.btn-primary {
  background: var(--accent-color);
  color: white;
}

.btn-primary:hover:not(:disabled) {
  background: var(--accent-hover);
  transform: translateY(-1px);
}

.btn-primary:disabled {
  background: #ccc;
  cursor: not-allowed;
  transform: none;
}

.btn-secondary {
  background: var(--action-btn-bg);
  color: var(--primary-text-color);
}

.btn-secondary:hover {
  background: var(--accent-color);
  color: white;
}

.danger-text {
  color: #d9534f;
}

/* Dark mode specific adjustments */
:root.dark .error-message {
  background: rgba(217, 83, 79, 0.2);
  color: #ff6b6b;
}

:root.dark .success-message {
  background: rgba(92, 184, 92, 0.2);
  color: #51cf66;
}

:root.dark .avatar-placeholder {
  background: rgba(95, 179, 160, 0.1);
}

/* Responsive */
@media (max-width: 1024px) {
  .settings-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .page-container {
    padding: 1rem 3%;
  }
  
  .hero-header .page-title {
    font-size: 2rem;
  }
  
  .settings-card {
    padding: 1.5rem;
  }
  
  .modal-overlay {
    padding: 10px;
  }
  
  .modal-content {
    width: 100%;
    max-height: 95vh;
  }
  
  .modal-header, .modal-footer {
    padding: 1rem;
  }
  
  .modal-body {
    padding: 1rem;
    padding-bottom: 0;
  }
}
</style>