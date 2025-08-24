<template>
  <div v-if="isOpen" class="modal-overlay">
    <div class="modal-container">
      <div class="modal-header">
        <h2>Edit Profile</h2>
        <button @click="$emit('close')" class="close-btn">&times;</button>
      </div>
      <div class="modal-body">
        <div class="profile-pic-uploader">
          <div class="profile-pic-preview">
            <img v-if="previewUrl" :src="previewUrl" alt="Profile Preview" class="profile-pic" />
            <div v-else class="placeholder">
              <svg width="64" height="64" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12,4A4,4 0 0,1 16,8A4,4 0 0,1 12,12A4,4 0 0,1 8,8A4,4 0 0,1 12,4M12,14C16.42,14 20,15.79 20,18V20H4V18C4,15.79 7.58,14 12,14Z" />
              </svg>
            </div>
          </div>
          <input type="file" @change="handleFileChange" accept="image/*" class="file-input" ref="fileInput" />
          <button @click="openFilePicker" class="upload-btn">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M21.5 17.5l-2-2-4 4-2-2m-2-2l-4-4L2 12V22h20zM21.5 17.5l-2-2m-2-2l-4-4m-2-2l-4-4L2 12V22h20z"/>
              <circle cx="12" cy="7" r="4"/>
            </svg>
            Upload Photo
          </button>
        </div>

        <form @submit.prevent="saveProfile">
          <div class="form-group">
            <label for="fullName">Full Name</label>
            <input id="fullName" v-model="profileData.full_name" type="text" placeholder="Enter your full name" required />
          </div>
          <div class="form-group">
            <label for="bio">Bio</label>
            <textarea id="bio" v-model="profileData.bio" placeholder="Tell us about yourself..."></textarea>
          </div>
          
          <div class="modal-actions">
            <button type="button" @click="$emit('close')" class="cancel-btn">Cancel</button>
            <button type="submit" class="save-btn" :disabled="isLoading">
              <span v-if="isLoading">Saving...</span>
              <span v-else>Save Changes</span>
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, defineProps, defineEmits } from 'vue';
import { supabase } from '../supabase';
import { v4 as uuidv4 } from 'uuid';

const props = defineProps({
  isOpen: Boolean,
  initialData: Object,
  userId: String,
});

const emit = defineEmits(['close', 'profileUpdated']);

const profileData = ref({ ...props.initialData });
const file = ref(null);
const previewUrl = ref(props.initialData.avatar_url || '');
const isLoading = ref(false);
const fileInput = ref(null);

watch(() => props.isOpen, (newVal) => {
  if (newVal) {
    profileData.value = { ...props.initialData };
    previewUrl.value = props.initialData.avatar_url || '';
    file.value = null;
  }
}, { immediate: true });

const openFilePicker = () => {
  fileInput.value.click();
};

const handleFileChange = (e) => {
  const selectedFile = e.target.files[0];
  if (selectedFile) {
    file.value = selectedFile;
    previewUrl.value = URL.createObjectURL(selectedFile);
  }
};

const saveProfile = async () => {
  isLoading.value = true;
  try {
    let newAvatarUrl = profileData.value.avatar_url;

    if (file.value) {
      // 1. Upload new profile picture to Supabase Storage
      const fileExt = file.value.name.split('.').pop();
      const fileName = `${uuidv4()}.${fileExt}`;
      const filePath = `avatars/${fileName}`;
      
      const { error: uploadError } = await supabase.storage
        .from('avatars')
        .upload(filePath, file.value, {
          cacheControl: '3600',
          upsert: true,
        });

      if (uploadError) throw uploadError;

      // 2. Get public URL of the uploaded image
      const { data: publicUrlData } = supabase.storage
        .from('avatars')
        .getPublicUrl(filePath);

      newAvatarUrl = publicUrlData.publicUrl;
    }

    // 3. Update user profile in the 'profiles' table
    const updates = {
      full_name: profileData.value.full_name,
      bio: profileData.value.bio,
      avatar_url: newAvatarUrl,
      updated_at: new Date().toISOString(),
    };

    const { error: updateError } = await supabase
      .from('profiles')
      .update(updates)
      .eq('id', props.userId);

    if (updateError) throw updateError;
    
    // 4. Emit event to notify parent component of the update
    emit('profileUpdated', updates);
    emit('close');
    
  } catch (error) {
    console.error('Error saving profile:', error);
    alert('Failed to save profile. Please try again.');
  } finally {
    isLoading.value = false;
  }
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.4);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  animation: fadeIn 0.3s ease-out;
}

.modal-container {
  background: white;
  padding: 2rem;
  border-radius: 20px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
  width: 90%;
  max-width: 500px;
  max-height: 90vh;
  overflow-y: auto;
  transform: translateY(-20px);
  animation: slideIn 0.3s ease-out forwards;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
  border-bottom: 1px solid #eee;
  padding-bottom: 1rem;
}

.modal-header h2 {
  font-size: 1.8rem;
  font-weight: 700;
  color: #3D8D7A;
  margin: 0;
}

.close-btn {
  background: none;
  border: none;
  font-size: 2rem;
  font-weight: 300;
  color: #888;
  cursor: pointer;
  line-height: 1;
  transition: transform 0.2s ease;
}

.close-btn:hover {
  transform: rotate(90deg);
  color: #555;
}

.profile-pic-uploader {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 2rem;
}

.profile-pic-preview {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  overflow: hidden;
  background: #f0f0f0;
  border: 4px solid #3D8D7A;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1rem;
}

.profile-pic-preview img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.profile-pic-preview .placeholder {
  color: #999;
}

.file-input {
  display: none;
}

.upload-btn {
  background: #e0f0e8;
  color: #3D8D7A;
  border: 1px solid #3D8D7A;
  padding: 0.75rem 1.5rem;
  border-radius: 25px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.upload-btn:hover {
  background: #3D8D7A;
  color: white;
  box-shadow: 0 4px 15px rgba(61, 141, 122, 0.3);
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  font-size: 1rem;
  font-weight: 600;
  color: #555;
  margin-bottom: 0.5rem;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ccc;
  border-radius: 12px;
  font-family: 'Inter', sans-serif;
  font-size: 1rem;
  transition: border-color 0.3s;
}

.form-group input:focus,
.form-group textarea:focus {
  outline: none;
  border-color: #3D8D7A;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
}

.form-group textarea {
  resize: vertical;
  min-height: 100px;
}

.modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
  margin-top: 2rem;
}

.cancel-btn, .save-btn {
  padding: 0.75rem 1.5rem;
  border-radius: 15px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.cancel-btn {
  background: #f0f0f0;
  color: #555;
  border: 1px solid #ddd;
}

.cancel-btn:hover {
  background: #e0e0e0;
}

.save-btn {
  background: #3D8D7A;
  color: white;
  border: none;
}

.save-btn:hover:not(:disabled) {
  background: #2b7060;
}

.save-btn:disabled {
  background: #ccc;
  cursor: not-allowed;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes slideIn {
  from { transform: translateY(-20px) scale(0.95); opacity: 0; }
  to { transform: translateY(0) scale(1); opacity: 1; }
}
</style>