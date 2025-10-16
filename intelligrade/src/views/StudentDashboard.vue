<template>
  <div class="dashboard-container">
    <aside class="sidebar">
      <div class="user-info">
        <div class="profile-pic-container">
          <div class="profile-pic-placeholder" :style="{ background: currentAvatar.color }">
  <span class="avatar-emoji">{{ currentAvatar.emoji }}</span>
</div>
        </div>
        <div class="user-details">
          <!-- Fixed: Better loading and fallback states -->
          <h3 v-if="isLoading" class="loading-text">
            <span class="loading-spinner"></span>
            Loading...
          </h3>
          <h3 v-else-if="userProfile.fullName" class="user-name">
            {{ userProfile.fullName }}
          </h3>
          <h3 v-else class="no-name-text">
            Name not available
          </h3>
          
          <p class="role">STUDENT</p>
          
          <!-- Fixed: Better grade display -->
          <p v-if="!isLoading && userProfile.grade" class="grade">
            GRADE {{ userProfile.grade }}
          </p>
          <p v-else-if="!isLoading" class="grade grade-missing">
            GRADE NOT SET
          </p>
          <div v-else class="grade-skeleton"></div>
          
          <!-- Fixed: Better student ID display -->
          <p v-if="!isLoading && userProfile.studentId" class="student-id">
            STUDENT ID: {{ userProfile.studentId }}
          </p>
          <p v-else-if="!isLoading" class="student-id student-id-missing">
            STUDENT ID: NOT SET
          </p>
          <div v-else class="student-id-skeleton"></div>
        </div>
      </div>

      <nav class="nav-links">
        <a
          href="#"
          @click.prevent="navigateTo('home')"
          :class="['nav-item', { 'is-active': currentView === 'home' }]"
        >
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M10,20V14H14V20H19V12H22L12,3L2,12H5V20H10Z" />
          </svg>
          <span>Home</span>
        </a>
        <a
          href="#"
          @click.prevent="navigateTo('subjects')"
          :class="['nav-item', { 'is-active': currentView === 'subjects' }]"
        >
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M3,5.5V18.5A2.5,2.5 0 0,0 5.5,21A2.5,2.5 0 0,0 8,18.5V5.5A2.5,2.5 0 0,0 5.5,3A2.5,2.5 0 0,0 3,5.5M12,5.5V18.5A2.5,2.5 0 0,0 14.5,21A2.5,2.5 0 0,0 17,18.5V5.5A2.5,2.5 0 0,0 14.5,3A2.5,2.5 0 0,0 12,5.5M21,5.5V18.5A2.5,2.5 0 0,0 23.5,21A2.5,2.5 0 0,0 26,18.5V5.5A2.5,2.5 0 0,0 23.5,3A2.5,2.5 0 0,0 21,5.5Z" />
          </svg>
          <span>Subjects</span>
        </a>
        <a
          href="#"
          @click.prevent="navigateTo('calendar')"
          :class="['nav-item', { 'is-active': currentView === 'calendar' }]"
        >
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M19,19H5V8H19M19,3H18V1H16V3H8V1H6V3H5C3.89,3 3,3.89 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5C21,3.89 20.1,3 19,3M16.5,13.5H11V18.5H16.5V13.5Z" />
          </svg>
          <span>Calendar</span>
        </a>
        <a
          href="#"
          @click.prevent="navigateTo('messages')"
          :class="['nav-item', { 'is-active': currentView === 'messages' }]"
        >
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" class="messages-icon">
            <path d="M22 6c0-1.1-.9-2-2-2H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6zM4 6h16v.5l-8 5-8-5V6zm0 13.5V8l8 5 8-5v11.5H4z"/>
          </svg>
          <span>Messages</span>
        </a>
        <a
          href="#"
          @click.prevent="navigateTo('settings')"
          :class="['nav-item', { 'is-active': currentView === 'settings' }]"
        >
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12,15.5A3.5,3.5 0 0,1 8.5,12A3.5,3.5 0 0,1 12,8.5A3.5,3.5 0 0,1 15.5,12A3.5,3.5 0 0,1 12,15.5M19.43,12.97C19.47,12.65 19.5,12.33 19.5,12C19.5,11.67 19.47,11.34 19.43,11.03L21.54,9.37C21.73,9.22 21.78,8.95 21.67,8.75L19.67,5.27C19.56,5.08 19.3,5.03 19.1,5.12L16.9,6C16.5,5.65 16.08,5.36 15.61,5.1L15.2,2.83C15.15,2.56 14.9,2.33 14.62,2.33L9.38,2.33C9.1,2.33 8.85,2.56 8.8,2.83L8.39,5.09C7.92,5.34 7.5,5.65 7.1,6L4.9,5.12C4.7,5.03 4.44,5.08 4.33,5.27L2.33,8.75C2.22,8.95 2.27,9.22 2.46,9.37L4.57,11.03C4.53,11.34 4.5,11.67 4.5,12C4.5,12.33 4.53,12.65 4.57,12.97L2.46,14.63C2.27,14.78 2.22,15.05 2.33,15.25L4.33,18.73C4.44,18.92 4.7,18.97 4.9,18.88L7.1,18C7.5,18.35 7.92,18.64 8.39,18.9L8.8,21.17C8.85,21.44 9.1,21.67 9.38,21.67L14.62,21.67C14.9,21.67 15.15,21.44 15.2,21.17L15.61,18.91C16.08,18.66 16.5,18.35 16.9,18L19.1,18.88C19.3,18.97 19.56,18.92 19.67,18.73L21.67,15.25C21.78,15.05 21.73,14.78 21.54,14.63L19.43,12.97Z" />
          </svg>
          <span>Settings</span>
        </a>
      </nav>

      <button @click="showLogoutModal" class="logout-btn">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
          <path d="M16,17V14H9V10H16V7L21,12L16,17M14,2A2,2 0 0,1 16,4V6H14V4H5V20H14V18H16V20A2,2 0 0,1 14,22H5A2,2 0 0,1 3,20V4A2,2 0 0,1 5,2H14Z" />
        </svg>
        <span>Logout</span>
      </button>
    </aside>

    <main class="main-content">
      <component :is="currentComponent" />
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


