<template>
  <div class="dashboard-container">
    <!-- Top Navigation Bar (Clean) -->
    <nav class="top-navbar">
      <div class="navbar-content">
        <!-- Left: Logo and Brand -->
        <div class="navbar-left">
          <div class="brand-logo">
            <img src="@/assets/LOGO WAY BG.png" alt="DigiCheck" class="logo-img" />
            <span class="brand-name">DigiCheck</span>
          </div>
        </div>
        <!-- Center: Empty space for clean look -->
        <div class="navbar-center">
        </div>
        
        <!-- Right: User Profile and Notifications -->
        <div class="navbar-right">
          <!-- Notification Bell -->
          <div class="notif-wrapper">
            <button class="nav-icon-btn rounded-bg" @click="toggleNotifDropdown" aria-label="Notifications">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
                <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
              </svg>
              <span v-if="notifications.length" class="notification-badge">{{ notifications.length }}</span>
            </button>
            
            <!-- Notification Dropdown -->
            <div v-if="showNotifDropdown" class="notification-dropdown">
              <div class="dropdown-header">
                <h3>Notifications</h3>
              </div>
              <div class="notification-list">
                <div v-if="notifications.length === 0" class="no-notifications">
                  No new notifications
                </div>
                <div v-for="notif in notifications" :key="notif.id" class="notification-item" @click="handleNotificationClick(notif)">
                  <div class="notif-content">
                    <h4>{{ notif.title }}</h4>
                    <p>{{ notif.body }}</p>
                    <span class="notif-time">{{ notif.date }}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
          
          <!-- User Profile -->
          <div class="user-profile-wrapper">
            <div class="user-profile rounded-bg" @click="toggleProfileDropdown">
              <div class="user-avatar">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                  <circle cx="12" cy="7" r="4"></circle>
                </svg>
              </div>
              <span class="user-name">{{ fullName }}</span>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" class="dropdown-arrow">
                <path d="M7 10l5 5 5-5z"/>
              </svg>
            </div>
            
            <!-- Profile Dropdown -->
            <div v-if="showProfileDropdown" class="profile-dropdown">
              <div class="dropdown-header" style="padding: 1.5rem; background: linear-gradient(135deg, #3D8D7A, #2d6a5a); color: white; border-bottom: none; border: none;">
                <div class="profile-info">
                  <div class="profile-avatar">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                      <circle cx="12" cy="7" r="4"></circle>
                    </svg>
                  </div>
                  <div class="profile-details">
                    <h4>{{ fullName }}</h4>
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
                
                <button @click="logout" class="dropdown-item logout-btn">
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

    <!-- Sidebar Navigation - Custom Tooltip Labels on Hover -->
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
        
        <button @click="logout" class="sidebar-item sidebar-logout rounded-bg">
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
              <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor">
                <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
              </svg>
            </div>
            <div>
              <h1 class="header-title">Teacher Messages</h1>
              <p class="header-subtitle">Connect with your students and manage communication</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Loading Overlay -->
      <div v-if="isLoading" class="loading-overlay">
        <div class="loading-content">
          <div class="loading-spinner-container">
            <div class="loading-spinner"></div>
          </div>
          <p class="loading-text">{{ loadingMessage || 'Loading...' }}</p>
        </div>
      </div>

      <!-- Content Area -->

    <!-- Filter and Search Controls -->
    <div class="controls-section">
      <div class="search-box">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
          <path d="M9.5,3A6.5,6.5 0 0,1 16,9.5C16,11.11 15.41,12.59 14.44,13.73L14.71,14H15.5L20.5,19L19,20.5L14,15.5V14.71L13.73,14.44C12.59,15.41 11.11,16 9.5,16A6.5,6.5 0 0,1 3,9.5A6.5,6.5 0 0,1 9.5,3M9.5,5C7,5 5,7 5,9.5C5,12 7,14 9.5,14C12,14 14,12 14,9.5C14,7 12,5 9.5,5Z" />
        </svg>
        <input 
          type="text" 
          v-model="searchQuery" 
          placeholder="Search students or sections..."
          class="search-input"
        />
      </div>
      <div class="filter-tabs">
        <button 
          :class="['filter-tab', { 'active': currentTab === 'students' && !showArchive }]"
          @click="currentTab = 'students'; showArchive = false; showBroadcastHistory = false"
        >
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
            <circle cx="12" cy="7" r="4"/>
          </svg>
          My Students
        </button>
        <button 
          :class="['filter-tab', { 'active': currentTab === 'broadcast' && !showBroadcastHistory }]"
          @click="currentTab = 'broadcast'; showArchive = false; showBroadcastHistory = false"
        >
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M10 3h4a8 8 0 0 1 0 16v-2.5"/>
            <path d="M6 14c2-2 3-3.5 3-6"/>
          </svg>
          Broadcast
        </button>
        <button 
          :class="['filter-tab', { 'active': showArchive }]"
          @click="currentTab = 'students'; showArchive = true; showBroadcastHistory = false"
        >
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="21 8 21 21 3 21 3 8"></polyline>
            <rect x="1" y="3" width="22" height="5"></rect>
            <line x1="10" y1="12" x2="14" y2="12"></line>
          </svg>
          Archive
        </button>
      </div>
    </div>

    <!-- Grade Level Filter (only show for students tab and not in archive) -->
    <div v-if="currentTab === 'students' && !showArchive && !showStudentsInSection" class="grade-filters">
      <div class="grade-filter-tabs">
        <button 
          :class="['grade-tab', { 'active': selectedGradeFilter === 'all' }]"
          @click="selectedGradeFilter = 'all'"
        >
          All Grades
        </button>
        <button 
          v-for="grade in availableGrades" 
          :key="grade"
          :class="['grade-tab', { 'active': selectedGradeFilter === grade }]"
          @click="selectedGradeFilter = grade"
        >
          Grade {{ grade }}
        </button>
      </div>
    </div>

    <!-- Debug Info -->
    <div v-if="debugMode" class="debug-section">
      <div class="debug-header">
        <h3>Debug Information</h3>
        <button @click="debugMode = false" class="close-debug-btn">×</button>
      </div>
      <div class="debug-content">
        <p><strong>Auth User ID:</strong> {{ currentUser?.id || 'None' }}</p>
        <p><strong>Teacher Profile ID:</strong> {{ teacherProfile?.id || 'None' }}</p>
        <p><strong>Teacher ID:</strong> {{ currentTeacherId || 'None' }}</p>
        <p><strong>Teacher Name:</strong> {{ teacherProfile?.full_name || 'None' }}</p>
        <p><strong>Contacts Count:</strong> {{ studentContacts.length }}</p>
      </div>
    </div>

    <!-- Main Content Area -->
    <div class="content-area">
        <!-- Students Tab -->
        <div v-if="currentTab === 'students' && !showArchive" class="tab-content">
          <!-- Section Students View -->
          <div v-if="showStudentsInSection" class="section-students-view">
            <div class="section-students-header">
              <button class="back-to-sections-btn" @click="backToSections()">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <line x1="19" y1="12" x2="5" y2="12"></line>
                  <polyline points="12 19 5 12 12 5"></polyline>
                </svg>
                Back to Subjects
              </button>
              <div class="section-students-info">
                <h3>{{ selectedSectionView?.subject_name }} - {{ selectedSectionView?.section_name }}</h3>
                <div class="section-students-meta">
                  <span class="section-code">{{ selectedSectionView?.section_code }}</span>
                  <span class="grade-info">Grade {{ selectedSectionView?.grade_level }}</span>
                  <span class="student-count">{{ selectedSectionView?.students.length }} enrolled students</span>
                </div>
              </div>
              <button 
                class="section-broadcast-btn" 
                @click="openBroadcastModal(); broadcastSection = selectedSectionView?.section_id"
              >
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M3 11l18-5v12L3 14v-3z"/>
                </svg>
                Send Broadcast
              </button>
            </div>

            <div class="section-students-list">
              <div 
                v-for="student in selectedSectionView?.students || []" 
                :key="`${student.student_id}-${selectedSectionView?.section_id}`"
                :class="['section-student-item', { 'has-unread': student.unread_count > 0 }]"
                @click="startChatWithStudent(student)"
              >
                <div class="section-student-info">
                  <div class="section-student-avatar">
                    <span>{{ student.student_name?.[0] || 'S' }}</span>
                    <span v-if="studentPresence[student.auth_user_id]?.is_online" class="online-indicator" title="Online now"></span>
                  </div>
                  <div class="section-student-details">
                    <h4 class="section-student-name">{{ student.student_name }}</h4>
                    <p class="section-student-email">{{ student.student_email }}</p>
                    <p class="section-student-id">Student ID: {{ student.student_number }}</p>
                    <p class="presence-status">{{ getPresenceStatus(student.auth_user_id) }}</p>
                    <p class="section-last-message">{{ student.last_message || `Enrolled ${formatDate(student.enrolled_date)}` }}</p>
                  </div>
                </div>
                <div class="section-message-status">
                  <span v-if="student.unread_count > 0" class="section-unread-badge">{{ student.unread_count }}</span>
                  <span class="section-last-time">{{ formatTime(student.last_message_date || student.enrolled_date) }}</span>
                  <div class="section-chat-icon">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
                    </svg>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Sections Overview -->
          <div v-else>
            <!-- Removed redundant search bar and section filter -->
            
            <!-- Students grouped by section -->
            <div v-if="groupedStudents.length === 0" class="empty-state">
              <div class="empty-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
                  <circle cx="8.5" cy="7" r="4"/>
                </svg>
              </div>
              <p>No enrolled students found</p>
              <span class="empty-subtext">Students who join your sections will appear here.</span>
            </div>

            <div v-else class="sections-overview">
              <div v-for="(section, idx) in (groupedStudents as any[])" :key="section.section_id" class="section-overview-card" @click="viewSectionStudents(section)">
                <!-- Subject Icon and Title -->
                <div class="section-card-header">
                  <div class="section-icon" :style="{ background: getSectionIconColor(idx) }">
                    <span>{{ section.subject_name.charAt(0) }}</span>
                  </div>
                  <div class="section-title-area">
                    <h3 class="section-title">{{ section.subject_name }}</h3>
                    <p class="section-grade">Grade {{ section.grade_level }}</p>
                  </div>
                  <div class="section-options-container">
                    <button class="section-options-btn" @click.stop="toggleSectionOptions(section.section_id)">
                      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="12" r="1"></circle>
                        <circle cx="12" cy="5" r="1"></circle>
                        <circle cx="12" cy="19" r="1"></circle>
                      </svg>
                    </button>
                    <!-- Dropdown Menu -->
                    <div v-if="openSectionDropdown === section.section_id" class="section-options-dropdown" @click.stop>
                      <button class="dropdown-option delete" @click="deleteSectionConfirm(section)">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                          <polyline points="3 6 5 6 21 6"></polyline>
                          <path d="m19 6-1 14c0 1-1 2-2 2H8c-1 0-2-1-2-2L5 6"></path>
                          <path d="m10 11 0 6"></path>
                          <path d="m14 11 0 6"></path>
                          <path d="M7 6V4c0-1 1-2 2-2h6c0-1 1-2 2-2v2"></path>
                        </svg>
                        Delete Section
                      </button>
                      <button class="dropdown-option archive" @click="archiveSectionConfirm(section)">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                          <rect x="2" y="3" width="20" height="5"></rect>
                          <path d="m4 8 16 0 0 9a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V8Z"></path>
                          <path d="m10 12 4 0"></path>
                        </svg>
                        Archive Section
                      </button>
                    </div>
                  </div>
                </div>

                <!-- Section Stats -->
                <div class="section-stats">
                  <span class="section-students-count">{{ section.students.length }} sections • {{ section.students.length }} students</span>
                </div>

                <!-- Section Code -->
                <div class="section-code-display">
                  <div class="section-code-label">SECTION CODE</div>
                  <div class="section-code-value" @click.stop="copyToClipboard(section.section_code)">
                    {{ section.section_code }}
                    <button class="copy-code-btn">
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                        <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                      </svg>
                      Copy
                    </button>
                  </div>
                </div>

                <!-- Quick Actions -->
                <div class="section-card-actions">
                  <span class="students-count-badge">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
                      <circle cx="8.5" cy="7" r="4"/>
                      <path d="M20 8v6M23 11h-6"/>
                    </svg>
                    {{ section.students.length }} students
                  </span>
                  <button class="broadcast-quick-btn" @click.stop="openBroadcastModal(); broadcastSection = section.section_id">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon>
                    </svg>
                    Broadcast
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Archive Tab -->
        <div v-else-if="currentTab === 'students' && showArchive" class="tab-content">

          <div v-if="archivedChats.length === 0" class="empty-state">
            <div class="empty-icon">
              <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="21 8 21 21 3 21 3 8"></polyline>
                <rect x="1" y="3" width="22" height="5"></rect>
                <line x1="10" y1="12" x2="14" y2="12"></line>
              </svg>
            </div>
            <p>No archived conversations</p>
            <span class="empty-subtext">Archived chats will appear here</span>
          </div>

          <div v-else class="students-list">
            <div 
              v-for="student in archivedChats" 
              :key="student.student_id"
              class="student-item archived"
            >
              <div class="student-info" @click="startChatWithStudent(student)">
                <div class="student-avatar">
                  <span>{{ student.student_name?.[0] || 'S' }}</span>
                </div>
                <div class="student-details">
                  <h4 class="student-name">Student: {{ student.student_name }}</h4>
                  <p class="student-email">{{ student.student_email }}</p>
                  <p class="last-message">{{ student.last_message }}</p>
                </div>
              </div>
              <button class="restore-btn" @click="restoreChat(student.student_id)">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <polyline points="23 4 23 10 17 10"></polyline>
                  <path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"></path>
                </svg>
                Restore
              </button>
            </div>
          </div>
        </div>

        <!-- Broadcast Tab -->
        <div v-else-if="currentTab === 'broadcast'" class="tab-content">
          <div v-if="!showBroadcastHistory" class="broadcast-section">
            <!-- Simple Broadcast Header -->
            <div class="simple-broadcast-header">
              <div class="simple-header-content">
                <div class="simple-header-icon">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M3 11l18-5v12L3 14v-3z"/>
                    <circle cx="12" cy="12" r="2"/>
                  </svg>
                </div>
                <div class="simple-header-text">
                  <h2>Send Broadcast Message</h2>
                  <p>Announce to your entire section instantly</p>
                </div>
              </div>
              <button class="simple-history-btn" @click="showBroadcastHistory = true">
                <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <circle cx="12" cy="12" r="10"></circle>
                  <polyline points="12 6 12 12 16 14"></polyline>
                </svg>
                View History
              </button>
            </div>
            
            <!-- Full Screen Enhanced Broadcast Form -->
            <div class="broadcast-form-fullscreen">
              <div class="broadcast-form-columns">
                <!-- Left Column: Form Fields -->
                <div class="broadcast-form-left">
                  <!-- Section Selection -->
                  <div class="broadcast-form-row">
                    <div class="form-group-compact">
                      <label>
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                          <path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
                          <circle cx="8.5" cy="7" r="4"/>
                          <path d="M20 8v6M23 11h-6"/>
                        </svg>
                        Select Section
                      </label>
                      <select v-model="broadcastSection" class="form-input-compact">
                        <option value="" disabled>Choose a section to broadcast...</option>
                        <option v-for="section in uniqueSections" :key="section.section_id" :value="section.section_id">
                          {{ section.section_name }} - {{ section.subject_name }} (Grade {{ section.grade_level }})
                        </option>
                      </select>
                    </div>
                  </div>

                  <!-- Message Input -->
                  <div class="broadcast-form-row">
                    <div class="form-group-compact">
                      <label>
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                          <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
                        </svg>
                        Your Message
                      </label>
                      <textarea 
                        v-model="broadcastMessage" 
                        placeholder="Type your announcement here... Make it clear and engaging for your students."
                        class="form-textarea-compact"
                        maxlength="500"
                      ></textarea>
                      <div class="char-count-inline">{{ broadcastMessage.length }} / 500 characters</div>
                    </div>
                  </div>

                  <!-- File Upload Row -->
                  <div class="broadcast-form-row">
                    <div class="form-group-compact">
                      <label>
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                          <path d="m21.44 11.05-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48"/>
                        </svg>
                        Attachments (Optional)
                      </label>
                    </div>
                    <input 
                      type="file" 
                      ref="broadcastFileInput" 
                      @change="handleBroadcastFileSelect" 
                      multiple 
                      accept="image/*,.pdf,.doc,.docx,.xls,.xlsx,.ppt,.pptx,.txt"
                      style="display: none"
                    />
                    <button class="upload-button-inline" @click="($refs.broadcastFileInput as HTMLInputElement)?.click()">
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                        <polyline points="17 8 12 3 7 8"></polyline>
                        <line x1="12" y1="3" x2="12" y2="15"></line>
                      </svg>
                      Add Files
                    </button>
                  </div>

                  <!-- Action Buttons -->
                  <div class="action-buttons-fullwidth">
                    <button class="btn-cancel-full" @click="cancelBroadcast()">
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <line x1="18" y1="6" x2="6" y2="18"></line>
                        <line x1="6" y1="6" x2="18" y2="18"></line>
                      </svg>
                      <span>Cancel</span>
                    </button>
                    <button 
                      class="btn-send-full"
                      @click="sendBroadcastMessage"
                      :disabled="!broadcastMessage.trim() || !broadcastSection"
                    >
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <line x1="22" y1="2" x2="11" y2="13"></line>
                        <polygon points="22 2 15.46 22 11 13 2 9.54 22 2"></polygon>
                      </svg>
                      <span>Send Broadcast</span>
                    </button>
                  </div>
                </div>

                <!-- Right Column: Preview & Attachments -->
                <div class="broadcast-form-right">
                  <!-- Preview Section -->
                  <div class="preview-section-compact">
                    <h4>Preview</h4>
                    <div v-if="broadcastMessage.trim()" class="preview-content">
                      <p>{{ broadcastMessage }}</p>
                    </div>
                    <div v-else class="preview-placeholder">
                      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                        <polyline points="14 2 14 8 20 8"/>
                        <line x1="16" y1="13" x2="8" y2="13"/>
                        <line x1="16" y1="17" x2="8" y2="17"/>
                      </svg>
                      <span>Your message preview will appear here</span>
                    </div>
                  </div>

                  <!-- Attachments Section -->
                  <div class="attachments-section-compact">
                    <h4>Attachments</h4>
                    <div v-if="broadcastAttachments.length > 0" class="attachments-preview-grid">
                      <div v-for="(att, idx) in broadcastAttachments" :key="idx" class="attachment-preview-card">
                        <div class="attachment-preview-thumb">
                          <img v-if="att.type === 'image'" :src="att.url" class="attachment-preview-img" />
                          <div v-else class="attachment-file-preview">
                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                              <path d="M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/>
                              <polyline points="13 2 13 9 20 9"/>
                            </svg>
                          </div>
                        </div>
                        <div class="attachment-preview-info">
                          <p class="attachment-preview-name">{{ att.name }}</p>
                          <span class="attachment-preview-size">{{ att.size }}</span>
                        </div>
                        <button @click="broadcastAttachments.splice(idx, 1)" class="attachment-remove-btn">
                          <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <line x1="18" y1="6" x2="6" y2="18"></line>
                            <line x1="6" y1="6" x2="18" y2="18"></line>
                          </svg>
                        </button>
                      </div>
                    </div>
                    <div v-else class="attachments-placeholder">
                      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="m21.44 11.05-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48"/>
                      </svg>
                      <span>No attachments selected</span>
                    </div>
                  </div>

                  <!-- Ready Status -->
                  <div v-if="broadcastMessage.trim() && broadcastSection" class="ready-status">
                    <div class="ready-indicator">
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                        <polyline points="22 4 12 14.01 9 11.01"></polyline>
                      </svg>
                      Ready to broadcast
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Broadcast History -->
          <div v-else class="broadcast-history">
            <!-- Broadcast Section Messages View -->
            <div v-if="showBroadcastMessages" class="broadcast-messages-view">
              <div class="broadcast-messages-header-card">
                <button class="back-to-history-btn" @click="backToBroadcastHistory()">
                  <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="19" y1="12" x2="5" y2="12"></line>
                    <polyline points="12 19 5 12 12 5"></polyline>
                  </svg>
                  Back to Overview
                </button>
                <div class="broadcast-section-details">
                  <div class="section-badge">
                    <div class="section-badge-icon">
                      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M22 10v6M2 10l10-5 10 5-10 5z"/>
                        <path d="M6 12v5c3 3 9 3 12 0v-5"/>
                      </svg>
                    </div>
                    <div class="section-badge-content">
                      <h3>{{ selectedBroadcastSection?.subject_name }}</h3>
                      <p class="section-meta">{{ selectedBroadcastSection?.section_name }} • {{ selectedBroadcastSection?.section_code }}</p>
                      <p class="section-stats">Grade {{ selectedBroadcastSection?.grade_level }} • {{ selectedBroadcastSection?.broadcasts.length }} announcements</p>
                    </div>
                  </div>
                </div>
              </div>

              <div class="broadcast-messages-list-enhanced">
                <div v-for="broadcast in selectedBroadcastSection?.broadcasts || []" :key="broadcast.id" class="broadcast-message-card-enhanced">
                  <div class="broadcast-card-header-enhanced">
                    <div class="broadcast-timestamp-enhanced">
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <circle cx="12" cy="12" r="10"></circle>
                        <polyline points="12 6 12 12 16 14"></polyline>
                      </svg>
                      <span>{{ formatDate(broadcast.sent_at) }} at {{ formatTime(broadcast.sent_at) }}</span>
                    </div>
                    <div class="broadcast-actions-dropdown">
                      <button class="dropdown-trigger" @click.stop="toggleBroadcastOptions(broadcast.id)">
                        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                          <circle cx="12" cy="12" r="1"></circle>
                          <circle cx="12" cy="5" r="1"></circle>
                          <circle cx="12" cy="19" r="1"></circle>
                        </svg>
                      </button>
                      <div v-if="showBroadcastOptionsMenu === broadcast.id" class="dropdown-menu" @click.stop>
                        <button class="dropdown-item" @click="editBroadcast(broadcast)">
                          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path>
                            <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>
                          </svg>
                          Edit Message
                        </button>
                        <button class="dropdown-item" @click="archiveBroadcast(broadcast.id)">
                          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <polyline points="21 8 21 21 3 21 3 8"></polyline>
                            <rect x="1" y="3" width="22" height="5"></rect>
                            <line x1="10" y1="12" x2="14" y2="12"></line>
                          </svg>
                          Archive
                        </button>
                        <div class="dropdown-divider"></div>
                        <button class="dropdown-item danger" @click="deleteBroadcast(broadcast.id)">
                          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <polyline points="3 6 5 6 21 6"></polyline>
                            <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2 2h4a2 2 0 0 1 2 2v2"></path>
                          </svg>
                          Delete
                        </button>
                      </div>
                    </div>
                  </div>
                  
                  <div class="broadcast-content-enhanced">
                    <div class="broadcast-message-section">
                      <div class="broadcast-icon-badge-enhanced">
                        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                          <path d="M3 11l18-5v12L3 14v-3z"/>
                        </svg>
                      </div>
                      <p class="broadcast-message-text-enhanced">{{ broadcast.message }}</p>
                    </div>
                    
                    <!-- Enhanced Attachments with Full Screen Utilization -->
                    <div v-if="broadcast.attachments && broadcast.attachments.length > 0" class="attachments-section-enhanced">
                      <div class="attachments-header-enhanced">
                        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                          <path d="m21.44 11.05-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48"/>
                        </svg>
                        <span>{{ broadcast.attachments.length }} attachment{{ broadcast.attachments.length > 1 ? 's' : '' }}</span>
                      </div>
                      
                      <!-- Enhanced Attachments Gallery with Full Space Usage -->
                      <div class="attachments-gallery-enhanced">
                        <div v-for="(att, idx) in broadcast.attachments" :key="idx" class="attachment-item-enhanced" @click="viewAttachment(att)">
                          <div v-if="att.type === 'image'" class="image-attachment-enhanced">
                            <img :src="att.url" class="attachment-image-full" :alt="att.name" />
                            <div class="image-overlay-enhanced">
                              <div class="overlay-content">
                                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                  <circle cx="11" cy="11" r="8"></circle>
                                  <path d="m21 21-4.35-4.35"></path>
                                </svg>
                                <span>View Full Size</span>
                              </div>
                            </div>
                            <div class="image-info-badge">
                              <span class="image-filename">{{ att.name }}</span>
                            </div>
                          </div>
                          
                          <div v-else class="file-attachment-enhanced">
                            <div class="file-preview-enhanced">
                              <div class="file-icon-large">
                                <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                  <path d="M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/>
                                  <polyline points="13 2 13 9 20 9"/>
                                </svg>
                              </div>
                              <div class="file-type-badge">{{ att.name.split('.').pop()?.toUpperCase() || 'FILE' }}</div>
                            </div>
                            <div class="file-details-enhanced">
                              <p class="file-name-enhanced">{{ att.name }}</p>
                              <span class="file-size-enhanced">{{ att.size || 'Unknown size' }}</span>
                              <button class="download-btn-enhanced" @click.stop="downloadAttachment(att)">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                  <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                                  <polyline points="7 10 12 15 17 10"></polyline>
                                  <line x1="12" y1="15" x2="12" y2="3"></line>
                                </svg>
                                Download
                              </button>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Simple Broadcast History Overview -->
            <div v-else>
              <div class="simple-history-header">
                <div class="simple-history-content">
                  <button class="simple-back-btn" @click="showBroadcastHistory = false">
                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <line x1="19" y1="12" x2="5" y2="12"></line>
                      <polyline points="12 19 5 12 12 5"></polyline>
                    </svg>
                    Back to Broadcast
                  </button>
                  <div class="simple-history-info">
                    <div class="simple-history-icon">
                      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <circle cx="12" cy="12" r="10"></circle>
                        <polyline points="12 6 12 12 16 14"></polyline>
                      </svg>
                    </div>
                    <div>
                      <h2>Broadcast History</h2>
                      <p>View and manage all your section announcements</p>
                    </div>
                  </div>
                  <div class="simple-stats-badge">
                    <span class="simple-stats-number">{{ groupedBroadcasts.length }}</span>
                    <span class="simple-stats-label">SECTIONS</span>
                  </div>
                </div>
              </div>

              <div v-if="groupedBroadcasts.length === 0" class="empty-state-modern">
                <div class="empty-illustration">
                  <svg xmlns="http://www.w3.org/2000/svg" width="120" height="120" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                    <path d="M3 11l18-5v12L3 14v-3z"/>
                    <circle cx="12" cy="12" r="2"/>
                  </svg>
                </div>
                <h3>No Broadcasts Yet</h3>
                <p>Your sent announcements will appear here</p>
                <button class="create-broadcast-btn" @click="showBroadcastHistory = false">
                  <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M12 5v14M5 12h14"/>
                  </svg>
                  Create Your First Broadcast
                </button>
              </div>

              <div v-else class="history-grid-enhanced-fullwidth">
                <div v-for="section in (groupedBroadcasts as any[])" :key="section.section_id" class="history-card-enhanced-wide" @click="viewBroadcastSection(section)">
                  <div class="card-layout-horizontal">
                    <!-- Left Section: Subject Info -->
                    <div class="subject-info-section">
                      <div class="subject-avatar-enhanced">
                        <span>{{ section.subject_name.charAt(0) }}</span>
                      </div>
                      <div class="subject-details-enhanced">
                        <h3>{{ section.subject_name }}</h3>
                        <div class="section-badges-enhanced">
                          <span class="section-badge">{{ section.section_name }}</span>
                          <span class="code-badge">{{ section.section_code }}</span>
                          <span class="grade-badge">Grade {{ section.grade_level }}</span>
                        </div>
                      </div>
                    </div>

                    <!-- Middle Section: Latest Broadcast Content -->
                    <div class="latest-message-content">
                      <div v-if="section.broadcasts && section.broadcasts.length > 0" class="latest-broadcast-enhanced">
                        <div class="latest-indicator">
                          <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <circle cx="12" cy="12" r="10"></circle>
                            <polyline points="12 6 12 12 16 14"></polyline>
                          </svg>
                          <span>Latest: {{ formatDate(section.broadcasts[0].sent_at) }}</span>
                        </div>
                        
                        <div class="latest-content-enhanced">
                          <p class="latest-message-text">{{ section.broadcasts[0].message }}</p>
                          
                          <!-- Compact Attachments Preview -->
                          <div v-if="section.broadcasts[0].attachments && section.broadcasts[0].attachments.length > 0" class="attachments-preview-compact">
                            <div class="attachments-row">
                              <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="m21.44 11.05-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48"/>
                              </svg>
                              <span class="attachment-summary-icon">{{ section.broadcasts[0].attachments.length }} attachment{{ section.broadcasts[0].attachments.length > 1 ? 's' : '' }}</span>
                              <div class="attachments-mini-preview">
                                <div v-for="(att, idx) in section.broadcasts[0].attachments.slice(0, 3)" :key="idx" class="mini-attachment">
                                  <div v-if="att.type === 'image'" class="mini-image">
                                    <img :src="att.url" :alt="att.name" />
                                  </div>
                                  <div v-else class="mini-file">
                                    <span>{{ att.name.split('.').pop()?.toUpperCase() || 'FILE' }}</span>
                                  </div>
                                </div>
                                <div v-if="section.broadcasts[0].attachments.length > 3" class="mini-more">
                                  +{{ section.broadcasts[0].attachments.length - 3 }}
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>

                    <!-- Right Section: Stats and Action -->
                    <div class="stats-and-action-section">
                      <div class="broadcast-stats-enhanced">
                        <div class="stats-number">{{ section.broadcasts.length }}</div>
                        <div class="stats-label">broadcasts</div>
                      </div>
                      <div class="view-arrow">
                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                          <polyline points="9 18 15 12 9 6"></polyline>
                        </svg>
                      </div>
                    </div>
                  </div>
                </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Individual Chat Modal -->
    <div v-if="isModalOpen" class="modal-overlay" @click.self="closeModal">
      <div class="modal-content">
        <div class="modal-header">
          <button @click="closeModal" class="close-btn">&times;</button>
          <div class="header-info">
            <div class="student-avatar">
              <span>{{ activeConversation?.student_name?.[0] || 'S' }}</span>
            </div>
            <div class="header-details">
              <h2 class="modal-title">Student: {{ activeConversation?.student_name || 'Student' }}</h2>
              <span class="section-info">{{ activeConversation?.subject_name }}</span>
            </div>
          </div>
        </div>
        <div class="modal-body">
          <!-- Loading indicator for messages -->
          <div v-if="loadingMessages" class="messages-loading">
            <div class="messages-loading-spinner"></div>
            <p>Loading messages...</p>
          </div>
          
          <div v-else class="messages-container" ref="messagesContainer">
            <div 
              v-for="message in currentMessages" 
              :key="message.id" 
              :class="['message-bubble', { 'sent': message.sender_id === currentTeacherId, 'received': message.sender_id !== currentTeacherId }]"
            >
              <p class="message-text">{{ message.message_text }}</p>
              
              <!-- Display attachments if any -->
              <div v-if="message.attachments && message.attachments.length > 0" class="message-attachments">
                <div v-for="(attachment, idx) in message.attachments" :key="idx" class="attachment-item">
                  <!-- Image preview with better visibility -->
                  <div v-if="attachment.type === 'image'" class="attachment-image-container" @click="viewAttachment(attachment)">
                    <img :src="attachment.url" class="attachment-image" alt="Attachment" />
                    <div class="image-overlay">
                      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                        <circle cx="12" cy="12" r="3"></circle>
                      </svg>
                      <span>Click to view</span>
                    </div>
                  </div>
                  
                  <!-- File download -->
                  <div v-else class="attachment-file">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/>
                      <polyline points="13 2 13 9 20 9"/>
                    </svg>
                    <span>{{ attachment.name }}</span>
                    <div class="attachment-actions">
                      <button @click="viewAttachment(attachment)" class="attachment-btn" title="View">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                          <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                          <circle cx="12" cy="12" r="3"></circle>
                        </svg>
                      </button>
                      <button @click="downloadAttachment(attachment)" class="attachment-btn" title="Download">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                          <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                          <polyline points="7 10 12 15 17 10"></polyline>
                          <line x1="12" y1="15" x2="12" y2="3"></line>
                        </svg>
                      </button>
                    </div>
                  </div>
                </div>
              </div>

              <div class="message-footer">
                <span class="message-time">{{ formatTime(message.sent_at) }}</span>
                
                <!-- Message Status for Sent Messages -->
                <span v-if="message.sender_id === currentTeacherId" class="message-status">
                  <span v-if="message.is_read" class="status-read">
                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <polyline points="20 6 9 17 4 12"></polyline>
                    </svg>
                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-left: -8px;">
                      <polyline points="20 6 9 17 4 12"></polyline>
                    </svg>
                    <span v-if="message.read_at" class="read-time">Read {{ formatTime(message.read_at) }}</span>
                  </span>
                  <span v-else class="status-sent">
                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <polyline points="20 6 9 17 4 12"></polyline>
                    </svg>
                    Sent
                  </span>
                </span>
              </div>
            </div>
            <div v-if="currentMessages.length === 0" class="no-messages">
              <p>No messages yet. Start the conversation!</p>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <!-- Attachment Preview -->
          <div v-if="messageAttachments.length > 0" class="attachments-preview">
            <div class="attachment-preview-list">
              <div v-for="(att, idx) in messageAttachments" :key="idx" class="attachment-preview-item">
                <img v-if="att.type === 'image'" :src="att.url" class="attachment-preview-image" />
                <div v-else class="attachment-preview-file">
                  <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/>
                    <polyline points="13 2 13 9 20 9"/>
                  </svg>
                  <span>{{ att.name }}</span>
                </div>
                <button @click="messageAttachments.splice(idx, 1)" class="remove-attachment-btn">
                  <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <line x1="18" y1="6" x2="6" y2="18"></line>
                    <line x1="6" y1="6" x2="18" y2="18"></line>
                  </svg>
                </button>
              </div>
            </div>
          </div>

          <div class="message-input-area">
            <input 
              type="file" 
              ref="messageFileInput" 
              @change="handleMessageFileSelect" 
              multiple 
              accept="image/*,.pdf,.doc,.docx,.xls,.xlsx,.ppt,.pptx,.txt"
              style="display: none"
            />
            <button class="attach-file-btn" @click="($refs.messageFileInput as HTMLInputElement)?.click()">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="m21.44 11.05-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48"/>
              </svg>
            </button>
            <input 
              type="text" 
              v-model="newMessage" 
              @keyup.enter="handleSendMessage" 
              placeholder="Type your message to the student..." 
              class="message-input"
            />
            <button class="send-btn" @click="handleSendMessage" :disabled="!newMessage.trim() && messageAttachments.length === 0">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <line x1="22" y1="2" x2="11" y2="13"></line>
                <polygon points="22 2 15.46 22 11 13 2 9.54 22 2"></polygon>
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Attachment Viewer Modal -->
    <div v-if="viewingAttachment" class="modal-overlay attachment-modal-overlay" @click.self="closeAttachmentViewer">
      <div class="attachment-viewer">
        <button @click="closeAttachmentViewer" class="close-btn viewer-close-btn">&times;</button>
        <div class="attachment-viewer-content">
          <img v-if="viewingAttachment.type === 'image'" :src="viewingAttachment.url" class="viewer-image" alt="Attachment" />
          <div v-else class="viewer-file">
            <svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/>
              <polyline points="13 2 13 9 20 9"/>
            </svg>
            <h3>{{ viewingAttachment.name }}</h3>
            <button @click="downloadAttachment(viewingAttachment)" class="download-viewer-btn">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                <polyline points="7 10 12 15 17 10"></polyline>
                <line x1="12" y1="15" x2="12" y2="3"></line>
              </svg>
              Download File
            </button>
          </div>
        </div>
      </div>
    </div>

    </main>


    <!-- Individual Chat Modal -->
    <div v-if="isModalOpen" class="modal-overlay" @click.self="closeModal">
      <div class="modal-content">
        <div class="modal-header">
          <button @click="closeModal" class="close-btn">&times;</button>
          <div class="header-info">
            <div class="student-avatar">
              <span>{{ activeConversation?.student_name?.[0] || 'S' }}</span>
            </div>
            <div class="header-details">
              <h2 class="modal-title">Student: {{ activeConversation?.student_name || 'Student' }}</h2>
              <span class="section-info">{{ activeConversation?.subject_name }}</span>
            </div>
          </div>
        </div>
        <div class="modal-body">
          <!-- Loading indicator for messages -->
          <div v-if="loadingMessages" class="messages-loading">
            <div class="messages-loading-spinner"></div>
            <p>Loading messages...</p>
          </div>
          
          <div v-else class="messages-container" ref="messagesContainer">
            <div 
              v-for="message in currentMessages" 
              :key="message.id" 
              :class="['message-bubble', { 'sent': message.sender_id === currentTeacherId, 'received': message.sender_id !== currentTeacherId }]"
            >
              <p class="message-text">{{ message.message_text }}</p>
              
              <!-- Display attachments if any -->
              <div v-if="message.attachments && message.attachments.length > 0" class="message-attachments">
                <div v-for="(attachment, idx) in message.attachments" :key="idx" class="attachment-item">
                  <!-- Image preview with better visibility -->
                  <div v-if="attachment.type === 'image'" class="attachment-image-container" @click="viewAttachment(attachment)">
                    <img :src="attachment.url" class="attachment-image" alt="Attachment" />
                    <div class="image-overlay">
                      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                        <circle cx="12" cy="12" r="3"></circle>
                      </svg>
                      <span>Click to view</span>
                    </div>
                  </div>
                  
                  <!-- File download -->
                  <div v-else class="attachment-file">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/>
                      <polyline points="13 2 13 9 20 9"/>
                    </svg>
                    <span>{{ attachment.name }}</span>
                    <div class="attachment-actions">
                      <button @click="viewAttachment(attachment)" class="attachment-btn" title="View">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                          <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                          <circle cx="12" cy="12" r="3"></circle>
                        </svg>
                      </button>
                      <button @click="downloadAttachment(attachment)" class="attachment-btn" title="Download">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                          <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                          <polyline points="7 10 12 15 17 10"></polyline>
                          <line x1="12" y1="15" x2="12" y2="3"></line>
                        </svg>
                      </button>
                    </div>
                  </div>
                </div>
              </div>

              <div class="message-footer">
                <span class="message-time">{{ formatTime(message.sent_at) }}</span>
                
                <!-- Message Status for Sent Messages -->
                <span v-if="message.sender_id === currentTeacherId" class="message-status">
                  <span v-if="message.is_read" class="status-read">
                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <polyline points="20 6 9 17 4 12"></polyline>
                    </svg>
                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-left: -8px;">
                      <polyline points="20 6 9 17 4 12"></polyline>
                    </svg>
                    <span v-if="message.read_at" class="read-time">Read {{ formatTime(message.read_at) }}</span>
                  </span>
                  <span v-else class="status-sent">
                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <polyline points="20 6 9 17 4 12"></polyline>
                    </svg>
                    Sent
                  </span>
                </span>
              </div>
            </div>
            <div v-if="currentMessages.length === 0" class="no-messages">
              <p>No messages yet. Start the conversation!</p>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <!-- Attachment Preview -->
          <div v-if="messageAttachments.length > 0" class="attachments-preview">
            <div class="attachment-preview-list">
              <div v-for="(att, idx) in messageAttachments" :key="idx" class="attachment-preview-item">
                <img v-if="att.type === 'image'" :src="att.url" class="attachment-preview-image" />
                <div v-else class="attachment-preview-file">
                  <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/>
                    <polyline points="13 2 13 9 20 9"/>
                  </svg>
                  <span>{{ att.name }}</span>
                </div>
                <button @click="messageAttachments.splice(idx, 1)" class="remove-attachment-btn">
                  <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <line x1="18" y1="6" x2="6" y2="18"></line>
                    <line x1="6" y1="6" x2="18" y2="18"></line>
                  </svg>
                </button>
              </div>
            </div>
          </div>

          <div class="message-input-area">
            <input 
              type="file" 
              ref="messageFileInput" 
              @change="handleMessageFileSelect" 
              multiple 
              accept="image/*,.pdf,.doc,.docx,.xls,.xlsx,.ppt,.pptx,.txt"
              style="display: none"
            />
            <button class="attach-file-btn" @click="($refs.messageFileInput as HTMLInputElement)?.click()">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="m21.44 11.05-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48"/>
              </svg>
            </button>
            <input 
              type="text" 
              v-model="newMessage" 
              @keyup.enter="handleSendMessage" 
              placeholder="Type your message to the student..." 
              class="message-input"
            />
            <button class="send-btn" @click="handleSendMessage" :disabled="!newMessage.trim() && messageAttachments.length === 0">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <line x1="22" y1="2" x2="11" y2="13"></line>
                <polygon points="22 2 15.46 22 11 13 2 9.54 22 2"></polygon>
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Attachment Viewer Modal -->
    <div v-if="viewingAttachment" class="modal-overlay attachment-modal-overlay" @click.self="closeAttachmentViewer">
      <div class="attachment-viewer">
        <button @click="closeAttachmentViewer" class="close-btn viewer-close-btn">&times;</button>
        <div class="attachment-viewer-content">
          <img v-if="viewingAttachment.type === 'image'" :src="viewingAttachment.url" class="viewer-image" alt="Attachment" />
          <div v-else class="viewer-file">
            <svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/>
              <polyline points="13 2 13 9 20 9"/>
            </svg>
            <h3>{{ viewingAttachment.name }}</h3>
            <button @click="downloadAttachment(viewingAttachment)" class="download-viewer-btn">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                <polyline points="7 10 12 15 17 10"></polyline>
                <line x1="12" y1="15" x2="12" y2="3"></line>
              </svg>
              Download File
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Loading Overlay -->
    <div v-if="isLoading" class="loading-overlay">
      <div class="loading-content">
        <div class="loading-spinner"></div>
        <p class="loading-text">{{ loadingMessage || 'Loading...' }}</p>
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


