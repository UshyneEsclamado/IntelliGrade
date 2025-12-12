<template>
  <div class="dashboard-container">
    <!-- Top Navigation Bar (Clean) -->
    <nav class="top-navbar">
      <div class="navbar-content">
        <!-- Left: Logo and Brand -->
        <div class="navbar-left">
          <div class="brand-logo">
            <img src="@/assets/LOGO WAY BG.png" alt="IntelliGrade" class="logo-img" />
            <span class="brand-name">IntelliGrade</span>
          </div>
        </div>
        <!-- Center: Empty space for clean look -->
        <div class="navbar-center">
        </div>
        
        <!-- Right: User Profile and Notifications -->
        <div class="navbar-right">
          <!-- User Profile -->
          <div class="user-profile-wrapper">
            <div class="user-profile rounded-bg" @click="toggleUserDropdown">
              <div class="user-avatar">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                  <circle cx="12" cy="7" r="4"></circle>
                </svg>
              </div>
              <span class="user-name">{{ userProfile.name || 'Teacher' }}</span>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" class="dropdown-arrow">
                <path d="M7 10l5 5 5-5z"/>
              </svg>
            </div>
            
            <!-- Profile Dropdown -->
            <div v-if="showUserDropdown" class="profile-dropdown">
              <div class="dropdown-header">
                <div class="profile-info">
                  <div class="profile-avatar">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                      <circle cx="12" cy="7" r="4"></circle>
                    </svg>
                  </div>
                  <div class="profile-details">
                    <h4>{{ userProfile.name || 'Teacher' }}</h4>
                    <p>Teacher</p>
                  </div>
                </div>
              </div>
              
              <div class="dropdown-menu">
                <router-link to="/teacher/settings" class="dropdown-item">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12 2C13.1 2 14 2.9 14 4C14 5.1 13.1 6 12 6C10.9 6 10 5.1 10 4C10 2.9 10.9 2 12 2ZM21 9V7L15 1V3H9V1L3 7V9H5V20A2 2 0 0 0 7 22H17A2 2 0 0 0 19 20V9H21M17 20H7V9H10V12H14V9H17V20Z"/>
                  </svg>
                  <span>Profile & Settings</span>
                </router-link>
                
                <div class="dropdown-divider"></div>
                
                <button @click="handleLogout" class="dropdown-item logout-btn">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M16 17V14H9V10H16V7L21 12L16 17M14 2A2 2 0 0 1 16 4V6H14V4H5V20H14V18H16V20A2 2 0 0 1 14 22H5A2 2 0 0 1 3 20V4A2 2 0 0 1 5 2H14Z"/>
                  </svg>
                  <span>Logout</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <!-- Sidebar Navigation -->
    <aside class="sidebar" style="background:#3D8D7A; border-right:none;">
      <nav class="sidebar-nav">
        <router-link to="/teacher/dashboard" class="sidebar-item rounded-bg" :class="{ 'active': $route.path === '/teacher/dashboard' }">
          <div class="sidebar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M10 20v-6h4v6m5-8h3L12 3 2 12h3v8h5v-6h4v6h5v-8z" />
            </svg>
          </div>
          <span class="sidebar-tooltip">Dashboard</span>
        </router-link>
        <router-link to="/teacher/subjects" class="sidebar-item rounded-bg" :class="{ 'active': $route.path.includes('/teacher/subjects') }">
          <div class="sidebar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="7" width="18" height="13" rx="2" />
              <path d="M3 7l9-4 9 4" />
            </svg>
          </div>
          <span class="sidebar-tooltip">Classes</span>
        </router-link>
        <router-link to="/teacher/gradebook" class="sidebar-item rounded-bg" :class="{ 'active': $route.path === '/teacher/gradebook' }">
          <div class="sidebar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="4" y="4" width="16" height="16" rx="2" />
              <path d="M8 2v4M16 2v4" />
            </svg>
          </div>
          <span class="sidebar-tooltip">Gradebook</span>
        </router-link>
        <router-link to="/teacher/analytics" class="sidebar-item rounded-bg" :class="{ 'active': $route.path === '/teacher/analytics' }">
          <div class="sidebar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="12" width="4" height="8" />
              <rect x="10" y="8" width="4" height="12" />
              <rect x="17" y="4" width="4" height="16" />
            </svg>
          </div>
          <span class="sidebar-tooltip">Analytics</span>
        </router-link>
        <router-link to="/teacher/messages" class="sidebar-item rounded-bg" :class="{ 'active': $route.path === '/teacher/messages' }">
          <div class="sidebar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="5" width="18" height="14" rx="2" />
              <path d="M3 5l9 7 9-7" />
            </svg>
          </div>
          <span class="sidebar-tooltip">Messages</span>
        </router-link>
        
        <div class="sidebar-divider"></div>
        
        <router-link to="/teacher/settings" class="sidebar-item rounded-bg" :class="{ 'active': $route.path === '/teacher/settings' }">
          <div class="sidebar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
              <circle cx="12" cy="7" r="4"></circle>
            </svg>
          </div>
          <span class="sidebar-tooltip">Profile & Settings</span>
        </router-link>
        
        <button @click="handleLogout" class="sidebar-item sidebar-logout rounded-bg">
          <div class="sidebar-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path>
              <polyline points="16 17 21 12 16 7"></polyline>
              <line x1="21" y1="12" x2="9" y2="12"></line>
            </svg>
          </div>
          <span class="sidebar-tooltip">Logout</span>
        </button>
      </nav>
    </aside>

    <!-- Main Content Area -->
    <main class="main-content">
      <!-- Page Header -->
      <div class="page-header">
        <div class="header-content">
          <div class="header-left">
            <div class="header-icon">
              <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M12,15.5A3.5,3.5 0 0,1 8.5,12A3.5,3.5 0 0,1 12,8.5A3.5,3.5 0 0,1 15.5,12A3.5,3.5 0 0,1 12,15.5M19.43,12.97C19.47,12.65 19.5,12.33 19.5,12C19.5,11.67 19.47,11.34 19.43,11.03L21.54,9.37C21.73,9.22 21.78,8.95 21.67,8.75L19.67,5.27C19.56,5.08 19.3,5.03 19.1,5.12L16.9,6C16.5,5.65 16.08,5.36 15.61,5.1L15.2,2.83C15.15,2.56 14.9,2.33 14.62,2.33L9.38,2.33C9.1,2.33 8.85,2.56 8.8,2.83L8.39,5.09C7.92,5.34 7.5,5.65 7.1,6L4.9,5.12C4.7,5.03 4.44,5.08 4.33,5.27L2.33,8.75C2.22,8.95 2.27,9.22 2.46,9.37L4.57,11.03C4.53,11.34 4.5,11.67 4.5,12C4.5,12.33 4.53,12.65 4.57,12.97L2.46,14.63C2.27,14.78 2.22,15.05 2.33,15.25L4.33,18.73C4.44,18.92 4.7,18.97 4.9,18.88L7.1,18C7.5,18.35 7.92,18.64 8.39,18.9L8.8,21.17C8.85,21.44 9.1,21.67 9.38,21.67L14.62,21.67C14.9,21.67 15.15,21.44 15.2,21.17L15.61,18.91C16.08,18.66 16.5,18.35 16.9,18L19.1,18.88C19.3,18.97 19.56,18.92 19.67,18.73L21.67,15.25C21.78,15.05 21.73,14.78 21.54,14.63L19.43,12.97Z" />
              </svg>
            </div>
            <div>
              <h1 class="header-title">Settings</h1>
              <p class="header-subtitle">Manage your account, profile, and app preferences</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Content Area -->
      <div class="main-wrapper">
        <div class="content-card">
          <!-- Account & Profile Card -->
          <div class="settings-card">
            <h2 class="section-title">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="section-icon">
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
                <circle cx="12" cy="7" r="4"/>
              </svg> 
              Account & Profile
            </h2>
            <p class="section-subtitle">Update your personal information and profile settings</p>
            <div class="settings-list">
              <div class="setting-item" @click="openProfileModal">
                <span>Update Profile Info</span>
                <button class="action-btn">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/>
                  </svg>
                </button>
              </div>
              <div class="setting-item" @click="openPasswordModal">
                <span>Change Password</span>
                <button class="action-btn">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                    <circle cx="12" cy="16" r="1"></circle>
                    <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                  </svg>
                </button>
              </div>
            </div>
          </div>
          
          <!-- App Preferences Card -->
          <div class="settings-card">
            <h2 class="section-title">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="section-icon">
                <circle cx="12" cy="12" r="3"/>
                <path d="m12 1 0 6m0 6 0 6"/>
                <path d="m21 12-6 0m-6 0-6 0"/>
              </svg> 
              App Preferences
            </h2>
            <p class="section-subtitle">Customize the app's look and feel</p>
            <div class="settings-list">
              <div class="setting-item">
                <span>Dark Mode</span>
                <label class="switch">
                  <input type="checkbox" v-model="isDarkMode" @change="handleDarkModeToggle">
                  <span class="slider round"></span>
                </label>
              </div>
            </div>
          </div>

          <!-- Privacy & Legal Card -->
          <div class="settings-card">
            <h2 class="section-title">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="section-icon">
                <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
              </svg> 
              Privacy & Legal
            </h2>
            <p class="section-subtitle">Understand our policies and manage your data</p>
            <div class="settings-list">
              <div class="setting-item" @click="showPrivacyPolicy">
                <span>Privacy Policy</span>
                <button class="action-btn">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" />
                    <polyline points="14 2 14 8 20 8" />
                    <line x1="16" y1="13" x2="8" y2="13" />
                    <line x1="16" y1="17" x2="8" y2="17" />
                  </svg>
                </button>
              </div>
              <div class="setting-item" @click="showTermsOfService">
                <span>Terms of Service</span>
                <button class="action-btn">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" />
                    <polyline points="14 2 14 8 20 8" />
                    <line x1="16" y1="13" x2="8" y2="13" />
                    <line x1="16" y1="17" x2="8" y2="17" />
                  </svg>
                </button>
              </div>
            </div>
          </div>

          <!-- Danger Zone Card -->
          <div class="settings-card danger-zone">
            <h2 class="section-title">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="section-icon">
                <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/>
                <line x1="12" y1="9" x2="12" y2="13"/>
                <line x1="12" y1="17" x2="12.01" y2="17"/>
              </svg> 
              Danger Zone
            </h2>
            <p class="section-subtitle">Sensitive actions that cannot be undone</p>
            <div class="settings-list">
              <div class="setting-item" @click="openDeleteAccountModal">
                <span class="danger-text">Delete Account</span>
                <button class="action-btn danger-btn">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M3 6l3 0l0 15a2 2 0 0 0 2 2l8 0a2 2 0 0 0 2 -2l0 -15l3 0"/>
                    <path d="M14 10l0 5"/>
                    <path d="M10 10l0 5"/>
                    <path d="M18 6l-12 0"/>
                    <path d="M10 3l4 0l0 3l-4 0l0 -3z"/>
                  </svg>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>

  <!-- Profile Update Modal -->
  <div v-if="showProfileModal" class="modal-overlay" @click="closeProfileModal">
    <div class="modal-content" @click.stop>
      <div class="modal-header">
        <h3>Update Profile</h3>
        <button @click="closeProfileModal" class="close-btn">×</button>
      </div>
      <div class="modal-body">
        <div class="form-group">
          <label>Profile Picture</label>
          <div class="avatar-upload-section">
            <div v-if="imagePreview || currentProfilePicture" class="current-avatar">
              <img 
                :src="imagePreview || currentProfilePicture" 
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
              @change="handleImageSelect"
              accept="image/*"
              class="file-input"
              id="avatar-upload"
            >
            <label for="avatar-upload" class="file-input-label">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3l-2.5-3z"/>
                <circle cx="12" cy="13" r="3"/>
              </svg>
              {{ selectedImage ? 'Change Photo' : 'Choose Photo' }}
            </label>
            <div v-if="selectedImage" class="selected-file">
              Selected: {{ selectedImage.name }}
            </div>
          </div>
        </div>
        
        <div class="form-group">
          <label>Full Name</label>
          <input 
            type="text" 
            v-model="profileData.full_name" 
            placeholder="Enter your full name"
            class="form-input"
          >
        </div>
        
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
            placeholder="Enter new password"
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
  <div v-if="showPrivacyModal" class="modal-overlay" @click="showPrivacyModal = false">
    <div class="modal-content info-modal" @click.stop>
      <div class="modal-header">
        <h3>Privacy Policy</h3>
        <button @click="showPrivacyModal = false" class="close-btn">×</button>
      </div>
      <div class="modal-body info-content">
        <h4>IntelliGrade Privacy Policy</h4>
        <p><strong>Last Updated:</strong> January 2025</p>
        
        <h5>1. Information We Collect</h5>
        <p>We collect information you provide directly to us, including your name, email address, and profile information when you create an account.</p>
        
        <h5>2. How We Use Your Information</h5>
        <p>We use the information we collect to provide, maintain, and improve our services, to communicate with you, and to protect IntelliGrade and our users.</p>
        
        <h5>3. Information Sharing</h5>
        <p>We do not share your personal information with third parties except as described in this privacy policy or with your consent.</p>
        
        <h5>4. Data Security</h5>
        <p>We implement appropriate technical and organizational measures to protect your personal information against unauthorized access, alteration, or destruction.</p>
        
        <h5>5. Your Rights</h5>
        <p>You have the right to access, update, or delete your personal information at any time through your account settings.</p>
        
        <h5>6. Contact Us</h5>
        <p>If you have any questions about this Privacy Policy, please contact us at privacy@intelligrade.com</p>
      </div>
      <div class="modal-footer">
        <button @click="showPrivacyModal = false" class="btn-primary">Close</button>
      </div>
    </div>
  </div>

  <!-- Terms of Service Modal -->
  <div v-if="showTermsModal" class="modal-overlay" @click="showTermsModal = false">
    <div class="modal-content info-modal" @click.stop>
      <div class="modal-header">
        <h3>Terms of Service</h3>
        <button @click="showTermsModal = false" class="close-btn">×</button>
      </div>
      <div class="modal-body info-content">
        <h4>IntelliGrade Terms of Service</h4>
        <p><strong>Last Updated:</strong> January 2025</p>
        
        <h5>1. Acceptance of Terms</h5>
        <p>By accessing and using IntelliGrade, you accept and agree to be bound by the terms and provisions of this agreement.</p>
        
        <h5>2. User Accounts</h5>
        <p>You are responsible for maintaining the confidentiality of your account credentials and for all activities that occur under your account.</p>
        
        <h5>3. Acceptable Use</h5>
        <p>You agree to use IntelliGrade only for lawful purposes and in accordance with these Terms. You must not use our service to transmit harmful, offensive, or illegal content.</p>
        
        <h5>4. Intellectual Property</h5>
        <p>The service and its original content, features, and functionality are owned by IntelliGrade and are protected by international copyright, trademark, and other intellectual property laws.</p>
        
        <h5>5. Termination</h5>
        <p>We may terminate or suspend your account immediately, without prior notice, for conduct that we believe violates these Terms or is harmful to other users, us, or third parties.</p>
        
        <h5>6. Limitation of Liability</h5>
        <p>IntelliGrade shall not be liable for any indirect, incidental, special, consequential, or punitive damages resulting from your use of or inability to use the service.</p>
        
        <h5>7. Changes to Terms</h5>
        <p>We reserve the right to modify these terms at any time. We will notify users of any material changes via email or through the service.</p>
        
        <h5>8. Contact Information</h5>
        <p>For questions about these Terms, please contact us at terms@intelligrade.com</p>
      </div>
      <div class="modal-footer">
        <button @click="showTermsModal = false" class="btn-primary">Close</button>
      </div>
    </div>
  </div>

  <!-- Delete Account Confirmation Modal -->
  <div v-if="showDeleteModal" class="modal-overlay" @click="closeDeleteModal">
    <div class="modal-content delete-modal" @click.stop>
      <div class="modal-header delete-header">
        <h3>Delete Account</h3>
        <button @click="closeDeleteModal" class="close-btn" v-if="!isDeleting">×</button>
      </div>
      <div class="modal-body">
        <p class="delete-warning-text">This action cannot be undone. This will permanently delete your account and all associated data.</p>
        
        <!-- Show form when not deleting -->
        <div v-if="!isDeleting">
          <div class="form-group">
            <label class="delete-label">Type DELETE to confirm:</label>
            <p class="helper-text">⚠️ Must be typed in CAPS LOCK: <strong>DELETE</strong></p>
            <input 
              type="text" 
              v-model="deleteConfirmation" 
              placeholder="TYPE DELETE TO CONFIRM"
              class="form-input delete-input"
            >
          </div>
          
          <div v-if="deleteError" class="error-message">{{ deleteError }}</div>
        </div>
        
        <!-- Show loading indicator when deleting -->
        <div v-if="isDeleting" class="loading-container">
          <div class="spinner"></div>
          <p class="loading-text">{{ deleteSuccess }}</p>
        </div>
      </div>
      <div class="modal-footer" v-if="!isDeleting">
        <button @click="closeDeleteModal" class="btn-secondary">Cancel</button>
        <button 
          @click="deleteAccount" 
          class="btn-danger" 
          :disabled="deleteConfirmation.trim() !== 'DELETE'"
        >
          DELETE ACCOUNT
        </button>
      </div>
    </div>
  </div>

  <!-- Logout Confirmation Modal -->
  <div v-if="showLogoutModal" class="modal-overlay" @click="closeLogoutModal">
    <div class="modal-content logout-modal" @click.stop>
      <div class="modal-header logout-header">
        <h3>Confirm Logout</h3>
      </div>
      <div class="modal-body">
        <div class="logout-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/>
            <polyline points="16 17 21 12 16 7"/>
            <line x1="21" y1="12" x2="9" y2="12"/>
          </svg>
        </div>
        <p class="logout-message">Are you sure you want to logout?</p>
        <p class="logout-submessage">You will be redirected to the login page.</p>
      </div>
      <div class="modal-footer logout-footer">
        <button @click="closeLogoutModal" class="btn-cancel" :disabled="isLoggingOut">Cancel</button>
        <button @click="confirmLogout" class="btn-logout" :disabled="isLoggingOut">
          <span v-if="!isLoggingOut">Logout</span>
          <span v-else class="loading-text">
            <div class="logout-spinner"></div>
            Redirecting...
          </span>
        </button>
      </div>
    </div>
  </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { supabase } from '../../supabase.js';