<script>
import Home from './student/Home.vue';
import Subjects from './student/Subjects.vue';
import Calendar from './student/Calendar.vue';
import Messages from './student/Messages.vue';
import Settings from './student/Settings.vue';
import { supabase } from '../supabase.js';

export default {
  name: 'StudentDashboard',
  data() {
    return {
      userProfile: {
        fullName: null,
        studentId: null,
        grade: null,
        email: null,
        role: null,
        avatar: '1' // Default avatar
      },
      avatarOptions: [
        { id: '1', emoji: '😊', color: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)' },
        { id: '2', emoji: '🎓', color: 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)' },
        { id: '3', emoji: '📚', color: 'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)' },
        { id: '4', emoji: '✨', color: 'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)' },
        { id: '5', emoji: '🚀', color: 'linear-gradient(135deg, #fa709a 0%, #fee140 100%)' },
        { id: '6', emoji: '🎨', color: 'linear-gradient(135deg, #30cfd0 0%, #330867 100%)' },
        { id: '7', emoji: '🌟', color: 'linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)' },
        { id: '8', emoji: '💡', color: 'linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%)' },
        { id: '9', emoji: '🎯', color: 'linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%)' },
        { id: '10', emoji: '🏆', color: 'linear-gradient(135deg, #fbc2eb 0%, #a6c1ee 100%)' },
        { id: '11', emoji: '🎵', color: 'linear-gradient(135deg, #fdcbf1 0%, #e6dee9 100%)' },
        { id: '12', emoji: '🌈', color: 'linear-gradient(135deg, #a1c4fd 0%, #c2e9fb 100%)' }
      ],
      currentView: 'home',
      isLogoutModalVisible: false,
      isLoading: true,
      profileSubscription: null,
      retryCount: 0,
      maxRetries: 3
    };
  },
  computed: {
    currentComponent() {
      switch (this.currentView) {
        case 'home':
          return Home;
        case 'subjects':
          return Subjects;
        case 'calendar':
          return Calendar;
        case 'messages':
          return Messages;
        case 'settings':
          return Settings;
        default:
          return Home;
      }
    },
    currentAvatar() {
      const avatar = this.avatarOptions.find(a => a.id === this.userProfile.avatar);
      return avatar || this.avatarOptions[0];
    }
  },
  async mounted() {
    await this.loadUserProfile();
    this.setupProfileSubscription();
    this.initializeDarkMode();
    
    // Listen for profile updates from Settings component
    window.addEventListener('profileUpdated', this.handleProfileUpdate);
  },
  beforeUnmount() {
    if (this.profileSubscription) {
      this.profileSubscription.unsubscribe();
    }
    window.removeEventListener('profileUpdated', this.handleProfileUpdate);
  },
  methods: {
    async loadUserProfile() {
      try {
        this.isLoading = true;
        
        // Get the current user from Supabase auth
        const { data: { user }, error: authError } = await supabase.auth.getUser();
        console.log('Current user:', user);
        
        if (authError || !user) {
          console.error('Auth error:', authError);
          this.handleAuthError();
          return;
        }

        // Fetch student profile using the new database structure
        await this.fetchStudentProfile(user.id);
        
        // Load avatar from localStorage
        const savedAvatar = localStorage.getItem('userAvatar');
        if (savedAvatar) {
          this.userProfile.avatar = savedAvatar;
          console.log('Loaded avatar from localStorage:', savedAvatar);
        }

      } catch (error) {
        console.error('Error loading user profile:', error);
        this.handleProfileError();
      } finally {
        this.isLoading = false;
      }
    },

    async fetchStudentProfile(userId) {
      try {
        console.log(`Fetching student profile for user ID: ${userId}`);
        
        // First, get profile data and verify role
        const { data: profile, error: profileError } = await supabase
          .from('profiles')
          .select('id, full_name, email, role')
          .eq('auth_user_id', userId)
          .single();

        console.log('Profile data:', profile);
        console.log('Profile error:', profileError);

        if (profileError) {
          if (profileError.code === 'PGRST116') {
            console.warn('No profile found for user');
            await this.handleMissingStudentRecord(userId);
            return;
          }
          throw profileError;
        }

        // Verify user is a student
        if (profile.role !== 'student') {
          console.warn('Access denied: User is not a student');
          this.$router.push('/login');
          return;
        }

        console.log('Profile data from DB:', profile);

        // Now fetch student-specific data with better error handling
        const { data: studentData, error: studentError } = await supabase
          .from('students')
          .select('student_id, grade_level, full_name, email')
          .eq('profile_id', profile.id)
          .single();

        console.log('Student data query result:', { studentData, studentError });

        if (studentError) {
          console.warn('Student data fetch error:', studentError);
          
          // Check if it's a missing record (no rows returned)
          if (studentError.code === 'PGRST116') {
            console.log('No student record found, creating one...');
            await this.createMissingStudentRecord(profile);
            return;
          }
          
          // For other errors, use profile data as fallback with generated student ID
          const tempStudentId = await this.generateStudentId(profile.id);
          this.userProfile = {
            fullName: profile.full_name || 'Student',
            email: profile.email || '',
            studentId: tempStudentId,
            grade: null,
            role: profile.role,
            avatar: this.userProfile.avatar
          };
          return;
        }

        console.log('Student data from DB:', studentData);
        
        // Check if student_id is missing and generate one if needed
        let finalStudentId = studentData.student_id;
        if (!finalStudentId) {
          console.log('Student ID missing, generating new one...');
          finalStudentId = await this.generateStudentId(profile.id);
          await this.updateStudentId(profile.id, finalStudentId);
        }
        
        // Combine profile and student data - ensure student_id is always visible
        this.userProfile = {
          fullName: studentData.full_name || profile.full_name || 'Student',
          email: studentData.email || profile.email || '',
          studentId: finalStudentId,
          grade: studentData.grade_level || null,
          role: profile.role,
          avatar: this.userProfile.avatar
        };
        
        console.log('Final profile data set:', this.userProfile);

      } catch (error) {
        console.error('Error fetching student profile:', error);
        throw error;
      }
    },

    async generateStudentId(profileId) {
      try {
        // Generate a student ID using current year + last 6 chars of profile ID + random 2 digits
        const year = new Date().getFullYear();
        const shortId = profileId.slice(-6).toUpperCase();
        const random = Math.floor(Math.random() * 99).toString().padStart(2, '0');
        const studentId = `${year}${shortId}${random}`;
        
        // Check if this ID already exists, if so, generate a new one
        const { data: existingStudent } = await supabase
          .from('students')
          .select('student_id')
          .eq('student_id', studentId)
          .single();
        
        if (existingStudent) {
          // If ID exists, recursively generate a new one
          return await this.generateStudentId(profileId);
        }
        
        console.log('Generated student ID:', studentId);
        return studentId;
      } catch (error) {
        console.error('Error generating student ID:', error);
        // Fallback to a simpler format if there's an error
        return `ST${Date.now().toString().slice(-8)}`;
      }
    },

    async createMissingStudentRecord(profile) {
      try {
        console.log('Creating missing student record for profile:', profile.id);
        
        const newStudentId = await this.generateStudentId(profile.id);
        const defaultGrade = 7; // Default to grade 7, user can update later
        
        const { data, error } = await supabase
          .from('students')
          .insert([{
            profile_id: profile.id,
            student_id: newStudentId,
            full_name: profile.full_name,
            email: profile.email,
            grade_level: defaultGrade,
            is_active: true
          }])
          .select()
          .single();

        if (error) {
          console.error('Error creating student record:', error);
          // Use fallback data even if creation fails
          this.userProfile = {
            fullName: profile.full_name || 'Student',
            email: profile.email || '',
            studentId: newStudentId,
            grade: defaultGrade,
            role: profile.role,
            avatar: this.userProfile.avatar
          };
          return;
        }

        console.log('Created student record:', data);
        
        // Update the user profile with the new data
        this.userProfile = {
          fullName: data.full_name,
          email: data.email,
          studentId: data.student_id,
          grade: data.grade_level,
          role: profile.role,
          avatar: this.userProfile.avatar
        };
        
      } catch (error) {
        console.error('Error in createMissingStudentRecord:', error);
        // Ensure we still set a profile even if record creation fails
        const tempStudentId = await this.generateStudentId(profile.id);
        this.userProfile = {
          fullName: profile.full_name || 'Student',
          email: profile.email || '',
          studentId: tempStudentId,
          grade: null,
          role: profile.role,
          avatar: this.userProfile.avatar
        };
      }
    },

    async updateStudentId(profileId, studentId) {
      try {
        const { error } = await supabase
          .from('students')
          .update({ student_id: studentId })
          .eq('profile_id', profileId);

        if (error) {
          console.error('Error updating student ID:', error);
        } else {
          console.log('Student ID updated successfully:', studentId);
        }
      } catch (error) {
        console.error('Error in updateStudentId:', error);
      }
    },

    async handleMissingStudentRecord(userId) {
      try {
        // Get user email from auth
        const { data: { user } } = await supabase.auth.getUser();
        
        // Create a temporary student ID
        const tempStudentId = await this.generateStudentId(userId);
        
        this.userProfile = {
          fullName: user?.user_metadata?.full_name || user?.email?.split('@')[0] || 'Student',
          email: user?.email || '',
          studentId: tempStudentId,
          grade: null,
          role: 'student',
          avatar: this.userProfile.avatar
        };
        
        console.log('Using fallback profile with temp ID:', this.userProfile);
        
      } catch (error) {
        console.error('Error handling missing student record:', error);
        this.handleProfileError();
      }
    },

    handleAuthError() {
      this.userProfile = {
        fullName: 'Authentication Error',
        email: '',
        studentId: 'AUTH_ERROR',
        grade: null,
        role: null,
        avatar: '1'
      };
      setTimeout(() => {
        this.$router.push('/login');
      }, 2000);
    },

    handleProfileError() {
      this.userProfile = {
        fullName: 'Profile Load Error',
        email: 'Error loading data',
        studentId: 'ERROR_LOADING',
        grade: null,
        role: null,
        avatar: '1'
      };
    },

    handleProfileUpdate() {
      console.log('Profile update event received, reloading profile...');
      this.loadUserProfile();
    },

    setupProfileSubscription() {
      supabase.auth.getUser().then(({ data: { user } }) => {
        if (user) {
          console.log('Setting up profile subscription...');
          
          // Subscribe to profiles table changes
          const profilesSubscription = supabase
            .channel('profile_changes')
            .on(
              'postgres_changes',
              {
                event: '*',
                schema: 'public',
                table: 'profiles',
                filter: `auth_user_id=eq.${user.id}`
              },
              (payload) => {
                console.log('Profile updated via subscription:', payload);
                if (payload.new) {
                  this.loadUserProfile(); // Reload full profile data
                }
              }
            )
            .subscribe();

          // Subscribe to students table changes
          const studentsSubscription = supabase
            .channel('student_changes')
            .on(
              'postgres_changes',
              {
                event: '*',
                schema: 'public',
                table: 'students'
              },
              (payload) => {
                console.log('Student data updated via subscription:', payload);
                this.loadUserProfile(); // Reload full profile data
              }
            )
            .subscribe();

          this.profileSubscription = {
            unsubscribe: () => {
              profilesSubscription.unsubscribe();
              studentsSubscription.unsubscribe();
            }
          };
        }
      });
    },

    navigateTo(view) {
      this.currentView = view;
    },

    initializeDarkMode() {
      const savedTheme = localStorage.getItem('darkMode');
      if (savedTheme === 'true') {
        document.documentElement.classList.add('dark');
      } else {
        document.documentElement.classList.remove('dark');
      }
    },

    showLogoutModal() {
      this.isLogoutModalVisible = true;
    },

    hideLogoutModal() {
      this.isLogoutModalVisible = false;
    },

    async confirmLogout() {
      this.isLogoutModalVisible = false;
      
      try {
        if (this.profileSubscription) {
          this.profileSubscription.unsubscribe();
        }
        
        const { error } = await supabase.auth.signOut();
        if (error) {
          console.error('Logout error:', error);
        }
        
        localStorage.removeItem('userProfile');
        localStorage.removeItem('darkMode');
        localStorage.removeItem('userAvatar');
        
        console.log('User logged out');
        this.$router.push('/');
      } catch (error) {
        console.error('Error during logout:', error);
        this.$router.push('/');
      }
    },
  },
};
</script>