jhsckskfdvdsdokdkfmv
<script setup lang="ts">
// Notification Bell State and Methods
import { ref, computed, onMounted, onUnmounted, nextTick, watch } from 'vue'
import { useRouter } from 'vue-router'
import { supabase } from '@/supabase.js'
import { useDarkMode } from '../../composables/useDarkMode.js'

// Dark mode
const { isDarkMode, toggleDarkMode, initDarkMode } = useDarkMode()

const router = useRouter()

// ================================
// STATE MANAGEMENT
// ================================

// Notification state
const showNotifDropdown = ref(false)
const notifications = ref([])

// User authentication
const currentUser = ref<any>(null)
const currentTeacherId = ref<string | null>(null)
const teacherProfile = ref<any>(null)
const debugMode = ref(false)
const showProfileDropdown = ref(false)
const fullName = ref('Teacher')

// Logout modal states
const showLogoutModal = ref(false)
const isLoggingOut = ref(false)

// UI State
const currentTab = ref('students')
const isModalOpen = ref(false)
const isBroadcastModalOpen = ref(false)
const isLoading = ref(false)
const loadingMessage = ref('Loading...')
const loadingMessages = ref(false)
const showArchive = ref(false)
const showBroadcastHistory = ref(false)
const showChatOptions = ref(false)
const showBroadcastOptionsMenu = ref<string | null>(null)
const viewingAttachment = ref<any>(null)
const expandedSections = ref(new Set())
const selectedSectionView = ref<any>(null)
const showStudentsInSection = ref(false)
const openSectionDropdown = ref<string | null>(null)

// Search and Filter
const searchQuery = ref('')
const selectedSection = ref('')
const selectedGradeFilter = ref('all')

// Chat State
const selectedChat = ref<any>(null)
const activeConversation = ref<any>(null)
const newMessage = ref('')
const messagesContainer = ref<HTMLElement | null>(null)
const messageFileInput = ref<HTMLInputElement | null>(null)
const messageAttachments = ref<any[]>([])

// Broadcast State
const broadcastMessage = ref('')
const broadcastSection = ref('')
const broadcastFileInput = ref<HTMLInputElement | null>(null)
const broadcastAttachments = ref<any[]>([])
const broadcastHistory = ref<any[]>([])
const archivedBroadcasts = ref<any[]>([])
const selectedBroadcastSection = ref<any>(null)
const showBroadcastMessages = ref(false)

// Data
const studentContacts = ref<any[]>([])
const currentMessages = ref<any[]>([])
const archivedChats = ref<any[]>([])
const studentPresence = ref<Record<string, any>>({})

// ================================
// NOTIFICATION FUNCTIONS
// ================================

function toggleNotifDropdown() {
  showNotifDropdown.value = !showNotifDropdown.value
}

function handleNotificationClick(notif: any) {
  // Mark as read and navigate if needed
  notifications.value = notifications.value.filter((n: any) => n.id !== notif.id)
}

// ================================
// FILE UPLOAD FUNCTIONS
// ================================

const uploadFileToStorage = async (file: File, folder = 'message-attachments') => {
  try {
    const fileExt = file.name.split('.').pop()
    const fileName = `${Date.now()}-${Math.random().toString(36).substring(7)}.${fileExt}`
    const filePath = `${folder}/${fileName}`
    
    console.log('Uploading file:', filePath)
    
    const { data, error } = await supabase.storage
      .from('attachments')
      .upload(filePath, file, {
        cacheControl: '3600',
        upsert: false
      })
    
    if (error) {
      console.error('Upload error:', error)
      throw error
    }
    
    const { data: urlData } = supabase.storage
      .from('attachments')
      .getPublicUrl(filePath)
    
    console.log('File uploaded successfully:', urlData.publicUrl)
    
    return {
      path: filePath,
      url: urlData.publicUrl,
      name: file.name,
      type: file.type.startsWith('image/') ? 'image' : 'file',
      size: file.size,
      mimeType: file.type
    }
  } catch (error) {
    console.error('Error uploading file:', error)
    throw error
  }
}

const saveMessageAttachments = async (messageId: string, attachments: any[]) => {
  try {
    // Check if message_attachments table exists
    const attachmentRecords = attachments.map(att => ({
      message_id: messageId,
      file_name: att.name,
      file_path: att.path,
      file_url: att.url,
      file_type: att.type,
      file_size: att.size,
      mime_type: att.mimeType
    }))
    
    const { data, error } = await supabase
      .from('message_attachments')
      .insert(attachmentRecords)
      .select()
    
    if (error) {
      console.error('Error saving attachments:', error)
      // If table doesn't exist, just log and continue
      if (error.code === '42P01') {
        console.warn('message_attachments table does not exist, skipping attachment save')
        return []
      }
      throw error
    }
    
    return data
  } catch (error) {
    console.error('Error saving message attachments:', error)
    // Don't throw, just return empty array
    return []
  }
}

// ================================
// AUTHENTICATION FUNCTIONS
// ================================

const getCurrentUser = async () => {
  try {
    loadingMessage.value = 'Checking authentication...'
    
    const { data: { session }, error: sessionError } = await supabase.auth.getSession()
    if (sessionError) {
      console.error('Session error:', sessionError)
      throw sessionError
    }
    
    if (!session || !session.user) {
      console.log('No valid session found')
      await router.push('/login')
      return null
    }
    
    console.log('Session user:', session.user.id, session.user.email)
    currentUser.value = session.user
    
    loadingMessage.value = 'Loading teacher profile...'
    
    const { data: profile, error: profileError } = await supabase
      .from('profiles')
      .select('id, auth_user_id, full_name, email, role')
      .eq('auth_user_id', session.user.id)
      .eq('role', 'teacher')
      .single()
    
    console.log('Profile lookup result:', { profile, profileError })
    
    if (profileError || !profile) {
      throw new Error(`Teacher profile not found for auth user: ${session.user.id}`)
    }
    
    const { data: teacher, error: teacherError } = await supabase
      .from('teachers')
      .select('*')
      .eq('profile_id', profile.id)
      .single()
    
    console.log('Teacher lookup result:', { teacher, teacherError })
    
    if (teacherError || !teacher) {
      throw new Error(`Teacher record not found for profile: ${profile.id}`)
    }
    
    if (!teacher.is_active) {
      throw new Error('Teacher account is not active')
    }
    
    teacherProfile.value = teacher
    currentTeacherId.value = teacher.id
    fullName.value = teacher.full_name || profile.full_name || 'Teacher'
    
    console.log('Teacher authenticated:', {
      id: teacher.id,
      name: teacher.full_name,
      email: teacher.email,
      active: teacher.is_active
    })
    
    return {
      authUser: session.user,
      teacherId: teacher.id,
      profile: teacher
    }
    
  } catch (error: any) {
    console.error('Error getting current user:', error)
    alert(`Authentication error: ${error.message}`)
    await router.push('/login')
    return null
  }
}

// ================================
// UTILITY METHODS
// ================================

const copyToClipboard = async (text: string) => {
  try {
    await navigator.clipboard.writeText(text)
    console.log('Section code copied to clipboard:', text)
  } catch (err) {
    console.error('Failed to copy to clipboard:', err)
    const textArea = document.createElement('textarea')
    textArea.value = text
    document.body.appendChild(textArea)
    textArea.select()
    document.execCommand('copy')
    document.body.removeChild(textArea)
  }
}

// ================================
// PROFILE DROPDOWN FUNCTIONS
// ================================

const toggleProfileDropdown = () => {
  showProfileDropdown.value = !showProfileDropdown.value
}

const openLogoutModal = () => {
  showLogoutModal.value = true
}

const closeLogoutModal = () => {
  showLogoutModal.value = false
}

const confirmLogout = () => {
  console.log('🚪 Logging out...')
  
  // Clear storage immediately
  localStorage.clear()
  sessionStorage.clear()
  
  // Sign out from Supabase (don't wait)
  supabase.auth.signOut().catch(err => console.log('Signout error:', err))
  
  // Immediate redirect - no waiting!
  setTimeout(() => {
    window.location.assign('/login')
  }, 100)
  
  console.log('✅ Logout initiated')
}

const logout = () => {
  openLogoutModal()
}

const handleClickOutside = (event: MouseEvent) => {
  const target = event.target as HTMLElement
  if (!target.closest('.user-profile-wrapper')) {
    showProfileDropdown.value = false
  }
}

// ================================
// DATA LOADING METHODS
// ================================

const loadTeacherContacts = async () => {
  try {
    if (!currentTeacherId.value) {
      console.error('No teacher ID available')
      return
    }
    
    isLoading.value = true
    loadingMessage.value = 'Loading your students...'
    
    console.log('Loading contacts for teacher:', currentTeacherId.value)
    
    // Try to use the view first
    const { data: contacts, error: contactsError } = await supabase
      .from('teacher_contacts')
      .select('*')
      .eq('teacher_id', currentTeacherId.value)
      .order('subject_name', { ascending: true })
      .order('section_name', { ascending: true })
      .order('student_name', { ascending: true })
    
    if (contactsError) {
      console.error('Error loading from teacher_contacts view:', contactsError)
      console.log('Falling back to manual query...')
      const manualContacts = await loadContactsManually()
      studentContacts.value = manualContacts || []
      return
    }
    
    console.log('Contacts loaded from view:', contacts?.length || 0)
    
    if (!contacts || contacts.length === 0) {
      console.log('No students found for this teacher')
      studentContacts.value = []
      return
    }
    
    // Get auth_user_ids for presence tracking
    const studentIds = contacts.map(c => c.student_id).filter(Boolean)
    let authUserMap: Record<string, string> = {}
    
    if (studentIds.length > 0) {
      const { data: students } = await supabase
        .from('students')
        .select('id, profile_id')
        .in('id', studentIds)
      
      if (students) {
        const profileIds = students.map(s => s.profile_id).filter(Boolean)
        
        if (profileIds.length > 0) {
          const { data: profiles } = await supabase
            .from('profiles')
            .select('id, auth_user_id')
            .in('id', profileIds)
          
          if (profiles) {
            const profileToAuth: Record<string, string> = {}
            profiles.forEach(p => {
              profileToAuth[p.id] = p.auth_user_id
            })
            
            students.forEach(s => {
              if (s.profile_id && profileToAuth[s.profile_id]) {
                authUserMap[s.id] = profileToAuth[s.profile_id]
              }
            })
          }
        }
      }
    }
    
    const mappedContacts = contacts.map(contact => ({
      student_id: contact.student_id,
      student_name: contact.student_name,
      student_email: contact.student_email,
      student_number: contact.student_number,
      grade_level: contact.grade_level,
      subject_id: contact.subject_id,
      subject_name: contact.subject_name,
      section_id: contact.section_id,
      section_name: contact.section_name,
      section_code: contact.section_code,
      enrolled_date: contact.enrolled_date,
      last_message_date: contact.last_message_date,
      last_message: contact.last_message || `Enrolled ${formatDate(contact.enrolled_date)}`,
      unread_count: contact.unread_count || 0,
      auth_user_id: authUserMap[contact.student_id] || null
    }))
    
    studentContacts.value = mappedContacts
    console.log('Mapped contacts:', mappedContacts.length)
    
  } catch (error: any) {
    console.error('Error loading teacher contacts:', error)
    alert(`Error loading students: ${error.message}`)
  } finally {
    isLoading.value = false
  }
}