import { useRouter } from 'vue-router';

// Click outside directive
const vClickOutside = {
  mounted(el, binding) {
    el.clickOutsideEvent = function(event) {
      if (!(el === event.target || el.contains(event.target))) {
        binding.value();
      }
    };
    document.addEventListener('click', el.clickOutsideEvent);
  },
  unmounted(el) {
    document.removeEventListener('click', el.clickOutsideEvent);
  }
};

const router = useRouter();

// ===== USER PROFILE & DROPDOWN =====
const userProfile = ref({
  name: '',
  avatar: null
});
const showUserDropdown = ref(false);

// ===== THEME MANAGEMENT =====
const isDarkMode = ref(false);

const handleDarkModeToggle = () => {
  localStorage.setItem('darkMode', isDarkMode.value.toString());
  applyTheme();
};

const applyTheme = () => {
  if (isDarkMode.value) {
    document.documentElement.classList.add('dark');
    document.body.classList.add('dark-mode');
  } else {
    document.documentElement.classList.remove('dark');
    document.body.classList.remove('dark-mode');
  }
};

const initializeTheme = () => {
  const savedTheme = localStorage.getItem('darkMode');
  if (savedTheme !== null) {
    isDarkMode.value = savedTheme === 'true';
    applyTheme();
  }
};