<style scoped>
/*
 * Imported fonts
 */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/*
 * Student Dashboard Styles - Enhanced with better loading states
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

.sidebar {
  width: 280px;
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

.profile-pic-placeholder svg {
  width: 32px;
  height: 32px;
}

.user-details {
  width: 100%;
}

.user-info h3 {
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--accent-color);
  margin-bottom: 0.5rem;
  word-break: break-word;
  line-height: 1.2;
  min-height: 1.5rem;
}

.user-name {
  color: var(--accent-color);
  font-weight: 700;
}

.loading-text {
  color: var(--text-secondary);
  opacity: 0.7;
  font-style: italic;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.loading-spinner {
  width: 16px;
  height: 16px;
  border: 2px solid var(--border-color);
  border-top: 2px solid var(--accent-color);
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.no-name-text {
  color: var(--text-muted);
  opacity: 0.6;
  font-style: italic;
  font-weight: 500;
}

.user-info .role {
  font-size: 0.75rem;
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

.user-info .grade {
  font-size: 0.75rem;
  color: var(--accent-color);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 0.5rem;
  word-break: break-word;
  min-height: 1rem;
}

.grade-missing {
  color: var(--text-muted) !important;
  opacity: 0.7;
  font-style: italic;
}

.grade-skeleton,
.student-id-skeleton {
  height: 1rem;
  background: var(--border-color);
  border-radius: 4px;
  margin-bottom: 0.5rem;
  animation: pulse 1.5s ease-in-out infinite;
}

.student-id-skeleton {
  height: 0.8rem;
  width: 80%;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

.user-info .student-id {
  font-size: 0.7rem;
  color: var(--text-secondary);
  font-weight: 500;
  margin-bottom: 0;
  opacity: 0.8;
  word-break: break-word;
  text-transform: uppercase;
  letter-spacing: 0.3px;
  min-height: 0.8rem;
}

.student-id-missing {
  color: var(--text-muted) !important;
  opacity: 0.6;
  font-style: italic;
}

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
  font-size: 0.85rem;
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

.nav-item.is-active {
  background: rgba(95, 179, 160, 0.12);
  border-color: rgba(95, 179, 160, 0.3);
  box-shadow: 0 2px 8px rgba(95, 179, 160, 0.1);
  color: var(--accent-color);
  transform: none;
}

.nav-item.is-active svg {
  fill: var(--accent-color);
}

.nav-item.is-active span {
  color: var(--accent-color);
  font-weight: 600;
}

:root.dark .nav-item.is-active {
  background: rgba(95, 179, 160, 0.15);
  border-color: rgba(95, 179, 160, 0.35);
  box-shadow: 0 2px 8px rgba(95, 179, 160, 0.15);
}

.logout-btn {
  display: flex;
  align-items: center;
  padding: 0.75rem 1rem;
  border-radius: 12px;
  color: var(--text-inverse);
  text-decoration: none;
  font-weight: 600;
  font-size: 0.85rem;
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
  border-radius: 24px;
  padding: 2.5rem;
  max-width: 450px;
  width: 90%;
  box-shadow: 
    0 20px 60px rgba(61, 141, 122, 0.3),
    0 0 0 1px rgba(255, 255, 255, 0.2);
  border: 1px solid rgba(61, 141, 122, 0.1);
  animation: modalSlideIn 0.3s ease-out;
  text-align: center;
}

:root.dark .modal-container {
  background: rgba(30, 35, 34, 0.95);
  border: 1px solid rgba(95, 179, 160, 0.2);
  box-shadow: 
    0 20px 60px rgba(0, 0, 0, 0.4),
    0 0 0 1px rgba(95, 179, 160, 0.1);
}

.modal-header {
  margin-bottom: 2rem;
}

.modal-icon {
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 1.5rem;
  color: white;
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.3);
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
  border-color: rgba(61, 141, 122, 0.3);
  transform: none;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.08);
}

.btn-confirm {
  background: var(--accent-color);
  color: var(--text-inverse);
  box-shadow: 0 2px 8px var(--shadow-medium);
}

.btn-confirm:hover {
  background: var(--accent-hover);
  color: var(--text-inverse);
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.15);
  transform: none;
}

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

:root.dark .modal-title {
  color: var(--text-primary);
}

:root.dark .modal-message {
  color: var(--text-secondary);
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
  
  .profile-pic-placeholder {
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
  
  .user-info .grade {
    font-size: 0.7rem;
    margin-bottom: 0.25rem;
  }
  
  .user-info .student-id {
    font-size: 0.65rem;
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
  
  .profile-pic-placeholder {
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
  
  .user-info .role {
    font-size: 0.7rem;
    padding: 0.15rem 0.4rem;
  }
  
  .user-info .grade {
    font-size: 0.65rem;
  }
  
  .user-info .student-id {
    font-size: 0.6rem;
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
/* Global styles - same as teacher dashboard */
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
  --bg-primary: #fefefe;
  --bg-secondary: #f8faf9;
  --bg-accent: rgba(251, 255, 228, 0.6);
  --bg-accent-hover: rgba(251, 255, 228, 0.8);
  
  --card-background: rgba(255, 255, 255, 0.8);
  --card-background-hover: rgba(255, 255, 255, 0.9);
  
  --accent-color: #3D8D7A;
  --accent-hover: #2A6B5B;
  --accent-light: #5FB3A0;
  --accent-lighter: #A3D1C6;
  
  --text-primary: #1a1a1a;
  --text-secondary: #4a4a4a;
  --text-muted: #7a7a7a;
  --text-inverse: #ffffff;
  
  --border-color: rgba(61, 141, 122, 0.12);
  --border-hover: rgba(61, 141, 122, 0.2);
  
  --shadow-light: rgba(61, 141, 122, 0.05);
  --shadow-medium: rgba(61, 141, 122, 0.1);
  --shadow-strong: rgba(61, 141, 122, 0.2);
}

/* Dark mode colors */
:root.dark {
  --bg-primary: #0f1211;
  --bg-secondary: #1a1f1e;
  --bg-accent: rgba(30, 35, 34, 0.6);
  --bg-accent-hover: rgba(30, 35, 34, 0.8);
  
  --card-background: rgba(30, 35, 34, 0.8);
  --card-background-hover: rgba(30, 35, 34, 0.9);
  
  --accent-color: #5FB3A0;
  --accent-hover: #4A9085;
  --accent-light: #7BC4B5;
  --accent-lighter: #A3D1C6;
  
  --text-primary: #f0f0f0;
  --text-secondary: #c0c0c0;
  --text-muted: #909090;
  --text-inverse: #ffffff;
  
  --border-color: rgba(95, 179, 160, 0.15);
  --border-hover: rgba(95, 179, 160, 0.25);
  
  --shadow-light: rgba(0, 0, 0, 0.1);
  --shadow-medium: rgba(0, 0, 0, 0.2);
  --shadow-strong: rgba(0, 0, 0, 0.3);
}

.avatar-emoji {
  font-size: 32px;
}
</style>