const loadContactsManually = async () => {
  try {
    console.log('Loading contacts manually for teacher:', currentTeacherId.value)
    
    // Get teacher's subjects
    const { data: subjects, error: subjectsError } = await supabase
      .from('subjects')
      .select('id, name, grade_level')
      .eq('teacher_id', currentTeacherId.value)
      .eq('is_active', true)
    
    if (subjectsError || !subjects || subjects.length === 0) {
      console.log('No subjects found for teacher')
      return []
    }
    
    const subjectIds = subjects.map(s => s.id)
    
    // Get sections for these subjects
    const { data: sections, error: sectionsError } = await supabase
      .from('sections')
      .select('id, name, section_code, subject_id')
      .in('subject_id', subjectIds)
      .eq('is_active', true)
    
    if (sectionsError || !sections || sections.length === 0) {
      console.log('No sections found')
      return []
    }
    
    const sectionIds = sections.map(s => s.id)
    
    // Get enrollments
    const { data: enrollments, error: enrollmentsError } = await supabase
      .from('enrollments')
      .select('id, student_id, section_id, subject_id, enrolled_at')
      .in('section_id', sectionIds)
      .eq('status', 'active')
    
    if (enrollmentsError || !enrollments || enrollments.length === 0) {
      console.log('No enrollments found')
      return []
    }
    
    const studentIds = [...new Set(enrollments.map(e => e.student_id))]
    
    // Get students
    const { data: students, error: studentsError } = await supabase
      .from('students')
      .select('id, full_name, email, student_id, grade_level, profile_id')
      .in('id', studentIds)
      .eq('is_active', true)
    
    if (studentsError || !students) {
      console.log('No students found')
      return []
    }
    
    // Get auth_user_ids
    const profileIds = students.map(s => s.profile_id).filter(Boolean)
    let authUserMap: Record<string, string> = {}
    
    if (profileIds.length > 0) {
      const { data: profiles } = await supabase
        .from('profiles')
        .select('id, auth_user_id')
        .in('id', profileIds)
      
      if (profiles) {
        profiles.forEach(p => {
          const student = students.find(s => s.profile_id === p.id)
          if (student) {
            authUserMap[student.id] = p.auth_user_id
          }
        })
      }
    }
    
    // Build contacts
    const contacts: any[] = []
    
    enrollments.forEach(enrollment => {
      const student = students.find(s => s.id === enrollment.student_id)
      const section = sections.find(s => s.id === enrollment.section_id)
      const subject = subjects.find(s => s.id === section?.subject_id)
      
      if (student && section && subject) {
        contacts.push({
          student_id: student.id,
          student_name: student.full_name,
          student_email: student.email,
          student_number: student.student_id,
          grade_level: student.grade_level,
          subject_id: subject.id,
          subject_name: subject.name,
          section_id: section.id,
          section_name: section.name,
          section_code: section.section_code,
          enrolled_date: enrollment.enrolled_at,
          last_message_date: null,
          last_message: `Enrolled ${formatDate(enrollment.enrolled_at)}`,
          unread_count: 0,
          auth_user_id: authUserMap[student.id] || null
        })
      }
    })
    
    console.log('Manual contacts loaded:', contacts.length)
    return contacts
    
  } catch (error) {
    console.error('Error in manual contact loading:', error)
    return []
  }
}



const loadBroadcastHistory = async () => {
  try {
    if (!currentTeacherId.value) return
    
    const { data: broadcasts, error } = await supabase
      .from('messages')
      .select(`
        id,
        message_text,
        sent_at,
        message_type,
        section_id
      `)
      .eq('sender_id', currentTeacherId.value)
      .eq('message_type', 'announcement')
      .is('recipient_id', null)
      .order('sent_at', { ascending: false })
    
    if (error) {
      console.error('Error loading broadcast history:', error)
      return
    }
    
    if (!broadcasts || broadcasts.length === 0) {
      broadcastHistory.value = []
      return
    }
    
    // Get section details
    const sectionIds = [...new Set(broadcasts.map(b => b.section_id))]
    const { data: sections } = await supabase
      .from('sections')
      .select(`
        id,
        name,
        section_code,
        subject_id
      `)
      .in('id', sectionIds)
    
    // Get subject details
    const subjectIds = sections?.map(s => s.subject_id).filter(Boolean) || []
    const { data: subjects } = await supabase
      .from('subjects')
      .select('id, name, grade_level')
      .in('id', subjectIds)
    
    // Load attachments for all broadcast messages
    const broadcastIds = broadcasts.map(b => b.id)
    let attachmentsMap: Record<string, any[]> = {}
    
    if (broadcastIds.length > 0) {
      try {
        const { data: attachments, error: attachError } = await supabase
          .from('message_attachments')
          .select('*')
          .in('message_id', broadcastIds)
        
        if (attachError) {
          console.warn('Error fetching attachments:', attachError)
        } else if (attachments) {
          attachmentsMap = attachments.reduce((acc: Record<string, any[]>, att) => {
            if (!acc[att.message_id]) acc[att.message_id] = []
            acc[att.message_id].push({
              name: att.file_name,
              url: att.file_url,
              type: att.file_type,
              size: att.file_size || 'Unknown size',
              path: att.file_path,
              mimeType: att.mime_type
            })
            return acc
          }, {})
        }
      } catch (attachError) {
        console.warn('Attachments table not found or error fetching attachments:', attachError)
      }
    }
    
    const transformedBroadcasts = broadcasts.map(b => {
      const section = sections?.find(s => s.id === b.section_id)
      const subject = subjects?.find(s => s.id === section?.subject_id)
      
      return {
        id: b.id,
        message: b.message_text,
        sent_at: b.sent_at,
        section_id: b.section_id,
        section_name: section?.name || 'Unknown',
        section_code: section?.section_code || '',
        subject_name: subject?.name || 'Unknown',
        grade_level: subject?.grade_level || 0,
        attachments: attachmentsMap[b.id] || [],
        recipient_count: 0
      }
    })
    
    broadcastHistory.value = transformedBroadcasts
    console.log('Broadcast history loaded with attachments:', transformedBroadcasts.length)
    
  } catch (error) {
    console.error('Error loading broadcast history:', error)
  }
}


// ================================
// COMPUTED PROPERTIES
// ================================

const filteredStudents = computed(() => {
  let students = studentContacts.value
  
  if (selectedSection.value) {
    students = students.filter(s => s.section_id === selectedSection.value)
  }
  
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    students = students.filter(s => 
      s.student_name?.toLowerCase().includes(query) ||
      s.subject_name?.toLowerCase().includes(query) ||
      s.section_name?.toLowerCase().includes(query)
    )
  }
  
  return students
})

const groupedStudents = computed(() => {
  const sections: Record<string, any> = {}
  
  let filteredData = filteredStudents.value
  
  if (selectedGradeFilter.value !== 'all') {
    filteredData = filteredData.filter(student => 
      student.grade_level === parseInt(selectedGradeFilter.value)
    )
  }
  
  filteredData.forEach(student => {
    const sectionKey = student.section_id
    if (!sections[sectionKey]) {
      sections[sectionKey] = {
        section_id: student.section_id,
        subject_id: student.subject_id,
        section_name: student.section_name,
        section_code: student.section_code,
        subject_name: student.subject_name,
        grade_level: student.grade_level,
        students: [],
        total_unread: 0
      }
    }
    sections[sectionKey].students.push(student)
    sections[sectionKey].total_unread += student.unread_count || 0
  })
  
  return Object.values(sections)
})

const availableGrades = computed(() => {
  const grades = new Set<number>()
  studentContacts.value.forEach(student => {
    if (student.grade_level) {
      grades.add(student.grade_level)
    }
  })
  return Array.from(grades).sort((a, b) => a - b)
})

const groupedBroadcasts = computed(() => {
  const sections: Record<string, any> = {}
  
  broadcastHistory.value.forEach(broadcast => {
    const sectionKey = broadcast.section_id
    if (!sections[sectionKey]) {
      sections[sectionKey] = {
        section_id: broadcast.section_id,
        section_name: broadcast.section_name,
        section_code: broadcast.section_code,
        subject_name: broadcast.subject_name,
        grade_level: broadcast.grade_level,
        broadcasts: []
      }
    }
    sections[sectionKey].broadcasts.push(broadcast)
  })
  
  return Object.values(sections)
})

const uniqueSections = computed(() => {
  const sectionsMap = new Map()
  
  studentContacts.value.forEach(student => {
    const key = student.section_id
    if (!sectionsMap.has(key)) {
      sectionsMap.set(key, {
        section_id: student.section_id,
        section_name: student.section_name,
        section_code: student.section_code,
        subject_name: student.subject_name,
        grade_level: student.grade_level
      })
    }
  })
  
  return Array.from(sectionsMap.values())
})

// ================================
// CHAT METHODS
// ================================

const startChatWithStudent = async (student: any) => {
  console.log('Starting chat with student:', student)
  
  activeConversation.value = {
    ...student,
    student_name: student.student_name || student.name
  }
  
  selectedChat.value = student
  isModalOpen.value = true
  showChatOptions.value = false
  
  await loadConversationMessages(student.student_id, student.section_id)
  
  await nextTick()
  scrollToBottom()
}

const loadConversationMessages = async (studentId: string, sectionId: string) => {
  try {
    if (!currentTeacherId.value) return
    
    loadingMessages.value = true
    
    console.log('Loading messages between teacher and student:', { 
      teacherId: currentTeacherId.value, 
      studentId, 
      sectionId 
    })
    
    // Load messages
    const { data: messages, error: messagesError } = await supabase
      .from('messages')
      .select('*')
      .eq('section_id', sectionId)
      .eq('message_type', 'direct')
      .or(`and(sender_id.eq.${currentTeacherId.value},recipient_id.eq.${studentId}),and(sender_id.eq.${studentId},recipient_id.eq.${currentTeacherId.value})`)
      .order('sent_at', { ascending: true })
    
    if (messagesError) {
      console.error('Error loading messages:', messagesError)
      currentMessages.value = []
      return
    }
    
    // Try to load attachments
    let attachmentsMap: Record<string, any[]> = {}
    if (messages && messages.length > 0) {
      const messageIds = messages.map(m => m.id)
      
      try {
        const { data: attachments } = await supabase
          .from('message_attachments')
          .select('*')
          .in('message_id', messageIds)
        
        if (attachments) {
          attachments.forEach(att => {
            if (!attachmentsMap[att.message_id]) {
              attachmentsMap[att.message_id] = []
            }
            attachmentsMap[att.message_id].push({
              name: att.file_name,
              url: att.file_url,
              type: att.file_type,
              size: att.file_size || 'Unknown size',
              path: att.file_path
            })
          })
        }
      } catch (e) {
        console.log('No attachments table or error fetching')
      }
    }
    
    // Add attachments to messages
    const messagesWithAttachments = (messages || []).map(msg => ({
      ...msg,
      attachments: attachmentsMap[msg.id] || []
    }))
    
    currentMessages.value = messagesWithAttachments
    console.log('Loaded messages:', messagesWithAttachments.length)
    
    await nextTick()
    forceScrollToBottom()
    
    // Mark as read
    markConversationAsRead(sectionId, studentId)
    
  } catch (error) {
    console.error('Error loading conversation messages:', error)
    currentMessages.value = []
  } finally {
    loadingMessages.value = false
  }
}

const handleSendMessage = async () => {
  if ((!newMessage.value.trim() && messageAttachments.value.length === 0) || !activeConversation.value || !currentTeacherId.value) {
    console.log('Cannot send: missing required data')
    return
  }
  
  const messageText = newMessage.value.trim() || '📎 Attachment'
  const attachmentsToSend = [...messageAttachments.value]
  
  console.log('Sending message:', {
    text: messageText,
    sectionId: activeConversation.value.section_id,
    senderId: currentTeacherId.value,
    recipientId: activeConversation.value.student_id,
    attachments: attachmentsToSend.length
  })
  
  // Create temp message for optimistic UI
  const tempMessage = {
    id: 'temp-' + Date.now(),
    sender_id: currentTeacherId.value,
    recipient_id: activeConversation.value.student_id,
    message_text: messageText,
    sent_at: new Date().toISOString(),
    is_read: false,
    message_type: 'direct',
    sending: true,
    attachments: attachmentsToSend.map(att => ({
      name: att.name,
      url: att.url,
      type: att.type,
      size: att.size || 'Unknown size'
    }))
  }
  
  currentMessages.value.push(tempMessage)
  newMessage.value = ''
  messageAttachments.value = []
  
  await nextTick()
  forceScrollToBottom()
  
  try {
    // Upload attachments first
    let uploadedAttachments: any[] = []
    if (attachmentsToSend.length > 0) {
      console.log('Uploading attachments...')
      for (const attachment of attachmentsToSend) {
        if (attachment.file) {
          const uploaded = await uploadFileToStorage(attachment.file)
          uploadedAttachments.push(uploaded)
        }
      }
      console.log('Attachments uploaded:', uploadedAttachments.length)
    }
    
    // Try using the RPC function first
    let messageId: string | null = null
    
    const { data: rpcResult, error: rpcError } = await supabase
      .rpc('send_direct_message', {
        p_section_id: activeConversation.value.section_id,
        p_sender_id: currentTeacherId.value,
        p_recipient_id: activeConversation.value.student_id,
        p_message_text: messageText
      })
    
    if (rpcError) {
      console.error('RPC error:', rpcError)
      // Fallback to direct insert
      console.log('Falling back to direct insert...')
      
      const { data: insertData, error: insertError } = await supabase
        .from('messages')
        .insert({
          section_id: activeConversation.value.section_id,
          sender_id: currentTeacherId.value,
          recipient_id: activeConversation.value.student_id,
          message_text: messageText,
          message_type: 'direct',
          is_read: false
        })
        .select('id')
        .single()
      
      if (insertError) {
        console.error('Insert error:', insertError)
        throw new Error(`Failed to send message: ${insertError.message}`)
      }
      
      messageId = insertData?.id
    } else {
      messageId = rpcResult
    }
    
    console.log('Message sent with ID:', messageId)
    
    // Save attachments if any
    if (uploadedAttachments.length > 0 && messageId) {
      await saveMessageAttachments(messageId, uploadedAttachments)
    }
    
    // Update temp message with real data
    const tempIndex = currentMessages.value.findIndex(m => m.id === tempMessage.id)
    if (tempIndex !== -1) {
      currentMessages.value[tempIndex] = {
        ...currentMessages.value[tempIndex],
        id: messageId,
        sending: false,
        attachments: uploadedAttachments.map(att => ({
          name: att.name,
          url: att.url,
          type: att.type,
          size: att.size || 'Unknown size',
          path: att.path
        }))
      }
    }
    
    await nextTick()
    setTimeout(() => {
      forceScrollToBottom()
    }, 100)
    
    // Refresh contacts to update last message
    await loadTeacherContacts()
    
  } catch (error: any) {
    console.error('Failed to send message:', error)
    
    // Remove temp message
    const tempIndex = currentMessages.value.findIndex(m => m.id === tempMessage.id)
    if (tempIndex !== -1) {
      currentMessages.value.splice(tempIndex, 1)
    }
    
    // Restore input
    newMessage.value = messageText
    messageAttachments.value = attachmentsToSend
    alert(`Failed to send message: ${error.message}`)
  }
}

const closeModal = () => {
  isModalOpen.value = false
  activeConversation.value = null
  selectedChat.value = null
  currentMessages.value = []
  messageAttachments.value = []
  showChatOptions.value = false
  loadingMessages.value = false
}

const markConversationAsRead = async (sectionId: string, studentId: string) => {
  try {
    // Try RPC first
    const { error } = await supabase.rpc('mark_conversation_read', {
      p_section_id: sectionId,
      p_other_user_id: studentId,
      p_current_user_id: currentTeacherId.value
    })
    
    if (error && error.code !== '42883') {
      console.error('Error marking conversation as read:', error)
    } else if (!error) {
      const student = studentContacts.value.find(s => s.student_id === studentId && s.section_id === sectionId)
      if (student) {
        student.unread_count = 0
      }
    }
  } catch (error: any) {
    console.log('Could not mark conversation as read:', error.message)
  }
}

// ================================
// ATTACHMENT METHODS
// ================================

const handleMessageFileSelect = (event: Event) => {
  const target = event.target as HTMLInputElement
  const files = Array.from(target.files || [])
  
  files.forEach(file => {
    const fileType = file.type.startsWith('image/') ? 'image' : 'file'
    const tempUrl = URL.createObjectURL(file)
    
    messageAttachments.value.push({
      type: fileType,
      name: file.name,
      size: `${(file.size / 1024 / 1024).toFixed(2)} MB`,
      url: tempUrl,
      file: file
    })
  })
  
  target.value = ''
}

const handleBroadcastFileSelect = (event: Event) => {
  const target = event.target as HTMLInputElement
  const files = Array.from(target.files || [])
  
  files.forEach(file => {
    const reader = new FileReader()
    const fileType = file.type.startsWith('image/') ? 'image' : 'file'
    
    reader.onload = (e) => {
      broadcastAttachments.value.push({
        type: fileType,
        name: file.name,
        size: `${(file.size / 1024 / 1024).toFixed(2)} MB`,
        url: e.target?.result as string,
        file: file
      })
    }
    
    reader.readAsDataURL(file)
  })
  
  target.value = ''
}

const viewAttachment = (attachment: any) => {
  viewingAttachment.value = attachment
}

const closeAttachmentViewer = () => {
  viewingAttachment.value = null
}

const downloadAttachment = (attachment: any) => {
  const link = document.createElement('a')
  link.href = attachment.url
  link.download = attachment.name
  link.target = '_blank'
  document.body.appendChild(link)
  link.click()
  document.body.removeChild(link)
}

// ================================
// ARCHIVE & DELETE METHODS
// ================================

const handleArchiveChat = (studentId: string) => {
  const student = studentContacts.value.find(s => s.student_id === studentId)
  if (student) {
    archivedChats.value.push(student)
    studentContacts.value = studentContacts.value.filter(s => s.student_id !== studentId)
    closeModal()
    alert(`Conversation with ${student.student_name} has been archived.`)
  }
}

const handleDeleteChat = (studentId: string) => {
  if (confirm('Are you sure you want to delete this conversation? This action cannot be undone.')) {
    const student = studentContacts.value.find(s => s.student_id === studentId)
    studentContacts.value = studentContacts.value.filter(s => s.student_id !== studentId)
    closeModal()
    
    if (student) {
      alert(`Conversation with ${student.student_name} has been deleted.`)
    }
  }
}

const restoreChat = (studentId: string) => {
  const student = archivedChats.value.find(s => s.student_id === studentId)
  if (student) {
    studentContacts.value.push(student)
    archivedChats.value = archivedChats.value.filter(s => s.student_id !== studentId)
    alert(`Conversation with ${student.student_name} has been restored.`)
  }
}

// ================================
// BROADCAST METHODS
// ================================

const openBroadcastModal = () => {
  currentTab.value = 'broadcast'
  showBroadcastHistory.value = false
  broadcastMessage.value = ''
  broadcastAttachments.value = []
}

const closeBroadcastModal = () => {
  isBroadcastModalOpen.value = false
  broadcastMessage.value = ''
  broadcastSection.value = ''
  broadcastAttachments.value = []
}

const cancelBroadcast = () => {
  if (broadcastMessage.value.trim() || broadcastAttachments.value.length > 0) {
    if (confirm('Are you sure you want to cancel? All changes will be lost.')) {
      broadcastMessage.value = ''
      broadcastSection.value = ''
      broadcastAttachments.value = []
    }
  } else {
    broadcastMessage.value = ''
    broadcastSection.value = ''
    broadcastAttachments.value = []
  }
}

const viewBroadcastSection = (section: any) => {
  selectedBroadcastSection.value = section
  showBroadcastMessages.value = true
}

const backToBroadcastHistory = () => {
  selectedBroadcastSection.value = null
  showBroadcastMessages.value = false
}

const sendBroadcastMessage = async () => {
  if (!broadcastMessage.value.trim() || !broadcastSection.value || !currentTeacherId.value) {
    alert('Please select a section and enter a message.')
    return
  }
  
  try {
    isLoading.value = true
    loadingMessage.value = 'Sending broadcast message...'
    
    const attachmentsToSend = [...broadcastAttachments.value]
    
    // Upload attachments
    const uploadedAttachments: any[] = []
    if (attachmentsToSend.length > 0) {
      loadingMessage.value = 'Uploading attachments...'
      for (const attachment of attachmentsToSend) {
        if (attachment.file) {
          const uploaded = await uploadFileToStorage(attachment.file, 'broadcast-attachments')
          uploadedAttachments.push(uploaded)
        }
      }
    }
    
    loadingMessage.value = 'Sending to students...'
    
    // Try RPC first
    let messageId: string | null = null
    
    const { data: rpcResult, error: rpcError } = await supabase
      .rpc('send_section_announcement', {
        p_section_id: broadcastSection.value,
        p_teacher_id: currentTeacherId.value,
        p_message_text: broadcastMessage.value.trim()
      })
    
    if (rpcError) {
      console.error('RPC error for announcement:', rpcError)
      // Fallback to direct insert
      const { data: insertData, error: insertError } = await supabase
        .from('messages')
        .insert({
          section_id: broadcastSection.value,
          sender_id: currentTeacherId.value,
          recipient_id: null,
          message_text: broadcastMessage.value.trim(),
          message_type: 'announcement',
          is_read: false
        })
        .select('id')
        .single()
      
      if (insertError) {
        console.error('Insert error:', insertError)
        throw new Error(`Failed to send broadcast: ${insertError.message}`)
      }
      
      messageId = insertData?.id
    } else {
      messageId = rpcResult
    }
    
    console.log('Broadcast message sent with ID:', messageId)
    
    // Save attachments
    if (uploadedAttachments.length > 0 && messageId) {
      await saveMessageAttachments(messageId, uploadedAttachments)
    }
    
    const selectedSectionInfo = uniqueSections.value.find(s => s.section_id === broadcastSection.value)
    const sectionName = selectedSectionInfo ? selectedSectionInfo.section_name : 'Selected Section'
    alert(`Broadcast message sent successfully to all students in ${sectionName}!`)
    
    broadcastMessage.value = ''
    broadcastSection.value = ''
    broadcastAttachments.value = []
    
    await loadTeacherContacts()
    await loadBroadcastHistory()
    
  } catch (error: any) {
    console.error('Error sending broadcast message:', error)
    alert(`Failed to send broadcast message: ${error.message}`)
  } finally {
    isLoading.value = false
  }
}

const toggleBroadcastOptions = (broadcastId: string) => {
  showBroadcastOptionsMenu.value = showBroadcastOptionsMenu.value === broadcastId ? null : broadcastId
}

const editBroadcast = (broadcast: any) => {
  broadcastMessage.value = broadcast.message
  broadcastSection.value = broadcast.section_id
  broadcastAttachments.value = [...(broadcast.attachments || [])]
  showBroadcastHistory.value = false
  showBroadcastOptionsMenu.value = null
  
  alert('Edit mode: Update your message and click Send to save changes.')
}

const archiveBroadcast = (broadcastId: string) => {
  const broadcast = broadcastHistory.value.find(b => b.id === broadcastId)
  if (broadcast) {
    archivedBroadcasts.value.push(broadcast)
    broadcastHistory.value = broadcastHistory.value.filter(b => b.id !== broadcastId)
    showBroadcastOptionsMenu.value = null
    alert('Broadcast has been archived.')
  }
}

const deleteBroadcast = async (broadcastId: string) => {
  if (confirm('Are you sure you want to delete this broadcast? This will also remove it from student message pages.')) {
    try {
      // Delete attachments first
      try {
        await supabase
          .from('message_attachments')
          .delete()
          .eq('message_id', broadcastId)
      } catch (e) {
        console.log('No attachments to delete or table not found')
      }
      
      const { error: msgError } = await supabase
        .from('messages')
        .delete()
        .eq('id', broadcastId)
      
      if (msgError) {
        console.error('Error deleting broadcast:', msgError)
        alert('Failed to delete broadcast.')
        return
      }
      
      broadcastHistory.value = broadcastHistory.value.filter(b => b.id !== broadcastId)
      showBroadcastOptionsMenu.value = null
      alert('Broadcast has been deleted.')
      
    } catch (error) {
      console.error('Error deleting broadcast:', error)
      alert('Failed to delete broadcast.')
    }
  }
}

// ================================
// UTILITY METHODS
// ================================

const toggleSection = (sectionId: string) => {
  if (expandedSections.value.has(sectionId)) {
    expandedSections.value.delete(sectionId)
  } else {
    expandedSections.value.add(sectionId)
  }
}

const viewSectionStudents = (section: any) => {
  selectedSectionView.value = section
  showStudentsInSection.value = true
}

const backToSections = () => {
  selectedSectionView.value = null
  showStudentsInSection.value = false
}

const toggleSectionOptions = (sectionId: string) => {
  openSectionDropdown.value = openSectionDropdown.value === sectionId ? null : sectionId
}

const deleteSectionConfirm = (section: any) => {
  if (confirm(`Are you sure you want to delete the section "${section.subject_name} - Grade ${section.grade_level}"? This action cannot be undone.`)) {
    deleteSection(section)
  }
  openSectionDropdown.value = null
}

const archiveSectionConfirm = (section: any) => {
  if (confirm(`Archive the section "${section.subject_name} - Grade ${section.grade_level}"?`)) {
    archiveSection(section)
  }
  openSectionDropdown.value = null
}

const deleteSection = async (section: any) => {
  try {
    console.log('Deleting section:', section)
    alert('Section deleted successfully!')
  } catch (error) {
    console.error('Error deleting section:', error)
    alert('Failed to delete section.')
  }
}

const archiveSection = async (section: any) => {
  try {
    console.log('Archiving section:', section)
    alert('Section archived successfully!')
  } catch (error) {
    console.error('Error archiving section:', error)
    alert('Failed to archive section.')
  }
}

const markAllAsRead = async () => {
  try {
    if (!currentTeacherId.value) return
    
    const unreadStudents = studentContacts.value.filter(s => s.unread_count > 0)
    
    if (unreadStudents.length === 0) {
      alert('No unread messages to mark as read.')
      return
    }
    
    isLoading.value = true
    loadingMessage.value = 'Marking messages as read...'
    
    for (const student of unreadStudents) {
      await markConversationAsRead(student.section_id, student.student_id)
    }
    
    await loadTeacherContacts()
    alert('All messages marked as read!')
    
  } catch (error) {
    console.error('Error marking all as read:', error)
  } finally {
    isLoading.value = false
  }
}

const scrollToBottom = () => {
  if (messagesContainer.value) {
    messagesContainer.value.scrollTo({
      top: messagesContainer.value.scrollHeight,
      behavior: 'smooth'
    })
  }
}

const scrollToTop = () => {
  if (messagesContainer.value) {
    messagesContainer.value.scrollTo({
      top: 0,
      behavior: 'smooth'
    })
  }
}

const forceScrollToBottom = () => {
  if (messagesContainer.value) {
    const element = messagesContainer.value
    element.scrollTop = element.scrollHeight
    
    requestAnimationFrame(() => {
      if (element) {
        element.scrollTop = element.scrollHeight
        setTimeout(() => {
          if (element) {
            element.scrollTo({
              top: element.scrollHeight,
              behavior: 'smooth'
            })
          }
        }, 10)
      }
    })
  }
}

