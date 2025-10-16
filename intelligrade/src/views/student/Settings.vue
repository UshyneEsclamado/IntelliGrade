<template>
  <div class="page-container">
    <div class="main-wrapper">

      <!-- Header Section -->
      <div class="section-header-card">
        <div class="section-header-left">
          <div class="section-header-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M12,15.5A3.5,3.5 0 0,1 8.5,12A3.5,3.5 0 0,1 12,8.5A3.5,3.5 0 0,1 15.5,12A3.5,3.5 0 0,1 12,15.5M19.43,12.97C19.47,12.65 19.5,12.33 19.5,12C19.5,11.67 19.47,11.34 19.43,11.03L21.54,9.37C21.73,9.22 21.78,8.95 21.67,8.75L19.67,5.27C19.56,5.08 19.3,5.03 19.1,5.12L16.9,6C16.5,5.65 16.08,5.36 15.61,5.1L15.2,2.83C15.15,2.56 14.9,2.33 14.62,2.33L9.38,2.33C9.1,2.33 8.85,2.56 8.8,2.83L8.39,5.09C7.92,5.34 7.5,5.65 7.1,6L4.9,5.12C4.7,5.03 4.44,5.08 4.33,5.27L2.33,8.75C2.22,8.95 2.27,9.22 2.46,9.37L4.57,11.03C4.53,11.34 4.5,11.67 4.5,12C4.5,12.33 4.53,12.65 4.57,12.97L2.46,14.63C2.27,14.78 2.22,15.05 2.33,15.25L4.33,18.73C4.44,18.92 4.7,18.97 4.9,18.88L7.1,18C7.5,18.35 7.92,18.64 8.39,18.9L8.8,21.17C8.85,21.44 9.1,21.67 9.38,21.67L14.62,21.67C14.9,21.67 15.15,21.44 15.2,21.17L15.61,18.91C16.08,18.66 16.5,18.35 16.9,18L19.1,18.88C19.3,18.97 19.56,18.92 19.67,18.73L21.67,15.25C21.78,15.05 21.73,14.78 21.54,14.63L19.43,12.97Z" />
            </svg>
          </div>
          <div>
            <div class="section-header-title">Settings</div>
            <div class="section-header-sub">Manage your account, profile, and app preferences.</div>
          </div>
        </div>
      </div>
      
      <!-- Settings Grid -->
      <section class="settings-grid">
        <!-- Account & Profile Card -->
        <div class="card-box settings-card">
          <h2>
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="section-icon">
              <path d="M12,4A4,4 0 0,1 16,8A4,4 0 0,1 12,12A4,4 0 0,1 8,8A4,4 0 0,1 12,4M12,14C16.42,14 20,15.79 20,18V20H4V18C4,15.79 7.58,14 12,14Z" />
            </svg> 
            Account & Profile
          </h2>
          <p class="section-subtitle">Update your personal information and profile settings.</p>
          <ul class="settings-list">
            <li>
              <div class="setting-item">
                <span>Update Profile Info</span>
                <button @click="openProfileModal" class="action-btn">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/>
                  </svg>
                </button>
              </div>
            </li>
            <li>
              <div class="setting-item">
                <span>Change Password</span>
                <button @click="openPasswordModal" class="action-btn">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                    <circle cx="12" cy="16" r="1"></circle>
                    <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                  </svg>
                </button>
              </div>
            </li>
          </ul>
        </div>
        
        <!-- App Preferences Card -->
        <div class="card-box settings-card">
          <h2>
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="section-icon">
              <path d="M17 3a2.85 2.85 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"/>
            </svg> 
            App Preferences
          </h2>
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

        <!-- Privacy & Legal Card -->
        <div class="card-box settings-card">
          <h2>
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="section-icon">
              <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
            </svg> 
            Privacy & Legal
          </h2>
          <p class="section-subtitle">Understand our policies and manage your data.</p>
          <ul class="settings-list">
            <li>
              <div class="setting-item">
                <span>Privacy Policy</span>
                <button @click="openPrivacyPolicy" class="action-btn">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" />
                    <polyline points="14 2 14 8 20 8" />
                    <line x1="16" y1="13" x2="8" y2="13" />
                    <line x1="16" y1="17" x2="8" y2="17" />
                    <polyline points="10 9 9 9 8 9" />
                  </svg>
                </button>
              </div>
            </li>
            <li>
              <div class="setting-item">
                <span>Terms of Service</span>
                <button @click="openTermsOfService" class="action-btn">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" />
                    <polyline points="14 2 14 8 20 8" />
                    <line x1="16" y1="13" x2="8" y2="13" />
                    <line x1="16" y1="17" x2="8" y2="17" />
                    <polyline points="10 9 9 9 8 9" />
                  </svg>
                </button>
              </div>
            </li>
          </ul>
        </div>

        <!-- Danger Zone Card -->
        <div class="card-box settings-card danger-zone">
          <h2>
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="section-icon">
              <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/>
              <line x1="12" y1="9" x2="12" y2="13"/>
              <line x1="12" y1="17" x2="12.01" y2="17"/>
            </svg> 
            Danger Zone
          </h2>
          <p class="section-subtitle">Sensitive actions that cannot be undone.</p>
          <ul class="settings-list">
            <li>
              <div class="setting-item">
                <span class="danger-text">Delete Account</span>
                <button @click="confirmDeleteAccount" class="action-btn danger-btn">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M3 6l3 0l0 15a2 2 0 0 0 2 2l8 0a2 2 0 0 0 2 -2l0 -15l3 0"/>
                    <path d="M14 10l0 5"/>
                    <path d="M10 10l0 5"/>
                    <path d="M18 6l-12 0"/>
                    <path d="M10 3l4 0l0 3l-4 0l0 -3z"/>
                  </svg>
                </button>
              </div>
            </li>
          </ul>
        </div>
      </section>
      
      <!-- About Section -->
      <section class="about-section">
        <div class="about-card card-box">
          <h2>IntelliGrade</h2>
          <p class="copyright-text">© 2025 IntelliGrade. All Rights Reserved.</p>
        </div>
      </section>
    </div>
  </div>

  <!-- Profile Update Modal -->
  <div v-if="showProfileModal" class="modal-overlay" @click="closeProfileModal">
    <div class="modal-content" @click.stop>
      <div class="modal-header">
        <h3>Update Profile</h3>
        <button @click="closeProfileModal" class="close-btn">×</button>
      </div>
      <div class="modal-body">
        <!-- Avatar Selection Section -->
        <div class="form-group">
          <label>Choose Avatar</label>
          <div class="avatar-grid">
            <div 
              v-for="avatar in avatarOptions" 
              :key="avatar.id"
              @click="selectAvatar(avatar.id)"
              :class="['avatar-option', { 'selected': profileData.avatar === avatar.id }]"
            >
              <div class="avatar-icon" :style="{ background: avatar.color }">
                {{ avatar.emoji }}
              </div>
            </div>
          </div>
        </div>
        
        <!-- Full Name Section -->
        <div class="form-group">
          <label>Full Name</label>
          <input 
            type="text" 
            v-model="profileData.full_name" 
            placeholder="Enter your full name"
            class="form-input"
          >
        </div>
        
        <!-- Error/Success Messages -->
        <div v-if="profileError" class="error-message">{{ profileError }}</div>
        <div v-if="profileSuccess" class="success-message">{{ profileSuccess }}</div>
      </div>
      <div class="modal-footer">
        <button @click="closeProfileModal" class="btn-secondary">Cancel</button>
        <button @click="saveProfile" class="btn-primary" :disabled="isSaving">
          {{ isSaving ? 'Saving...' : 'Save Profile' }}
        </button>
      </div>
    </div>
  </div>

  <!-- Password Change Modal -->
  <div v-if="showPasswordModal" class="modal-overlay" @click="closePasswordModal">
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
            v-model="passwordData.currentPassword" 
            placeholder="Enter current password"
            class="form-input"
          >
        </div>
        <div class="form-group">
          <label>New Password</label>
          <input 
            type="password" 
            v-model="passwordData.newPassword" 
            placeholder="Enter new password (min 6 characters)"
            class="form-input"
          >
        </div>
        <div class="form-group">
          <label>Confirm New Password</label>
          <input 
            type="password" 
            v-model="passwordData.confirmPassword" 
            placeholder="Confirm new password"
            class="form-input"
          >
        </div>
        
        <!-- Error/Success Messages -->
        <div v-if="passwordError" class="error-message">{{ passwordError }}</div>
        <div v-if="passwordSuccess" class="success-message">{{ passwordSuccess }}</div>
      </div>
      <div class="modal-footer">
        <button @click="closePasswordModal" class="btn-secondary">Cancel</button>
        <button @click="changePassword" class="btn-primary" :disabled="isChangingPassword">
          {{ isChangingPassword ? 'Updating...' : 'Update Password' }}
        </button>
      </div>
    </div>
  </div>

  <!-- Privacy Policy Modal -->
  <div v-if="showPrivacyModal" class="modal-overlay" @click="closePrivacyModal">
    <div class="modal-content document-modal" @click.stop>
      <div class="modal-header">
        <h3>Privacy Policy</h3>
        <button @click="closePrivacyModal" class="close-btn">×</button>
      </div>
      <div class="modal-body document-body">
        <div class="document-content">
          <h4>IntelliGrade Privacy Policy</h4>
          <p class="document-date">Last Updated: January 2025</p>
          
          <section>
            <h5>1. Information We Collect</h5>
            <p>We collect information that you provide directly to us, including:</p>
            <ul>
              <li>Account information (name, email, student ID)</li>
              <li>Profile information (grade level)</li>
              <li>Academic records and grades</li>
              <li>Messages and communications within the platform</li>
              <li>Usage data and analytics</li>
            </ul>
          </section>

          <section>
            <h5>2. How We Use Your Information</h5>
            <p>We use the information we collect to:</p>
            <ul>
              <li>Provide, maintain, and improve our educational services</li>
              <li>Process enrollments and manage class sections</li>
              <li>Facilitate communication between teachers and students</li>
              <li>Monitor and analyze usage patterns</li>
              <li>Ensure platform security and prevent fraud</li>
              <li>Comply with legal obligations</li>
            </ul>
          </section>

          <section>
            <h5>3. Information Sharing</h5>
            <p>We do not sell your personal information. We may share your information with:</p>
            <ul>
              <li>Teachers and administrators within your educational institution</li>
              <li>Service providers who assist in operating our platform</li>
              <li>Legal authorities when required by law</li>
            </ul>
          </section>

          <section>
            <h5>4. Data Security</h5>
            <p>We implement appropriate technical and organizational measures to protect your personal information against unauthorized access, alteration, disclosure, or destruction.</p>
          </section>

          <section>
            <h5>5. Your Rights</h5>
            <p>You have the right to:</p>
            <ul>
              <li>Access and update your personal information</li>
              <li>Request deletion of your account</li>
              <li>Opt-out of non-essential communications</li>
              <li>Export your data</li>
            </ul>
          </section>

          <section>
            <h5>6. Children's Privacy</h5>
            <p>Our platform is designed for students in grades 7-12. We comply with applicable laws regarding the collection and use of information from minors.</p>
          </section>

          <section>
            <h5>7. Contact Us</h5>
            <p>If you have questions about this Privacy Policy, please contact us at privacy@intelligrade.edu</p>
          </section>
        </div>
      </div>
      <div class="modal-footer">
        <button @click="closePrivacyModal" class="btn-primary">Close</button>
      </div>
    </div>
  </div>

  <!-- Terms of Service Modal -->
  <div v-if="showTermsModal" class="modal-overlay" @click="closeTermsModal">
    <div class="modal-content document-modal" @click.stop>
      <div class="modal-header">
        <h3>Terms of Service</h3>
        <button @click="closeTermsModal" class="close-btn">×</button>
      </div>
      <div class="modal-body document-body">
        <div class="document-content">
          <h4>IntelliGrade Terms of Service</h4>
          <p class="document-date">Last Updated: January 2025</p>
          
          <section>
            <h5>1. Acceptance of Terms</h5>
            <p>By accessing and using IntelliGrade, you accept and agree to be bound by these Terms of Service. If you do not agree to these terms, please do not use our platform.</p>
          </section>

          <section>
            <h5>2. User Accounts</h5>
            <p>You are responsible for:</p>
            <ul>
              <li>Maintaining the confidentiality of your account credentials</li>
              <li>All activities that occur under your account</li>
              <li>Notifying us immediately of any unauthorized access</li>
              <li>Providing accurate and complete information</li>
            </ul>
          </section>

          <section>
            <h5>3. Acceptable Use</h5>
            <p>You agree not to:</p>
            <ul>
              <li>Use the platform for any illegal or unauthorized purpose</li>
              <li>Violate any laws in your jurisdiction</li>
              <li>Infringe on intellectual property rights</li>
              <li>Transmit malicious code or harmful content</li>
              <li>Harass, abuse, or harm other users</li>
              <li>Attempt to gain unauthorized access to the system</li>
            </ul>
          </section>

          <section>
            <h5>4. Academic Integrity</h5>
            <p>All users must maintain academic integrity. Cheating, plagiarism, or any form of academic dishonesty is strictly prohibited and may result in account suspension or termination.</p>
          </section>

          <section>
            <h5>5. Content Ownership</h5>
            <p>You retain ownership of content you create on the platform. By posting content, you grant IntelliGrade a license to use, store, and display that content as necessary to provide our services.</p>
          </section>

          <section>
            <h5>6. Service Availability</h5>
            <p>We strive to provide continuous access to our platform but do not guarantee uninterrupted service. We may suspend or terminate access for maintenance, updates, or violations of these terms.</p>
          </section>

          <section>
            <h5>7. Limitation of Liability</h5>
            <p>IntelliGrade is provided "as is" without warranties of any kind. We are not liable for any indirect, incidental, or consequential damages arising from your use of the platform.</p>
          </section>

          <section>
            <h5>8. Termination</h5>
            <p>We reserve the right to suspend or terminate your account if you violate these terms or engage in conduct that we deem harmful to the platform or other users.</p>
          </section>

          <section>
            <h5>9. Changes to Terms</h5>
            <p>We may modify these terms at any time. Continued use of the platform after changes constitutes acceptance of the modified terms.</p>
          </section>

          <section>
            <h5>10. Contact Information</h5>
            <p>For questions about these Terms of Service, contact us at support@intelligrade.edu</p>
          </section>
        </div>
      </div>
      <div class="modal-footer">
        <button @click="closeTermsModal" class="btn-primary">Close</button>
      </div>
    </div>
  </div>
