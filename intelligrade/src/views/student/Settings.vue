<template>
  <div class="settings-container">
    <div class="settings-header">
      <h1>Settings</h1>
      <p>Manage your account settings and preferences</p>
    </div>

    <div class="settings-content">
      <!-- Profile Settings Card -->
      <div class="settings-card">
        <div class="card-header">
          <h2>Profile Information</h2>
          <p>Update your personal information</p>
        </div>
        
        <div class="profile-section">
          <div class="profile-photo-section">
            <div class="current-photo">
              <img 
                v-if="profilePhoto" 
                :src="profilePhoto" 
                alt="Profile Photo"
                class="profile-photo"
              />
              <div v-else class="profile-photo-placeholder">
                <svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M12,4A4,4 0 0,1 16,8A4,4 0 0,1 12,12A4,4 0 0,1 8,8A4,4 0 0,1 12,4M12,14C16.42,14 20,15.79 20,18V20H4V18C4,15.79 7.58,14 12,14Z" />
                </svg>
              </div>
            </div>
            
            <div class="photo-actions">
              <input 
                type="file" 
                ref="photoInput" 
                @change="handlePhotoChange"
                accept="image/jpeg,image/png,image/gif,image/webp"
                style="display: none"
              />
              <button @click="$refs.photoInput.click()" class="btn-secondary">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M9,2V8H11V11H5C3.89,11 3,11.89 3,13V19H1V21H23V19H21V13C21,11.89 20.11,11 19,11H13V8H15V2M11,4H13V6H11M9,13H11V19H9M13,13H15V19H13V13Z" />
                </svg>
                Change Photo
              </button>
              <button 
                v-if="profilePhoto" 
                @click="removePhoto" 
                class="btn-danger-outline"
              >
                Remove
              </button>
              <p class="photo-hint">JPG, PNG, GIF or WebP (Max 5MB)</p>
            </div>
          </div>

          <div class="form-section">
            <div class="form-group">
              <label for="fullName">Full Name</label>
              <input 
                type="text" 
                id="fullName"
                v-model="formData.fullName"
                placeholder="Enter your full name"
                class="form-input"
              />
            </div>

            <div class="form-group">
              <label for="email">Email Address</label>
              <input 
                type="email" 
                id="email"
                v-model="formData.email"
                placeholder="Enter your email"
                class="form-input"
                disabled
              />
              <p class="input-hint">Email cannot be changed</p>
            </div>

            <div class="form-group">
              <label for="grade">Grade Level</label>
              <select 
                id="grade"
                v-model="formData.grade"
                class="form-input"
              >
                <option :value="null">Select grade level</option>
                <option v-for="grade in [7, 8, 9, 10, 11, 12]" :key="grade" :value="grade">
                  Grade {{ grade }}
                </option>
              </select>
            </div>

            <div class="form-group">
              <label for="studentId">Student ID</label>
              <input 
                type="text" 
                id="studentId"
                :value="formData.studentId"
                class="form-input"
                disabled
              />
              <p class="input-hint">Student ID is auto-generated</p>
            </div>

            <!-- Error/Success Messages -->
            <div v-if="errorMessage" class="alert alert-error">
              {{ errorMessage }}
            </div>
            <div v-if="successMessage" class="alert alert-success">
              {{ successMessage }}
            </div>

            <div class="form-actions">
              <button 
                @click="saveProfile" 
                :disabled="isSaving"
                class="btn-primary"
              >
                <span v-if="isSaving">
                  <svg class="spinner" width="20" height="20" viewBox="0 0 24 24">
                    <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" fill="none" opacity="0.25"/>
                    <path fill="currentColor" d="M12 2a10 10 0 0 1 10 10h-4a6 6 0 0 0-6-6V2z" opacity="0.75"/>
                  </svg>
                  Saving...
                </span>
                <span v-else>
                  Save Changes
                </span>
              </button>
              <button @click="resetForm" class="btn-secondary">
                Reset
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Dark Mode Settings Card -->
      <div class="settings-card">
        <div class="card-header">
          <h2>Appearance</h2>
          <p>Customize how the app looks</p>
        </div>
        
        <div class="appearance-section">
          <div class="setting-item">
            <div class="setting-info">
              <h3>Dark Mode</h3>
              <p>Switch between light and dark theme</p>
            </div>
            <label class="toggle-switch">
              <input 
                type="checkbox" 
                v-model="isDarkMode"
                @change="toggleDarkMode"
              />
              <span class="toggle-slider"></span>
            </label>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { supabase } from '../../supabase.js';