// ===== MODAL STATES =====
const showProfileModal = ref(false);
const showPasswordModal = ref(false);
const showPrivacyModal = ref(false);
const showTermsModal = ref(false);
const showDeleteModal = ref(false);

// ===== PROFILE MANAGEMENT =====
const profileData = ref({
  full_name: '',
  profile_id: null,
  auth_user_id: null
});

const selectedImage = ref(null);
const imagePreview = ref(null);
const currentProfilePicture = ref(null);
const isSaving = ref(false);
const profileError = ref('');
const profileSuccess = ref('');
const userRole = ref('');

// Profile Modal Functions
const openProfileModal = async () => {
  showProfileModal.value = true;
  await loadUserProfile();
  clearMessages();
};

const closeProfileModal = () => {
  showProfileModal.value = false;
  selectedImage.value = null;
  imagePreview.value = null;
  clearMessages();
};

// Load user profile data
const loadUserProfile = async () => {
  try {
    const { data: { user } } = await supabase.auth.getUser();
    if (!user) {
      return;
    }

    const { data: profile, error: fetchError } = await supabase
      .from('profiles')
      .select('id, full_name, role, auth_user_id')
      .eq('auth_user_id', user.id)
      .single();

    if (fetchError) throw fetchError;

    if (profile) {
      profileData.value.profile_id = profile.id;
      profileData.value.auth_user_id = profile.auth_user_id;
      profileData.value.full_name = profile.full_name || '';
      userRole.value = profile.role;

      if (profile.role === 'student') {
        const { data: studentData } = await supabase
          .from('students')
          .select('full_name')
          .eq('profile_id', profile.id)
          .single();
        
        if (studentData) {
          profileData.value.full_name = studentData.full_name;
        }
      } else if (profile.role === 'teacher') {
        const { data: teacherData } = await supabase
          .from('teachers')
          .select('full_name')
          .eq('profile_id', profile.id)
          .single();
        
        if (teacherData) {
          profileData.value.full_name = teacherData.full_name;
        }
      }
    }
  } catch (error) {
    console.error('Error loading profile:', error);
    profileError.value = 'Failed to load profile data';
  }
};