const formatTime = (dateString: string) => {
  if (!dateString) return ''
  
  const date = new Date(dateString)
  const now = new Date()
  const diffMs = now.getTime() - date.getTime()
  const diffDays = Math.floor(diffMs / (1000 * 60 * 60 * 24))
  
  if (diffDays === 0) {
    return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
  } else if (diffDays === 1) {
    return 'Yesterday'
  } else if (diffDays < 7) {
    return date.toLocaleDateString([], { weekday: 'short' })
  } else {
    return date.toLocaleDateString([], { month: 'short', day: 'numeric' })
  }
}

const formatDate = (dateString: string) => {
  if (!dateString) return ''
  return new Date(dateString).toLocaleDateString()
}

const getPresenceStatus = (authUserId: string) => {
  const presence = studentPresence.value[authUserId]
  if (!presence || !presence.last_seen) return 'Offline'
  
  if (presence.is_online) {
    return 'Online now'
  }
  
  const now = new Date()
  const lastSeen = new Date(presence.last_seen)
  const diffMs = now.getTime() - lastSeen.getTime()
  const diffMinutes = Math.floor(diffMs / (1000 * 60))
  const diffHours = Math.floor(diffMs / (1000 * 60 * 60))
  const diffDays = Math.floor(diffMs / (1000 * 60 * 60 * 24))
  
  if (diffMinutes < 1) {
    return 'Online now'
  } else if (diffMinutes < 60) {
    return `Offline for ${diffMinutes} minute${diffMinutes > 1 ? 's' : ''}`
  } else if (diffHours < 24) {
    return `Offline for ${diffHours} hour${diffHours > 1 ? 's' : ''}`
  } else if (diffDays === 1) {
    return 'Offline for a day'
  } else if (diffDays < 7) {
    return `Offline for ${diffDays} days`
  } else {
    return 'Offline for a while'
  }
}

const setupPresenceTracking = async () => {
  if (!currentTeacherId.value) return
  
  const studentAuthIds = [...new Set(
    studentContacts.value
      .map(s => s.auth_user_id)
      .filter(id => id)
  )]
  
  if (studentAuthIds.length === 0) return
  
  console.log('Setting up presence tracking for students:', studentAuthIds.length)
  
  try {
    const { data: presenceData, error } = await supabase
      .from('user_presence')
      .select('*')
      .in('user_id', studentAuthIds)
    
    if (error) {
      console.error('Error fetching student presence:', error)
      return
    }
    
    if (presenceData) {
      presenceData.forEach(p => {
        studentPresence.value[p.user_id] = {
          is_online: p.is_online,
          last_seen: p.last_seen
        }
      })
    }
  } catch (e) {
    console.log('Presence tracking not available')
  }
}

const updateTeacherPresence = async (isOnline: boolean) => {
  if (!currentUser.value) return
  
  try {
    await supabase
      .from('user_presence')
      .upsert({
        user_id: currentUser.value.id,
        is_online: isOnline,
        last_seen: new Date().toISOString()
      }, {
        onConflict: 'user_id'
      })
  } catch (error) {
    console.log('Could not update presence')
  }
}

// ================================
// SECTION ICON COLORS
// ================================

const sectionIconColors = [
  'linear-gradient(135deg, #20c997 0%, #20c997 100%)',
  'linear-gradient(135deg, #6366f1 0%, #6366f1 100%)',
  'linear-gradient(135deg, #f59e0b 0%, #f59e0b 100%)',
  'linear-gradient(135deg, #ef4444 0%, #ef4444 100%)',
  'linear-gradient(135deg, #8b5cf6 0%, #8b5cf6 100%)',
  'linear-gradient(135deg, #10b981 0%, #10b981 100%)',
]

const getSectionIconColor = (idx: number) => {
  return sectionIconColors[idx % sectionIconColors.length]
}

// ================================
// WATCHERS
// ================================

watch(currentMessages, (newMessages, oldMessages) => {
  if (newMessages.length > (oldMessages?.length || 0) && isModalOpen.value) {
    nextTick(() => {
      forceScrollToBottom()
    })
  }
}, { deep: true, immediate: false })

watch(isModalOpen, (isOpen) => {
  if (isOpen && currentMessages.value.length > 0) {
    nextTick(() => {
      setTimeout(() => {
        forceScrollToBottom()
      }, 100)
    })
  }
})

// ================================
// LIFECYCLE METHODS
// ================================

const setupAuthListener = () => {
  supabase.auth.onAuthStateChange(async (event, session) => {
    console.log('Auth state change:', event)
    
    if (event === 'SIGNED_OUT' || !session) {
      currentUser.value = null
      currentTeacherId.value = null
      teacherProfile.value = null
      studentContacts.value = []
      console.log('User signed out, redirecting to login')
      await router.push('/login')
      return
    }
    
    if (event === 'SIGNED_IN' && session?.user) {
      console.log('User signed in, loading data')
      const userData = await getCurrentUser()
      if (userData) {
        await loadTeacherContacts()
        await loadBroadcastHistory()
      }
    }
  })
}

onMounted(async () => {
  console.log('Teacher messages component mounted')
  
  initDarkMode()
  setupAuthListener()
  
  document.addEventListener('click', () => {
    openSectionDropdown.value = null
  })
  
  document.addEventListener('click', handleClickOutside)
  
  const userData = await getCurrentUser()
  if (userData) {
    console.log('Teacher authenticated:', userData.profile.full_name)
    await loadTeacherContacts()
    await loadBroadcastHistory()
    await setupPresenceTracking()
    await updateTeacherPresence(true)
  }
})

onUnmounted(() => {
  console.log('Teacher messages component unmounted')
  updateTeacherPresence(false)
  document.removeEventListener('click', handleClickOutside)
})
</script>
        

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

/* Reset and Hide Parent Layouts */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Hide any parent layout elements */
body, html {
  overflow-x: hidden !important;
}

/* Dashboard Container Layout */
.dashboard-container {
  min-height: 100vh;
  width: 100vw;
  background: #f8fafc;
  font-family: 'Inter', sans-serif;
  overflow-x: hidden;
}

.dark .dashboard-container {
  background: #0f172a;
}

/* Sidebar Navigation - Simple Outlined Icons Only, Single Color, Active Highlight */
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
  display: flex;
  align-items: center;
  justify-content: center;
  height: 56px;
  width: 56px;
  margin: 8px 0;
  border-radius: 12px;
  transition: background 0.2s, box-shadow 0.2s;
  cursor: pointer;
  position: relative;
}

.sidebar-item.active {
  background: rgba(255,255,255,0.15);
  border: 2px solid #fff;
}