export default {
  name: 'Settings',
  data() {
    return {
      formData: {
        fullName: '',
        email: '',
        grade: null,
        studentId: ''
      },
      profilePhoto: null,
      selectedFile: null,
      isDarkMode: false,
      isSaving: false,
      errorMessage: '',
      successMessage: '',
      currentUserId: null,
      currentProfileId: null
    };
  },
  async mounted() {
    await this.loadUserData();
    this.initializeDarkMode();
  },
  methods: {
    async loadUserData() {
      try {
        // Get current authenticated user
        const { data: { user }, error: authError } = await supabase.auth.getUser();
        
        if (authError || !user) {
          console.error('Auth error:', authError);
          return;
        }

        this.currentUserId = user.id;

        // Get profile data
        const { data: profile, error: profileError } = await supabase
          .from('profiles')
          .select('id, full_name, email, profile_photo')
          .eq('auth_user_id', user.id)
          .single();

        if (profileError) {
          console.error('Profile error:', profileError);
          return;
        }

        this.currentProfileId = profile.id;

        // Get student data
        const { data: studentData, error: studentError } = await supabase
          .from('students')
          .select('student_id, grade_level')
          .eq('profile_id', profile.id)
          .single();

        // Populate form data
        this.formData = {
          fullName: profile.full_name || '',
          email: profile.email || '',
          grade: studentData?.grade_level || null,
          studentId: studentData?.student_id || ''
        };

        this.profilePhoto = profile.profile_photo || null;

        console.log('User data loaded:', this.formData);

      } catch (error) {
        console.error('Error loading user data:', error);
        this.errorMessage = 'Failed to load user data';
      }
    },

    handlePhotoChange(event) {
      const file = event.target.files[0];
      if (!file) return;

      // Validate file type
      const validTypes = ['image/jpeg', 'image/png', 'image/gif', 'image/webp'];
      if (!validTypes.includes(file.type)) {
        this.errorMessage = 'Please select a valid image file (JPG, PNG, GIF, or WebP)';
        return;
      }

      // Validate file size (5MB max)
      const maxSize = 5 * 1024 * 1024; // 5MB in bytes
      if (file.size > maxSize) {
        this.errorMessage = 'File size must be less than 5MB';
        return;
      }

      this.selectedFile = file;
      
      // Preview the image
      const reader = new FileReader();
      reader.onload = (e) => {
        this.profilePhoto = e.target.result;
      };
      reader.readAsDataURL(file);

      this.errorMessage = '';
      console.log('Photo selected:', file.name);
    },

    async removePhoto() {
      this.selectedFile = null;
      this.profilePhoto = null;
      
      // Clear the file input
      if (this.$refs.photoInput) {
        this.$refs.photoInput.value = '';
      }
    },

    async uploadProfilePhoto() {
      if (!this.selectedFile) {
        return null; // No photo to upload
      }

      try {
        const fileExt = this.selectedFile.name.split('.').pop();
        const fileName = `${this.currentUserId}-${Date.now()}.${fileExt}`;
        const filePath = fileName;

        console.log('Uploading photo to storage:', filePath);

        // Upload file to Supabase storage
        const { data: uploadData, error: uploadError } = await supabase.storage
          .from('profile-photos')
          .upload(filePath, this.selectedFile, { 
            upsert: true,
            contentType: this.selectedFile.type
          });

        if (uploadError) {
          console.error('Upload error:', uploadError);
          throw uploadError;
        }

        console.log('Photo uploaded successfully:', uploadData);

        // Get public URL
        const { data: urlData } = supabase.storage
          .from('profile-photos')
          .getPublicUrl(filePath);

        console.log('Public URL:', urlData.publicUrl);
        return urlData.publicUrl;

      } catch (error) {
        console.error('Error uploading photo:', error);
        throw new Error('Failed to upload photo: ' + error.message);
      }
    },

    async saveProfile() {
      this.isSaving = true;
      this.errorMessage = '';
      this.successMessage = '';

      try {
        // Validate required fields
        if (!this.formData.fullName || !this.formData.fullName.trim()) {
          throw new Error('Full name is required');
        }

        let photoUrl = this.profilePhoto;

        // Upload photo only if a new file was selected
        if (this.selectedFile) {
          console.log('Uploading new profile photo...');
          photoUrl = await this.uploadProfilePhoto();
          console.log('Photo uploaded, URL:', photoUrl);
        }

        // Update profiles table
        console.log('Updating profile...');
        const { error: profileError } = await supabase
          .from('profiles')
          .update({
            full_name: this.formData.fullName.trim(),
            profile_photo: photoUrl,
            updated_at: new Date().toISOString()
          })
          .eq('id', this.currentProfileId);

        if (profileError) {
          console.error('Profile update error:', profileError);
          throw profileError;
        }

        console.log('Profile updated successfully');

        // Update students table
        console.log('Updating student data...');
        const { error: studentError } = await supabase
          .from('students')
          .update({
            full_name: this.formData.fullName.trim(),
            grade_level: this.formData.grade,
            updated_at: new Date().toISOString()
          })
          .eq('profile_id', this.currentProfileId);

        if (studentError) {
          console.error('Student update error:', studentError);
          throw studentError;
        }

        console.log('Student data updated successfully');

        // Clear selected file after successful save
        this.selectedFile = null;
        if (this.$refs.photoInput) {
          this.$refs.photoInput.value = '';
        }

        this.successMessage = 'Profile updated successfully!';
        
        // Emit event to notify dashboard
        window.dispatchEvent(new CustomEvent('profileUpdated'));

        // Clear success message after 3 seconds
        setTimeout(() => {
          this.successMessage = '';
        }, 3000);

      } catch (error) {
        console.error('Error saving profile:', error);
        this.errorMessage = error.message || 'Failed to save profile. Please try again.';
      } finally {
        this.isSaving = false;
      }
    },

    resetForm() {
      this.loadUserData();
      this.selectedFile = null;
      this.errorMessage = '';
      this.successMessage = '';
      
      // Clear the file input
      if (this.$refs.photoInput) {
        this.$refs.photoInput.value = '';
      }
    },

    initializeDarkMode() {
      const savedTheme = localStorage.getItem('darkMode');
      this.isDarkMode = savedTheme === 'true';
    },

    toggleDarkMode() {
      localStorage.setItem('darkMode', this.isDarkMode);
      if (this.isDarkMode) {
        document.documentElement.classList.add('dark');
      } else {
        document.documentElement.classList.remove('dark');
      }
    }
  }
};
</script>