</template>

<script>
import { supabase } from '@/Supabase.js';

export default {
  name: 'Settings',
  data() {
    return {
      // User data
      currentUser: null,
      userProfile: null,
      
      // Theme and preferences
      isDarkMode: false,
      notificationsEnabled: false,
      
      // Modal states
      showProfileModal: false,
      showPasswordModal: false,
      showPrivacyModal: false,
      showTermsModal: false,
      
      // Profile management
      profileData: {
        full_name: '',
        avatar: '1'
      },
      isSaving: false,
      profileError: '',
      profileSuccess: '',
      
      // Password management
      passwordData: {
        currentPassword: '',
        newPassword: '',
        confirmPassword: ''
      },
      isChangingPassword: false,
      passwordError: '',
      passwordSuccess: '',
      
      // Avatar options
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
      ]
    };
  },
  async mounted() {
    // Load saved preferences
    const savedNotifications = localStorage.getItem('notifications');
    if (savedNotifications !== null) {
      this.notificationsEnabled = savedNotifications === 'true';
    }
    
    // Load theme preference
    const savedTheme = localStorage.getItem('darkMode');
    if (savedTheme !== null) {
      this.isDarkMode = savedTheme === 'true';
      this.applyTheme();
    }
    
    // Load user data
    await this.loadUserData();
  },
  methods: {
    // ==================== USER DATA METHODS ====================
    async loadUserData() {
      try {
        // Get current authenticated user
        const { data: { user }, error: authError } = await supabase.auth.getUser();
        
        if (authError) throw authError;
        if (!user) {
          this.$router.push('/login');
          return;
        }
        
        this.currentUser = user;
        
        // Get profile data
        const { data: profile, error: profileError } = await supabase
          .from('profiles')
          .select('*')
          .eq('auth_user_id', user.id)
          .single();
        
        if (profileError) throw profileError;
        
        // Verify this is a student
        if (profile.role !== 'student') {
          alert('This settings page is for students only');
          this.$router.push('/');
          return;
        }
        
        this.userProfile = profile;
        
        // Get student details
        const { data: studentData, error: studentError } = await supabase
          .from('students')
          .select('*')
          .eq('profile_id', profile.id)
          .single();
        
        if (studentError) throw studentError;
        this.userProfile = { ...this.userProfile, ...studentData };
        
        // Load saved avatar
        const savedAvatar = localStorage.getItem('userAvatar');
        if (savedAvatar) {
          this.userProfile.avatar = savedAvatar;
        }
        
      } catch (error) {
        console.error('Error loading user data:', error);
        alert('Failed to load user data. Please refresh the page.');
      }
    },
    
    // ==================== THEME METHODS ====================
    handleDarkModeToggle() {
      localStorage.setItem('darkMode', this.isDarkMode.toString());
      this.applyTheme();
    },
    
    applyTheme() {
      if (this.isDarkMode) {
        document.documentElement.classList.add('dark');
      } else {
        document.documentElement.classList.remove('dark');
      }
    },
    
    toggleNotifications() {
      localStorage.setItem('notifications', this.notificationsEnabled.toString());
    },
    
    // ==================== PROFILE MODAL METHODS ====================
    openProfileModal() {
      if (!this.userProfile) {
        alert('User profile not loaded yet. Please wait...');
        return;
      }
      
      // Load REAL user data into the form
      this.profileData = {
        full_name: this.userProfile.full_name || '',
        avatar: this.userProfile.avatar || localStorage.getItem('userAvatar') || '1'
      };
      this.showProfileModal = true;
      this.clearMessages();
    },
    
    closeProfileModal() {
      this.showProfileModal = false;
      this.clearMessages();
    },
    
    selectAvatar(avatarId) {
      this.profileData.avatar = avatarId;
    },
    
    async saveProfile() {
      this.clearMessages();

      if (!this.profileData.full_name.trim()) {
        this.profileError = 'Full name is required';
        return;
      }

      this.isSaving = true;

      try {
        // Update profiles table
        const { error: profileError } = await supabase
          .from('profiles')
          .update({
            full_name: this.profileData.full_name.trim(),
            updated_at: new Date().toISOString()
          })
          .eq('id', this.userProfile.id);

        if (profileError) throw profileError;

        // Update students table
        const { error: studentError } = await supabase
          .from('students')
          .update({
            full_name: this.profileData.full_name.trim(),
            updated_at: new Date().toISOString()
          })
          .eq('profile_id', this.userProfile.id);

        if (studentError) throw studentError;

        // Save avatar preference to localStorage
        localStorage.setItem('userAvatar', this.profileData.avatar);

        this.profileSuccess = 'Profile updated successfully!';
        
        // Reload user data to reflect changes
        await this.loadUserData();
        
        setTimeout(() => {
          this.closeProfileModal();
        }, 1500);
        
      } catch (error) {
        console.error('Error saving profile:', error);
        this.profileError = 'Failed to save profile. Please try again.';
      } finally {
        this.isSaving = false;
      }
    },
    
    // ==================== PASSWORD MODAL METHODS ====================
    openPasswordModal() {
      this.showPasswordModal = true;
      this.resetPasswordForm();
      this.clearMessages();
    },
    
    closePasswordModal() {
      this.showPasswordModal = false;
      this.resetPasswordForm();
    },
    
    resetPasswordForm() {
      this.passwordData = {
        currentPassword: '',
        newPassword: '',
        confirmPassword: ''
      };
    },
    
    async changePassword() {
      this.clearMessages();

      // Validation
      if (!this.passwordData.currentPassword || !this.passwordData.newPassword || !this.passwordData.confirmPassword) {
        this.passwordError = 'All fields are required';
        return;
      }

      if (this.passwordData.newPassword.length < 6) {
        this.passwordError = 'New password must be at least 6 characters';
        return;
      }

      if (this.passwordData.newPassword !== this.passwordData.confirmPassword) {
        this.passwordError = 'New passwords do not match';
        return;
      }

      if (this.passwordData.currentPassword === this.passwordData.newPassword) {
        this.passwordError = 'New password must be different from current password';
        return;
      }

      this.isChangingPassword = true;

      try {
        // First, verify current password by trying to sign in
        const { error: signInError } = await supabase.auth.signInWithPassword({
          email: this.userProfile.email,
          password: this.passwordData.currentPassword
        });

        if (signInError) {
          this.passwordError = 'Current password is incorrect';
          this.isChangingPassword = false;
          return;
        }

        // Update to new password
        const { error: updateError } = await supabase.auth.updateUser({
          password: this.passwordData.newPassword
        });

        if (updateError) throw updateError;

        // Update password_changed_at in profiles table
        await supabase
          .from('profiles')
          .update({
            password_changed_at: new Date().toISOString(),
            updated_at: new Date().toISOString()
          })
          .eq('id', this.userProfile.id);

        // Log password change event
        await supabase
          .from('security_events')
          .insert({
            profile_id: this.userProfile.id,
            event_type: 'password_change',
            details: { changed_at: new Date().toISOString() }
          });

        this.passwordSuccess = 'Password updated successfully!';
        
        setTimeout(() => {
          this.closePasswordModal();
        }, 1500);
        
      } catch (error) {
        console.error('Error changing password:', error);
        this.passwordError = error.message || 'Failed to update password. Please try again.';
      } finally {
        this.isChangingPassword = false;
      }
    },
    
    // ==================== PRIVACY & TERMS METHODS ====================
    openPrivacyPolicy() {
      this.showPrivacyModal = true;
    },
    
    closePrivacyModal() {
      this.showPrivacyModal = false;
    },
    
    openTermsOfService() {
      this.showTermsModal = true;
    },
    
    closeTermsModal() {
      this.showTermsModal = false;
    },
    
    // ==================== DELETE ACCOUNT METHOD ====================
    async confirmDeleteAccount() {
      const firstConfirm = confirm(
        '⚠️ WARNING: Are you sure you want to delete your account?\n\n' +
        'This will permanently delete:\n' +
        '• Your profile and personal information\n' +
        '• All your enrollments and grades\n' +
        '• All your messages and communications\n\n' +
        'This action CANNOT be undone!'
      );
      
      if (!firstConfirm) return;
      
      const secondConfirm = confirm(
        '🚨 FINAL CONFIRMATION\n\n' +
        'This will permanently delete ALL your data.\n' +
        'Type YES in your mind and click OK to proceed with account deletion.\n\n' +
        'Click Cancel to keep your account.'
      );
      
      if (!secondConfirm) return;
      
      try {
        // Log the deletion event first
        await supabase
          .from('security_events')
          .insert({
            profile_id: this.userProfile.id,
            event_type: 'account_deletion',
            details: { 
              deleted_at: new Date().toISOString(),
              user_role: 'student'
            }
          });
        
        // Delete the profile (cascade will handle related records)
        const { error: deleteError } = await supabase
          .from('profiles')
          .delete()
          .eq('id', this.userProfile.id);
        
        if (deleteError) throw deleteError;
        
        // Sign out the user
        await supabase.auth.signOut();
        
        alert('Your account has been permanently deleted. You will now be redirected to the login page.');
        
        // Redirect to login
        this.$router.push('/login');
        
      } catch (error) {
        console.error('Error deleting account:', error);
        alert('Failed to delete account. Please try again or contact support.');
      }
    },
    
    // ==================== UTILITY METHODS ====================
    clearMessages() {
      this.profileError = '';
      this.profileSuccess = '';
      this.passwordError = '';
      this.passwordSuccess = '';
    }
  }
};
</script>