// Handle image selection
const handleImageSelect = (event) => {
  const file = event.target.files[0];
  if (!file) return;

  if (!file.type.startsWith('image/')) {
    profileError.value = 'Please select an image file';
    return;
  }

  if (file.size > 5 * 1024 * 1024) {
    profileError.value = 'File size must be less than 5MB';
    return;
  }

  selectedImage.value = file;
  profileError.value = '';

  const reader = new FileReader();
  reader.onload = (e) => {
    imagePreview.value = e.target.result;
  };
  reader.readAsDataURL(file);
};

// Upload image to Supabase Storage
const uploadImage = async () => {
  if (!selectedImage.value) return null;

  try {
    const { data: { user } } = await supabase.auth.getUser();
    if (!user) throw new Error('No user logged in');

    const fileExt = selectedImage.value.name.split('.').pop();
    const fileName = `${user.id}-${Date.now()}.${fileExt}`;

    const { error: uploadError } = await supabase.storage
      .from('profiles')
      .upload(fileName, selectedImage.value, { 
        cacheControl: '3600', 
        upsert: true 
      });

    if (uploadError) throw uploadError;

    const { data: { publicUrl } } = supabase.storage
      .from('profiles')
      .getPublicUrl(fileName);

    return publicUrl;
  } catch (error) {
    console.error('Upload error:', error);
    throw error;
  }
};

// Save profile
const saveProfile = async () => {
  clearMessages();

  if (!profileData.value.full_name.trim()) {
    profileError.value = 'Full name is required';
    return;
  }

  isSaving.value = true;

  try {
    const { data: { user } } = await supabase.auth.getUser();
    if (!user) throw new Error('No user logged in');

    let profileUrl = currentProfilePicture.value;
    if (selectedImage.value) {
      profileUrl = await uploadImage();
    }

    const { error: profileUpdateError } = await supabase
      .from('profiles')
      .update({ 
        full_name: profileData.value.full_name.trim(),
        updated_at: new Date().toISOString()
      })
      .eq('auth_user_id', user.id);

    if (profileUpdateError) throw profileUpdateError;

    if (userRole.value === 'student') {
      const { error: studentError } = await supabase
        .from('students')
        .update({ 
          full_name: profileData.value.full_name.trim(),
          updated_at: new Date().toISOString()
        })
        .eq('profile_id', profileData.value.profile_id);
      
      if (studentError) throw studentError;
    } else if (userRole.value === 'teacher') {
      const { error: teacherError } = await supabase
        .from('teachers')
        .update({ 
          full_name: profileData.value.full_name.trim(),
          updated_at: new Date().toISOString()
        })
        .eq('profile_id', profileData.value.profile_id);
        if (teacherError) throw teacherError;
    }

    if (profileUrl) {
      currentProfilePicture.value = profileUrl;
    }

    profileSuccess.value = 'Profile updated successfully!';
    
    window.dispatchEvent(new CustomEvent('teacherProfileUpdated', {
      detail: {
        nameChanged: true,
        photoChanged: selectedImage.value !== null,
        newName: profileData.value.full_name.trim(),
        newPhoto: profileUrl
      }
    }));

    setTimeout(() => {
      closeProfileModal();
    }, 1500);

  } catch (error) {
    console.error('Profile save error:', error);
    profileError.value = error.message || 'Failed to save profile';
  } finally {
    isSaving.value = false;
  }
};

// ===== PASSWORD MANAGEMENT =====
const passwordData = ref({
  currentPassword: '',
  newPassword: '',
  confirmPassword: ''
});

const passwordError = ref('');
const passwordSuccess = ref('');
const isChangingPassword = ref(false);

const openPasswordModal = () => {
  showPasswordModal.value = true;
  resetPasswordForm();
  clearMessages();
};

const closePasswordModal = () => {
  showPasswordModal.value = false;
  resetPasswordForm();
};

const resetPasswordForm = () => {
  passwordData.value = {
    currentPassword: '',
    newPassword: '',
    confirmPassword: ''
  };
};

const changePassword = async () => {
  clearMessages();

  if (!passwordData.value.newPassword || !passwordData.value.confirmPassword) {
    passwordError.value = 'All fields are required';
    return;
  }

  if (passwordData.value.newPassword.length < 6) {
    passwordError.value = 'New password must be at least 6 characters';
    return;
  }

  if (passwordData.value.newPassword !== passwordData.value.confirmPassword) {
    passwordError.value = 'Passwords do not match';
    return;
  }

  isChangingPassword.value = true;

  try {
    const { error } = await supabase.auth.updateUser({ 
      password: passwordData.value.newPassword 
    });
    
    if (error) throw error;

    const { data: { user } } = await supabase.auth.getUser();
    if (user) {
      await supabase
        .from('profiles')
        .update({ 
          password_changed_at: new Date().toISOString() 
        })
        .eq('auth_user_id', user.id);
    }
    
    passwordSuccess.value = 'Password updated successfully!';
    setTimeout(() => {
      closePasswordModal();
    }, 1500);
  } catch (error) {
    passwordError.value = error.message || 'Failed to update password';
  } finally {
    isChangingPassword.value = false;
  }
};

// ===== PRIVACY & LEGAL =====
const showPrivacyPolicy = () => {
  showPrivacyModal.value = true;
};

const showTermsOfService = () => {
  showTermsModal.value = true;
};

// ===== DELETE ACCOUNT =====
const deleteConfirmation = ref('');
const deleteError = ref('');
const deleteSuccess = ref('');
const isDeleting = ref(false);

const openDeleteAccountModal = () => {
  showDeleteModal.value = true;
  deleteConfirmation.value = '';
  deleteError.value = '';
  deleteSuccess.value = '';
};

const closeDeleteModal = () => {
  if (!isDeleting.value) {
    showDeleteModal.value = false;
    deleteConfirmation.value = '';
    deleteError.value = '';
    deleteSuccess.value = '';
  }
};