.sidebar-item:hover {
  background: rgba(255,255,255,0.22);
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
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

/* Top Navigation Bar (Greenish Theme) */
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

.navbar-right {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.nav-icon-btn {
  width: 44px;
  height: 44px;
  background: rgba(255, 255, 255, 0.15);
  border: none;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
  color: rgba(255, 255, 255, 0.9);
  position: relative;
}

.nav-icon-btn:hover {
  background: rgba(255, 255, 255, 0.25);
  color: white;
}

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
  color: rgba(255, 255, 255, 0.8);
  transition: transform 0.2s;
}

.user-profile:hover .dropdown-arrow {
  transform: rotate(180deg);
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

/* Notification dropdown styles */
.notif-wrapper {
  position: relative;
}

.notification-badge {
  position: absolute;
  top: -2px;
  right: -2px;
  background: #ef4444;
  color: white;
  border-radius: 50%;
  width: 18px;
  height: 18px;
  font-size: 0.75rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid #3D8D7A;
}

.notification-dropdown {
  position: absolute;
  top: 55px;
  right: 0;
  width: 360px;
  max-height: 480px;
  background: white;
  border-radius: 16px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
  overflow: hidden;
  z-index: 1001;
  border: 1px solid #e2e8f0;
}

.notification-dropdown .dropdown-header {
  padding: 1.25rem 1.5rem;
  border-bottom: 1px solid #e2e8f0;
  background: #fafafa;
}

.notification-dropdown .dropdown-header h3 {
  font-size: 1.1rem;
  font-weight: 600;
  color: #1e293b;
}

.notification-list {
  max-height: 400px;
  overflow-y: auto;
}

.no-notifications {
  padding: 3rem 1.5rem;
  text-align: center;
  color: #94a3b8;
  font-size: 0.9rem;
}

.notification-item {
  padding: 1rem 1.5rem;
  border-bottom: 1px solid #f1f5f9;
  transition: background 0.2s;
  cursor: pointer;
}

.notification-item:hover {
  background: #f8fafc;
}

.notification-item:last-child {
  border-bottom: none;
}

.notif-content h4 {
  font-size: 0.9rem;
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 0.25rem;
}

.notif-content p {
  font-size: 0.8rem;
  color: #64748b;
  margin-bottom: 0.5rem;
}

.notif-time {
  font-size: 0.75rem;
  color: #94a3b8;
}

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

/* Profile dropdown styling moved to end of file for specificity */

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
}

.profile-details p {
  font-size: 0.85rem;
  opacity: 0.9;
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

.logout-btn {
  color: #ef4444 !important;
}

.logout-btn:hover {
  background: #fef2f2 !important;
  color: #dc2626 !important;
}

.logout-btn svg {
  color: #ef4444 !important;
}

.logout-btn:hover svg {
  color: #dc2626 !important;
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
}

.header-title {
  font-size: 1.75rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 0.25rem;
}

.header-subtitle {
  font-size: 0.95rem;
  color: #64748b;
}

/* Loading Overlay - Green Theme */
.loading-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(251, 255, 228, 0.95);
  backdrop-filter: blur(8px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 100;
  animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.dark .loading-overlay {
  background: rgba(24, 28, 32, 0.95);
}

.loading-content {
  background: white;
  padding: 3rem 4rem;
  border-radius: 20px;
  text-align: center;
  box-shadow: 0 20px 60px rgba(61, 141, 122, 0.15);
  border: 2px solid #a3d1c6;
  animation: slideUp 0.4s ease;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.dark .loading-content {
  background: #23272b;
  border-color: #374151;
}

.loading-spinner-container {
  position: relative;
  width: 80px;
  height: 80px;
  margin: 0 auto 1.5rem;
}

.loading-spinner {
  width: 80px;
  height: 80px;
  border: 5px solid rgba(61, 141, 122, 0.1);
  border-left: 5px solid #3d8d7a;
  border-top: 5px solid #20c997;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto;
  box-shadow: 0 0 20px rgba(61, 141, 122, 0.1);
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.dark .loading-spinner {
  border: 5px solid rgba(32, 201, 151, 0.1);
  border-left: 5px solid #20c997;
  border-top: 5px solid #18a577;
  box-shadow: 0 0 20px rgba(32, 201, 151, 0.1);
}

.loading-text {
  font-size: 1.125rem;
  font-weight: 600;
  color: #1f2937;
  margin: 0;
  letter-spacing: 0.025em;
}

.dark .loading-text {
  color: #A3D1C6;
}

/* Full Screen Broadcast Form Enhancement */
.broadcast-form-fullscreen {
  width: 100%;
  min-height: calc(100vh - 200px);
  padding: 24px;
  background: white;
  border-radius: 16px;
  border: 1px solid #e5e7eb;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
}

.broadcast-form-columns {
  display: grid;
  grid-template-columns: 1fr 380px;
  gap: 32px;
  min-height: calc(100vh - 280px);
}

.broadcast-form-left {
  display: flex;
  flex-direction: column;
  gap: 20px;
  min-width: 0;
}

.broadcast-form-row {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 16px;
  align-items: end;
}

.form-group-compact {
  margin-bottom: 0;
  flex: 1;
}

.form-group-compact label {
  font-size: 14px;
  font-weight: 600;
  color: #374151;
  margin-bottom: 8px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.form-input-compact, .form-textarea-compact {
  width: 100%;
  padding: 12px 16px;
  border: 1px solid #d1d5db;
  border-radius: 10px;
  font-size: 15px;
  transition: all 0.2s;
  font-family: inherit;
}

.form-input-compact {
  min-height: 44px;
}

.form-textarea-compact {
  min-height: 140px;
  resize: vertical;
}

.form-input-compact:focus, .form-textarea-compact:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.char-count-inline {
  font-size: 12px;
  color: #6b7280;
  margin-top: 6px;
  text-align: right;
}

.upload-button-inline {
  padding: 12px 20px;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 10px;
  color: #475569;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 8px;
  white-space: nowrap;
  height: 44px;
}

.upload-button-inline:hover {
  background: #f1f5f9;
  border-color: #cbd5e1;
  transform: translateY(-1px);
}

.broadcast-form-right {
  width: 380px;
  border-left: 1px solid #f1f5f9;
  padding-left: 32px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.preview-section-compact, .attachments-section-compact {
  background: #f8fafc;
  border-radius: 12px;
  padding: 20px;
  border: 1px solid #f1f5f9;
}

.preview-section-compact h4, .attachments-section-compact h4 {
  margin: 0 0 16px 0;
  font-size: 15px;
  font-weight: 600;
  color: #374151;
}

.preview-content p {
  font-size: 14px;
  line-height: 1.5;
  color: #4b5563;
  margin: 0;
}

.preview-placeholder, .attachments-placeholder {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  padding: 32px;
  color: #9ca3af;
  text-align: center;
}

.attachments-preview-grid {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.attachment-preview-card {
  display: flex;
  align-items: center;
  gap: 12px;
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  padding: 12px;
  position: relative;
}

.attachment-preview-thumb {
  width: 48px;
  height: 48px;
  border-radius: 6px;
  overflow: hidden;
  flex-shrink: 0;
}

.attachment-preview-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.attachment-file-preview {
  width: 100%;
  height: 100%;
  background: #f3f4f6;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #6b7280;
}

.attachment-preview-info {
  flex: 1;
  min-width: 0;
}

.attachment-preview-name {
  font-size: 13px;
  font-weight: 500;
  color: #374151;
  margin: 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.attachment-preview-size {
  font-size: 12px;
  color: #6b7280;
}

.attachment-remove-btn {
  width: 24px;
  height: 24px;
  border: none;
  background: #fee2e2;
  color: #dc2626;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
}

.attachment-remove-btn:hover {
  background: #fecaca;
}

.ready-status {
  background: #ecfdf5;
  border: 1px solid #d1fae5;
  border-radius: 12px;
  padding: 16px;
  margin-top: auto;
}

.ready-indicator {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #059669;
  font-size: 14px;
  font-weight: 600;
}

.action-buttons-fullwidth {
  display: flex;
  gap: 16px;
  margin-top: 24px;
  width: 100%;
  justify-content: flex-end;
}

.btn-cancel-full, .btn-send-full {
  padding: 14px 24px;
  border-radius: 10px;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 8px;
  border: none;
  min-width: 160px;
  height: 48px;
  box-sizing: border-box;
  justify-content: center;
}

.btn-cancel-full {
  background: #f8fafc;
  color: #475569;
  border: 1px solid #e2e8f0;
}

.btn-cancel-full:hover {
  background: #f1f5f9;
  transform: translateY(-1px);
}

.btn-send-full {
  background: #3b82f6;
  color: white;
}

.btn-send-full:hover:not(:disabled) {
  background: #2563eb;
  transform: translateY(-1px);
}

.btn-send-full:disabled {
  background: #9ca3af;
  cursor: not-allowed;
  transform: none;
}

/* Enhanced Individual Broadcast Message Cards */
.broadcast-messages-list-enhanced {
  display: flex;
  flex-direction: column;
  gap: 24px;
  padding: 24px;
  max-width: 100%;
}

.broadcast-message-card-enhanced {
  background: white;
  border-radius: 16px;
  border: 1px solid #e5e7eb;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
  transition: all 0.2s;
  overflow: hidden;
}

.broadcast-message-card-enhanced:hover {
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
  transform: translateY(-1px);
}

.broadcast-card-header-enhanced {
  padding: 20px 24px 16px 24px;
  border-bottom: 1px solid #f1f5f9;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.broadcast-timestamp-enhanced {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #6b7280;
  font-size: 14px;
  font-weight: 500;
}

.broadcast-content-enhanced {
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.broadcast-message-section {
  display: flex;
  gap: 16px;
  align-items: flex-start;
}

.broadcast-icon-badge-enhanced {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, #3b82f6, #1d4ed8);
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
}

.broadcast-message-text-enhanced {
  font-size: 16px;
  line-height: 1.6;
  color: #374151;
  margin: 0;
  flex: 1;
}

.attachments-section-enhanced {
  border-top: 1px solid #f1f5f9;
  padding-top: 24px;
}

.attachments-header-enhanced {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 20px;
  font-size: 15px;
  font-weight: 600;
  color: #374151;
}

.attachments-gallery-enhanced {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  width: 100%;
}

.attachment-item-enhanced {
  border-radius: 12px;
  overflow: hidden;
  cursor: pointer;
  transition: all 0.2s;
  border: 1px solid #e5e7eb;
}

.attachment-item-enhanced:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
}

.image-attachment-enhanced {
  position: relative;
  width: 100%;
  height: 240px;
  overflow: hidden;
  background: #f8fafc;
}

.attachment-image-full {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s;
}

.attachment-item-enhanced:hover .attachment-image-full {
  transform: scale(1.05);
}

.image-overlay-enhanced {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, rgba(59, 130, 246, 0.8), rgba(29, 78, 216, 0.8));
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s;
}

.attachment-item-enhanced:hover .image-overlay-enhanced {
  opacity: 1;
}

.overlay-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  color: white;
  font-weight: 600;
}

.image-info-badge {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(to top, rgba(0, 0, 0, 0.8), transparent);
  padding: 16px;
}

.image-filename {
  color: white;
  font-size: 13px;
  font-weight: 600;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}

.file-attachment-enhanced {
  background: #f8fafc;
  padding: 24px;
  display: flex;
  align-items: center;
  gap: 20px;
  min-height: 120px;
}

.file-preview-enhanced {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  flex-shrink: 0;
}

.file-icon-large {
  color: #6b7280;
}

.file-type-badge {
  background: #3b82f6;
  color: white;
  padding: 4px 8px;
  border-radius: 6px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.05em;
}

.file-details-enhanced {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.file-name-enhanced {
  font-size: 16px;
  font-weight: 600;
  color: #374151;
  margin: 0;
}

.file-size-enhanced {
  font-size: 14px;
  color: #6b7280;
}

.download-btn-enhanced {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 16px;
  background: #3b82f6;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  align-self: flex-start;
}

.download-btn-enhanced:hover {
  background: #2563eb;
  transform: translateY(-1px);
}

/* Responsive for Enhanced Message Cards */
@media (max-width: 768px) {
  .broadcast-messages-list-enhanced {
    padding: 16px;
    gap: 16px;
  }
  
  .broadcast-content-enhanced {
    padding: 20px;
  }
  
  .attachments-gallery-enhanced {
    grid-template-columns: 1fr;
  }
  
  .image-attachment-enhanced {
    height: 200px;
  }
  
  .file-attachment-enhanced {
    flex-direction: column;
    text-align: center;
    gap: 16px;
  }
}

@media (max-width: 1200px) {
  .attachments-gallery-enhanced {
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  }
}

/* Enhanced Fullwidth History Grid */
.history-grid-enhanced-fullwidth {
  display: flex;
  flex-direction: column;
  gap: 12px;
  width: 100%;
  padding: 20px;
  max-width: none;
}

.history-card-enhanced-wide {
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.2s ease;
  overflow: hidden;
}

.history-card-enhanced-wide:hover {
  border-color: #3b82f6;
  box-shadow: 0 4px 12px rgba(59, 130, 246, 0.1);
  transform: translateY(-1px);
}

.card-layout-horizontal {
  display: grid;
  grid-template-columns: 280px 1fr 140px;
  padding: 20px 24px;
  gap: 24px;
  align-items: center;
  min-height: 100px;
}

.subject-info-section {
  display: flex;
  gap: 16px;
  align-items: center;
}

.subject-avatar-enhanced {
  width: 56px;
  height: 56px;
  background: linear-gradient(135deg, #3b82f6, #1d4ed8);
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 700;
  font-size: 20px;
  flex-shrink: 0;
  box-shadow: 0 4px 12px rgba(59, 130, 246, 0.2);
}

.subject-details-enhanced {
  min-width: 0;
  flex: 1;
}

.subject-details-enhanced h3 {
  margin: 0 0 8px 0;
  font-size: 18px;
  font-weight: 700;
  color: #111827;
  line-height: 1.3;
}

.section-badges-enhanced {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.section-badge, .code-badge, .grade-badge {
  font-size: 11px;
  padding: 3px 8px;
  border-radius: 6px;
  font-weight: 600;
  letter-spacing: 0.02em;
}

.section-badge {
  background: #dbeafe;
  color: #1e40af;
}

.code-badge {
  background: #f3f4f6;
  color: #374151;
}

.grade-badge {
  background: #dcfce7;
  color: #166534;
}

.latest-indicator {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  color: #6b7280;
  font-weight: 500;
}

.latest-message-content {
  width: 100%;
}

.latest-message-text {
  font-size: 14px;
  color: #374151;
  line-height: 1.5;
  margin: 0 0 8px 0;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}

.attachments-preview-compact {
  margin-top: 8px;
}

.attachments-row {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 12px;
  color: #6b7280;
}

.attachment-summary-icon {
  font-weight: 500;
}

.attachments-mini-preview {
  display: flex;
  gap: 4px;
  margin-left: auto;
}

.mini-attachment {
  width: 24px;
  height: 24px;
  border-radius: 4px;
  overflow: hidden;
  border: 1px solid #e5e7eb;
}

.mini-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.mini-file {
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f3f4f6;
  font-size: 8px;
  font-weight: 600;
  color: #6b7280;
}

.mini-more {
  width: 24px;
  height: 24px;
  border-radius: 4px;
  background: #f3f4f6;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 10px;
  font-weight: 600;
  color: #6b7280;
}

.stats-and-action-section {
  display: flex;
  align-items: center;
  gap: 16px;
  justify-content: flex-end;
}

.broadcast-stats-enhanced {
  text-align: center;
  background: #f8fafc;
  border-radius: 8px;
  padding: 8px 12px;
  border: 1px solid #f1f5f9;
  min-width: 60px;
}

.stats-number {
  font-size: 18px;
  font-weight: 700;
  color: #1f2937;
  line-height: 1;
}

.stats-label {
  font-size: 11px;
  color: #6b7280;
  font-weight: 500;
  margin-top: 2px;
}

.view-arrow {
  color: #9ca3af;
  transition: all 0.2s ease;
}

.history-card-enhanced-wide:hover .view-arrow {
  color: #3b82f6;
  transform: translateX(2px);
}

/* Responsive Design for Fullwidth Layout */
@media (max-width: 768px) {
  .history-grid-enhanced-fullwidth {
    padding: 12px;
  }

  .card-layout-horizontal {
    grid-template-columns: 1fr;
    gap: 16px;
    padding: 16px;
  }

  .subject-info-section {
    gap: 12px;
  }

  .stats-and-action-section {
    justify-content: space-between;
  }

  .latest-message-text {
    -webkit-line-clamp: 3;
    line-clamp: 3;
  }
}

.stats-label {
  font-size: 11px;
  color: #6b7280;
  font-weight: 600;
  margin-top: 4px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.latest-broadcast-enhanced {
  background: #f8fafc;
  border-radius: 12px;
  padding: 18px;
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 14px;
  border: 1px solid #f1f5f9;
}

.latest-header-enhanced {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
}

.latest-indicator {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  font-weight: 700;
  color: #059669;
}

.latest-timestamp {
  font-size: 12px;
  color: #6b7280;
  font-weight: 500;
}

.latest-content-enhanced {
  display: flex;
  flex-direction: column;
  gap: 14px;
  flex: 1;
}

.latest-message {
  font-size: 14px;
  color: #374151;
  line-height: 1.5;
  margin: 0;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.attachments-preview-enhanced {
  background: white;
  border-radius: 10px;
  padding: 14px;
  border: 1px solid #e5e7eb;
}

.attachments-grid-enhanced {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(80px, 1fr));
  gap: 10px;
  margin-bottom: 12px;
}

.attachment-tile-enhanced {
  width: 80px;
  height: 80px;
  border-radius: 8px;
  overflow: hidden;
  background: #f3f4f6;
  border: 1px solid #e5e7eb;
}

.image-tile-enhanced {
  position: relative;
  width: 100%;
  height: 100%;
}

.tile-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.image-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.3);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  opacity: 0;
  transition: opacity 0.2s;
}

.attachment-tile-enhanced:hover .image-overlay {
  opacity: 1;
}

.file-tile-enhanced {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 4px;
  background: #f9fafb;
}

.file-icon-enhanced {
  color: #6b7280;
}

.file-extension {
  font-size: 10px;
  font-weight: 700;
  color: #374151;
  text-transform: uppercase;
}

.more-attachments-tile {
  width: 80px;
  height: 80px;
  border-radius: 8px;
  background: #f3f4f6;
  border: 1px solid #e5e7eb;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2px;
}

.more-count {
  font-size: 16px;
  font-weight: 800;
  color: #3b82f6;
}

.more-label {
  font-size: 10px;
  font-weight: 600;
  color: #6b7280;
}

.attachments-summary {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  color: #6b7280;
  font-weight: 500;
}

.card-footer-enhanced {
  padding-top: 16px;
  border-top: 1px solid #f1f5f9;
}

.view-action {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 14px;
  font-weight: 600;
  color: #3b82f6;
}

/* Responsive Design */
@media (max-width: 1400px) {
  .broadcast-form-columns {
    grid-template-columns: 1fr 320px;
    gap: 24px;
  }
  
  .broadcast-form-right {
    width: 320px;
    padding-left: 24px;
  }
}

@media (max-width: 1200px) {
  .broadcast-form-columns {
    grid-template-columns: 1fr;
    gap: 24px;
  }
  
  .broadcast-form-right {
    width: 100%;
    border-left: none;
    border-top: 1px solid #f1f5f9;
    padding-left: 0;
    padding-top: 24px;
  }
  
  .history-grid-enhanced {
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 16px;
    padding: 16px;
  }
}

@media (max-width: 768px) {
  .broadcast-form-row {
    grid-template-columns: 1fr;
    gap: 12px;
  }
  
  .upload-button-inline {
    align-self: flex-start;
  }
  
  .history-grid-enhanced {
    grid-template-columns: 1fr;
    padding: 12px;
  }
  
  .card-header-enhanced {
    flex-direction: column;
    align-items: flex-start;
    gap: 16px;
  }
  
  .broadcast-stats-enhanced {
    align-self: flex-end;
  }
  
  .attachments-grid-enhanced {
    grid-template-columns: repeat(auto-fit, minmax(60px, 1fr));
  }
  
  .attachment-tile-enhanced, .more-attachments-tile {
    width: 60px;
    height: 60px;
  }
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Main Container */
.messages-container {
  min-height: 100vh;
  background: #FBFFE4;
  padding: 1.5rem 2rem;
  font-family: 'Inter', sans-serif;
  max-width: 1400px;
  margin: 0 auto;
}
.dark .messages-container {
  background: #181c20;
}

/* Header Section (Simple Uniform Style) */
.section-header-card {
  background: white;
  border-radius: 16px;
  padding: 1.5rem 2.5rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
  border: 2px solid #A3D1C6;
  width: 100%;
  max-width: none;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.dark .section-header-card {
  background: #23272b;
  border: 2px solid #20c997;
  box-shadow: 0 2px 8px rgba(0,0,0,0.25);
}

.section-header-left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.section-header-icon {
  width: 56px;
  height: 56px;
  background: linear-gradient(135deg, #A3D1C6 0%, #87C5B8 100%);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  box-shadow: 0 4px 12px rgba(163, 209, 198, 0.3);
}
.dark .section-header-icon {
  background: linear-gradient(135deg, #20c997 0%, #17a085 100%);
}

.section-header-title {
  font-size: 1.5rem;
  font-weight: 500;
  color: #2c3e50;
  margin-bottom: 0.25rem;
}
.dark .section-header-title {
  color: #ffffff;
}

.section-header-sub {
  font-size: 1rem;
  color: #6c757d;
  font-weight: 400;
}
.dark .section-header-sub {
  color: #adb5bd;
}

/* Header Actions */
.header-actions {
  display: flex;
  gap: 0.75rem;
  align-items: center;
}

.simple-action-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1rem;
  border: 2px solid #e9ecef;
  background: white;
  color: #6c757d;
  border-radius: 10px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  font-size: 0.9rem;
}
.dark .simple-action-btn {
  background: #2c3135;
  border-color: #495057;
  color: #adb5bd;
}

.simple-action-btn:hover {
  border-color: #20c997;
  background: rgba(32, 201, 151, 0.1);
  color: #2c3e50;
  transform: translateY(-1px);
}
.dark .simple-action-btn:hover {
  border-color: #20c997;
  background: rgba(32, 201, 151, 0.1);
  color: #ffffff;
}

.simple-action-btn.primary {
  border-color: #20c997;
  background: #20c997;
  color: white;
  box-shadow: 0 4px 12px rgba(32, 201, 151, 0.3);
}
.dark .simple-action-btn.primary {
  border-color: #20c997;
  background: #20c997;
  color: #ffffff;
}

.simple-action-btn.icon-only {
  padding: 0.75rem;
}

/* Controls Section */
.controls-section {
  display: flex;
  gap: 1.5rem;
  margin-bottom: 2rem;
  align-items: center;
  flex-wrap: wrap;
}

.search-box {
  position: relative;
  flex: 1;
  min-width: 300px;
}

.search-box svg {
  position: absolute;
  left: 1rem;
  top: 50%;
  transform: translateY(-50%);
  color: #6c757d;
}
.dark .search-box svg {
  color: #adb5bd;
}

.search-input {
  width: 100%;
  padding: 0.875rem 1rem 0.875rem 3rem;
  border: 2px solid #e9ecef;
  border-radius: 12px;
  font-size: 1rem;
  font-weight: 400;
  background: white;
  color: #495057;
  transition: all 0.2s ease;
}
.dark .search-input {
  background: #2c3135;
  border-color: #495057;
  color: #ffffff;
}

.search-input:focus {
  outline: none;
  border-color: #20c997;
  box-shadow: 0 0 0 3px rgba(32, 201, 151, 0.1);
}
.dark .search-input:focus {
  border-color: #20c997;
  box-shadow: 0 0 0 3px rgba(32, 201, 151, 0.1);
}

.filter-tabs {
  display: flex;
  gap: 0.5rem;
}

.filter-tab {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.75rem 1.25rem;
  border: 2px solid #e9ecef;
  background: white;
  color: #6c757d;
  border-radius: 10px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  font-size: 0.9rem;
}
.dark .filter-tab {
  background: #2c3135;
  border-color: #495057;
  color: #adb5bd;
}

.filter-tab:hover {
  border-color: #20c997;
  background: rgba(32, 201, 151, 0.1);
  color: #2c3e50;
  transform: translateY(-1px);
}
.dark .filter-tab:hover {
  border-color: #20c997;
  background: rgba(32, 201, 151, 0.1);
  color: #ffffff;
}

.filter-tab.active {
  border-color: #20c997;
  background: #20c997;
  color: white;
  box-shadow: 0 4px 12px rgba(32, 201, 151, 0.3);
}
.dark .filter-tab.active {
  border-color: #20c997;
  background: #20c997;
  color: #ffffff;
}

/* Grade Filter Tabs */
.grade-filter-tabs {
  display: flex;
  gap: 0.375rem;
  flex-wrap: wrap;
  margin-bottom: 1rem;
}

.grade-tab {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0.5rem 1rem;
  border: 2px solid #e9ecef;
  background: white;
  color: #6c757d;
  border-radius: 8px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  font-size: 0.85rem;
}

.dark .grade-tab {
  background: #2c3135;
  border-color: #495057;
  color: #adb5bd;
}

.grade-tab:hover {
  border-color: #20c997;
  background: rgba(32, 201, 151, 0.1);
  color: #2c3e50;
  transform: translateY(-1px);
}

.dark .grade-tab:hover {
  background: rgba(32, 201, 151, 0.15);
  color: #e9ecef;
}

.grade-tab.active {
  border-color: #20c997;
  background: #20c997;
  color: white;
  transform: translateY(-1px);
  box-shadow: 0 4px 15px rgba(32, 201, 151, 0.3);
}

.filter-tab.debug {
  border-color: #ffc107;
  color: #856404;
}
.dark .filter-tab.debug {
  border-color: #ffc107;
  color: #ffc107;
}

/* Debug Section */
.debug-section {
  background: white;
  border: 2px solid #ffc107;
  border-radius: 12px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
}
.dark .debug-section {
  background: #23272b;
  border-color: #ffc107;
}

.debug-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.debug-header h3 {
  color: #856404;
  font-size: 1.1rem;
  font-weight: 600;
}
.dark .debug-header h3 {
  color: #ffc107;
}

.close-debug-btn {
  background: none;
  border: none;
  font-size: 1.5rem;
  color: #856404;
  cursor: pointer;
}
.dark .close-debug-btn {
  color: #ffc107;
}

.debug-content p {
  margin-bottom: 0.5rem;
  color: #495057;
}
.dark .debug-content p {
  color: #adb5bd;
}

/* Content Area */
.content-area {
  min-height: 400px;
}

.tab-content {
  width: 100%;
}

/* Section Overview Cards */
.section-overview-card {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 10px;
  padding: 1.25rem;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
  margin-bottom: 1rem;
}

.section-overview-card:hover {
  border-color: #20c997;
  box-shadow: 0 2px 4px rgba(32, 201, 151, 0.08);
  transform: translateY(-1px);
}

.dark .section-overview-card {
  background: #1e293b;
  border-color: #334155;
}
.dark .section-overview-card:hover {
  border-color: #20c997;
  box-shadow: 0 2px 4px rgba(32, 201, 151, 0.08);
}

.section-icon {
  width: 44px;
  height: 44px;
  background: linear-gradient(135deg, #20c997 0%, #20c997 100%);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 600;
  font-size: 1.1rem;
  margin-bottom: 1rem;
}

.section-title {
  font-size: 1.1rem;
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 0.25rem;
}
.dark .section-title {
  color: #f8fafc;
}

.section-grade {
  font-size: 0.875rem;
  color: #64748b;
  margin-bottom: 1rem;
}
.dark .section-grade {
  color: #94a3b8;
}

.section-students-count {
  font-size: 0.875rem;
  color: #64748b;
}
.dark .section-students-count {
  color: #94a3b8;
}

.section-code-value {
  background: #f1f5f9;
  padding: 0.5rem;
  border-radius: 6px;
  font-family: monospace;
  font-size: 0.875rem;
  color: #1e293b;
  cursor: pointer;
}
.dark .section-code-value {
  background: #334155;
  color: #f8fafc;
}

.broadcast-quick-btn {
  background: #20c997;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.2s ease;
}
.broadcast-quick-btn:hover {
  background: #17a085;
}

/* Section Students View */
.section-students-view {
  width: 100%;
}

.section-students-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.5rem;
  padding: 1rem;
  background: white;
  border-radius: 10px;
  border: 1px solid #e2e8f0;
}
.dark .section-students-header {
  background: #1e293b;
  border-color: #334155;
}

.back-to-sections-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1rem;
  background: white;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  color: #64748b;
  cursor: pointer;
  transition: all 0.2s ease;
}
.back-to-sections-btn:hover {
  border-color: #20c997;
  color: #20c997;
}
.dark .back-to-sections-btn {
  background: #334155;
  border-color: #475569;
  color: #94a3b8;
}

.section-students-info h3 {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 0.5rem;
}
.dark .section-students-info h3 {
  color: #f8fafc;
}

.section-students-meta {
  display: flex;
  gap: 1rem;
  font-size: 0.875rem;
  color: #64748b;
}
.dark .section-students-meta {
  color: #94a3b8;
}

.section-broadcast-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1rem;
  background: #20c997;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
}
.section-broadcast-btn:hover {
  background: #17a085;
}

.section-students-list {
  display: grid;
  gap: 1rem;
}

.section-student-item {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 10px;
  padding: 1.25rem;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  gap: 1rem;
}

.section-student-item:hover {
  border-color: #20c997;
  box-shadow: 0 2px 4px rgba(32, 201, 151, 0.08);
  transform: translateY(-1px);
}

.dark .section-student-item {
  background: #1e293b;
  border-color: #334155;
}
.dark .section-student-item:hover {
  border-color: #20c997;
}

.section-student-item.has-unread {
  border-left: 3px solid #dc3545;
}

.section-student-avatar {
  width: 44px;
  height: 44px;
  background: linear-gradient(135deg, #20c997 0%, #20c997 100%);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 600;
  font-size: 1.1rem;
  position: relative;
}

.online-indicator {
  position: absolute;
  bottom: -2px;
  right: -2px;
  width: 12px;
  height: 12px;
  background: #10b981;
  border: 2px solid white;
  border-radius: 50%;
  animation: pulse-online 2s infinite;
}

.section-student-details {
  flex: 1;
}

.section-student-name {
  font-size: 1.05rem;
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 0.25rem;
}
.dark .section-student-name {
  color: #f8fafc;
}

.section-student-email {
  font-size: 0.875rem;
  color: #64748b;
  margin-bottom: 0.25rem;
}
.dark .section-student-email {
  color: #94a3b8;
}

.section-student-id {
  font-size: 0.75rem;
  color: #94a3b8;
  margin-bottom: 0.25rem;
}
.dark .section-student-id {
  color: #64748b;
}

.presence-status {
  font-size: 0.75rem;
  color: #10b981;
}

.section-last-message {
  font-size: 0.875rem;
  color: #64748b;
  margin-top: 0.5rem;
}
.dark .section-last-message {
  color: #94a3b8;
}

/* Empty States */
.empty-state {
  text-align: center;
  padding: 4rem 2rem;
  color: #6c757d;
}
.dark .empty-state {
  color: #adb5bd;
}

.empty-state p {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: #495057;
}
.dark .empty-state p {
  color: #ffffff;
}

.empty-subtext {
  font-size: 1rem;
  color: #6c757d;
}
.dark .empty-subtext {
  color: #adb5bd;
}

/* Simple Loading Overlay */
.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
}

.loading-content {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  text-align: center;
  min-width: 200px;
}

.dark .loading-content {
  background: #232c2d;
  color: #b3d8a8;
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 3px solid #e5e7eb;
  border-top: 3px solid #3d8d7a;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 1rem;
}

.dark .loading-spinner {
  border: 3px solid #2a3c36;
  border-top: 3px solid #b3d8a8;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.loading-text {
  font-size: 1rem;
  font-weight: 500;
  color: #374151;
  margin: 0;
}

.dark .loading-text {
  color: #b3d8a8;
}

/* Responsive Design */
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
  
  .header-content {
    flex-direction: column;
    align-items: stretch;
    gap: 1rem;
  }
  
  .navbar-content {
    padding: 0 0.5rem;
  }
  
  .brand-name {
    display: none;
  }
  
  .controls-section {
    flex-direction: column;
    align-items: stretch;
  }
  
  .search-box {
    min-width: auto;
  }
  
  .filter-tabs {
    justify-content: center;
    flex-wrap: wrap;
  }
  
  .filter-tab {
    flex: 1;
    min-width: 0;
    padding: 0.75rem 0.5rem;
    font-size: 0.85rem;
  }
  
  .grade-filter-tabs {
    justify-content: center;
    gap: 0.25rem;
  }
  
  .grade-tab {
    padding: 0.5rem 0.75rem;
    font-size: 0.8rem;
    min-width: auto;
  }
}

/* Keep existing modal and specialized component styles below this comment */

.header-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.header-icon {
  width: 56px;
  height: 56px;
  background: #3D8D7A;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.dark .header-icon {
  background: #A3D1C6;
  color: #23272b;
}

.header-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1f2937;
  margin: 0;
}

.dark .header-title {
  color: #FBFFE4;
}

.header-subtitle {
  color: #6b7280;
  font-size: 0.9rem;
  font-weight: 500;
  margin: 0.25rem 0 0 0;
}

.dark .header-subtitle {
  color: #B3D8A8;
}

.header-actions {
  display: flex;
  gap: 0.75rem;
}

/* Buttons */
.action-btn, .debug-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 8px;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
  font-family: 'Inter', sans-serif;
}

.action-btn {
  background: #20c997;
  color: #181c20;
  border: 1px solid #A3D1C6;
}

.action-btn:hover {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
  transform: translateY(-1px);
}

.dark-mode-toggle {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border: none;
  border-radius: 8px;
  background: #B3D8A8;
  color: #3D8D7A;
  cursor: pointer;
  transition: all 0.2s;
}

.dark-mode-toggle:hover {
  background: #A3D1C6;
  transform: translateY(-1px);
}

.dark .dark-mode-toggle {
  background: #3D8D7A;
  color: #B3D8A8;
}

.dark .dark-mode-toggle:hover {
  background: #2d6b5a;
}

.debug-btn {
  background: #B3D8A8;
  color: #1f2937;
}

.debug-btn:hover {
  background: #9bc993;
  transform: translateY(-1px);
}

.dark .action-btn {
  background: #20c997;
  color: #181c20;
  border: 1px solid #A3D1C6;
}

.dark .debug-btn {
  background: #A3D1C6;
  color: #23272b;
}

/* Content Card */
.content-card {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}

.dark .content-card {
  background: #23272b;
  border: 1px solid #20c997;
  box-shadow: 0 2px 8px rgba(0,0,0,0.25);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.25rem; 
}

.card-header h3 {
  font-size: 1.125rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.25rem;
}
.dark .card-header h3 {
  color: #A3D1C6;
}

/* Tabs - Enhanced to match MySubjects.vue */
.tabs {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}

.tab-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.25rem;
  border: 1.5px solid #A3D1C6;
  border-radius: 8px;
  font-size: 0.875rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  background: #FBFFE4;
  color: #3D8D7A;
  font-family: 'Inter', sans-serif;
}

.tab-btn.active {
  background: #3D8D7A;
  color: white;
  border-color: #3D8D7A;
  box-shadow: 0 2px 4px rgba(61, 141, 122, 0.1);
}

.tab-btn:hover:not(.active) {
  background: white;
  border-color: #3D8D7A;
  transform: translateY(-1px);
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.15);
}

.dark .tab-btn {
  background: #181c1f;
  border: 1.5px solid #20c997;
  color: #A3D1C6;
}

.dark .tab-btn.active {
  background: #20c997;
  color: #181c20;
  border-color: #20c997;
}

.dark .tab-btn:hover:not(.active) {
  background: #20242a;
  border-color: #20c997;
}

/* Tab Content */
.tab-content {
  min-height: 400px;
}

/* Section Overview Cards - Complete MySubjects.vue Style */
.sections-overview {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 1.5rem;
  max-width: 100%;
  margin-top: 1.5rem;
}

.section-overview-card {
  background: #ffffff;
  border: 1.5px solid #B3D8A8;
  border-radius: 12px;
  padding: 1.5rem;
  transition: all 0.2s ease;
  cursor: pointer;
  position: relative;
}

.section-overview-card:hover {
  border-color: #3D8D7A;
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(61, 141, 122, 0.15);
}

.dark .section-overview-card {
  background: #2a2d35;
  border: 1.5px solid #3a3f47;
}

.dark .section-overview-card:hover {
  border-color: #A3D1C6;
  box-shadow: 0 4px 16px rgba(163, 209, 198, 0.15);
}

/* Section Card Header */
.section-card-header {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  margin-bottom: 1rem;
}

.section-icon {
  width: 48px;
  height: 48px;
  background: #20c997;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 1.25rem;
  color: white;
  flex-shrink: 0;
}

.section-title-area {
  flex: 1;
  min-width: 0;
}

.section-title {
  font-size: 0.92rem;
  font-weight: 600;
  color: #23423a;
  margin: 0;
  font-family: 'Inter', sans-serif;
}

.dark .section-title {
  color: #fff;
}

.section-grade {
  font-size: 0.875rem;
  color: #3D8D7A;
  margin: 0;
  font-family: 'Inter', sans-serif;
}

.dark .section-grade {
  color: #B3D8A8;
}

.section-options-btn {
  background: none;
  border: none;
  color: #9ca3af;
  cursor: pointer;
  padding: 0.25rem;
  border-radius: 4px;
  transition: all 0.2s ease;
}

.section-options-btn:hover {
  background: #374151;
  color: #20c997;
}

/* Section Options Container */
.section-options-container {
  position: relative;
}

/* Section Options Dropdown */
.section-options-dropdown {
  position: absolute;
  top: 100%;
  right: 0;
  background: #fff;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  min-width: 160px;
  z-index: 1000;
  overflow: hidden;
}

.dark .section-options-dropdown {
  background: #23272b;
  border-color: #374151;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}

.dropdown-option {
  width: 100%;
  padding: 0.75rem 1rem;
  border: none;
  background: none;
  color: #374151;
  font-size: 0.875rem;
  font-weight: 500;
  text-align: left;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.dropdown-option:hover {
  background: #f3f4f6;
}

.dark .dropdown-option {
  color: #e5e7eb;
}

.dark .dropdown-option:hover {
  background: #374151;
}

.dropdown-option.delete {
  color: #dc2626;
}

.dropdown-option.delete:hover {
  background: #fef2f2;
  color: #b91c1c;
}

.dark .dropdown-option.delete {
  color: #f87171;
}

.dark .dropdown-option.delete:hover {
  background: #451a1a;
  color: #fca5a5;
}

.dropdown-option.archive {
  color: #d97706;
}

.dropdown-option.archive:hover {
  background: #fffbeb;
  color: #b45309;
}

.dark .dropdown-option.archive {
  color: #fbbf24;
}

.dark .dropdown-option.archive:hover {
  background: #451a03;
  color: #fcd34d;
}

/* Section Stats */
.section-stats {
  margin-bottom: 1rem;
}

.section-students-count {
  font-size: 0.875rem;
  color: #9ca3af;
  font-family: 'Inter', sans-serif;
}

/* Section Code Display */
.section-code-display {
  margin-bottom: 1rem;
}

.section-code-label {
  font-size: 0.75rem;
  font-weight: 600;
  color: #6b7280;
  margin-bottom: 0.5rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.section-code-value {
  background: #fff;
  border: 1.5px solid #B3D8A8;
  border-radius: 8px;
  padding: 0.75rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-family: 'Courier New', monospace;
  font-size: 0.95rem;
  color: #1f2937;
  font-weight: 600;
  transition: background 0.2s, border 0.2s;
}

.dark .section-code-value {
  background: #1f2937;
  border: 1.5px solid #374151;
  color: #fff;
}

.copy-code-btn {
  background: #20c997;
  border: none;
  border-radius: 6px;
  padding: 0.25rem 0.5rem;
  color: #1f2937;
  font-size: 0.75rem;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.25rem;
  transition: all 0.2s ease;
}

.copy-code-btn:hover {
  background: #18b087;
  transform: scale(1.05);
}

/* Section Card Actions */
.section-card-actions {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

.students-count-badge {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.875rem;
  color: #9ca3af;
}

.broadcast-quick-btn {
  background: #374151;
  border: 1px solid #4b5563;
  border-radius: 6px;
  padding: 0.5rem 0.75rem;
  color: #d1d5db;
  font-size: 0.875rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.2s ease;
}

.broadcast-quick-btn:hover {
  background: #4b5563;
  border-color: #20c997;
  color: #20c997;
}

.section-overview-header {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
}

.section-overview-icon {
  width: 48px;
  height: 48px;
  background: #3D8D7A;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
  font-weight: 600;
  font-size: 1.25rem;
}

.section-overview-info {
  flex: 1;
}

.section-overview-title {
  color: #3D8D7A;
  font-size: 1rem;
  font-weight: 600;
  margin-bottom: 0.25rem;
  line-height: 1.3;
}

.dark .section-overview-title {
  color: #A3D1C6;
  font-weight: 700;
}

.section-overview-subtitle {
  font-size: 0.875rem;
  color: #6b7280;
  margin-bottom: 0.25rem;
}
.dark .section-overview-subtitle {
  color: #A3D1C6;
}

.section-overview-grade {
  font-size: 0.813rem;
  color: #6b7280;
}
.dark .section-overview-grade {
  color: #A3D1C6;
}

/* Section Code Inline - Like MySubjects.vue */
.section-code-inline {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: #F8F9FA;
  border: 1px solid #A3D1C6;
  border-radius: 6px;
  padding: 0.25rem 0.6rem;
  font-size: 0.875rem;
  margin-bottom: 0.25rem;
}

.dark .section-code-inline {
  background: #181c1f;
  border: 1px solid #20c997;
}

.code-label {
  color: #3D8D7A;
  font-weight: 600;
  font-size: 0.75rem;
}

.dark .code-label {
  color: #20c997;
}

.section-code-value {
  background: #fff;
  border: 1.5px solid #B3D8A8;
  border-radius: 8px;
  padding: 0.6rem 0.7rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-family: 'Fira Mono', 'Consolas', 'Courier New', monospace;
  font-size: 0.85rem;
  color: #23423a;
  font-weight: 500;
  letter-spacing: 0.04em;
  transition: background 0.2s, border 0.2s;
  white-space: nowrap;
  overflow-x: auto;
}

.count-number {
  display: block;
  font-size: 1.25rem;
  font-weight: 700;
  color: #3D8D7A;
  line-height: 1;
}

.count-label {
  font-size: 0.75rem;
  color: #6b7280;
  font-weight: 500;
  margin-top: 0.25rem;
}
.dark .count-label {
  color: #A3D1C6;
}

.section-overview-unread {
  background: #ef4444;
  color: white;
  padding: 0.25rem 0.5rem;
  border-radius: 999px;
  font-size: 0.75rem;
  font-weight: 600;
  text-align: center;
}

.unread-number {
  display: block;
  font-weight: 700;
}

.unread-label {
  font-size: 0.688rem;
}

/* Student List Items - Enhanced to match MySubjects.vue */
.students-list, .section-students-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.student-item, .section-student-item {
  background: #FBFFE4;
  border: 1.5px solid #A3D1C6;
  border-radius: 12px;
  padding: 1.25rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  transition: all 0.2s ease;
  cursor: pointer;
  font-family: 'Inter', sans-serif;
}

.student-item:hover, .section-student-item:hover {
  background: white;
  border-color: #3D8D7A;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.15);
}

.student-item.has-unread, .section-student-item.has-unread {
  border-color: #3D8D7A;
  background: #f0fdf4;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.1);
}

.dark .student-item, 
.dark .section-student-item {
  background: #181c1f;
  border: 1.5px solid #20c997;
}

.dark .student-item:hover, 
.dark .section-student-item:hover {
  background: #20242a;
  border-color: #20c997;
  box-shadow: 0 4px 12px rgba(32, 201, 151, 0.15);
}

.dark .student-item.has-unread, 
.dark .section-student-item.has-unread {
  border-color: #20c997;
  background: #0f1b16;
  box-shadow: 0 2px 8px rgba(32, 201, 151, 0.1);
}

.student-avatar, .section-student-avatar {
  width: 40px;
  height: 40px;
  background: #3D8D7A;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 600;
  font-size: 0.875rem;
  flex-shrink: 0;
  position: relative;
}

.online-indicator {
  position: absolute;
  bottom: -2px;
  right: -2px;
  width: 12px;
  height: 12px;
  background: #28a745;
  border: 2px solid white;
  border-radius: 50%;
  box-shadow: 0 0 0 2px rgba(40, 167, 69, 0.3);
  animation: pulse-online 2s infinite;
}

.dark .online-indicator {
  border-color: #181c1f;
}

@keyframes pulse-online {
  0%, 100% {
    box-shadow: 0 0 0 2px rgba(40, 167, 69, 0.3);
  }
  50% {
    box-shadow: 0 0 0 4px rgba(40, 167, 69, 0.1);
  }
}

.student-info, .section-student-info {
  flex: 1;
}

.student-name, .section-student-name {
  font-size: 0.938rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.25rem;
}
.dark .student-name, 
.dark .section-student-name {
  color: #A3D1C6;
}

.student-email, .section-student-email {
  font-size: 0.813rem;
  color: #6b7280;
  margin-bottom: 0.125rem;
}
.dark .student-email, 
.dark .section-student-email {
  color: #A3D1C6;
}

.section-student-id {
  font-size: 0.75rem;
  color: #6b7280;
}
.dark .section-student-id {
  color: #A3D1C6;
}

.presence-status {
  font-size: 0.75rem;
  color: #28a745;
  margin: 0.25rem 0 0 0;
  font-weight: 500;
}
.dark .presence-status {
  color: #20c997;
}

.last-message, .section-last-message {
  font-style: italic;
  color: #6b7280;
  font-size: 0.75rem;
}

.message-status, .section-message-status {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 0.25rem;
}

.unread-badge, .section-unread-badge {
  background: #ef4444;
  color: white;
  padding: 0.125rem 0.375rem;
  border-radius: 999px;
  font-size: 0.688rem;
  font-weight: 600;
}

.last-time, .section-last-time {
  color: #6b7280;
  font-size: 0.75rem;
}

.chat-icon, .section-chat-icon {
  color: #3D8D7A;
}

/* Archived Items - MySubjects.vue style */
.student-item.archived {
  background: #f3f4f6;
  border: 1.5px solid #d1d5db;
  opacity: 0.8;
}

.student-item.archived:hover {
  background: #e5e7eb;
  border-color: #9ca3af;
  opacity: 1;
}

.dark .student-item.archived {
  background: #111;
  border: 1.5px solid #374151;
  opacity: 0.8;
}

.dark .student-item.archived:hover {
  background: #1f2937;
  border-color: #4b5563;
  opacity: 1;
}

/* Back to Sections Button */
.back-to-sections-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  background: white;
  color: #6b7280;
  cursor: pointer;
  transition: all 0.2s;
  font-size: 0.875rem;
  font-weight: 500;
  font-family: 'Inter', sans-serif;
}

.back-to-sections-btn:hover {
  background: #f9fafb;
  border-color: #3D8D7A;
  color: #3D8D7A;
}

.dark .back-to-sections-btn {
  background: #374151;
  border-color: #4b5563;
  color: #A3D1C6;
}

.dark .back-to-sections-btn:hover {
  background: #4b5563;
  border-color: #20c997;
  color: #20c997;
}

/* Section Students Header */
.section-students-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.5rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid #e5e7eb;
}
.dark .section-students-header {
  border-bottom-color: #374151;
}

.section-students-info h3 {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.5rem;
}
.dark .section-students-info h3 {
  color: #A3D1C6;
}

.section-students-meta {
  display: flex;
  gap: 1rem;
  color: #6b7280;
  font-size: 0.875rem;
}
.dark .section-students-meta {
  color: #A3D1C6;
}

.section-broadcast-btn {
  background: #3D8D7A;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.2s;
  font-size: 0.875rem;
  font-weight: 500;
  font-family: 'Inter', sans-serif;
}

.section-broadcast-btn:hover {
  background: #2d6b5a;
  transform: translateY(-1px);
}

.dark .section-broadcast-btn {
  background: #20c997;
  color: #181c20;
}

/* Search and Actions */
.section-actions {
  display: flex;
  gap: 1rem;
  margin-bottom: 1.25rem;
  align-items: center;
}

.search-bar {
  position: relative;
  flex: 1;
  max-width: 400px;
}

.search-icon {
  position: absolute;
  left: 0.75rem;
  top: 50%;
  transform: translateY(-50%);
  color: #6b7280;
}

.search-input {
  width: 100%;
  padding: 0.75rem 0.75rem 0.75rem 2.75rem;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  font-size: 0.875rem;
  font-family: 'Inter', sans-serif;
  background: white;
  color: #1f2937;
}

.search-input:focus {
  outline: none;
  border-color: #3D8D7A;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
}

.dark .search-input {
  background: #374151;
  border-color: #4b5563;
  color: #A3D1C6;
}

.dark .search-input:focus {
  border-color: #20c997;
  box-shadow: 0 0 0 3px rgba(32, 201, 151, 0.1);
}

.section-filter {
  padding: 0.75rem 1rem;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  font-size: 0.875rem;
  background: white;
  color: #1f2937;
  font-family: 'Inter', sans-serif;
}

.dark .section-filter {
  background: #374151;
  border-color: #4b5563;
  color: #A3D1C6;
}

.dark .header-subtitle {
  color: #a0a0a0;
}

.header-actions {
  display: flex;
  gap: 12px;
}

/* Buttons */
.action-btn, .debug-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  border: none;
  border-radius: 6px;
  font-size: 0.9rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
}

.action-btn {
  background: #3D8D7A;
  color: white;
}

.action-btn:hover {
  background: #2d6b5a;
}

.debug-btn {
  background: #B3D8A8;
  color: #2c3e50;
}

.debug-btn:hover {
  background: #9bc993;
}

.dark .action-btn {
  background: #3D8D7A;
}

.dark .debug-btn {
  background: #B3D8A8;
  color: #2c3e50;
}

/* Content Card */
.content-card {
  background: white;
  border-radius: 12px;
  padding: 24px;
  margin-bottom: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  border: 1px solid #e0e0e0;
}

.dark .content-card {
  background: #2a2a2a;
  border-color: #404040;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  border-bottom: 1px solid #e0e0e0;
  padding-bottom: 16px;
}

.dark .card-header {
  border-bottom-color: #404040;
}

/* Tabs */
.tabs {
  display: flex;
  gap: 8px;
}

.tab-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 20px;
  border: none;
  border-radius: 8px;
  font-size: 0.9rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  background: #f8f9fa;
  color: #6c757d;
}

.tab-btn.active {
  background: #3D8D7A;
  color: white;
}

.tab-btn:hover:not(.active) {
  background: #e9ecef;
}

.dark .tab-btn {
  background: #404040;
  color: #a0a0a0;
}

.dark .tab-btn.active {
  background: #3D8D7A;
  color: white;
}

.dark .tab-btn:hover:not(.active) {
  background: #505050;
}

/* Tab Content */
.tab-content {
  min-height: 400px;
}

/* Students View */
.section-students-view {
  padding: 20px 0;
}

.section-students-header {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 24px;
  padding-bottom: 16px;
  border-bottom: 1px solid #e0e0e0;
}

.dark .section-students-header {
  border-bottom-color: #404040;
}

.back-to-sections-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  background: white;
  color: #6c757d;
  cursor: pointer;
  transition: all 0.3s ease;
}

.back-to-sections-btn:hover {
  background: #f8f9fa;
  border-color: #3D8D7A;
  color: #3D8D7A;
}

.dark .back-to-sections-btn {
  background: #404040;
  border-color: #505050;
  color: #a0a0a0;
}

.dark .back-to-sections-btn:hover {
  background: #505050;
  border-color: #3D8D7A;
  color: #3D8D7A;
}

.section-students-info {
  flex: 1;
}

.section-students-info h3 {
  margin: 0 0 4px 0;
  color: #2c3e50;
  font-size: 1.2rem;
}

.dark .section-students-info h3 {
  color: #e0e0e0;
}

.section-students-meta {
  display: flex;
  gap: 16px;
  color: #6c757d;
  font-size: 0.9rem;
}

.section-broadcast-btn {
  background: #3D8D7A;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 6px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 8px;
  transition: all 0.3s ease;
}

.section-broadcast-btn:hover {
  background: #2d6b5a;
}

/* Student Lists */
.section-students-list, .students-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.section-student-item, .student-item {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 16px;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.section-student-item:hover, .student-item:hover {
  background: #f8f9fa;
  transform: translateY(-1px);
}

.section-student-item.has-unread, .student-item.has-unread {
  border-color: #3D8D7A;
  background: #f0f9f7;
}

.dark .section-student-item, .dark .student-item {
  border-color: #404040;
  background: #333;
}

.dark .section-student-item:hover, .dark .student-item:hover {
  background: #404040;
}

.dark .section-student-item.has-unread, .dark .student-item.has-unread {
  border-color: #3D8D7A;
  background: #2a3d37;
}

.section-student-avatar, .student-avatar {
  width: 40px;
  height: 40px;
  background: #3D8D7A;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: bold;
}

.section-student-info, .student-info {
  flex: 1;
}

.section-student-details, .student-details {
  flex: 1;
}

.section-student-name, .student-name {
  margin: 0 0 4px 0;
  color: #2c3e50;
  font-size: 1rem;
}

.dark .section-student-name, .dark .student-name {
  color: #e0e0e0;
}

.section-student-email, .student-email {
  margin: 0 0 2px 0;
  color: #6c757d;
  font-size: 0.9rem;
}

.section-student-id {
  margin: 0 0 2px 0;
  color: #6c757d;
  font-size: 0.8rem;
}

.section-last-message, .last-message {
  font-style: italic;
  color: #6c757d !important;
  font-size: 0.8rem !important;
}

.section-message-status, .message-status {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 4px;
}

.section-unread-badge, .unread-badge {
  background: #dc3545;
  color: white;
  padding: 2px 6px;
  border-radius: 10px;
  font-size: 0.7rem;
  font-weight: bold;
}

.section-last-time, .last-time {
  color: #6c757d;
  font-size: 0.8rem;
}

.section-chat-icon, .chat-icon {
  color: #3D8D7A;
}

/* Sections Overview */
.sections-overview {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
}

.section-overview-card {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  overflow: hidden;
  transition: all 0.3s ease;
}

.section-overview-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.dark .section-overview-card {
  border-color: #404040;
  background: #333;
}

.section-overview-header {
  padding: 20px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 16px;
}

.section-overview-icon {
  width: 40px;
  height: 40px;
  background: #B3D8A8;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #2c3e50;
}

.section-overview-info {
  flex: 1;
}

.section-overview-title {
  margin: 0 0 4px 0;
  color: #2c3e50;
  font-size: 1.1rem;
}

.dark .section-overview-title {
  color: #e0e0e0;
}

.section-overview-subtitle {
  margin: 0 0 4px 0;
  color: #6c757d;
  font-size: 0.9rem;
}

.section-overview-grade {
  margin: 0;
  color: #6c757d;
  font-size: 0.8rem;
}

.section-overview-stats {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}

.section-overview-count {
  text-align: center;
}

.count-number {
  display: block;
  font-size: 1.2rem;
  font-weight: bold;
  color: #3D8D7A;
}

.count-label {
  font-size: 0.8rem;
  color: #6c757d;
}

.section-overview-unread {
  background: #dc3545;
  color: white;
  padding: 4px 8px;
  border-radius: 12px;
  font-size: 0.8rem;
  text-align: center;
}

.unread-number {
  display: block;
  font-weight: bold;
}

.unread-label {
  font-size: 0.7rem;
}

/* Search and Actions */
.section-actions {
  display: flex;
  gap: 16px;
  margin-bottom: 20px;
  align-items: center;
}

.search-bar {
  position: relative;
  flex: 1;
  max-width: 400px;
}

.search-icon {
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  color: #6c757d;
}

.search-input {
  width: 100%;
  padding: 12px 12px 12px 44px;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  font-size: 0.9rem;
}

.dark .search-input {
  background: #404040;
  border-color: #505050;
  color: #e0e0e0;
}

.section-filter {
  padding: 12px 16px;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  font-size: 0.9rem;
  background: white;
}

.dark .section-filter {
  background: #404040;
  border-color: #505050;
  color: #e0e0e0;
}

/* Broadcast Form */
.broadcast-form {
  max-width: 600px;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  font-weight: 500;
  color: #2c3e50;
}

.dark .form-group label {
  color: #e0e0e0;
}

.form-input, .form-textarea, .form-select {
  width: 100%;
  padding: 12px;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  font-size: 0.9rem;
}

.form-textarea {
  min-height: 120px;
  resize: vertical;
}

.dark .form-input,
.dark .form-textarea,
.dark .form-select {
  background: #404040;
  border-color: #505050;
  color: #e0e0e0;
}

/* Attachments */
.attachments-preview {
  background: #f8f9fa;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 12px;
  margin-bottom: 12px;
}

.dark .attachments-preview {
  background: #333;
  border-color: #404040;
}

.attachment-preview-list {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.attachment-preview-item {
  display: flex;
  align-items: center;
  gap: 8px;
  background: white;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  padding: 8px;
}

.dark .attachment-preview-item {
  background: #404040;
  border-color: #505050;
}

.attachment-preview-image {
  width: 30px;
  height: 30px;
  object-fit: cover;
  border-radius: 4px;
}

.attachment-preview-file {
  display: flex;
  align-items: center;
  gap: 6px;
}

.attachment-name {
  font-size: 0.8rem;
  color: #2c3e50;
}

.dark .attachment-name {
  color: #e0e0e0;
}

.remove-attachment-btn {
  background: #dc3545;
  color: white;
  border: none;
  border-radius: 50%;
  width: 20px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 0.7rem;
}

/* Modal Styles - Simple & Clean Design */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  border-radius: 12px;
  max-width: 700px;
  width: 90%;
  max-height: 85vh;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
  display: flex;
  flex-direction: column;
}

.dark .modal-content {
  background: #1f2937;
  border: 1px solid #374151;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  border-bottom: 1px solid #e5e7eb;
  background: #f9fafb;
}

.dark .modal-header {
  border-bottom-color: #374151;
  background: #111827;
}

.modal-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1f2937;
  margin: 0;
  font-family: 'Inter', sans-serif;
}

.dark .modal-title {
  color: #f3f4f6;
}

.header-info {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex: 1;
}

.student-avatar {
  width: 45px;
  height: 45px;
  border-radius: 50%;
  background: #20c997;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 1.1rem;
  font-family: 'Inter', sans-serif;
}

.header-details {
  flex: 1;
  min-width: 0;
}

.section-info {
  font-size: 0.875rem;
  color: #6b7280;
  font-weight: 500;
  margin-top: 0.25rem;
}

.dark .section-info {
  color: #d1d5db;
}

.close-btn {
  background: #f3f4f6;
  border: 1px solid #e5e7eb;
  font-size: 1.5rem;
  color: #6b7280;
  cursor: pointer;
  padding: 0.5rem;
  border-radius: 8px;
  transition: all 0.2s ease;
  line-height: 1;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.close-btn:hover {
  background: #ef4444;
  border-color: #ef4444;
  color: white;
}

.dark .close-btn {
  background: #374151;
  border-color: #4b5563;
  color: #9ca3af;
}

.dark .close-btn:hover {
  background: #ef4444;
  border-color: #ef4444;
  color: white;
}

.options-menu-btn {
  background: #f3f4f6;
  border: 1px solid #e5e7eb;
  color: #6b7280;
  cursor: pointer;
  padding: 0.5rem;
  border-radius: 8px;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  margin-right: 0.5rem;
}

.options-menu-btn:hover {
  background: #20c997;
  border-color: #20c997;
  color: white;
}

.dark .options-menu-btn {
  background: #374151;
  border-color: #4b5563;
  color: #9ca3af;
}

.dark .options-menu-btn:hover {
  background: #20c997;
  border-color: #20c997;
  color: white;
}

.chat-options-menu {
  position: absolute;
  top: 100%;
  right: 4rem;
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  z-index: 10;
  min-width: 160px;
  padding: 0.5rem;
  margin-top: 0.5rem;
}

.dark .chat-options-menu {
  background: #374151;
  border-color: #4b5563;
}

.chat-options-menu button {
  width: 100%;
  padding: 0.75rem;
  border: none;
  background: transparent;
  color: #4b5563;
  cursor: pointer;
  border-radius: 6px;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.875rem;
  font-weight: 500;
  transition: all 0.2s ease;
}

.chat-options-menu button:hover {
  background: #f3f4f6;
  color: #1f2937;
}

.chat-options-menu button.delete-option:hover {
  background: #fef2f2;
  color: #ef4444;
}

.dark .chat-options-menu button {
  color: #d1d5db;
}

.dark .chat-options-menu button:hover {
  background: #4b5563;
  color: #f3f4f6;
}

.dark .chat-options-menu button.delete-option:hover {
  background: #450a0a;
  color: #f87171;
}

.modal-body {
  flex: 1;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  background: #ffffff;
}

.dark .modal-body {
  background: #1f2937;
}

/* Simple Messages Container */
.modal-body .messages-container {
  flex: 1;
  overflow-y: auto;
  padding: 1.5rem;
  background: transparent;
  margin: 0;
  border: none;
  border-radius: 0;
  position: relative;
  min-height: 400px;
  max-height: calc(100vh - 240px);
  scroll-behavior: smooth;
  overflow-x: hidden;
  /* Smooth Scrolling Enhancement */
  scroll-padding-bottom: 20px;
}

.modal-body .messages-container::-webkit-scrollbar {
  width: 8px;
}

.modal-body .messages-container::-webkit-scrollbar-track {
  background: #f3f4f6;
}

.modal-body .messages-container::-webkit-scrollbar-thumb {
  background: #20c997;
  border-radius: 4px;
}

.modal-body .messages-container::-webkit-scrollbar-thumb:hover {
  background: #18a577;
}

.dark .modal-body .messages-container::-webkit-scrollbar-track {
  background: #374151;
}

/* Simple Loading */
.messages-loading {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 3rem;
  color: #6b7280;
  font-family: 'Inter', sans-serif;
}

.messages-loading-spinner {
  width: 32px;
  height: 32px;
  border: 3px solid rgba(32, 201, 151, 0.2);
  border-top: 3px solid #20c997;
  border-radius: 50%;
  animation: fastSpin 0.6s linear infinite;
  margin-bottom: 1rem;
}

@keyframes fastSpin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.messages-loading p {
  font-weight: 500;
  font-size: 0.9rem;
}

.dark .messages-loading {
  color: #9ca3af;
}

.dark .messages-loading-spinner {
  border-color: #4b5563;
  border-top-color: #20c997;
}

/* Simple Message Bubbles */
.message-bubble {
  margin-bottom: 1.5rem;
  display: flex;
  flex-direction: column;
  scroll-margin-bottom: 20px;
}

.message-bubble:last-child {
  margin-bottom: 2rem;
}

.message-bubble.sent {
  align-items: flex-end;
}

.message-bubble.received {
  align-items: flex-start;
}

.message-text {
  max-width: 75%;
  padding: 0.875rem 1rem;
  border-radius: 16px;
  background: #20c997;
  color: white;
  word-wrap: break-word;
  margin: 0;
  font-size: 0.9rem;
  line-height: 1.5;
  font-family: 'Inter', sans-serif;
  font-weight: 500;
}

.message-bubble.sent .message-text {
  border-bottom-right-radius: 4px;
}

.message-bubble.received .message-text {
  background: white;
  color: #1f2937;
  border: 1px solid #e5e7eb;
  border-bottom-left-radius: 4px;
}

.dark .message-bubble.received .message-text {
  background: #374151;
  color: #f3f4f6;
  border-color: #4b5563;
}

.message-footer {
  margin-top: 0.375rem;
  font-size: 0.8rem;
  color: #9ca3af;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0 0.25rem;
}

.message-bubble.sent .message-footer {
  justify-content: flex-end;
}

.message-bubble.received .message-footer {
  justify-content: flex-start;
}

.message-time {
  font-size: 0.75rem;
  color: #9ca3af;
  font-weight: 500;
}

.dark .message-time {
  color: #6b7280;
}

.message-status {
  display: flex;
  align-items: center;
  gap: 0.25rem;
}

.status-read, .status-sent {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  color: #20c997;
  font-size: 0.75rem;
  font-weight: 500;
}

.read-time {
  color: #20c997;
  font-size: 0.7rem;
  margin-left: 0.25rem;
}

.dark .status-read, 
.dark .status-sent,
.dark .read-time {
  color: #34d399;
}

/* Form Elements */
.form-group {
  margin-bottom: 1.25rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
  color: #1f2937;
  font-size: 0.875rem;
  font-family: 'Inter', sans-serif;
}

.dark .form-group label {
  color: #A3D1C6;
}

.form-input, .form-textarea, .form-select {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  font-size: 0.875rem;
  font-family: 'Inter', sans-serif;
  background: white;
  color: #1f2937;
  transition: all 0.2s;
}

.form-input:focus, .form-textarea:focus, .form-select:focus {
  outline: none;
  border-color: #3D8D7A;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
}

.form-textarea {
  min-height: 120px;
  resize: vertical;
}

.dark .form-input,
.dark .form-textarea,
.dark .form-select {
  background: #374151;
  border-color: #4b5563;
  color: #A3D1C6;
}

.dark .form-input:focus,
.dark .form-textarea:focus,
.dark .form-select:focus {
  border-color: #20c997;
  box-shadow: 0 0 0 3px rgba(32, 201, 151, 0.1);
}

/* Simple Message Input Area */
.message-input-area {
  padding: 1rem;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 0.75rem;
  align-items: center;
  background: #f9fafb;
}

.dark .message-input-area {
  border-top-color: #374151;
  background: #111827;
}

.attach-file-btn, .send-btn {
  padding: 0.75rem;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
  flex-shrink: 0;
  width: 42px;
  height: 42px;
}

.attach-file-btn {
  background: white;
  color: #20c997;
}

.attach-file-btn:hover {
  background: #20c997;
  border-color: #20c997;
  color: white;
}

.send-btn {
  background: #20c997;
  color: white;
  border-color: #20c997;
}

.send-btn:hover:not(:disabled) {
  background: #17a085;
  border-color: #17a085;
}

.send-btn:disabled {
  background: #d1d5db;
  border-color: #d1d5db;
  cursor: not-allowed;
  color: #9ca3af;
}

.dark .attach-file-btn {
  background: #374151;
  border-color: #4b5563;
  color: #20c997;
}

.dark .attach-file-btn:hover {
  background: #20c997;
  border-color: #20c997;
  color: white;
}

.dark .send-btn:disabled {
  background: #4b5563;
  border-color: #4b5563;
  color: #6b7280;
}

.message-input {
  flex: 1;
  padding: 0.875rem 1rem;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  font-size: 0.9rem;
  font-family: 'Inter', sans-serif;
  background: white;
  color: #1f2937;
  transition: all 0.2s ease;
}

.message-input::placeholder {
  color: #9ca3af;
}

.message-input:focus {
  outline: none;
  border-color: #20c997;
  box-shadow: 0 0 0 3px rgba(32, 201, 151, 0.1);
}

.dark .message-input {
  background: #374151;
  border-color: #4b5563;
  color: #f3f4f6;
}

.dark .message-input::placeholder {
  color: #6b7280;
}

.dark .message-input:focus {
  border-color: #20c997;
  box-shadow: 0 0 0 3px rgba(32, 201, 151, 0.1);
}

/* Simple Attachments */
.attachments-preview {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  padding: 0.75rem;
  margin-bottom: 0.75rem;
}

.dark .attachments-preview {
  background: #374151;
  border-color: #4b5563;
}

.attachment-preview-list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.attachment-preview-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 6px;
  padding: 0.5rem;
  transition: all 0.2s ease;
}

.attachment-preview-item:hover {
  border-color: #20c997;
}

.dark .attachment-preview-item {
  background: #4b5563;
  border-color: #6b7280;
}

.dark .attachment-preview-item:hover {
  border-color: #20c997;
}

.attachment-preview-image {
  width: 30px;
  height: 30px;
  object-fit: cover;
  border-radius: 4px;
}

.attachment-preview-file {
  display: flex;
  align-items: center;
  gap: 0.375rem;
}

.attachment-preview-file svg {
  color: #20c997;
}

.attachment-name {
  font-size: 0.8rem;
  color: #1f2937;
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  max-width: 100px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.dark .attachment-name {
  color: #f3f4f6;
}

.remove-attachment-btn {
  background: #ef4444;
  color: white;
  border: none;
  border-radius: 4px;
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
}

.remove-attachment-btn:hover {
  background: #dc2626;
}

/* Simple No Messages State */
.no-messages {
  text-align: center;
  padding: 3rem 2rem;
  color: #6b7280;
  font-family: 'Inter', sans-serif;
  background: #f9fafb;
  border-radius: 8px;
  border: 1px dashed #d1d5db;
  margin: 1rem 0;
}

.no-messages p {
  font-size: 1rem;
  font-weight: 500;
  margin: 0;
  color: #4b5563;
}

.dark .no-messages {
  background: #374151;
  border-color: #4b5563;
}

.dark .no-messages p {
  color: #9ca3af;
}

/* Simple Mobile Responsive */
@media (max-width: 768px) {
  .modal-content {
    width: 95%;
    max-height: 90vh;
  }
  
  .modal-header {
    padding: 1rem;
  }
  
  .modal-title {
    font-size: 1.1rem;
  }
  
  .student-avatar {
    width: 40px;
    height: 40px;
    font-size: 1rem;
  }
  
  .header-info {
    gap: 0.75rem;
  }
  
  .modal-body .messages-container {
    padding: 1rem;
  }
  
  .message-text {
    max-width: 85%;
    padding: 0.75rem 1rem;
    font-size: 0.875rem;
  }
  
  .message-input-area {
    padding: 1rem;
  }
  
  .message-input {
    padding: 0.75rem;
    font-size: 0.875rem;
  }
  
  .attach-file-btn, .send-btn {
    width: 38px;
    height: 38px;
    padding: 0.625rem;
  }
  
  .close-btn, .options-menu-btn {
    width: 36px;
    height: 36px;
    padding: 0.5rem;
  }
  
  .no-messages {
    padding: 2rem 1rem;
  }
}

.dark .attachment-preview-item {
  background: #374151;
  border-color: #4b5563;
}

.attachment-preview-image {
  width: 30px;
  height: 30px;
  object-fit: cover;
  border-radius: 4px;
}

.attachment-preview-file {
  display: flex;
  align-items: center;
  gap: 0.375rem;
}

.attachment-name {
  font-size: 0.75rem;
  color: #1f2937;
  font-family: 'Inter', sans-serif;
}

.dark .attachment-name {
  color: #A3D1C6;
}

.remove-attachment-btn {
  background: #ef4444;
  color: white;
  border: none;
  border-radius: 50%;
  width: 20px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 0.688rem;
  transition: all 0.2s;
}

.remove-attachment-btn:hover {
  background: #dc2626;
  transform: scale(1.1);
}

/* Broadcast Form Styling - Enhanced to match MySubjects.vue */
.broadcast-form {
  max-width: 600px;
  background: #FBFFE4;
  border: 1.5px solid #A3D1C6;
  border-radius: 12px;
  padding: 1.5rem;
  transition: all 0.2s ease;
}

.dark .broadcast-form {
  background: #181c1f;
  border: 1.5px solid #20c997;
}

.broadcast-header {
  margin-bottom: 1.5rem;
}

.broadcast-header h3 {
  font-size: 1.25rem;
  font-weight: 600;
  color: #3D8D7A;
  margin-bottom: 0.5rem;
  font-family: 'Inter', sans-serif;
}

.dark .broadcast-header h3 {
  color: #20c997;
}

.broadcast-header p {
  color: #6b7280;
  font-size: 0.875rem;
  margin-bottom: 1rem;
}

.dark .broadcast-header p {
  color: #A3D1C6;
}

.view-history-btn {
  background: #A3D1C6;
  color: #1f2937;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.2s;
  font-size: 0.875rem;
  font-weight: 500;
  font-family: 'Inter', sans-serif;
}

.view-history-btn:hover {
  background: #86c5b7;
  transform: translateY(-1px);
}

.dark .view-history-btn {
  background: #20c997;
  color: #181c20;
}

/* Broadcast Messages - Enhanced to match MySubjects.vue */
.broadcast-messages-view {
  width: 100%;
  max-width: none;
}

.broadcast-messages-header {
  background: #FBFFE4;
  border: 1.5px solid #A3D1C6;
  border-radius: 12px;
  padding: 1.25rem;
  margin-bottom: 1.5rem;
}

.dark .broadcast-messages-header {
  background: #181c1f;
  border: 1.5px solid #20c997;
}

.broadcast-messages-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.broadcast-message-item {
  background: #FBFFE4;
  border: 1.5px solid #A3D1C6;
  border-radius: 12px;
  padding: 1.25rem;
  transition: all 0.2s ease;
}

.broadcast-message-item:hover {
  background: white;
  border-color: #3D8D7A;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.15);
}

.dark .broadcast-message-item {
  background: #181c1f;
  border: 1.5px solid #20c997;
}

.dark .broadcast-message-item:hover {
  background: #20242a;
  border-color: #20c997;
  box-shadow: 0 4px 12px rgba(32, 201, 151, 0.15);
}

/* Empty State */
.empty-state {
  text-align: center;
  padding: 3rem 1.25rem;
  color: #6b7280;
}

.dark .empty-state {
  color: #A3D1C6;
}

.empty-state svg {
  margin-bottom: 1rem;
  opacity: 0.5;
}

.empty-state p {
  margin: 0 0 1.25rem 0;
  font-size: 1.125rem;
  font-weight: 500;
  font-family: 'Inter', sans-serif;
}

.empty-subtext {
  font-size: 0.875rem;
  color: #9ca3af;
  margin-bottom: 1.25rem;
}

.dark .empty-subtext {
  color: #A3D1C6;
}

/* Additional responsive improvements */
@media (max-width: 768px) {
  .messages-container {
    padding: 1rem;
  }
  
  .header-card {
    padding: 1rem;
  }
  
  .content-card {
    padding: 1rem;
  }
  
  .sections-overview {
    grid-template-columns: 1fr;
  }
  
  .modal-content {
    width: 95%;
    margin: 1rem;
  }
  
  .header-actions {
    flex-direction: column;
    gap: 0.5rem;
  }
  
  .tab-btn {
    padding: 0.5rem 0.75rem;
    font-size: 0.813rem;
  }
}

/* Accessibility improvements */
.tab-btn:focus,
.action-btn:focus,
.debug-btn:focus,
.send-btn:focus,
.attach-file-btn:focus {
  outline: 2px solid #3D8D7A;
  outline-offset: 2px;
}

.dark .tab-btn:focus,
.dark .action-btn:focus,
.dark .debug-btn:focus,
.dark .send-btn:focus,
.dark .attach-file-btn:focus {
  outline-color: #20c997;
}

.message-text {
  max-width: 70%;
  padding: 12px 16px;
  border-radius: 18px;
  background: #3D8D7A;
  color: white;
  word-wrap: break-word;
  margin: 0;
}

.message-bubble.received .message-text {
  background: white;
  color: #2c3e50;
  border: 1px solid #e0e0e0;
}

.dark .message-bubble.received .message-text {
  background: #404040;
  color: #e0e0e0;
  border-color: #505050;
}

.message-footer {
  margin-top: 4px;
  font-size: 0.8rem;
  color: #6c757d;
  display: flex;
  align-items: center;
  gap: 8px;
}

.message-time {
  font-size: 0.8rem;
  color: #6c757d;
}

.message-status {
  display: flex;
  align-items: center;
  gap: 4px;
}

.status-read, .status-sent {
  display: flex;
  align-items: center;
  gap: 2px;
  color: #3D8D7A;
}

/* Message Input */
.message-input-area {
  padding: 16px;
  border-top: 1px solid #e0e0e0;
  display: flex;
  gap: 12px;
  align-items: center;
}

.dark .message-input-area {
  border-top-color: #404040;
}

.attach-file-btn, .send-btn {
  padding: 12px;
  border: none;
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.attach-file-btn {
  background: #B3D8A8;
  color: #2c3e50;
}

.attach-file-btn:hover {
  background: #9bc993;
}

.send-btn {
  background: #3D8D7A;
  color: white;
}

.send-btn:hover:not(:disabled) {
  background: #2d6b5a;
}

.send-btn:disabled {
  background: #ccc;
  cursor: not-allowed;
}

.message-input {
  flex: 1;
  padding: 12px;
  border: 1px solid #e0e0e0;
  border-radius: 20px;
  font-size: 0.9rem;
}

.dark .message-input {
  background: #404040;
  border-color: #505050;
  color: #e0e0e0;
}

/* Debug Content */
.debug-content {
  padding: 16px;
  background: #f8f9fa;
  border-radius: 8px;
  border: 1px solid #e0e0e0;
}

.dark .debug-content {
  background: #333;
  border-color: #404040;
}

.debug-content p {
  margin: 8px 0;
  font-size: 0.9rem;
}

/* Empty State */
.empty-state {
  text-align: center;
  padding: 60px 20px;
  color: #6c757d;
}

.empty-state svg {
  margin-bottom: 16px;
  opacity: 0.5;
}

.empty-state p {
  margin: 0 0 20px 0;
  font-size: 1.1rem;
}

.empty-subtext {
  font-size: 0.9rem;
  color: #999;
  margin-bottom: 20px;
}

/* Broadcast History */
.broadcast-history {
  width: 100%;
  max-width: none;
}

.broadcast-history-header {
  display: flex;
  justify-content: between;
  align-items: center;
  margin-bottom: 20px;
}

.history-filters {
  display: flex;
  gap: 16px;
  margin-bottom: 20px;
}

.history-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.history-item {
  background: #f8f9fa;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 16px;
}

.dark .history-item {
  background: #333;
  border-color: #404040;
}

.history-item-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.history-subject {
  margin: 0;
  color: #2c3e50;
  font-size: 1rem;
}

.dark .history-subject {
  color: #e0e0e0;
}

.history-meta {
  display: flex;
  align-items: center;
  gap: 8px;
}

.history-date {
  color: #6c757d;
  font-size: 0.8rem;
}

.history-message {
  margin: 0 0 12px 0;
  color: #2c3e50;
  font-size: 0.9rem;
}

.dark .history-message {
  color: #e0e0e0;
}

.history-details {
  display: flex;
  gap: 16px;
  color: #6c757d;
  font-size: 0.8rem;
}

/* Responsive Design */
@media (max-width: 768px) {
  .messages-container {
    padding: 10px;
  }
  
  .header-content {
    flex-direction: column;
    gap: 16px;
    text-align: center;
  }
  
  .section-actions {
    flex-direction: column;
    align-items: stretch;
  }
  
  .sections-overview {
    grid-template-columns: 1fr;
  }
  
  .modal-content {
    width: 95%;
    margin: 10px;
  }
  
  .section-student-item, .student-item {
    flex-direction: column;
    align-items: flex-start;
    text-align: left;
  }
  
  .section-message-status, .message-status {
    align-self: flex-end;
    flex-direction: row;
    gap: 8px;
  }
}

@media (max-width: 480px) {
  .header-left {
    flex-direction: column;
    text-align: center;
    gap: 8px;
  }
  
  .tabs {
    flex-direction: column;
    gap: 4px;
  }
  
  .section-students-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 12px;
  }
  
  .message-input-area {
    flex-direction: column;
    gap: 8px;
  }
}

/* Loading Overlay (matching Subjects.vue) */
.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(251, 255, 228, 0.95);
  backdrop-filter: blur(8px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
  animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.loading-content {
  background: white;
  padding: 3rem 4rem;
  border-radius: 20px;
  text-align: center;
  box-shadow: 0 20px 60px rgba(61, 141, 122, 0.15);
  border: 2px solid #a3d1c6;
  animation: slideUp 0.4s ease;
}

.dark .loading-content {
  background: #23272b;
  border-color: #374151;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.loading-spinner-container {
  position: relative;
  width: 80px;
  height: 80px;
  margin: 0 auto 1.5rem;
}

.loading-spinner {
  width: 80px;
  height: 80px;
  border: 5px solid rgba(61, 141, 122, 0.1);
  border-left: 5px solid #3d8d7a;
  border-top: 5px solid #20c997;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto;
  box-shadow: 0 0 20px rgba(61, 141, 122, 0.1);
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

/* ============================================
   SIMPLE BROADCAST MESSAGE STYLES
   ============================================ */

/* Simple Broadcast Header */
.simple-broadcast-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1.5rem;
  padding: 1.25rem;
  background: #fff;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  box-shadow: 0 1px 4px rgba(32,201,151,0.07);
}

.dark .simple-broadcast-header {
  background: #23272b;
  border-color: #374151;
}

.simple-header-content {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.simple-header-icon {
  width: 40px;
  height: 40px;
  background: #20c997;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
}

.simple-header-text h2 {
  font-size: 1.25rem;
  font-weight: 600;
  margin: 0 0 0.25rem 0;
  color: #222;
  font-family: 'Inter', sans-serif;
}

.dark .simple-header-text h2 {
  color: #fff;
}

.simple-header-text p {
  font-size: 0.9rem;
  margin: 0;
  color: #666;
  font-weight: 400;
}

.dark .simple-header-text p {
  color: #A3D1C6;
}

.simple-history-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1rem;
  background: #f8fafc;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  color: #059669;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  font-family: 'Inter', sans-serif;
}

.simple-history-btn:hover {
  background: #f1f5f9;
  border-color: #20c997;
}

.dark .simple-history-btn {
  background: #374151;
  border-color: #4b5563;
  color: #20c997;
}

.dark .simple-history-btn:hover {
  background: #4b5563;
  border-color: #20c997;
}

/* Broadcast Form Container */
.broadcast-form-container {
  max-width: 700px;
  margin: 1.5rem auto;
  background: #f8fafc;
  border-radius: 12px;
  border: 1px solid #e5e7eb;
  box-shadow: 0 1px 4px rgba(32,201,151,0.07);
  padding: 2rem 0;
}

.broadcast-form-card {
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 1px 4px rgba(32,201,151,0.07);
  border: 1px solid #e5e7eb;
  padding: 2rem 2rem 1.5rem 2rem;
  margin: 0 2rem;
}

.dark .broadcast-form-card {
  background: #23272b;
  border: 1px solid #374151;
  box-shadow: 0 1px 4px rgba(32,201,151,0.13);
}

/* Form Fields */
.form-field {
  margin-bottom: 2rem;
}

.form-label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.98rem;
  font-weight: 500;
  color: #222;
  margin-bottom: 0.5rem;
  font-family: 'Inter', sans-serif;
}

.dark .form-label {
  color: #A3D1C6;
}

.form-label svg {
  color: #3D8D7A;
}

.dark .form-label svg {
  color: #20c997;
}

.optional-label {
  font-size: 0.813rem;
  font-weight: 400;
  color: #9ca3af;
  margin-left: 0.25rem;
}

/* Form Inputs */
.form-select-enhanced, .form-textarea-enhanced {
  border-radius: 8px;
  border: 1px solid #e5e7eb;
  background: #f8fafc;
  padding: 0.75rem 1rem;
  font-size: 1rem;
  margin-top: 0.5rem;
  width: 100%;
  transition: border-color 0.2s;
  font-family: 'Inter', sans-serif;
}

.form-select-enhanced:focus, .form-textarea-enhanced:focus {
  border-color: #20c997;
  outline: none;
  background: #fff;
}

.dark .form-select-enhanced, .dark .form-textarea-enhanced {
  background: #1f2937;
  border-color: #374151;
  color: #A3D1C6;
}

.dark .form-select-enhanced:focus, .dark .form-textarea-enhanced:focus {
  border-color: #20c997;
  background: #23272b;
}

.select-arrow {
  position: absolute;
  right: 1rem;
  top: 50%;
  transform: translateY(-50%);
  pointer-events: none;
  color: #6b7280;
  transition: transform 0.3s ease;
}

.select-wrapper:hover .select-arrow {
  transform: translateY(-50%) rotate(180deg);
}

/* Selected Section Info */
.selected-section-info {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-top: 0.75rem;
  padding: 0.75rem 1rem;
  background: linear-gradient(135deg, #dcfce7 0%, #d1fae5 100%);
  border: 1.5px solid #86efac;
  border-radius: 10px;
  font-size: 0.875rem;
  font-weight: 600;
  color: #166534;
  animation: slideDown 0.3s ease;
}

.dark .selected-section-info {
  background: linear-gradient(135deg, #064e3b 0%, #065f46 100%);
  border-color: #10b981;
  color: #6ee7b7;
}

.selected-section-info svg {
  color: #22c55e;
  flex-shrink: 0;
}

.dark .selected-section-info svg {
  color: #34d399;
}

@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Enhanced Textarea */
.textarea-wrapper {
  position: relative;
}

.form-textarea-enhanced {
  width: 100%;
  padding: 1rem 1.25rem;
  padding-bottom: 3rem;
  background: #f9fafb;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  font-size: 0.938rem;
  font-weight: 400;
  color: #1f2937;
  line-height: 1.6;
  resize: vertical;
  transition: all 0.3s ease;
  font-family: 'Inter', sans-serif;
  min-height: 140px;
}

.form-textarea-enhanced:focus {
  outline: none;
  border-color: #3D8D7A;
  background: white;
  box-shadow: 0 0 0 4px rgba(61, 141, 122, 0.1);
}

.form-textarea-enhanced::placeholder {
  color: #9ca3af;
}

.dark .form-textarea-enhanced {
  background: #1f2937;
  border-color: #374151;
  color: #A3D1C6;
}

.dark .form-textarea-enhanced:focus {
  border-color: #20c997;
  background: #23272b;
  box-shadow: 0 0 0 4px rgba(32, 201, 151, 0.1);
}

.textarea-footer {
  position: absolute;
  bottom: 1rem;
  right: 1.25rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.char-count {
  font-size: 0.813rem;
  font-weight: 500;
  color: #9ca3af;
  transition: color 0.3s ease;
}

.char-count.limit-near {
  color: #ef4444;
  font-weight: 600;
}

/* Attachments Grid */
.attachments-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
  gap: 1rem;
  margin-bottom: 1rem;
}

.attachment-card {
  background: #f9fafb;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  overflow: hidden;
  transition: all 0.3s ease;
  animation: fadeIn 0.3s ease;
}

.attachment-card:hover {
  border-color: #3D8D7A;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.15);
}

.dark .attachment-card {
  background: #1f2937;
  border-color: #374151;
}

.dark .attachment-card:hover {
  border-color: #20c997;
  box-shadow: 0 4px 12px rgba(32, 201, 151, 0.15);
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: scale(0.9);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

.attachment-preview {
  position: relative;
  width: 100%;
  height: 120px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #e5e7eb;
  overflow: hidden;
}

.dark .attachment-preview {
  background: #374151;
}

.attachment-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.attachment-file-icon {
  color: #6b7280;
}

.dark .attachment-file-icon {
  color: #9ca3af;
}

.remove-attachment {
  position: absolute;
  top: 0.5rem;
  right: 0.5rem;
  width: 28px;
  height: 28px;
  background: rgba(239, 68, 68, 0.95);
  backdrop-filter: blur(4px);
  border: none;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  cursor: pointer;
  opacity: 0;
  transition: all 0.3s ease;
}

.attachment-card:hover .remove-attachment {
  opacity: 1;
}

.remove-attachment:hover {
  background: #dc2626;
  transform: scale(1.1);
}

.attachment-info {
  padding: 0.75rem;
}

.attachment-name {
  font-size: 0.813rem;
  font-weight: 600;
  color: #1f2937;
  margin: 0 0 0.25rem 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.dark .attachment-name {
  color: #A3D1C6;
}

.attachment-size {
  font-size: 0.75rem;
  color: #9ca3af;
  font-weight: 500;
}

/* Upload Button */
.upload-btn {
  width: 100%;
  padding: 1rem;
  background: #f8fafc;
  border: 1px dashed #d1d5db;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
  transition: all 0.2s ease;
  font-family: 'Inter', sans-serif;
}

.upload-btn:hover {
  background: #f1f5f9;
  border-color: #20c997;
}

.dark .upload-btn {
  background: #1f2937;
  border-color: #4b5563;
}

.dark .upload-btn:hover {
  background: #374151;
  border-color: #20c997;
}

.upload-btn svg {
  color: #6b7280;
}

.dark .upload-btn svg {
  color: #9ca3af;
}

.upload-btn span {
  font-size: 0.9rem;
  font-weight: 500;
  color: #444;
}

.dark .upload-btn span {
  color: #A3D1C6;
}

.upload-hint {
  font-size: 0.8rem !important;
  font-weight: 400 !important;
  color: #9ca3af !important;
}

/* Broadcast Preview Box */
.broadcast-preview {
  background: #f8fafc;
  border-radius: 8px;
  border: 1px solid #e5e7eb;
  padding: 1rem 1.5rem;
  margin-top: 1.5rem;
  box-shadow: none;
}

.dark .broadcast-preview {
  background: #23272b;
  border-color: #374151;
}

.preview-header {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-weight: 500;
  color: #059669;
  margin-bottom: 0.5rem;
  font-size: 0.98rem;
}

.dark .preview-header {
  color: #20c997;
}

.preview-header svg {
  color: #059669;
}

.dark .preview-header svg {
  color: #20c997;
}

.preview-text {
  margin-top: 0.5rem;
  color: #444;
  font-size: 0.98rem;
  font-weight: 400;
  line-height: 1.5;
}

.dark .preview-text {
  color: #A3D1C6;
}

/* Form Actions */
.form-actions {
  display: flex;
  gap: 1rem;
  margin-top: 2rem;
  justify-content: flex-end;
  border-top: none;
  padding-top: 0;
}

.cancel-btn-enhanced,
.send-btn-enhanced {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 2rem;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  font-family: 'Inter', sans-serif;
  border: none;
}

.cancel-btn-enhanced {
  background: #fff;
  color: #059669;
  border: 1px solid #e5e7eb;
}

.cancel-btn-enhanced:hover {
  background: #f8fafc;
  border-color: #20c997;
}

.dark .cancel-btn-enhanced {
  background: #23272b;
  border-color: #374151;
  color: #20c997;
}

.dark .cancel-btn-enhanced:hover {
  background: #374151;
  border-color: #20c997;
}

.send-btn-enhanced {
  background: #20c997;
  color: #fff;
  box-shadow: none;
}

.send-btn-enhanced:hover {
  background: #18a577;
}

.send-btn-enhanced:disabled {
  background: #e5e7eb;
  color: #aaa;
  cursor: not-allowed;
}

.dark .send-btn-enhanced {
  background: #20c997;
}

.dark .send-btn-enhanced:hover {
  background: #18a577;
}

.dark .send-btn-enhanced:disabled {
  background: #374151;
  color: #6b7280;
}

/* Responsive Design for Broadcast Form */
@media (max-width: 768px) {
  .broadcast-main-header {
    flex-direction: column;
    text-align: center;
    gap: 1rem;
  }

  .broadcast-header-icon {
    width: 50px;
    height: 50px;
  }

  .broadcast-header-text h2 {
    font-size: 1.5rem;
  }

  .view-history-link {
    width: 100%;
    justify-content: center;
  }

  .broadcast-form-card {
    padding: 1.5rem;
  }

  .attachments-grid {
    grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
  }

  .form-actions {
    flex-direction: column-reverse;
    gap: 0.75rem;
  }

  .cancel-btn-enhanced,
  .send-btn-enhanced {
    width: 100%;
    justify-content: center;
  }
}

@media (max-width: 480px) {
  .broadcast-main-header {
    padding: 1.25rem;
  }

  .broadcast-header-text h2 {
    font-size: 1.25rem;
  }

  .broadcast-header-text p {
    font-size: 0.813rem;
  }

  .broadcast-form-card {
    padding: 1.25rem;
  }

  .form-select-enhanced,
  .form-textarea-enhanced {
    font-size: 0.875rem;
  }

  .attachments-grid {
    grid-template-columns: 1fr;
  }
}

/* Animation for form appearance */
@keyframes formSlideIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.broadcast-form-card {
  animation: formSlideIn 0.4s ease;
}

/* Focus visible for accessibility */
.form-select-enhanced:focus-visible,
.form-textarea-enhanced:focus-visible,
.upload-btn:focus-visible,
.send-btn-enhanced:focus-visible,
.cancel-btn-enhanced:focus-visible {
  outline: 3px solid #3D8D7A;
  outline-offset: 2px;
}

.dark .form-select-enhanced:focus-visible,
.dark .form-textarea-enhanced:focus-visible,
.dark .upload-btn:focus-visible,
.dark .send-btn-enhanced:focus-visible,
.dark .cancel-btn-enhanced:focus-visible {
  outline-color: #20c997;
}
/* ============================================
   SIMPLE BROADCAST HISTORY STYLES
   ============================================ */

/* Simple History Header */
.simple-history-header {
  background: #fff;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  padding: 1.25rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 1px 4px rgba(32,201,151,0.07);
}

.dark .simple-history-header {
  background: #23272b;
  border-color: #374151;
}

.simple-history-content {
  display: flex;
  align-items: center;
  gap: 1rem;
  justify-content: space-between;
}

.simple-back-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1rem;
  background: #f8fafc;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  color: #059669;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  font-family: 'Inter', sans-serif;
}

.simple-back-btn:hover {
  background: #f1f5f9;
  border-color: #20c997;
}

.dark .simple-back-btn {
  background: #374151;
  border-color: #4b5563;
  color: #20c997;
}

.dark .simple-back-btn:hover {
  background: #4b5563;
  border-color: #20c997;
}

.simple-history-info {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex: 1;
}

.simple-history-icon {
  width: 40px;
  height: 40px;
  background: #20c997;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
}

.simple-history-info h2 {
  font-size: 1.25rem;
  font-weight: 600;
  margin: 0 0 0.25rem 0;
  color: #222;
  font-family: 'Inter', sans-serif;
}

.dark .simple-history-info h2 {
  color: #fff;
}

.simple-history-info p {
  font-size: 0.9rem;
  margin: 0;
  color: #666;
  font-weight: 400;
}

.dark .simple-history-info p {
  color: #A3D1C6;
}

.simple-stats-badge {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0.75rem 1rem;
  background: #f8fafc;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  min-width: 80px;
}

.dark .simple-stats-badge {
  background: #374151;
  border-color: #4b5563;
}

.simple-stats-number {
  font-size: 1.5rem;
  font-weight: 700;
  color: #20c997;
  line-height: 1;
}

.simple-stats-label {
  font-size: 0.75rem;
  font-weight: 500;
  color: #666;
  margin-top: 0.25rem;
}

.dark .simple-stats-label {
  color: #A3D1C6;
}

.history-icon {
  width: 60px;
  height: 60px;
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(10px);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.history-title-section h2 {
  font-size: 1.75rem;
  font-weight: 700;
  margin: 0 0 0.25rem 0;
  font-family: 'Inter', sans-serif;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.history-title-section p {
  font-size: 0.938rem;
  margin: 0;
  opacity: 0.95;
  font-weight: 500;
}

.history-stats-badge {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1rem 1.5rem;
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(10px);
  border: 1.5px solid rgba(255, 255, 255, 0.3);
  border-radius: 16px;
  color: white;
  min-width: 100px;
}

.stats-number {
  font-size: 2rem;
  font-weight: 700;
  line-height: 1;
  margin-bottom: 0.25rem;
}

.stats-label {
  font-size: 0.813rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  opacity: 0.9;
}

/* Empty State Modern */
.empty-state-modern {
  text-align: center;
  padding: 4rem 2rem;
  animation: fadeIn 0.5s ease;
}

.empty-illustration {
  margin-bottom: 2rem;
  opacity: 0.3;
  animation: float 3s ease-in-out infinite;
}

@keyframes float {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-10px);
  }
}

.empty-state-modern h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1f2937;
  margin: 0 0 0.5rem 0;
  font-family: 'Inter', sans-serif;
}

.dark .empty-state-modern h3 {
  color: #A3D1C6;
}

.empty-state-modern p {
  font-size: 1rem;
  color: #6b7280;
  margin: 0 0 2rem 0;
}

.dark .empty-state-modern p {
  color: #9ca3af;
}

.create-broadcast-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 1rem 2rem;
  background: linear-gradient(135deg, #3D8D7A 0%, #20c997 100%);
  color: white;
  border: none;
  border-radius: 12px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  font-family: 'Inter', sans-serif;
  box-shadow: 0 4px 16px rgba(61, 141, 122, 0.3);
}

.create-broadcast-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 24px rgba(61, 141, 122, 0.4);
}

.dark .create-broadcast-btn {
  background: linear-gradient(135deg, #20c997 0%, #18a577 100%);
}

/* Simple History Grid */
.simple-history-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 1rem;
}

.simple-history-card {
  background: #fff;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  padding: 1.25rem;
  cursor: pointer;
  transition: all 0.2s ease;
  position: relative;
}

.simple-history-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 3px;
  height: 100%;
  background: #20c997;
  border-radius: 12px 0 0 12px;
  transform: scaleY(0);
  transition: transform 0.2s ease;
}

.simple-history-card:hover {
  border-color: #20c997;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(32, 201, 151, 0.1);
}

.simple-history-card:hover::before {
  transform: scaleY(1);
}

.dark .simple-history-card {
  background: #23272b;
  border-color: #374151;
}

.dark .simple-history-card:hover {
  border-color: #20c997;
  box-shadow: 0 4px 12px rgba(32, 201, 151, 0.15);
}

/* Simple Card Header */
.simple-card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid #f3f4f6;
}

.dark .simple-card-header {
  border-bottom-color: #374151;
}

.simple-subject-info {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  flex: 1;
}

.simple-subject-icon {
  width: 40px;
  height: 40px;
  background: #20c997;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 1.125rem;
  font-weight: 600;
  flex-shrink: 0;
}

.simple-subject-details h3 {
  font-size: 1rem;
  font-weight: 600;
  color: #222;
  margin: 0 0 0.25rem 0;
  font-family: 'Inter', sans-serif;
}

.dark .simple-subject-details h3 {
  color: #fff;
}

.simple-subject-details p {
  font-size: 0.875rem;
  color: #666;
  margin: 0;
  font-weight: 400;
}

.dark .simple-subject-details p {
  color: #A3D1C6;
}

.simple-broadcast-count {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 0.75rem;
  background: #f8fafc;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  color: #059669;
  font-size: 0.875rem;
  font-weight: 600;
}

.dark .simple-broadcast-count {
  background: #374151;
  border-color: #4b5563;
  color: #20c997;
}

/* Simple Card Metadata */
.simple-card-meta {
  display: flex;
  gap: 1rem;
  margin-bottom: 1rem;
}

.simple-meta-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #666;
  font-size: 0.875rem;
  font-weight: 500;
}

.dark .simple-meta-item {
  color: #A3D1C6;
}

.simple-meta-item svg {
  color: #20c997;
}

/* Simple Latest Broadcast */
.simple-latest-broadcast {
  margin-bottom: 1rem;
  padding: 1rem;
  background: #f8fafc;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
}

.dark .simple-latest-broadcast {
  background: #374151;
  border-color: #4b5563;
}

.simple-latest-label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #059669;
  font-size: 0.75rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.dark .simple-latest-label {
  color: #20c997;
}

.simple-latest-text {
  color: #444;
  font-size: 0.875rem;
  margin: 0 0 0.5rem 0;
  line-height: 1.4;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  -webkit-box-orient: vertical;
}

.dark .simple-latest-text {
  color: #e5e7eb;
}

.simple-latest-date {
  color: #666;
  font-size: 0.75rem;
  font-weight: 500;
}

.dark .simple-latest-date {
  color: #9ca3af;
}

/* Simple Card Footer */
.simple-card-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  color: #059669;
  font-size: 0.875rem;
  font-weight: 500;
}

.dark .simple-card-footer {
  color: #20c997;
}

/* Clean Simple Card Footer Button */
.simple-view-all-btn {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.75rem 1rem;
  background: transparent;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  color: #059669;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  font-family: 'Inter', sans-serif;
}

.simple-view-all-btn:hover {
  background: #f8fafc;
  border-color: #20c997;
  color: #059669;
}

.dark .simple-view-all-btn {
  border-color: #4b5563;
  color: #20c997;
}

.dark .simple-view-all-btn:hover {
  background: #374151;
  border-color: #20c997;
}

.dark .view-all-btn {
  border-color: #374151;
  color: #20c997;
}

.dark .view-all-btn:hover {
  background: #20c997;
  border-color: #20c997;
  color: #181c20;
}

/* Broadcast Messages View */
.broadcast-messages-view {
  animation: fadeIn 0.5s ease;
}

.broadcast-messages-header-card {
  background: white;
  border: 2px solid #e5e7eb;
  border-radius: 16px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.05);
}

.dark .broadcast-messages-header-card {
  background: #23272b;
  border: 2px solid #374151;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
}

.back-to-history-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.25rem;
  background: #f9fafb;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  color: #6b7280;
  font-size: 0.875rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  font-family: 'Inter', sans-serif;
  margin-bottom: 1rem;
}