<style scoped>
/* Base Styles */
.page-container {
  padding: 2rem 5%;
  font-family: 'Inter', sans-serif;
  min-height: 100vh;
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

/* Header Styles */
.section-header-card {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  background: var(--card-background);
  border-radius: 28px;
  box-shadow: 0 8px 32px rgba(61, 141, 122, 0.13);
  border: 1.5px solid #b6e2d3;
  padding: 3rem 4rem 3rem 3.5rem;
  margin-bottom: 2.8rem;
  min-height: 140px;
  gap: 2.5rem;
}

.section-header-left {
  display: flex;
  align-items: center;
  gap: 1.7rem;
}

.section-header-icon {
  width: 64px;
  height: 64px;
  background: linear-gradient(135deg, #4dbb98 0%, #33806b 100%);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 16px 0 rgba(61, 141, 122, 0.13);
  color: var(--text-inverse);
}

.section-header-title {
  font-size: 2.1rem;
  font-weight: 700;
  color: #33806b;
  margin-bottom: 0.18rem;
  letter-spacing: -0.01em;
}

.section-header-sub {
  font-size: 1.15rem;
  color: #5e8c7a;
  font-weight: 400;
  margin-bottom: 0;
}

/* Settings Grid */
.settings-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-bottom: 2rem;
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

/* Toggle Switch */
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

input:checked + .slider:before {
  transform: translateX(22px);
}

.slider.round {
  border-radius: 28px;
}

.slider.round:before {
  border-radius: 50%;
}

/* Danger Zone */
.danger-zone h2 {
  color: #d9534f;
}

.danger-zone .section-subtitle {
  color: #d9534f;
}

.danger-text {
  color: #d9534f;
}

.danger-btn {
  background-color: rgba(217, 83, 79, 0.1);
  color: #d9534f;
}

.danger-btn:hover {
  background-color: #d9534f;
  color: white;
}

/* About Section */
.about-section {
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
}

.copyright-text {
  color: var(--secondary-text-color);
  font-size: 1rem;
}

/* Modal Styles */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  padding: 20px;
  backdrop-filter: blur(4px);
}

.modal-content {
  background: var(--card-background);
  border-radius: 16px;
  width: 100%;
  max-width: 500px;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  color: var(--primary-text-color);
}

.document-modal {
  max-width: 700px;
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
  z-index: 10;
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
  transition: color 0.2s;
}

.close-btn:hover {
  color: var(--primary-text-color);
}

.modal-body {
  padding: 1.5rem;
}

.document-body {
  max-height: 60vh;
  overflow-y: auto;
}

.document-content {
  line-height: 1.7;
}

.document-content h4 {
  font-size: 1.8rem;
  color: var(--accent-color);
  margin-bottom: 0.5rem;
}

.document-date {
  color: var(--secondary-text-color);
  font-style: italic;
  margin-bottom: 2rem;
}

.document-content section {
  margin-bottom: 2rem;
}

.document-content h5 {
  font-size: 1.3rem;
  color: var(--primary-text-color);
  margin-bottom: 0.75rem;
  margin-top: 1.5rem;
}

.document-content p {
  margin-bottom: 1rem;
  color: var(--primary-text-color);
}

.document-content ul {
  margin-left: 1.5rem;
  margin-bottom: 1rem;
}

.document-content li {
  margin-bottom: 0.5rem;
  color: var(--primary-text-color);
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

/* Avatar Grid */
.avatar-grid {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 1rem;
  padding: 1rem;
  background: var(--action-btn-bg);
  border-radius: 12px;
}

.avatar-option {
  cursor: pointer;
  transition: all 0.2s;
  border-radius: 12px;
  padding: 0.5rem;
  border: 2px solid transparent;
}

.avatar-option:hover {
  transform: scale(1.1);
  border-color: var(--accent-color);
}

.avatar-option.selected {
  border-color: var(--accent-color);
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.2);
}

.avatar-icon {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.8rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

/* Messages */
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
  opacity: 0.6;
}

.btn-secondary {
  background: var(--action-btn-bg);
  color: var(--primary-text-color);
}

.btn-secondary:hover {
  background: var(--accent-color);
  color: white;
}

/* Responsive */
@media (max-width: 1024px) {
  .settings-grid {
    grid-template-columns: 1fr;
  }
  
  .avatar-grid {
    grid-template-columns: repeat(4, 1fr);
  }
}

@media (max-width: 768px) {
  .page-container {
    padding: 1rem 3%;
  }
  
  .section-header-card {
    padding: 2rem 1.5rem;
    gap: 1.5rem;
  }
  
  .section-header-title {
    font-size: 1.8rem;
  }
  
  .section-header-icon {
    width: 50px;
    height: 50px;
  }
  
  .settings-card {
    padding: 1.5rem;
  }
  
  .modal-overlay {
    padding: 10px;
  }
  
  .modal-content {
    max-height: 95vh;
  }
  
  .modal-header, .modal-footer, .modal-body {
    padding: 1rem;
  }
  
  .avatar-grid {
    grid-template-columns: repeat(3, 1fr);
  }
  
  .document-modal {
    max-width: 100%;
  }
}
</style>