<style scoped>
.settings-container {
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.settings-header {
  margin-bottom: 2rem;
}

.settings-header h1 {
  font-size: 2rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 0.5rem;
}

.settings-header p {
  color: var(--text-secondary);
  font-size: 1rem;
}

.settings-content {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.settings-card {
  background: var(--card-background);
  backdrop-filter: blur(20px);
  border-radius: 16px;
  padding: 2rem;
  border: 1px solid var(--border-color);
  box-shadow: 0 4px 16px var(--shadow-light);
}

.card-header {
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid var(--border-color);
}

.card-header h2 {
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--accent-color);
  margin-bottom: 0.5rem;
}

.card-header p {
  color: var(--text-secondary);
  font-size: 0.9rem;
}

.profile-section {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 2rem;
}

.profile-photo-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}

.current-photo {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  overflow: hidden;
  border: 4px solid var(--border-color);
  box-shadow: 0 4px 16px var(--shadow-medium);
}

.profile-photo {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.profile-photo-placeholder {
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #3D8D7A 0%, #5FB3A0 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.photo-actions {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  width: 100%;
}

.photo-hint {
  font-size: 0.75rem;
  color: var(--text-muted);
  text-align: center;
  margin-top: 0.5rem;
}

.form-section {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.form-group label {
  font-weight: 600;
  color: var(--text-primary);
  font-size: 0.9rem;
}

.form-input {
  padding: 0.75rem 1rem;
  border: 1px solid var(--border-color);
  border-radius: 8px;
  font-size: 1rem;
  background: var(--bg-accent);
  color: var(--text-primary);
  transition: all 0.3s ease;
}

.form-input:focus {
  outline: none;
  border-color: var(--accent-color);
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
}

.form-input:disabled {
  background: var(--bg-secondary);
  opacity: 0.6;
  cursor: not-allowed;
}

.input-hint {
  font-size: 0.75rem;
  color: var(--text-muted);
}

.alert {
  padding: 1rem;
  border-radius: 8px;
  font-size: 0.9rem;
}

.alert-error {
  background: rgba(239, 68, 68, 0.1);
  border: 1px solid rgba(239, 68, 68, 0.3);
  color: #dc2626;
}

.alert-success {
  background: rgba(34, 197, 94, 0.1);
  border: 1px solid rgba(34, 197, 94, 0.3);
  color: #16a34a;
}

.form-actions {
  display: flex;
  gap: 1rem;
  margin-top: 1rem;
}

.btn-primary,
.btn-secondary,
.btn-danger-outline {
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-weight: 600;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.3s ease;
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.btn-primary {
  background: var(--accent-color);
  color: white;
  flex: 1;
}

.btn-primary:hover:not(:disabled) {
  background: var(--accent-hover);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px var(--shadow-medium);
}

.btn-primary:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.btn-secondary {
  background: var(--bg-accent);
  color: var(--accent-color);
  border: 1px solid var(--border-color);
}

.btn-secondary:hover {
  background: var(--bg-accent-hover);
  border-color: var(--accent-color);
}

.btn-danger-outline {
  background: transparent;
  color: #dc2626;
  border: 1px solid #dc2626;
}

.btn-danger-outline:hover {
  background: rgba(239, 68, 68, 0.1);
}

.spinner {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.appearance-section {
  padding: 1rem 0;
}

.setting-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background: var(--bg-accent);
  border-radius: 12px;
  border: 1px solid var(--border-color);
}

.setting-info h3 {
  font-size: 1rem;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 0.25rem;
}

.setting-info p {
  font-size: 0.85rem;
  color: var(--text-secondary);
}

.toggle-switch {
  position: relative;
  display: inline-block;
  width: 50px;
  height: 26px;
}

.toggle-switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.toggle-slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: var(--border-color);
  transition: 0.4s;
  border-radius: 26px;
}

.toggle-slider:before {
  position: absolute;
  content: "";
  height: 20px;
  width: 20px;
  left: 3px;
  bottom: 3px;
  background-color: white;
  transition: 0.4s;
  border-radius: 50%;
}

input:checked + .toggle-slider {
  background-color: var(--accent-color);
}

input:checked + .toggle-slider:before {
  transform: translateX(24px);
}

@media (max-width: 768px) {
  .settings-container {
    padding: 1rem;
  }

  .profile-section {
    grid-template-columns: 1fr;
  }

  .form-actions {
    flex-direction: column;
  }

  .btn-primary,
  .btn-secondary {
    width: 100%;
  }
}
</style>