.back-to-history-btn:hover {
  background: white;
  border-color: #3D8D7A;
  color: #3D8D7A;
  transform: translateX(-4px);
}

.dark .back-to-history-btn {
  background: #1f2937;
  border-color: #374151;
  color: #9ca3af;
}

.dark .back-to-history-btn:hover {
  background: #374151;
  border-color: #20c997;
  color: #20c997;
}

/* Section Badge */
.broadcast-section-details {
  width: 100%;
}

.section-badge {
  display: flex;
  align-items: center;
  gap: 1.25rem;
  padding: 1.25rem;
  background: linear-gradient(135deg, #f0fdf4 0%, #dbeafe 100%);
  border: 2px solid #86efac;
  border-radius: 16px;
}

.dark .section-badge {
  background: linear-gradient(135deg, #064e3b 0%, #1e3a8a 100%);
  border-color: #10b981;
}

.section-badge-icon {
  width: 64px;
  height: 64px;
  background: white;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #3D8D7A;
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.15);
  flex-shrink: 0;
}

.dark .section-badge-icon {
  background: #23272b;
  color: #20c997;
}

.section-badge-content h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1f2937;
  margin: 0 0 0.25rem 0;
  font-family: 'Inter', sans-serif;
}

.dark .section-badge-content h3 {
  color: #A3D1C6;
}