const deleteAccount = async () => {
  if (deleteConfirmation.value.trim() !== 'DELETE') {
    deleteError.value = 'You must type DELETE exactly (in uppercase) to confirm';
    return;
  }

  isDeleting.value = true;
  deleteError.value = '';
  deleteSuccess.value = 'Deleting your account...';

  try {
    console.log('🗑️ Step 1: Starting deletion...');
    
    const { data: { user } } = await supabase.auth.getUser();
    if (!user) throw new Error('No user logged in');

    console.log('🗑️ Step 2: Calling RPC function...');
    const { data, error: rpcError } = await supabase.rpc('delete_user_account');

    if (rpcError) {
      console.error('❌ RPC Error:', rpcError);
      throw new Error(rpcError.message || 'Failed to delete account');
    }

    console.log('📝 Step 3: RPC Response:', data);

    if (data && !data.success) {
      throw new Error(data.message || 'Failed to delete account');
    }

    console.log('✅ Step 4: Account deleted!');
    deleteSuccess.value = '✅ Account deleted successfully!';
    
    console.log('🧹 Step 5: Clearing all storage...');
    localStorage.clear();
    sessionStorage.clear();
    
    console.log('🚪 Step 6: Signing out...');
    await supabase.auth.signOut({ scope: 'local' });
    
    console.log('🔄 Step 7: Redirecting to login page...');
    deleteSuccess.value = '🔄 Redirecting to login page...';
    
    // Force immediate redirect with multiple methods
    setTimeout(() => {
      window.location.href = '/login';
    }, 100);
    
    // Backup redirect method
    setTimeout(() => {
      window.location.replace('/login');
    }, 200);
    
    // Ultimate fallback - complete page reload to login
    setTimeout(() => {
      window.location.href = '/login';
    }, 300);

  } catch (error) {
    console.error('❌ Error:', error);
    deleteError.value = error.message || 'Failed to delete account';
    isDeleting.value = false;
  }
};

// ===== UTILITY FUNCTIONS =====
const clearMessages = () => {
  profileError.value = '';
  profileSuccess.value = '';
  passwordError.value = '';
  passwordSuccess.value = '';
  deleteError.value = '';
  deleteSuccess.value = '';
};

// ===== USER DROPDOWN FUNCTIONS =====
const toggleUserDropdown = () => {
  showUserDropdown.value = !showUserDropdown.value;
};

const closeUserDropdown = () => {
  showUserDropdown.value = false;
};

// Logout confirmation modal
const showLogoutModal = ref(false);

const openLogoutModal = () => {
  showLogoutModal.value = true;
};

const closeLogoutModal = () => {
  showLogoutModal.value = false;
};

const isLoggingOut = ref(false);

const confirmLogout = () => {
  console.log('🚪 Logging out...');
  
  // Clear storage immediately
  localStorage.clear();
  sessionStorage.clear();
  
  // Sign out from Supabase (don't wait)
  supabase.auth.signOut().catch(err => console.log('Signout error:', err));
  
  // Immediate redirect - no waiting!
  setTimeout(() => {
    window.location.assign('/login');
  }, 100);
  
  console.log('✅ Logout initiated');
};

const handleLogout = () => {
  openLogoutModal();
};

// Load user profile for navbar
const loadUserProfileForNavbar = async () => {
  try {
    const { data: { user } } = await supabase.auth.getUser();
    if (!user) return;

    const { data: profile } = await supabase
      .from('profiles')
      .select('id, full_name, role')
      .eq('auth_user_id', user.id)
      .single();

    if (profile) {
      userProfile.value.name = profile.full_name || 'User';
      
      // Get role-specific data
      if (profile.role === 'teacher') {
        const { data: teacherData } = await supabase
          .from('teachers')
          .select('full_name')
          .eq('profile_id', profile.id)
          .single();
        
        if (teacherData) {
          userProfile.value.name = teacherData.full_name || 'Teacher';
        }
      }
    }
  } catch (error) {
    console.error('Error loading user profile for navbar:', error);
  }
};

// ===== INITIALIZATION =====
onMounted(() => {
  initializeTheme();
  loadUserProfile();
  loadUserProfileForNavbar();
});
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

/* Dashboard Container */
.dashboard-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  background: #f8fafc;
  font-family: 'Inter', sans-serif;
}

/* Top Navigation Bar */
.top-navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 64px;
  background: linear-gradient(135deg, #3D8D7A, #2d6a5a);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  z-index: 1000;
  box-shadow: 0 4px 20px rgba(61, 141, 122, 0.3);
}

.navbar-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 1.5rem;
}

.navbar-left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.brand-logo {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: white;
  font-weight: 700;
  text-decoration: none;
}

.logo-img {
  width: 36px;
  height: 36px;
  object-fit: contain;
  filter: brightness(0) invert(1);
}

.brand-name {
  font-size: 1.4rem;
  font-weight: 800;
  color: white;
  letter-spacing: -0.5px;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

.navbar-center {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex: 1;
  justify-content: center;
  max-width: 600px;
}

.nav-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.25rem;
  padding: 0.75rem 1.5rem;
  border-radius: 12px;
  text-decoration: none;
  color: rgba(255, 255, 255, 0.8);
  transition: all 0.2s ease;
  position: relative;
  font-size: 0.75rem;
  font-weight: 500;
}

.nav-item:hover {
  background: rgba(255, 255, 255, 0.1);
  color: white;
}

.nav-item.active {
  color: white;
  background: rgba(255, 255, 255, 0.15);
}

.nav-item.active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 60%;
  height: 3px;
  background: white;
  border-radius: 2px 2px 0 0;
}

.navbar-right {
  display: flex;
  align-items: center;
  gap: 1rem;
}

/* User Profile Section */
.user-profile-wrapper {
  position: relative;
}

.user-profile {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.5rem 0.75rem;
  border-radius: 12px;
  transition: background 0.2s;
  cursor: pointer;
}

.user-profile:hover {
  background: rgba(255, 255, 255, 0.1);
}