.section-meta {
  font-size: 0.938rem;
  color: #6b7280;
  margin: 0 0 0.25rem 0;
  font-weight: 600;
}

.dark .section-meta {
  color: #9ca3af;
}

.section-stats {
  font-size: 0.813rem;
  color: #6b7280;
  margin: 0;
  font-weight: 500;
}

.dark .section-stats {
  color: #9ca3af;
}

/* Broadcast Messages List */
.broadcast-messages-list {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.broadcast-message-card {
  background: white;
  border: 2px solid #e5e7eb;
  border-radius: 16px;
  padding: 1.5rem;
  transition: all 0.3s ease;
  animation: slideUp 0.4s ease;
}

.broadcast-message-card:hover {
  border-color: #3D8D7A;
  box-shadow: 0 4px 16px rgba(61, 141, 122, 0.1);
  transform: translateY(-2px);
}

.dark .broadcast-message-card {
  background: #23272b;
  border: 2px solid #374151;
}

.dark .broadcast-message-card:hover {
  border-color: #20c997;
  box-shadow: 0 4px 16px rgba(32, 201, 151, 0.1);
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Broadcast Card Header */
.broadcast-card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1rem;
  padding-bottom: 1rem;
  border-bottom: 2px solid #f3f4f6;
}

.dark .broadcast-card-header {
  border-bottom-color: #374151;
}

.broadcast-timestamp {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.813rem;
  font-weight: 600;
  color: #6b7280;
}

.dark .broadcast-timestamp {
  color: #9ca3af;
}

.broadcast-timestamp svg {
  color: #3D8D7A;
}

.dark .broadcast-timestamp svg {
  color: #20c997;
}

/* Dropdown Menu */
.broadcast-actions-dropdown {
  position: relative;
}

.dropdown-trigger {
  width: 36px;
  height: 36px;
  background: #f9fafb;
  border: 2px solid #e5e7eb;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #6b7280;
  cursor: pointer;
  transition: all 0.2s ease;
}

.dropdown-trigger:hover {
  background: white;
  border-color: #3D8D7A;
  color: #3D8D7A;
}

.dark .dropdown-trigger {
  background: #1f2937;
  border-color: #374151;
  color: #9ca3af;
}

.dark .dropdown-trigger:hover {
  background: #374151;
  border-color: #20c997;
  color: #20c997;
}

.dropdown-menu {
  position: absolute;
  top: calc(100% + 0.5rem);
  right: 0;
  min-width: 200px;
  background: white;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
  padding: 0.5rem;
  z-index: 100;
  animation: dropdownSlide 0.2s ease;
}

@keyframes dropdownSlide {
  from {
    opacity: 0;
    transform: translateY(-8px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.dark .dropdown-menu {
  background: #23272b;
  border-color: #374151;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
}

.dropdown-item {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem 1rem;
  background: transparent;
  border: none;
  border-radius: 8px;
  color: #1f2937;
  font-size: 0.875rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  font-family: 'Inter', sans-serif;
  text-align: left;
}

.dropdown-item:hover {
  background: #f9fafb;
  color: #3D8D7A;
}

.dropdown-item.danger:hover {
  background: #fef2f2;
  color: #ef4444;
}

.dark .dropdown-item {
  color: #e5e7eb;
}

.dark .dropdown-item:hover {
  background: #374151;
  color: #20c997;
}

.dark .dropdown-item.danger:hover {
  background: #7f1d1d;
  color: #fca5a5;
}

.dropdown-divider {
  height: 1px;
  background: #e5e7eb;
  margin: 0.5rem 0;
}

.dark .dropdown-divider {
  background: #374151;
}

/* Broadcast Card Body */
.broadcast-card-body {
  display: flex;
  gap: 1rem;
  margin-bottom: 1rem;
}

.broadcast-icon-badge {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, #dbeafe 0%, #e0e7ff 100%);
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #1e40af;
  flex-shrink: 0;
}

.dark .broadcast-icon-badge {
  background: linear-gradient(135deg, #1e3a8a 0%, #5b21b6 100%);
  color: #bfdbfe;
}

.broadcast-message-text {
  flex: 1;
  font-size: 0.938rem;
  line-height: 1.6;
  color: #1f2937;
  margin: 0;
}

.dark .broadcast-message-text {
  color: #e5e7eb;
}

/* Broadcast Attachments Section */
.broadcast-attachments-section {
  padding-top: 1rem;
  border-top: 2px solid #f3f4f6;
}

.dark .broadcast-attachments-section {
  border-top-color: #374151;
}

.attachments-header {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.875rem;
  font-weight: 600;
  color: #6b7280;
  margin-bottom: 1rem;
}

.dark .attachments-header {
  color: #9ca3af;
}

.attachments-header svg {
  color: #3D8D7A;
}

.dark .attachments-header svg {
  color: #20c997;
}

.attachments-grid-view {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
  gap: 1rem;
}

.attachment-preview-card {
  position: relative;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  overflow: hidden;
  cursor: pointer;
  transition: all 0.3s ease;
}

.attachment-preview-card:hover {
  border-color: #3D8D7A;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.15);
}

.dark .attachment-preview-card {
  border-color: #374151;
}

.dark .attachment-preview-card:hover {
  border-color: #20c997;
  box-shadow: 0 4px 12px rgba(32, 201, 151, 0.15);
}

.attachment-thumbnail {
  width: 100%;
  height: 100px;
  background: #f9fafb;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.dark .attachment-thumbnail {
  background: #1f2937;
}

.attachment-thumb-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.attachment-file-preview {
  color: #6b7280;
}

.dark .attachment-file-preview {
  color: #9ca3af;
}

.attachment-info-overlay {
  padding: 0.5rem;
  background: white;
  border-top: 1px solid #e5e7eb;
}

.dark .attachment-info-overlay {
  background: #23272b;
  border-top-color: #374151;
}

.attachment-filename {
  font-size: 0.75rem;
  font-weight: 600;
  color: #1f2937;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  display: block;
}

.dark .attachment-filename {
  color: #e5e7eb;
}

/* Responsive Design for Broadcast History */
@media (max-width: 768px) {
  .broadcast-history-header {
    padding: 1.5rem;
  }

  .history-header-content {
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
  }

  .history-title-section {
    flex-direction: column;
    align-items: flex-start;
    text-align: left;
  }

  .history-icon {
    width: 50px;
    height: 50px;
  }

  .history-title-section h2 {
    font-size: 1.5rem;
  }

  .history-stats-badge {
    align-self: stretch;
    flex-direction: row;
    justify-content: center;
    gap: 0.5rem;
  }

  .stats-number {
    font-size: 1.5rem;
  }

  .broadcast-history-grid {
    grid-template-columns: 1fr;
  }

  .broadcast-messages-header-card {
    padding: 1rem;
  }

  .section-badge {
    flex-direction: column;
    text-align: center;
  }

  .section-badge-icon {
    width: 56px;
    height: 56px;
  }

  .broadcast-card-body {
    flex-direction: column;
  }

  .attachments-grid-view {
    grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
  }
}

@media (max-width: 480px) {
  .broadcast-history-header {
    padding: 1.25rem;
  }

  .history-title-section h2 {
    font-size: 1.25rem;
  }

  .back-to-broadcast-btn,
  .back-to-history-btn {
    width: 100%;
    justify-content: center;
  }

  .subject-icon {
    width: 48px;
    height: 48px;
    font-size: 1.25rem;
  }

  .subject-info h3 {
    font-size: 1rem;
  }

  .broadcast-message-card {
    padding: 1rem;
  }

  .section-metadata {
    flex-direction: column;
    gap: 0.5rem;
  }
}

/* ============================================
   MESSAGES LOADING INDICATOR
   ============================================ */

.messages-loading {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 3rem 2rem;
  min-height: 300px;
}

.messages-loading-spinner {
  width: 32px;
  height: 32px;
  border: 3px solid rgba(32, 201, 151, 0.2);
  border-top: 3px solid #20c997;
  border-radius: 50%;
  animation: fastSpin 0.6s linear infinite;
  margin-bottom: 1rem;
}

@keyframes fastSpin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.dark .messages-loading-spinner {
  border: 4px solid rgba(32, 201, 151, 0.2);
  border-left: 4px solid #20c997;
  border-top: 4px solid #18a577;
}

.messages-loading p {
  font-size: 0.938rem;
  font-weight: 600;
  color: #3D8D7A;
  margin: 0;
  font-family: 'Inter', sans-serif;
}

.dark .messages-loading p {
  color: #20c997;
}

/* ============================================
   ENHANCED IMAGE ATTACHMENTS WITH BETTER VISIBILITY
   ============================================ */

.message-attachments {
  margin-top: 0.5rem;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

/* ============================================
   SCROLL BUTTONS AND FAST LOADING STYLES
   ============================================ */

/* Scroll Buttons */
.scroll-top-btn, .scroll-bottom-btn {
  position: absolute;
  right: 1rem;
  width: 44px;
  height: 44px;
  background: #20c997;
  color: white;
  border: none;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px rgba(32, 201, 151, 0.3);
  z-index: 10;
  font-size: 0;
}

.scroll-top-btn {
  top: 1rem;
}

.scroll-bottom-btn {
  bottom: 1rem;
}

.scroll-top-btn:hover, .scroll-bottom-btn:hover {
  background: #18a577;
  transform: scale(1.1);
  box-shadow: 0 6px 20px rgba(32, 201, 151, 0.4);
}

.dark .scroll-top-btn, .dark .scroll-bottom-btn {
  background: #20c997;
  box-shadow: 0 4px 12px rgba(32, 201, 151, 0.4);
}

/* Fast Sending Indicator */
.sending-spinner {
  width: 14px;
  height: 14px;
  border: 2px solid rgba(32, 201, 151, 0.3);
  border-top: 2px solid #20c997;
  border-radius: 50%;
  animation: fastSpin 0.8s linear infinite;
  margin-right: 0.25rem;
}

@keyframes fastSpin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.message-bubble.sending {
  opacity: 0.8;
  transform: scale(0.98);
  transition: all 0.3s ease;
}

.status-sending {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  color: #20c997;
  font-size: 0.75rem;
  font-weight: 500;
}

/* Enhanced Message Bubbles with Green Theme */
.message-bubble.sent .message-text {
  background: linear-gradient(135deg, #20c997 0%, #18a577 100%);
  color: white;
  border-bottom-right-radius: 6px;
  box-shadow: 0 2px 8px rgba(32, 201, 151, 0.2);
}

.message-bubble.received .message-text {
  background: #f8fffe;
  color: #1f2937;
  border: 1px solid #d1fae5;
  border-bottom-left-radius: 6px;
  box-shadow: 0 1px 4px rgba(16, 185, 129, 0.1);
}

.dark .message-bubble.received .message-text {
  background: #064e3b;
  color: #d1fae5;
  border-color: #065f46;
}

/* Fast Loading Spinner */
.loading-spinner {
  width: 32px;
  height: 32px;
  border: 3px solid rgba(32, 201, 151, 0.2);
  border-top: 3px solid #20c997;
  border-radius: 50%;
  animation: fastSpin 0.6s linear infinite;
}

.dark .loading-spinner {
  border: 3px solid rgba(32, 201, 151, 0.3);
  border-top: 3px solid #20c997;
}

/* Enhanced Attachment Buttons */
.attachment-btn {
  background: #20c997;
  border: none;
  border-radius: 6px;
  color: white;
  transition: all 0.2s ease;
}

.attachment-btn:hover {
  background: #18a577;
  transform: scale(1.05);
}

/* Fast Message Input */
.message-input {
  border-color: #d1fae5;
  background: #f0fdf4;
  transition: all 0.2s ease;
}

.message-input:focus {
  border-color: #20c997;
  background: white;
  box-shadow: 0 0 0 3px rgba(32, 201, 151, 0.1);
}

.dark .message-input {
  background: #064e3b;
  border-color: #065f46;
  color: #d1fae5;
}

.dark .message-input:focus {
  background: #022c22;
  border-color: #20c997;
}

/* Enhanced Send Button */
.send-btn {
  background: linear-gradient(135deg, #20c997 0%, #18a577 100%);
  border-color: #20c997;
  transition: all 0.2s ease;
}

.send-btn:hover:not(:disabled) {
  background: linear-gradient(135deg, #18a577 0%, #16a085 100%);
  transform: scale(1.05);
}

/* Enhanced Attachment File Input */
.attach-file-btn {
  background: #ecfdf5;
  color: #20c997;
  border-color: #d1fae5;
  transition: all 0.2s ease;
}

.attach-file-btn:hover {
  background: #20c997;
  color: white;
  transform: scale(1.05);
}

.dark .attach-file-btn {
  background: #064e3b;
  border-color: #065f46;
}

.dark .attach-file-btn:hover {
  background: #20c997;
  color: #064e3b;
}

/* Fast Attachment Preview */
.attachment-preview-item {
  border-color: #d1fae5;
  background: #f0fdf4;
  transition: all 0.2s ease;
}

.attachment-preview-item:hover {
  border-color: #20c997;
  transform: translateY(-1px);
}

.dark .attachment-preview-item {
  background: #064e3b;
  border-color: #065f46;
}

/* Messages Container Enhancement */
.modal-body .messages-container {
  position: relative;
  scroll-behavior: smooth;
}

.modal-body .messages-container::-webkit-scrollbar-thumb {
  background: linear-gradient(180deg, #20c997 0%, #18a577 100%);
  border-radius: 4px;
}

.modal-body .messages-container::-webkit-scrollbar-track {
  background: #f0fdf4;
}

.dark .modal-body .messages-container::-webkit-scrollbar-track {
  background: #064e3b;
}

/* Green Theme System Colors */
:root {
  --primary-green: #20c997;
  --primary-green-hover: #18a577;
  --primary-green-light: #d1fae5;
  --primary-green-dark: #065f46;
  --bg-green-light: #f0fdf4;
  --bg-green-dark: #064e3b;
}

/* Status Indicators */
.status-sent {
  color: #20c997;
  font-weight: 500;
}

.dark .status-sent {
  color: #6ee7b7;
}

.attachment-item {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  max-width: fit-content;
}

/* Image Container with Overlay - Compact Size */
.attachment-image-container {
  position: relative;
  border-radius: 8px;
  overflow: hidden;
  cursor: pointer;
  max-width: 200px;
  width: 100%;
  background: #f3f4f6;
  transition: all 0.2s ease;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.dark .attachment-image-container {
  background: #1f2937;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
}

.attachment-image-container:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.15);
}

.dark .attachment-image-container:hover {
  box-shadow: 0 4px 12px rgba(32, 201, 151, 0.15);
}

.attachment-image {
  width: 100%;
  height: 120px;
  object-fit: cover;
  display: block;
  background: #ffffff;
}

.dark .attachment-image {
  background: #23272b;
}

/* Image Overlay */
.image-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(
    180deg,
    rgba(0, 0, 0, 0.1) 0%,
    rgba(0, 0, 0, 0.3) 100%
  );
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  opacity: 0;
  transition: opacity 0.3s ease;
  color: white;
}

.attachment-image-container:hover .image-overlay {
  opacity: 1;
}

.image-overlay svg {
  color: white;
  filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.3));
}

.image-overlay span {
  font-size: 0.875rem;
  font-weight: 600;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
  font-family: 'Inter', sans-serif;
}

/* File Attachment Styling */
.attachment-file {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.875rem 1rem;
  background: #f9fafb;
  border: 2px solid #e5e7eb;
  border-radius: 10px;
  transition: all 0.2s ease;
}

.dark .attachment-file {
  background: #1f2937;
  border-color: #374151;
}

.attachment-file:hover {
  background: white;
  border-color: #3D8D7A;
  transform: translateX(2px);
}

.dark .attachment-file:hover {
  background: #374151;
  border-color: #20c997;
}

.attachment-file > svg {
  color: #6b7280;
  flex-shrink: 0;
}

.dark .attachment-file > svg {
  color: #9ca3af;
}

.attachment-file > span {
  flex: 1;
  font-size: 0.875rem;
  font-weight: 600;
  color: #1f2937;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.dark .attachment-file > span {
  color: #e5e7eb;
}

.attachment-actions {
  display: flex;
  gap: 0.5rem;
  margin-left: auto;
}

.attachment-btn {
  width: 32px;
  height: 32px;
  background: #3D8D7A;
  border: none;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  cursor: pointer;
  transition: all 0.2s ease;
}

.attachment-btn:hover {
  background: #2d6b5a;
  transform: scale(1.1);
}

.dark .attachment-btn {
  background: #20c997;
  color: #181c20;
}

.dark .attachment-btn:hover {
  background: #18a577;
}

/* ============================================
   ENHANCED ATTACHMENT VIEWER MODAL
   ============================================ */

.attachment-modal-overlay {
  background: rgba(0, 0, 0, 0.85);
  backdrop-filter: blur(8px);
}

.attachment-viewer {
  background: white;
  border-radius: 16px;
  max-width: 90vw;
  max-height: 90vh;
  width: auto;
  height: auto;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  position: relative;
  animation: zoomIn 0.3s ease;
}

@keyframes zoomIn {
  from {
    opacity: 0;
    transform: scale(0.9);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

.dark .attachment-viewer {
  background: #23272b;
  border: 2px solid #374151;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.6);
}

.viewer-close-btn {
  position: absolute;
  top: 1rem;
  right: 1rem;
  width: 40px;
  height: 40px;
  background: rgba(0, 0, 0, 0.7);
  backdrop-filter: blur(10px);
  border: 2px solid rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  color: white;
  font-size: 1.5rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  z-index: 10;
  line-height: 1;
  padding: 0;
}

.viewer-close-btn:hover {
  background: rgba(239, 68, 68, 0.9);
  border-color: rgba(255, 255, 255, 0.4);
  transform: rotate(90deg) scale(1.1);
}

.attachment-viewer-content {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  min-width: 300px;
  min-height: 300px;
  max-height: 90vh;
}

.viewer-image {
  max-width: 100%;
  max-height: calc(90vh - 4rem);
  height: auto;
  width: auto;
  object-fit: contain;
  border-radius: 8px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
}

.viewer-file {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.5rem;
  padding: 2rem;
  text-align: center;
}

.viewer-file svg {
  color: #6b7280;
}

.dark .viewer-file svg {
  color: #9ca3af;
}

.viewer-file h3 {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1f2937;
  margin: 0;
  max-width: 400px;
  word-wrap: break-word;
  font-family: 'Inter', sans-serif;
}

.dark .viewer-file h3 {
  color: #e5e7eb;
}

.download-viewer-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.875rem 1.75rem;
  background: linear-gradient(135deg, #3D8D7A 0%, #20c997 100%);
  color: white;
  border: none;
  border-radius: 12px;
  font-size: 0.938rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  font-family: 'Inter', sans-serif;
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.3);
}

.download-viewer-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(61, 141, 122, 0.4);
}

.dark .download-viewer-btn {
  background: linear-gradient(135deg, #20c997 0%, #18a577 100%);
}

/* ============================================
   SENT MESSAGE BUBBLE ATTACHMENTS
   ============================================ */

.message-bubble.sent .attachment-image-container {
  background: rgba(61, 141, 122, 0.1);
}

.dark .message-bubble.sent .attachment-image-container {
  background: rgba(32, 201, 151, 0.1);
}

.message-bubble.sent .attachment-file {
  background: rgba(61, 141, 122, 0.05);
  border-color: rgba(61, 141, 122, 0.2);
}

.dark .message-bubble.sent .attachment-file {
  background: rgba(32, 201, 151, 0.05);
  border-color: rgba(32, 201, 151, 0.2);
}

/* ============================================
   RECEIVED MESSAGE BUBBLE ATTACHMENTS
   ============================================ */

.message-bubble.received .attachment-image-container {
  background: #f9fafb;
}

.dark .message-bubble.received .attachment-image-container {
  background: #2a2d35;
}

.message-bubble.received .attachment-file {
  background: white;
  border-color: #e5e7eb;
}

.dark .message-bubble.received .attachment-file {
  background: #2a2d35;
  border-color: #374151;
}

/* ============================================
   RESPONSIVE ADJUSTMENTS FOR ATTACHMENTS
   ============================================ */

@media (max-width: 768px) {
  .attachment-image-container {
    min-width: 200px;
  }

  .attachment-image {
    max-height: 300px;
  }

  .attachment-viewer {
    max-width: 95vw;
    max-height: 95vh;
  }

  .attachment-viewer-content {
    padding: 1rem;
  }

  .viewer-image {
    max-height: calc(95vh - 2rem);
  }

  .viewer-close-btn {
    top: 0.5rem;
    right: 0.5rem;
    width: 36px;
    height: 36px;
  }

  .image-overlay {
    opacity: 1;
    background: linear-gradient(
      180deg,
      rgba(0, 0, 0, 0.2) 0%,
      rgba(0, 0, 0, 0.4) 100%
    );
  }
}

@media (max-width: 480px) {
  .attachment-image-container {
    min-width: 150px;
  }

  .attachment-image {
    max-height: 250px;
  }

  .attachment-file {
    padding: 0.75rem;
    flex-wrap: wrap;
  }

  .attachment-actions {
    width: 100%;
    justify-content: flex-end;
    margin-left: 0;
    margin-top: 0.5rem;
  }

  .viewer-file {
    padding: 1rem;
  }

  .viewer-file h3 {
    font-size: 1rem;
    max-width: 250px;
  }

  .download-viewer-btn {
    padding: 0.75rem 1.5rem;
    font-size: 0.875rem;
  }
}

/* ============================================
   ACCESSIBILITY IMPROVEMENTS
   ============================================ */

.attachment-image-container:focus-visible,
.attachment-btn:focus-visible,
.download-viewer-btn:focus-visible {
  outline: 3px solid #3D8D7A;
  outline-offset: 2px;
}

.dark .attachment-image-container:focus-visible,
.dark .attachment-btn:focus-visible,
.dark .download-viewer-btn:focus-visible {
  outline-color: #20c997;
}

/* Screen reader only text */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}

/* ============================================
   LOADING STATE FOR ATTACHMENT IMAGES
   ============================================ */

.attachment-image-container::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 40px;
  height: 40px;
  border: 3px solid rgba(61, 141, 122, 0.2);
  border-top-color: #3D8D7A;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  z-index: 1;
}

.attachment-image-container.loaded::before {
  display: none;
}

.dark .attachment-image-container::before {
  border: 3px solid rgba(32, 201, 151, 0.2);
  border-top-color: #20c997;
}

/* Logout Modal Styles */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(5px);
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  animation: fadeIn 0.3s ease;
}

.logout-modal {
  max-width: 400px;
  border-radius: 16px;
  overflow: hidden;
  background: white;
  border: 2px solid #3D8D7A;
  animation: modalSlideIn 0.3s ease-out;
}

@keyframes modalSlideIn {
  from {
    opacity: 0;
    transform: translateY(-20px) scale(0.95);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

.logout-header {
  background: linear-gradient(135deg, #3D8D7A, #2d6a5a);
  color: white;
  padding: 1.5rem;
}

.logout-header h3 {
  font-size: 1.2rem;
  font-weight: 600;
  margin: 0;
}

.modal-body {
  padding: 2rem;
  text-align: center;
}

.logout-icon {
  display: flex;
  justify-content: center;
  margin-bottom: 1rem;
}

.logout-icon svg {
  color: #3D8D7A;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.05); }
}

.logout-message {
  font-size: 1rem;
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 0.5rem;
}

.logout-submessage {
  font-size: 0.85rem;
  color: #64748b;
  margin-bottom: 0;
}

.logout-footer {
  display: flex;
  gap: 0.75rem;
  padding: 1.5rem 2rem;
  background: #f8fafc;
}

.btn-cancel {
  flex: 1;
  padding: 0.75rem 1rem;
  background: #f1f5f9;
  color: #64748b;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  font-size: 0.9rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-cancel:hover {
  background: #e2e8f0;
  color: #1e293b;
}

.btn-logout {
  flex: 1;
  padding: 0.75rem 1rem;
  background: #ef4444;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 0.9rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.btn-logout:hover {
  background: #dc2626;
  transform: translateY(-1px);
}

.btn-logout:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.logout-spinner {
  width: 16px;
  height: 16px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top: 2px solid white;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.btn-logout .loading-text {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

/* Profile Dropdown Override - Maximum specificity */
div.profile-dropdown div.dropdown-header,
.profile-dropdown .dropdown-header {
  padding: 1.5rem !important;
  background: linear-gradient(135deg, #3D8D7A, #2d6a5a) !important;
  color: white !important;
  border-bottom: none !important;
  border: none !important;
  background-color: transparent !important;
}

/* Force override any potential conflicts */
[class*="profile-dropdown"] [class*="dropdown-header"] {
  background: linear-gradient(135deg, #3D8D7A, #2d6a5a) !important;
  border-bottom: none !important;
}

/* Nuclear option - override everything */
.profile-dropdown .dropdown-header {
  background: #3D8D7A !important;
  background-image: linear-gradient(135deg, #3D8D7A, #2d6a5a) !important;
}
</style>

<style>
/* Global override for MessagesPage profile dropdown */
.profile-dropdown .dropdown-header {
  padding: 1.5rem !important;
  background: linear-gradient(135deg, #3D8D7A, #2d6a5a) !important;
  color: white !important;
  border-bottom: none !important;
  border: none !important;
}
</style>