.user-avatar {
  width: 36px;
  height: 36px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.user-name {
  font-size: 0.9rem;
  font-weight: 600;
  color: white;
}

.dropdown-arrow {
  transition: transform 0.2s ease;
  color: white;
}

/* Profile Dropdown */
.profile-dropdown {
  position: absolute;
  top: 55px;
  right: 0;
  width: 280px;
  background: white;
  border-radius: 16px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
  overflow: hidden;
  z-index: 1001;
  border: 1px solid #e2e8f0;
}

.profile-dropdown .dropdown-header {
  padding: 1.5rem;
  background: linear-gradient(135deg, #3D8D7A, #2d6a5a);
  color: white;
}

.profile-info {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.profile-avatar {
  width: 48px;
  height: 48px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.profile-details h4 {
  font-size: 1rem;
  font-weight: 600;
  margin-bottom: 0.25rem;
  color: white;
}

.profile-details p {
  font-size: 0.85rem;
  opacity: 0.9;
  color: white;
  margin: 0;
}

.dropdown-menu {
  padding: 0.5rem;
}

.dropdown-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem 1rem;
  border-radius: 8px;
  text-decoration: none;
  color: #1e293b;
  font-size: 0.9rem;
  font-weight: 500;
  transition: all 0.2s;
  cursor: pointer;
  border: none;
  background: none;
  width: 100%;
}

.dropdown-item:hover {
  background: #f1f5f9;
  color: #3D8D7A;
}

.dropdown-item svg {
  color: #64748b;
  transition: color 0.2s;
}

.dropdown-item:hover svg {
  color: #3D8D7A;
}

.dropdown-divider {
  height: 1px;
  background: #e2e8f0;
  margin: 0.5rem 0;
}

/* Sidebar */
.sidebar {
  position: fixed;
  top: 64px;
  left: 0;
  width: 80px;
  height: calc(100vh - 64px);
  background: #3D8D7A;
  border-right: none;
  z-index: 900;
  box-shadow: 2px 0 10px rgba(0, 0, 0, 0.05);
  overflow: visible;
}

.sidebar-nav {
  padding: 2rem 0.5rem 1rem 0.5rem;
}

.sidebar-item {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 56px;
  width: 56px;
  margin: 8px 0;
  border-radius: 12px;
  background: transparent;
  color: white;
  text-decoration: none;
  transition: background 0.2s, box-shadow 0.2s;
  cursor: pointer;
  border: none;
}

.sidebar-item.active {
  background: rgba(255,255,255,0.15);
  border: 2px solid #fff;
}

.sidebar-item:hover {
  background: rgba(255,255,255,0.22);
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.sidebar-icon {
  display: flex;
  align-items: center;
  justify-content: center;
}

.sidebar-icon svg {
  display: block;
}

.sidebar-tooltip {
  position: absolute;
  left: 60px;
  top: 50%;
  transform: translateY(-50%);
  background: #fff;
  color: #3D8D7A;
  padding: 4px 12px;
  border-radius: 6px;
  font-size: 14px;
  font-family: 'Inter', sans-serif;
  white-space: nowrap;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s;
  z-index: 10;
}

.sidebar-item:hover .sidebar-tooltip {
  opacity: 1;
  pointer-events: auto;
}

.sidebar-divider {
  height: 1px;
  background: rgba(255, 255, 255, 0.2);
  margin: 8px 12px;
}

.sidebar-logout {
  background: transparent;
  border: none;
  cursor: pointer;
  padding: 0;
  margin: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.sidebar-logout:hover {
  background: rgba(255, 255, 255, 0.1);
}

/* Rounded semi-transparent backgrounds for sidebar and navbar icons/buttons */
.rounded-bg {
  background: rgba(255,255,255,0.13);
  border-radius: 16px;
  transition: background 0.2s;
}

.rounded-bg:hover {
  background: rgba(255,255,255,0.22);
}

.logout-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 0.75rem;
  background: rgba(255, 255, 255, 0.1);
  border: none;
  border-radius: 6px;
  color: white;
  font-size: 0.8rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
}

.logout-btn:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: translateY(-1px);
}

/* Main Content */
.main-content {
  margin-top: 64px;
  margin-left: 80px;
  padding: 1.5rem;
  width: calc(100% - 80px);
  height: calc(100vh - 64px);
  min-height: calc(100vh - 64px);
  position: relative;
  background: #f8fafc;
  overflow-y: auto;
  overflow-x: hidden;
  scroll-behavior: smooth;
}

/* Custom scrollbar for main content */
.main-content::-webkit-scrollbar {
  width: 8px;
}

.main-content::-webkit-scrollbar-track {
  background: #f1f5f9;
  border-radius: 8px;
}

.main-content::-webkit-scrollbar-thumb {
  background: #3D8D7A;
  border-radius: 8px;
}

.main-content::-webkit-scrollbar-thumb:hover {
  background: #2d6a5a;
}

/* Custom Scrollbar Styling - Green Theme */
::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

::-webkit-scrollbar-track {
  background: #f1f5f9;
  border-radius: 10px;
}

::-webkit-scrollbar-thumb {
  background: linear-gradient(135deg, #3D8D7A, #20c997);
  border-radius: 10px;
  border: 1px solid #e2e8f0;
  transition: all 0.3s ease;
}

::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(135deg, #2d6a5a, #18a577);
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.3);
}

::-webkit-scrollbar-thumb:active {
  background: linear-gradient(135deg, #1e5a4a, #146e5a);
}

::-webkit-scrollbar-corner {
  background: #f1f5f9;
}

/* Firefox Scrollbar */
* {
  scrollbar-width: thin;
  scrollbar-color: #3D8D7A #f1f5f9;
}

/* Dark mode scrollbar */
.dark ::-webkit-scrollbar-track {
  background: #1a1d21;
}

.dark ::-webkit-scrollbar-thumb {
  background: linear-gradient(135deg, #20c997, #18a577);
  border: 1px solid #374151;
}

.dark ::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(135deg, #18a577, #146e5a);
  box-shadow: 0 2px 8px rgba(32, 201, 151, 0.3);
}

.dark ::-webkit-scrollbar-corner {
  background: #1a1d21;
}

/* Page Header */
.page-header {
  background: white;
  border-radius: 16px;
  padding: 1.5rem 2rem;
  margin-bottom: 1.5rem;
  border: 1px solid #e2e8f0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}

.dark .page-header {
  background: #23272b;
  border: 1px solid #20c997;
  box-shadow: 0 2px 8px rgba(0,0,0,0.25);
}

/* CSS Variables */
:root {
  --bg-primary: #FBFFE4;
  --bg-card: white;
  --text-primary: #1f2937;
  --text-secondary: #6b7280;
  --text-accent: #3D8D7A;
  --border-color: #A3D1C6;
  --accent-color: #3D8D7A;
  --accent-hover: #2f6b5c;
  --success-color: #B3D8A8;
  --danger-color: #dc3545;
  --shadow-light: rgba(61, 141, 122, 0.1);
}

.dark {
  --bg-primary: #1e2127;
  --bg-card: #2a2e36;
  --text-primary: #e5e7eb;
  --text-secondary: #9ca3af;
  --text-accent: #3D8D7A;
  --border-color: #3D8D7A;
  --accent-color: #3D8D7A;
  --accent-hover: #2f6b5c;
  --success-color: #22c55e;
  --danger-color: #dc3545;
  --shadow-light: rgba(0, 0, 0, 0.2);
}

/* Main Container */
.analytics-container {
  min-height: 100vh;
  background: #f8fafc;
  font-family: 'Inter', sans-serif;
}

.page-container {
  min-height: 100vh;
  background: #FBFFE4;
  padding: 1.5rem;
  font-family: 'Inter', sans-serif;
}

.dark .analytics-container {
  background: #181c20 !important;
}

.dark .main-content {
  background: #181c20 !important;
}

.dark .page-container {
  background: #181c20;
}

.main-wrapper {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  width: 100%;
}

/* Header Card */
.header-card {
  background: white;
  border-radius: 16px;
  padding: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}

.dark .header-card {
  background: #23272b;
  border: 1px solid #20c997;
  box-shadow: 0 2px 8px rgba(0,0,0,0.25);
}

.header-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 1rem;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.header-icon {
  width: 56px;
  height: 56px;
  background: linear-gradient(135deg, #3D8D7A, #2d6a5a);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
}

.header-title {
  font-size: 1.75rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 0.25rem;
}

.dark .header-title {
  color: #A3D1C6;
}

.header-subtitle {
  font-size: 0.95rem;
  color: #64748b;
}

.dark .header-subtitle {
  color: #A3D1C6;
}

/* Content Card */
.content-card {
  background: white;
  border-radius: 16px;
  padding: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.dark .content-card {
  background: #23272b;
  border: 1px solid #20c997;
  box-shadow: 0 2px 8px rgba(0,0,0,0.25);
}

/* Settings Cards */
.settings-card {
  padding: 1.25rem;
  border: 1px solid #A3D1C6;
  border-radius: 12px;
  background: #FBFFE4;
  transition: all 0.2s;
}

.dark .settings-card {
  background: #23272b;
  border: 1px solid #20c997;
  box-shadow: 0 2px 8px rgba(0,0,0,0.25);
}

.section-title {
  font-size: 1.1rem;
  font-weight: 600;
  color: #3D8D7A;
  margin: 0 0 0.5rem 0;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.dark .section-title {
  color: #A3D1C6;
}

.section-icon {
  color: #3D8D7A;
}

.dark .section-icon {
  color: #A3D1C6;
}

.section-subtitle {
  color: #6b7280;
  font-size: 0.875rem;
  margin: 0 0 1.5rem 0;
  font-weight: 400;
}

.dark .section-subtitle {
  color: #A3D1C6;
}

.settings-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.setting-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 0;
  border-bottom: 1px solid #A3D1C6;
  font-size: 0.9rem;
  color: #1f2937;
}

.dark .setting-item {
  color: #A3D1C6;
  border-bottom: 1px solid #20c997;
}

.setting-item:last-child {
  border-bottom: none;
}

.action-btn {
  background: #3D8D7A;
  color: white;
  border: none;
  border-radius: 8px;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
}

.dark .action-btn {
  background: #20c997;
  color: white;
}

.action-btn:hover {
  background: #2f6b5c;
  transform: translateY(-1px);
}

.dark .action-btn:hover {
  background: #A3D1C6;
}

/* Toggle Switch */
.switch {
  position: relative;
  display: inline-block;
  width: 44px;
  height: 24px;
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
  transition: .3s;
  border-radius: 24px;
}

.slider:before {
  position: absolute;
  content: "";
  height: 18px;
  width: 18px;
  left: 3px;
  bottom: 3px;
  background-color: white;
  transition: .3s;
  border-radius: 50%;
}

input:checked + .slider {
  background-color: var(--accent-color);
}

input:checked + .slider:before {
  transform: translateX(20px);
}

/* Danger Zone */
.danger-zone .section-title {
  color: var(--danger-color);
}

.danger-zone .section-subtitle {
  color: var(--danger-color);
}

.danger-text {
  color: var(--danger-color);
  font-weight: 500;
}

.danger-btn {
  background-color: #dc3545 !important;
  color: white !important;
  border: 1px solid #dc3545 !important;
  box-shadow: 0 2px 8px rgba(220, 53, 69, 0.2);
  font-weight: 600;
}

.dark .danger-btn {
  background-color: #dc3545 !important;
  color: white !important;
  border: 1px solid #dc3545 !important;
}

.danger-btn:hover {
  background-color: #c82333 !important;
  border-color: #c82333 !important;
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
.danger-zone {
  border-color: #d9534f !important;
  background: rgba(217, 83, 79, 0.05) !important;
}
.dark .danger-zone {
  background: rgba(217, 83, 79, 0.1) !important;
  border-color: #d9534f !important;
}

.danger-zone h2 {
  color: #d9534f !important;
}

.danger-zone .section-subtitle {
  color: #d9534f !important;
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
  margin-top: 2rem;
  text-align: center;
}

.about-card {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
  border: 1px solid #A3D1C6;
  max-width: 600px;
  margin: 0 auto;
}
.dark .about-card {
  background: #23272b;
  border-color: #20c997;
  box-shadow: 0 2px 8px rgba(0,0,0,0.25);
}

.about-card h2 {
  font-size: 1.125rem;
  font-weight: 600;
  color: #20c997;
  margin-bottom: 0.5rem;
}
.dark .about-card h2 {
  color: #A3D1C6;
}

.copyright-text {
  color: #6b7280;
  font-size: 0.9rem;
  margin: 0;
}
.dark .copyright-text {
  color: #A3D1C6;
}

/* Modal Styles */
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
  width: 100%;
  max-width: 500px;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  color: var(--primary-text-color);
}

.info-modal {
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
}

.close-btn:hover {
  color: var(--primary-text-color);
}

.modal-body {
  padding: 1.5rem;
}

.info-content {
  line-height: 1.6;
}

.info-content h4 {
  color: var(--accent-color);
  margin-top: 0;
  margin-bottom: 1rem;
}

.info-content h5 {
  color: var(--primary-text-color);
  margin-top: 1.5rem;
  margin-bottom: 0.5rem;
}

.info-content p {
  color: var(--secondary-text-color);
  margin-bottom: 1rem;
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

/* Avatar Upload */
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

/* Warning Box */
.warning-box {
  background: rgba(217, 83, 79, 0.1);
  border: 2px solid #d9534f;
  border-radius: 12px;
  padding: 1.5rem;
  text-align: center;
  margin-bottom: 1.5rem;
}

.warning-box svg {
  color: #d9534f;
  margin-bottom: 1rem;
}

.warning-box h4 {
  color: #d9534f;
  margin: 0.5rem 0;
}

.warning-box p {
  color: var(--secondary-text-color);
  margin: 0.5rem 0 0 0;
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

.btn-primary, .btn-secondary, .btn-danger {
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

.btn-danger {
  background: #d9534f;
  color: white;
}

.btn-danger:hover:not(:disabled) {
  background: #c9302c;
  transform: translateY(-1px);
}

.btn-danger:disabled {
  background: #ccc;
  cursor: not-allowed;
  transform: none;
}

/* Dark mode adjustments */
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

/* Modal Styles */
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
  width: 100%;
  max-width: 500px;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  color: var(--primary-text-color);
}

.info-modal {
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
}

.close-btn:hover {
  color: var(--primary-text-color);
}

.modal-body {
  padding: 1.5rem;
}

.info-content {
  line-height: 1.6;
}

.info-content h4 {
  color: var(--accent-color);
  margin-top: 0;
  margin-bottom: 1rem;
}

.info-content h5 {
  color: var(--primary-text-color);
  margin-top: 1.5rem;
  margin-bottom: 0.5rem;
}

.info-content p {
  color: var(--secondary-text-color);
  margin-bottom: 1rem;
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

/* Avatar Upload */
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

/* Warning Box */
.warning-box {
  background: rgba(217, 83, 79, 0.1);
  border: 2px solid #d9534f;
  border-radius: 12px;
  padding: 1.5rem;
  text-align: center;
  margin-bottom: 1.5rem;
}

.warning-box svg {
  color: #d9534f;
  margin-bottom: 1rem;
}

.warning-box h4 {
  color: #d9534f;
  margin: 0.5rem 0;
}

.warning-box p {
  color: var(--secondary-text-color);
  margin: 0.5rem 0 0 0;
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

/* Button Styles */
.btn-primary {
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  border: none;
  background: var(--accent-color);
  color: white;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.btn-primary:hover:not(:disabled) {
  background: var(--accent-hover);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.3);
}

.btn-primary:disabled {
  background: var(--accent-color);
  transform: none;
  opacity: 0.6;
}

.btn-secondary {
  background: var(--bg-primary);
  color: var(--text-primary);
  border: 1px solid var(--border-color);
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.dark .btn-secondary {
  background: var(--bg-primary);
  color: var(--text-primary);
  border: 1px solid var(--border-color);
}

.btn-secondary:hover {
  background: var(--accent-color);
  color: white;
  border-color: var(--accent-color);
}

/* Danger Button */
.btn-danger {
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  border: none;
  background: #dc3545;
  color: white;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.btn-danger:hover:not(:disabled) {
  background: #c82333;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(220, 53, 69, 0.3);
}

.btn-danger:disabled {
  background: #dc3545;
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
}

/* Responsive Design for Navbar */
@media (max-width: 1200px) {
  .main-content {
    padding: 1.5rem;
  }
}

@media (max-width: 1024px) {
  .main-content {
    padding: 1rem;
  }
  
  .navbar-center {
    gap: 0.25rem;
  }
  
  .nav-item {
    padding: 0.5rem 1rem;
    font-size: 0.7rem;
  }
}

@media (max-width: 768px) {
  .main-content {
    padding: 1rem;
  }
  
  .page-header {
    padding: 1rem;
    margin-bottom: 1.5rem;
  }
  
  .navbar-content {
    padding: 0 0.5rem;
  }
  
  .brand-name {
    display: none;
  }
  
  .page-container {
    padding: 1rem;
  }
  
  .header-card {
    padding: 1.5rem;
  }
  
  .header-left {
    gap: 1rem;
  }
  
  .header-icon {
    width: 40px;
    height: 40px;
  }
  
  .header-title {
    font-size: 1.3rem;
  }
  
  .content-card {
    padding: 1rem;
    gap: 1.5rem;
  }
  
  .settings-card {
    padding: 1rem;
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
}

/* Delete Modal Styles - Matching Settings.vue */
.delete-modal {
  max-width: 400px;
  border: 1px solid #dc3545;
  border-radius: 16px;
  overflow: hidden;
  background: white;
}

.delete-header {
  background: white;
  border-bottom: 2px solid #dc3545;
  padding: 1.5rem;
}

.delete-header h3 {
  color: #dc3545;
  font-weight: 700;
  font-size: 1.25rem;
  margin: 0;
}

.delete-header .close-btn {
  color: #20c997;
  font-size: 1.5rem;
  width: auto;
  height: auto;
}

.delete-warning-text {
  color: #dc3545;
  font-weight: 500;
  font-size: 1rem;
  margin-bottom: 1.5rem;
  line-height: 1.5;
}

.delete-label {
  color: #1f2937;
  font-weight: 500;
  font-size: 1rem;
  margin-bottom: 0.5rem;
}

.delete-input {
  border: 2px solid #dc3545 !important;
  color: #20c997;
  font-weight: 600;
  text-align: center;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.delete-input:focus {
  border-color: #dc3545 !important;
  box-shadow: 0 0 0 3px rgba(220, 53, 69, 0.1);
}

.dark .delete-modal {
  background: #2a2e36;
  border: 1px solid #dc3545;
}

.dark .delete-header {
  background: #2a2e36;
}

.dark .delete-warning-text {
  color: #dc3545;
}

.dark .delete-label {
  color: #e5e7eb;
}

.dark .delete-input {
  background: #2a2e36;
  color: #20c997;
  border: 2px solid #dc3545 !important;
}

.helper-text {
  font-size: 0.85rem;
  color: #6b7280;
  margin: 0.5rem 0;
  padding: 0.5rem;
  background: rgba(220, 53, 69, 0.05);
  border-left: 3px solid #dc3545;
  border-radius: 4px;
}

.dark .helper-text {
  color: #9ca3af;
  background: rgba(220, 53, 69, 0.1);
}

.helper-text strong {
  color: #dc3545;
  font-weight: 700;
}

/* Loading Container */
.loading-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  gap: 1rem;
  min-height: 150px;
}

/* Spinner */
.spinner {
  width: 50px;
  height: 50px;
  border: 4px solid rgba(220, 53, 69, 0.1);
  border-top: 4px solid #dc3545;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.loading-text {
  color: #dc3545;
  font-weight: 600;
  font-size: 1rem;
  text-align: center;
  margin: 0;
  animation: pulse 1.5s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.7; }
}

.dark .loading-text {
  color: #ff6b6b;
}

.dark .spinner {
  border: 4px solid rgba(255, 107, 107, 0.1);
  border-top: 4px solid #ff6b6b;
}

/* Helper Text */
.helper-text {
  font-size: 0.85rem;
  color: #6b7280;
  margin: 0.5rem 0;
  padding: 0.5rem;
  background: rgba(220, 53, 69, 0.05);
  border-left: 3px solid #dc3545;
  border-radius: 4px;
}

.dark .helper-text {
  color: #9ca3af;
  background: rgba(220, 53, 69, 0.1);
}

.helper-text strong {
  color: #dc3545;
  font-weight: 700;
}

/* Logout Confirmation Modal */
.logout-modal {
  max-width: 400px;
  border-radius: 16px;
  overflow: hidden;
  background: white;
  border: 2px solid #3D8D7A;
}

.dark .logout-modal {
  background: #2a2e36;
  border: 2px solid #20c997;
}

.logout-header {
  background: linear-gradient(135deg, #3D8D7A, #2d6a5a);
  color: white;
  padding: 1.5rem;
  text-align: center;
}

.dark .logout-header {
  background: linear-gradient(135deg, #20c997, #17a085);
}

.logout-header h3 {
  margin: 0;
  font-size: 1.25rem;
  font-weight: 600;
  color: white;
}

.logout-icon {
  margin-bottom: 1rem;
  display: flex;
  justify-content: center;
}

.logout-icon svg {
  color: #3D8D7A;
  animation: pulse 2s infinite;
}

.dark .logout-icon svg {
  color: #20c997;
}

@keyframes pulse {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.1); opacity: 0.8; }
}

.logout-message {
  font-size: 1.1rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.5rem;
  text-align: center;
}

.dark .logout-message {
  color: #e5e7eb;
}

.logout-submessage {
  font-size: 0.9rem;
  color: #6b7280;
  margin: 0;
  text-align: center;
}

.dark .logout-submessage {
  color: #9ca3af;
}

.logout-footer {
  padding: 1.5rem;
  display: flex;
  gap: 1rem;
  justify-content: center;
  border-top: 1px solid #e2e8f0;
  background: #f8fafc;
}

.dark .logout-footer {
  border-top: 1px solid #3D8D7A;
  background: #1e2127;
}

.btn-cancel {
  padding: 0.75rem 1.5rem;
  border: 2px solid #e2e8f0;
  background: white;
  color: #6b7280;
  border-radius: 8px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  min-width: 100px;
}

.dark .btn-cancel {
  background: #2a2e36;
  border-color: #3D8D7A;
  color: #9ca3af;
}

.btn-cancel:hover {
  border-color: #3D8D7A;
  color: #3D8D7A;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.2);
}

.dark .btn-cancel:hover {
  border-color: #20c997;
  color: #20c997;
}

.btn-logout {
  padding: 0.75rem 1.5rem;
  border: none;
  background: linear-gradient(135deg, #dc3545, #c82333);
  color: white;
  border-radius: 8px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  min-width: 100px;
}

.btn-logout:hover {
  background: linear-gradient(135deg, #c82333, #a71e2a);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(220, 53, 69, 0.3);
}

.btn-logout:disabled {
  background: #ccc;
  cursor: not-allowed;
  transform: none;
  opacity: 0.6;
}

.logout-spinner {
  width: 12px;
  height: 12px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top: 2px solid white;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
  display: inline-block;
  margin-right: 0.5rem;
}

.btn-logout .loading-text {
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 0.9rem;
}
</style>