<template>
  <div class="messages-container" :class="{ 'dark': isDarkMode }">
    <!-- Consistent Header Card -->
    <div class="header-card">
      <div class="header-content">
        <div class="header-left">
          <div class="header-icon" style="background:#43907A;width:56px;height:56px;display:flex;align-items:center;justify-content:center;border-radius:14px;margin-right:1.5rem;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none">
              <rect width="24" height="24" rx="6" fill="none"/>
              <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" fill="#fff"/>
            </svg>
          </div>
          <div>
            <h1 class="header-title" style="font-size:2rem;font-weight:800;color:#222;margin-bottom:0.1rem;">Class Messaging</h1>
            <p class="header-subtitle" style="font-size:1.1rem;color:#6b7a89;font-weight:500;">Communicate with your students</p>
          </div>
        </div>
        <div class="header-actions">
          <button class="dark-mode-toggle" @click="toggleDarkMode">
            <svg v-if="!isDarkMode" width="24" height="24" fill="none" viewBox="0 0 24 24">
              <path fill="currentColor" d="M12 2a1 1 0 0 1 1 1v2a1 1 0 1 1-2 0V3a1 1 0 0 1 1-1Zm6.364 3.636a1 1 0 0 1 1.414 1.414l-1.414 1.414a1 1 0 1 1-1.414-1.414l1.414-1.414ZM21 11a1 1 0 1 1 0 2h-2a1 1 0 1 1 0-2h2Zm-2.222 7.364a1 1 0 0 1-1.415 1.415l-1.414-1.415a1 1 0 1 1 1.415-1.414l1.414 1.414ZM13 21a1 1 0 1 1-2 0v-2a1 1 0 1 1 2 0v2Zm-7.364-2.222a1 1 0 0 1-1.414-1.415l1.414-1.414a1 1 0 1 1 1.414 1.415l-1.414 1.414ZM3 13a1 1 0 1 1 0-2h2a1 1 0 1 1 0 2H3Zm2.222-7.364a1 1 0 0 1 1.415-1.414l1.414 1.414A1 1 0 1 1 6.05 6.05L4.636 4.636Z"/>
            </svg>
            <svg v-else width="24" height="24" fill="none" viewBox="0 0 24 24">
              <path fill="currentColor" d="M21 12.79A9 9 0 0 1 11.21 3a1 1 0 0 0-1.21 1v.09A9 9 0 1 0 20.91 13a1 1 0 0 0 1-1.21ZM12 21a7 7 0 0 1 0-14V5a7 7 0 0 1 0 14Z"/>
            </svg>
          </button>
          <button @click="markAllAsRead" class="action-btn">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <polyline points="20,6 9,17 4,12"/>
            </svg>
            Mark All Read
          </button>
        </div>
      </div>
    </div>

      <!-- Debug Info -->
      <div v-if="debugMode" class="content-card">
        <div class="card-header">
          <h3>Debug Information</h3>
          <button @click="debugMode = false" class="close-btn">×</button>
        </div>
        <div class="debug-content">
          <p><strong>Auth User ID:</strong> {{ currentUser?.id || 'None' }}</p>
          <p><strong>Teacher Profile ID:</strong> {{ teacherProfile?.id || 'None' }}</p>
          <p><strong>Teacher ID:</strong> {{ currentTeacherId || 'None' }}</p>
          <p><strong>Teacher Name:</strong> {{ teacherProfile?.full_name || 'None' }}</p>
          <p><strong>Contacts Count:</strong> {{ studentContacts.length }}</p>
        </div>
      </div>

      <!-- Main Content -->
      <div class="content-card">
        <div class="card-header">
          <div class="tabs">
            <button 
              :class="['tab-btn', { 'active': currentTab === 'students' }]"
              @click="currentTab = 'students'; showArchive = false"
            >
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
                <circle cx="8.5" cy="7" r="4"/>
              </svg>
              My Students
            </button>
            <button 
              :class="['tab-btn', { 'active': currentTab === 'broadcast' }]"
              @click="currentTab = 'broadcast'; showBroadcastHistory = false"
            >
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path d="M3 11l18-5v12L3 14v-3z"/>
              </svg>
              Broadcast Message
            </button>
            <button 
              :class="['tab-btn', { 'active': showArchive }]"
              @click="currentTab = 'students'; showArchive = true"
            >
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <rect x="1" y="3" width="22" height="5"></rect>
              </svg>
              Archive
            </button>
            <button @click="debugMode = true" class="debug-btn">Debug</button>
          </div>
        </div>

          <div class="tab-contents-wrapper">
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
                  Back to Sections
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
                    </div>
                    <div class="section-student-details">
                      <h4 class="section-student-name">{{ student.student_name }}</h4>
                      <p class="section-student-email">{{ student.student_email }}</p>
                      <p class="section-student-id">Student ID: {{ student.student_number }}</p>
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
              <div class="section-actions">
                <div class="search-bar">
                  <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="search-icon">
                    <circle cx="11" cy="11" r="8"></circle>
                    <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                  </svg>
                  <input type="text" v-model="searchQuery" placeholder="Search students or sections..." class="search-input" />
                </div>
                <div class="action-buttons horizontal-align">
                  <div class="filter-section">
                    <select v-model="selectedSection" class="section-filter">
                      <option value="">All Sections</option>
                      <option v-for="section in uniqueSections" :key="section.section_id" :value="section.section_id">
                        {{ section.section_name }} - {{ section.subject_name }}
                      </option>
                    </select>
                  </div>
                </div>
<!-- ...existing code... -->
              </div>
              
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
                <button @click="loadTeacherContacts" class="refresh-btn action-btn">Refresh Data</button>
              </div>

              <div v-else class="sections-overview">
                <div v-for="section in groupedStudents" :key="section.section_id" class="section-overview-card" @click="viewSectionStudents(section)">
                  <!-- Subject Icon and Title -->
                  <div class="section-card-header">
                    <div class="section-icon">
                      <span>{{ section.subject_name.charAt(0) }}</span>
                    </div>
                    <div class="section-title-area">
                      <h3 class="section-title">{{ section.subject_name }}</h3>
                      <p class="section-grade">Grade {{ section.grade_level }}</p>
                    </div>
                    <button class="section-options-btn" @click.stop>
                      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="12" r="1"></circle>
                        <circle cx="12" cy="5" r="1"></circle>
                        <circle cx="12" cy="19" r="1"></circle>
                      </svg>
                    </button>
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
            <div class="archive-header">
              <h3>Archived Conversations</h3>
              <p>View and restore archived student conversations</p>
            </div>

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
              <div class="broadcast-header">
                <h3>Send Section Announcement</h3>
                <p>Send a message to all students in a selected section</p>
                <button class="view-history-btn" @click="showBroadcastHistory = true">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="12" cy="12" r="10"></circle>
                    <polyline points="12 6 12 12 16 14"></polyline>
                  </svg>
                  View Broadcast History
                </button>
              </div>
              
              <div class="broadcast-form">
                <div class="form-group">
                  <label>Select Section</label>
                  <select v-model="broadcastSection" class="form-control">
                    <option value="">Choose a section</option>
                    <option v-for="section in uniqueSections" :key="section.section_id" :value="section.section_id">
                      {{ section.section_name }} - {{ section.subject_name }}
                    </option>
                  </select>
                </div>
                
                <div class="form-group">
                  <label>Message</label>
                  <textarea 
                    v-model="broadcastMessage" 
                    placeholder="Type your section announcement here..."
                    class="form-control message-textarea"
                    rows="6"
                  ></textarea>
                </div>

                <!-- Attachment Preview for Broadcast -->
                <div v-if="broadcastAttachments.length > 0" class="attachments-preview">
                  <label>Attachments</label>
                  <div class="attachment-list">
                    <div v-for="(att, idx) in broadcastAttachments" :key="idx" class="attachment-preview-item">
                      <img v-if="att.type === 'image'" :src="att.url" class="attachment-preview-image" />
                      <div v-else class="attachment-preview-file">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                          <path d="M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/>
                          <polyline points="13 2 13 9 20 9"/>
                        </svg>
                        <span>{{ att.name }}</span>
                      </div>
                      <button @click="broadcastAttachments.splice(idx, 1)" class="remove-attachment-btn">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                          <line x1="18" y1="6" x2="6" y2="18"></line>
                          <line x1="6" y1="6" x2="18" y2="18"></line>
                        </svg>
                      </button>
                    </div>
                  </div>
                </div>
                
                <div class="broadcast-actions">
                  <input 
                    type="file" 
                    ref="broadcastFileInput" 
                    @change="handleBroadcastFileSelect" 
                    multiple 
                    accept="image/*,.pdf,.doc,.docx,.xls,.xlsx,.ppt,.pptx,.txt"
                    style="display: none"
                  />
                  <button class="attach-btn" @click="$refs.broadcastFileInput.click()">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="m21.44 11.05-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48"/>
                    </svg>
                    Attach Files
                  </button>
                  <button class="cancel-broadcast-btn" @click="cancelBroadcast()">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <line x1="18" y1="6" x2="6" y2="18"></line>
                      <line x1="6" y1="6" x2="18" y2="18"></line>
                    </svg>
                    Cancel
                  </button>
                  <button 
                    class="broadcast-send-btn"
                    @click="sendBroadcastMessage"
                    :disabled="!broadcastMessage.trim() || !broadcastSection"
                  >
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M3 11l18-5v12L3 14v-3z"/>
                    </svg>
                    Send to Section Students
                  </button>
                </div>
              </div>
            </div>

            <!-- Broadcast History -->
            <div v-else class="broadcast-history">
              <!-- Broadcast Section Messages View -->
              <div v-if="showBroadcastMessages" class="broadcast-messages-view">
                <div class="broadcast-messages-header">
                  <button class="back-to-history-btn" @click="backToBroadcastHistory()">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <line x1="19" y1="12" x2="5" y2="12"></line>
                      <polyline points="12 19 5 12 12 5"></polyline>
                    </svg>
                    Back to History
                  </button>
                  <div class="broadcast-messages-info">
                    <h3>{{ selectedBroadcastSection?.subject_name }} - {{ selectedBroadcastSection?.section_name }}</h3>
                    <p>{{ selectedBroadcastSection?.section_code }} • Grade {{ selectedBroadcastSection?.grade_level }}</p>
                    <span class="broadcast-count">{{ selectedBroadcastSection?.broadcasts.length }} broadcast messages</span>
                  </div>
                  <button class="exit-btn" @click="showBroadcastHistory = false; showBroadcastMessages = false">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <line x1="18" y1="6" x2="6" y2="18"></line>
                      <line x1="6" y1="6" x2="18" y2="18"></line>
                    </svg>
                    Exit
                  </button>
                </div>

                <div class="broadcast-messages-list">
                  <div v-for="broadcast in selectedBroadcastSection?.broadcasts || []" :key="broadcast.id" class="broadcast-message-item">
                    <div class="broadcast-message-header">
                      <div class="broadcast-message-info">
                        <h4>{{ broadcast.message }}</h4>
                        <span class="broadcast-message-date">{{ formatDate(broadcast.sent_at) }} at {{ formatTime(broadcast.sent_at) }}</span>
                      </div>
                      <div class="broadcast-message-options">
                        <button class="options-btn" @click="toggleBroadcastOptions(broadcast.id)">
                          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <circle cx="12" cy="12" r="1"></circle>
                            <circle cx="12" cy="5" r="1"></circle>
                            <circle cx="12" cy="19" r="1"></circle>
                          </svg>
                        </button>
                        <div v-if="showBroadcastOptionsMenu === broadcast.id" class="options-menu">
                          <button @click="editBroadcast(broadcast)">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                              <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path>
                              <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>
                            </svg>
                            Edit
                          </button>
                          <button @click="archiveBroadcast(broadcast.id)">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                              <polyline points="21 8 21 21 3 21 3 8"></polyline>
                              <rect x="1" y="3" width="22" height="5"></rect>
                              <line x1="10" y1="12" x2="14" y2="12"></line>
                            </svg>
                            Archive
                          </button>
                          <button @click="deleteBroadcast(broadcast.id)" class="delete-option">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                              <polyline points="3 6 5 6 21 6"></polyline>
                              <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
                            </svg>
                            Delete
                          </button>
                        </div>
                      </div>
                    </div>
                    <div v-if="broadcast.attachments && broadcast.attachments.length > 0" class="broadcast-message-attachments">
                      <div v-for="(att, idx) in broadcast.attachments" :key="idx" class="broadcast-message-attachment">
                        <img v-if="att.type === 'image'" :src="att.url" class="broadcast-message-attachment-image" @click="viewAttachment(att)" />
                        <div v-else class="broadcast-message-attachment-file">
                          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/>
                            <polyline points="13 2 13 9 20 9"/>
                          </svg>
                          <span>{{ att.name }}</span>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Broadcast History Overview -->
              <div v-else>
                <div class="broadcast-header">
                  <button class="back-btn" @click="showBroadcastHistory = false">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <line x1="19" y1="12" x2="5" y2="12"></line>
                      <polyline points="12 19 5 12 12 5"></polyline>
                    </svg>
                    Back to Broadcast
                  </button>
                  <h3>Broadcast History</h3>
                  <p>View and manage all section announcements</p>
                </div>

                <div v-if="groupedBroadcasts.length === 0" class="empty-state">
                  <div class="empty-icon">
                    <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                      <path d="M3 11l18-5v12L3 14v-3z"/>
                    </svg>
                  </div>
                  <p>No broadcast history</p>
                  <span class="empty-subtext">Your sent broadcasts will appear here</span>
                </div>

                <div v-else class="broadcast-sections-overview">
                  <div v-for="section in groupedBroadcasts" :key="section.section_id" class="broadcast-section-card">
                    <div class="broadcast-section-header" @click="viewBroadcastSection(section)">
                      <div class="broadcast-section-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                          <path d="M3 11l18-5v12L3 14v-3z"/>
                          <path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"/>
                        </svg>
                      </div>
                      <div class="broadcast-section-info">
                        <h3 class="broadcast-section-title">{{ section.subject_name }}</h3>
                        <p class="broadcast-section-subtitle">{{ section.section_name }} - {{ section.section_code }}</p>
                        <p class="broadcast-section-grade">Grade {{ section.grade_level }}</p>
                      </div>
                      <div class="broadcast-section-stats">
                        <div class="broadcast-section-count">
                          <span class="broadcast-count-number">{{ section.broadcasts.length }}</span>
                          <span class="broadcast-count-label">Broadcasts</span>
                        </div>
                      </div>
                      <div class="broadcast-section-arrow">
                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
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
          <button class="options-menu-btn" @click="showChatOptions = !showChatOptions">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="1"></circle>
              <circle cx="12" cy="5" r="1"></circle>
              <circle cx="12" cy="19" r="1"></circle>
            </svg>
          </button>
          <div v-if="showChatOptions" class="chat-options-menu">
            <button @click="handleArchiveChat(activeConversation?.student_id)">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="21 8 21 21 3 21 3 8"></polyline>
                <rect x="1" y="3" width="22" height="5"></rect>
                <line x1="10" y1="12" x2="14" y2="12"></line>
              </svg>
              Archive Chat
            </button>
            <button @click="handleDeleteChat(activeConversation?.student_id)" class="delete-option">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <polyline points="3 6 5 6 21 6"></polyline>
                <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
              </svg>
              Delete Chat
            </button>
          </div>
        </div>
        <div class="modal-body">
          <div class="messages-container" ref="messagesContainer">
            <div 
              v-for="message in currentMessages" 
              :key="message.id" 
              :class="['message-bubble', { 'sent': message.sender_id === currentTeacherId, 'received': message.sender_id !== currentTeacherId }]"
            >
              <p class="message-text">{{ message.message_text }}</p>
              
              <!-- Display attachments if any -->
              <div v-if="message.attachments && message.attachments.length > 0" class="message-attachments">
                <div v-for="(attachment, idx) in message.attachments" :key="idx" class="attachment-item">
                  <!-- Image preview -->
                  <img v-if="attachment.type === 'image'" :src="attachment.url" class="attachment-image" @click="viewAttachment(attachment)" />
                  
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
            <button class="attach-file-btn" @click="$refs.messageFileInput.click()">
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
    <div v-if="viewingAttachment" class="modal-overlay" @click.self="closeAttachmentViewer">
      <div class="attachment-viewer">
        <button @click="closeAttachmentViewer" class="close-btn">&times;</button>
        <div class="attachment-viewer-content">
          <img v-if="viewingAttachment.type === 'image'" :src="viewingAttachment.url" class="viewer-image" />
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
        <p>{{ loadingMessage }}</p>
      </div>
    </div>
 </template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted, nextTick } from 'vue'
import { useRouter } from 'vue-router'
import { supabase } from '@/supabase.js'
import { useDarkMode } from '../../composables/useDarkMode.js'

// Dark mode
const { isDarkMode, toggleDarkMode } = useDarkMode()

const router = useRouter()

// ================================
// STATE MANAGEMENT
// ================================

// User authentication
const currentUser = ref(null)
const currentTeacherId = ref(null)
const teacherProfile = ref(null)
const debugMode = ref(false)

// UI State
const currentTab = ref('students')
const isModalOpen = ref(false)
const isBroadcastModalOpen = ref(false)
const isLoading = ref(false)
const loadingMessage = ref('Loading...')
const showArchive = ref(false)
const showBroadcastHistory = ref(false)
const showChatOptions = ref(false)
const showBroadcastOptionsMenu = ref(null)
const viewingAttachment = ref(null)
const expandedSections = ref(new Set())
const selectedSectionView = ref(null)
const showStudentsInSection = ref(false)

// Search and Filter
const searchQuery = ref('')
const selectedSection = ref('')

// Chat State
const selectedChat = ref(null)
const activeConversation = ref(null)
const newMessage = ref('')
const messagesContainer = ref(null)
const messageFileInput = ref(null)
const messageAttachments = ref([])

// Broadcast State
const broadcastMessage = ref('')
const broadcastSection = ref('')
const broadcastFileInput = ref(null)
const broadcastAttachments = ref([])
const broadcastHistory = ref([])
const archivedBroadcasts = ref([])
const selectedBroadcastSection = ref(null)
const showBroadcastMessages = ref(false)

// Data
const studentContacts = ref([])
const currentMessages = ref([])
const archivedChats = ref([])

// ================================
// FILE UPLOAD FUNCTIONS
// ================================

const uploadFileToStorage = async (file, folder = 'message-attachments') => {
  try {
    const fileExt = file.name.split('.').pop()
    const fileName = `${Date.now()}-${Math.random().toString(36).substring(7)}.${fileExt}`
    const filePath = `${folder}/${fileName}`
    
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
    
    // Get public URL
    const { data: urlData } = supabase.storage
      .from('attachments')
      .getPublicUrl(filePath)
    
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

const saveMessageAttachments = async (messageId, attachments) => {
  try {
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
      throw error
    }
    
    return data
  } catch (error) {
    console.error('Error saving message attachments:', error)
    throw error
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
    
  } catch (error) {
    console.error('Error getting current user:', error)
    alert(`Authentication error: ${error.message}`)
    await router.push('/login')
    return null
  }
}

// ================================
// UTILITY METHODS
// ================================

const copyToClipboard = async (text) => {
  try {
    await navigator.clipboard.writeText(text)
    // Simple feedback - you could add a toast notification here
    console.log('Section code copied to clipboard:', text)
  } catch (err) {
    console.error('Failed to copy to clipboard:', err)
    // Fallback for older browsers
    const textArea = document.createElement('textarea')
    textArea.value = text
    document.body.appendChild(textArea)
    textArea.select()
    document.execCommand('copy')
    document.body.removeChild(textArea)
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
      await debugTeacherData()
      return
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
      unread_count: contact.unread_count || 0
    }))
    
    studentContacts.value = mappedContacts
    console.log('Mapped contacts:', mappedContacts.length)
    
  } catch (error) {
    console.error('Error loading teacher contacts:', error)
    alert(`Error loading students: ${error.message}`)
  } finally {
    isLoading.value = false
  }
}

const loadContactsManually = async () => {
  try {
    console.log('Loading contacts manually for teacher:', currentTeacherId.value)
    
    const { data: contacts, error } = await supabase
      .from('enrollments')
      .select(`
        enrolled_at,
        section_id,
        students:student_id (
          id,
          full_name,
          email,
          student_id,
          grade_level
        ),
        sections:section_id (
          id,
          name,
          section_code,
          subjects:subject_id (
            id,
            name,
            teacher_id
          )
        )
      `)
      .eq('status', 'active')
      .eq('sections.subjects.teacher_id', currentTeacherId.value)
      .eq('sections.is_active', true)
      .eq('students.is_active', true)
    
    if (error) {
      console.error('Manual query error:', error)
      return []
    }
    
    if (!contacts || contacts.length === 0) {
      console.log('No enrollments found in manual query')
      return []
    }
    
    console.log('Manual query raw results:', contacts.length)
    
    const transformedContacts = contacts
      .filter(enrollment => {
        return enrollment.students && 
               enrollment.sections && 
               enrollment.sections.subjects &&
               enrollment.sections.subjects.teacher_id === currentTeacherId.value
      })
      .map(enrollment => ({
        student_id: enrollment.students.id,
        student_name: enrollment.students.full_name,
        student_email: enrollment.students.email,
        student_number: enrollment.students.student_id,
        grade_level: enrollment.students.grade_level,
        subject_id: enrollment.sections.subjects.id,
        subject_name: enrollment.sections.subjects.name,
        section_id: enrollment.sections.id,
        section_name: enrollment.sections.name,
        section_code: enrollment.sections.section_code,
        enrolled_date: enrollment.enrolled_at,
        last_message_date: null,
        last_message: `Enrolled ${formatDate(enrollment.enrolled_at)}`,
        unread_count: 0
      }))
    
    console.log('Transformed contacts:', transformedContacts.length)
    
    for (const contact of transformedContacts) {
      await updateStudentMessagingInfo(contact)
    }
    
    return transformedContacts
    
  } catch (error) {
    console.error('Error in manual contact loading:', error)
    return []
  }
}

const debugTeacherData = async () => {
  try {
    const { data: subjects } = await supabase
      .from('subjects')
      .select('id, name, is_active')
      .eq('teacher_id', currentTeacherId.value)
    
    console.log('Teacher subjects:', subjects)
    
    if (!subjects || subjects.length === 0) {
      console.log('❌ Teacher has no subjects. Create subjects first!')
      return
    }
    
    const subjectIds = subjects.map(s => s.id)
    const { data: sections } = await supabase
      .from('sections')
      .select('id, name, subject_id, is_active')
      .in('subject_id', subjectIds)
    
    console.log('Sections for teacher subjects:', sections)
    
    if (!sections || sections.length === 0) {
      console.log('❌ Subjects have no sections. Create sections for your subjects!')
      return
    }
    
    const sectionIds = sections.map(s => s.id)
    const { data: enrollments } = await supabase
      .from('enrollments')
      .select('id, student_id, section_id, status')
      .in('section_id', sectionIds)
    
    console.log('Enrollments in sections:', enrollments)
    
    if (!enrollments || enrollments.length === 0) {
      console.log('❌ No students enrolled in your sections yet!')
      return
    }
    
    const studentIds = [...new Set(enrollments.map(e => e.student_id))]
    const { data: students } = await supabase
      .from('students')
      .select('id, full_name, is_active')
      .in('id', studentIds)
    
    console.log('Enrolled students:', students)
    
    const activeStudents = students?.filter(s => s.is_active)
    console.log('Active enrolled students:', activeStudents?.length || 0)
    
    if (!activeStudents || activeStudents.length === 0) {
      console.log('❌ Enrolled students are not active!')
    }
    
  } catch (error) {
    console.error('Error in debug:', error)
  }
}

const updateStudentMessagingInfo = async (student) => {
  try {
    const { data: unreadMessages } = await supabase
      .from('messages')
      .select('id')
      .eq('section_id', student.section_id)
      .eq('sender_id', student.student_id)
      .eq('recipient_id', currentTeacherId.value)
      .is('recipient_id', currentTeacherId.value)
    
    if (unreadMessages) {
      const messageIds = unreadMessages.map(m => m.id)
      
      if (messageIds.length > 0) {
        const { data: readRecords } = await supabase
          .from('message_reads')
          .select('message_id')
          .in('message_id', messageIds)
          .eq('reader_id', currentTeacherId.value)
        
        const readMessageIds = new Set(readRecords?.map(r => r.message_id) || [])
        student.unread_count = messageIds.filter(id => !readMessageIds.has(id)).length
      } else {
        student.unread_count = 0
      }
    }
    
    const { data: lastMessage } = await supabase
      .from('messages')
      .select('message_text, sent_at')
      .eq('section_id', student.section_id)
      .or(`and(sender_id.eq.${student.student_id},recipient_id.eq.${currentTeacherId.value}),and(sender_id.eq.${currentTeacherId.value},recipient_id.eq.${student.student_id})`)
      .order('sent_at', { ascending: false })
      .limit(1)
      .single()
    
    if (lastMessage) {
      student.last_message = lastMessage.message_text
      student.last_message_date = lastMessage.sent_at
    }
    
  } catch (error) {
    console.log('Could not load messaging info for student:', student.student_id)
  }
}

// Load Broadcast History
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
        sections:section_id (
          id,
          name,
          section_code,
          subjects:subject_id (
            name,
            grade_level
          )
        )
      `)
      .eq('sender_id', currentTeacherId.value)
      .eq('message_type', 'announcement')
      .order('sent_at', { ascending: false })
    
    if (error) {
      console.error('Error loading broadcast history:', error)
      return
    }
    
    // Load attachments for each broadcast
    const broadcastIds = broadcasts?.map(b => b.id) || []
    let attachmentsMap = {}
    
    if (broadcastIds.length > 0) {
      const { data: attachments } = await supabase
        .from('message_attachments')
        .select('*')
        .in('message_id', broadcastIds)
      
      if (attachments) {
        attachmentsMap = attachments.reduce((acc, att) => {
          if (!acc[att.message_id]) acc[att.message_id] = []
          acc[att.message_id].push({
            name: att.file_name,
            url: att.file_url,
            type: att.file_type,
            size: att.file_size
          })
          return acc
        }, {})
      }
    }
    
    const transformedBroadcasts = broadcasts?.map(b => ({
      id: b.id,
      message: b.message_text,
      sent_at: b.sent_at,
      section_id: b.sections?.id,
      section_name: b.sections?.name,
      section_code: b.sections?.section_code,
      subject_name: b.sections?.subjects?.name,
      grade_level: b.sections?.subjects?.grade_level,
      attachments: attachmentsMap[b.id] || [],
      recipient_count: 0
    })) || []
    
    broadcastHistory.value = transformedBroadcasts
    
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
  const sections = {}
  
  filteredStudents.value.forEach(student => {
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

const groupedBroadcasts = computed(() => {
  const sections = {}
  
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

const startChatWithStudent = async (student) => {
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

const loadConversationMessages = async (studentId, sectionId) => {
  try {
    if (!currentTeacherId.value) return
    
    console.log('Loading messages between teacher and student:', { 
      teacherId: currentTeacherId.value, 
      studentId, 
      sectionId 
    })
    
    const { data: messages, error } = await supabase
      .from('messages')
      .select('*')
      .eq('section_id', sectionId)
      .eq('message_type', 'direct')
      .or(`and(sender_id.eq.${currentTeacherId.value},recipient_id.eq.${studentId}),and(sender_id.eq.${studentId},recipient_id.eq.${currentTeacherId.value})`)
      .order('sent_at', { ascending: true })
    
    if (error) {
      console.error('Error loading messages:', error)
      currentMessages.value = []
      return
    }
    
    // Load attachments for all messages
    if (messages && messages.length > 0) {
      const messageIds = messages.map(m => m.id)
      const { data: attachments } = await supabase
        .from('message_attachments')
        .select('*')
        .in('message_id', messageIds)
      
      // Group attachments by message_id
      const attachmentsMap = {}
      if (attachments) {
        attachments.forEach(att => {
          if (!attachmentsMap[att.message_id]) {
            attachmentsMap[att.message_id] = []
          }
          attachmentsMap[att.message_id].push({
            name: att.file_name,
            url: att.file_url,
            type: att.file_type,
            size: att.file_size,
            path: att.file_path
          })
        })
      }
      
      // Attach attachments to messages
      messages.forEach(msg => {
        msg.attachments = attachmentsMap[msg.id] || []
      })
    }
    
    currentMessages.value = messages || []
    console.log('Loaded messages:', messages?.length || 0)
    
    await markConversationAsRead(sectionId, studentId)
    
  } catch (error) {
    console.error('Error loading conversation messages:', error)
    currentMessages.value = []
  }
}

const handleSendMessage = async () => {
  if ((!newMessage.value.trim() && messageAttachments.value.length === 0) || !activeConversation.value || !currentTeacherId.value) return
  
  const messageText = newMessage.value.trim()
  const attachmentsToSend = [...messageAttachments.value]
  
  // Create temporary message for UI
  const tempMessage = {
    id: 'temp-' + Date.now(),
    sender_id: currentTeacherId.value,
    recipient_id: activeConversation.value.student_id,
    message_text: messageText || '📎 Attachment',
    sent_at: new Date().toISOString(),
    is_read: false,
    message_type: 'direct',
    attachments: attachmentsToSend.map(att => ({
      name: att.name,
      url: att.url,
      type: att.type
    }))
  }
  
  currentMessages.value.push(tempMessage)
  newMessage.value = ''
  messageAttachments.value = []
  
  await nextTick()
  scrollToBottom()
  
  try {
    isLoading.value = true
    loadingMessage.value = 'Sending message...'
    
    // Upload files first
    const uploadedAttachments = []
    if (attachmentsToSend.length > 0) {
      loadingMessage.value = 'Uploading attachments...'
      for (const attachment of attachmentsToSend) {
        const uploaded = await uploadFileToStorage(attachment.file)
        uploadedAttachments.push(uploaded)
      }
    }
    
    // Send message
    loadingMessage.value = 'Saving message...'
    const { data: messageId, error: sendError } = await supabase
      .rpc('send_direct_message', {
        p_section_id: activeConversation.value.section_id,
        p_sender_id: currentTeacherId.value,
        p_recipient_id: activeConversation.value.student_id,
        p_message_text: messageText || '📎 Attachment'
      })
    
    if (sendError) {
      console.log('Messaging function error:', sendError)
      alert('Messaging system not fully configured. Please run the messaging SQL script.')
      
      const tempIndex = currentMessages.value.findIndex(m => m.id === tempMessage.id)
      if (tempIndex !== -1) {
        currentMessages.value.splice(tempIndex, 1)
      }
      messageAttachments.value = attachmentsToSend
      return
    }
    
    // Save attachments to database
    if (uploadedAttachments.length > 0) {
      await saveMessageAttachments(messageId, uploadedAttachments)
    }
    
    console.log('Message sent successfully with ID:', messageId)
    
    // Update temp message with real ID and attachments
    const tempIndex = currentMessages.value.findIndex(m => m.id === tempMessage.id)
    if (tempIndex !== -1) {
      currentMessages.value[tempIndex].id = messageId
      currentMessages.value[tempIndex].attachments = uploadedAttachments.map(att => ({
        name: att.name,
        url: att.url,
        type: att.type,
        size: att.size
      }))
    }
    
    await loadTeacherContacts()
    
  } catch (error) {
    console.error('Failed to send message:', error)
    
    const tempIndex = currentMessages.value.findIndex(m => m.id === tempMessage.id)
    if (tempIndex !== -1) {
      currentMessages.value.splice(tempIndex, 1)
    }
    messageAttachments.value = attachmentsToSend
    alert('Failed to send message. Please try again.')
  } finally {
    isLoading.value = false
  }
}

const closeModal = () => {
  isModalOpen.value = false
  activeConversation.value = null
  selectedChat.value = null
  currentMessages.value = []
  messageAttachments.value = []
  showChatOptions.value = false
}

const markConversationAsRead = async (sectionId, studentId) => {
  try {
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
  } catch (error) {
    console.log('Could not mark conversation as read:', error.message)
  }
}

// ================================
// ATTACHMENT METHODS
// ================================

const handleMessageFileSelect = (event) => {
  const files = Array.from(event.target.files)
  
  files.forEach(file => {
    const reader = new FileReader()
    const fileType = file.type.startsWith('image/') ? 'image' : 'file'
    
    reader.onload = (e) => {
      messageAttachments.value.push({
        type: fileType,
        name: file.name,
        size: `${(file.size / 1024 / 1024).toFixed(2)} MB`,
        url: e.target.result,
        file: file
      })
    }
    
    reader.readAsDataURL(file)
  })
  
  event.target.value = ''
}

const handleBroadcastFileSelect = (event) => {
  const files = Array.from(event.target.files)
  
  files.forEach(file => {
    const reader = new FileReader()
    const fileType = file.type.startsWith('image/') ? 'image' : 'file'
    
    reader.onload = (e) => {
      broadcastAttachments.value.push({
        type: fileType,
        name: file.name,
        size: `${(file.size / 1024 / 1024).toFixed(2)} MB`,
        url: e.target.result,
        file: file
      })
    }
    

    
    reader.readAsDataURL(file)
  })
  
  event.target.value = ''
}

const viewAttachment = (attachment) => {
  viewingAttachment.value = attachment
}

const closeAttachmentViewer = () => {
  viewingAttachment.value = null
}

const downloadAttachment = (attachment) => {
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

const handleArchiveChat = (studentId) => {
  const student = studentContacts.value.find(s => s.student_id === studentId)
  if (student) {
    archivedChats.value.push(student)
    studentContacts.value = studentContacts.value.filter(s => s.student_id !== studentId)
    closeModal()
    alert(`Conversation with ${student.student_name} has been archived.`)
  }
}

const handleDeleteChat = (studentId) => {
  if (confirm('Are you sure you want to delete this conversation? This action cannot be undone.')) {
    const student = studentContacts.value.find(s => s.student_id === studentId)
    studentContacts.value = studentContacts.value.filter(s => s.student_id !== studentId)
    closeModal()
    
    if (student) {
      alert(`Conversation with ${student.student_name} has been deleted.`)
    }
  }
}

const restoreChat = (studentId) => {
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

const viewBroadcastSection = (section) => {
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
    
    // Upload files first
    const uploadedAttachments = []
    if (attachmentsToSend.length > 0) {
      loadingMessage.value = 'Uploading attachments...'
      for (const attachment of attachmentsToSend) {
        const uploaded = await uploadFileToStorage(attachment.file, 'broadcast-attachments')
        uploadedAttachments.push(uploaded)
      }
    }
    
    loadingMessage.value = 'Sending to students...'
    
    // Insert broadcast message directly into database
    const { data: messageData, error: insertError } = await supabase
      .from('messages')
      .insert({
        section_id: broadcastSection.value,
        sender_id: currentTeacherId.value,
        recipient_id: null, // null for broadcast messages
        message_text: broadcastMessage.value.trim(),
        message_type: 'announcement',
        is_read: false
      })
      .select()
      .single()
    
    if (insertError) {
      console.error('Error inserting broadcast message:', insertError)
      throw insertError
    }
    
    const messageId = messageData.id
    
    // Save attachments to database if broadcast was sent
    if (uploadedAttachments.length > 0 && messageId) {
      await saveMessageAttachments(messageId, uploadedAttachments)
    }
    
    console.log('Broadcast message sent successfully with ID:', messageId)
    
    const selectedSectionInfo = uniqueSections.value.find(s => s.section_id === broadcastSection.value)
    const sectionName = selectedSectionInfo ? selectedSectionInfo.section_name : 'Selected Section'
    alert(`Broadcast message sent successfully to all students in ${sectionName}!`)
    
    broadcastMessage.value = ''
    broadcastSection.value = ''
    broadcastAttachments.value = []
    
    await loadTeacherContacts()
    await loadBroadcastHistory()
    
  } catch (error) {
    console.error('Error sending broadcast message:', error)
    alert('Failed to send broadcast message. Please try again.')
  } finally {
    isLoading.value = false
  }
}

const toggleBroadcastOptions = (broadcastId) => {
  showBroadcastOptionsMenu.value = showBroadcastOptionsMenu.value === broadcastId ? null : broadcastId
}

const editBroadcast = (broadcast) => {
  broadcastMessage.value = broadcast.message
  broadcastSection.value = broadcast.section_id
  broadcastAttachments.value = [...(broadcast.attachments || [])]
  showBroadcastHistory.value = false
  showBroadcastOptionsMenu.value = null
  
  alert('Edit mode: Update your message and click Send to save changes.')
}

const archiveBroadcast = (broadcastId) => {
  const broadcast = broadcastHistory.value.find(b => b.id === broadcastId)
  if (broadcast) {
    archivedBroadcasts.value.push(broadcast)
    broadcastHistory.value = broadcastHistory.value.filter(b => b.id !== broadcastId)
    showBroadcastOptionsMenu.value = null
    alert('Broadcast has been archived.')
  }
}

const deleteBroadcast = async (broadcastId) => {
  if (confirm('Are you sure you want to delete this broadcast? This will also remove it from student message pages.')) {
    try {
      // Delete attachments first
      const { error: attachError } = await supabase
        .from('message_attachments')
        .delete()
        .eq('message_id', broadcastId)
      
      if (attachError) {
        console.error('Error deleting attachments:', attachError)
      }
      
      // Delete message
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

const toggleSection = (sectionId) => {
  if (expandedSections.value.has(sectionId)) {
    expandedSections.value.delete(sectionId)
  } else {
    expandedSections.value.add(sectionId)
  }
}

const viewSectionStudents = (section) => {
  selectedSectionView.value = section
  showStudentsInSection.value = true
}

const backToSections = () => {
  selectedSectionView.value = null
  showStudentsInSection.value = false
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
    messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
  }
}

const formatTime = (dateString) => {
  if (!dateString) return ''
  
  const date = new Date(dateString)
  const now = new Date()
  const diffMs = now - date
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

const formatDate = (dateString) => {
  if (!dateString) return ''
  return new Date(dateString).toLocaleDateString()
}

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
  
  setupAuthListener()
  
  const userData = await getCurrentUser()
  if (userData) {
    console.log('Teacher authenticated:', userData.profile.full_name)
    await loadTeacherContacts()
    await loadBroadcastHistory()
  }
})

onUnmounted(() => {
  console.log('Teacher messages component unmounted')
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Main Container - Enhanced to match MySubjects.vue */
.messages-container {
  min-height: 100vh;
  background: #FBFFE4;
  padding: 1.5rem;
  font-family: 'Inter', sans-serif;
}

.dark .messages-container {
  background: #181c20;
}

/* Header Card - Enhanced to match MySubjects.vue style */
.header-card {
  background: #ffffff;
  border: 1.5px solid #3D8D7A;
  border-radius: 16px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.1);
}

.dark .header-card {
  background: #2a2d35;
  border: 1.5px solid #A3D1C6;
  box-shadow: 0 2px 8px rgba(163, 209, 198, 0.1);
}

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
  color: #2a2d35;
}

.header-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #3D8D7A;
  margin-bottom: 0.25rem;
}

.dark .header-title {
  color: #A3D1C6;
}

.header-subtitle {
  font-size: 0.875rem;
  color: #3D8D7A;
  opacity: 0.8;
}

.dark .header-subtitle {
  color: #B3D8A8;
  opacity: 0.9;
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
  background: #3D8D7A;
  color: white;
}

.action-btn:hover {
  background: #2d6b5a;
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
  background: #A3D1C6;
  color: #2a2d35;
}

.dark .debug-btn {
  background: #A3D1C6;
  color: #2a2d35;
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
  border: 1px solid #A3D1C6;
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

/* Modal Styles */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  backdrop-filter: blur(4px);
}

.modal-content {
  background: white;
  border-radius: 16px;
  max-width: 700px;
  width: 90%;
  max-height: 85vh;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
  display: flex;
  flex-direction: column;
}

.dark .modal-content {
  background: #23272b;
  border: 1px solid #374151;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.4);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  border-bottom: 1px solid #e5e7eb;
}

.dark .modal-header {
  border-bottom-color: #374151;
}

.modal-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1f2937;
  margin: 0;
  font-family: 'Inter', sans-serif;
}

.dark .modal-title {
  color: #A3D1C6;
}

.header-info {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex: 1;
}

.header-details {
  flex: 1;
}

.section-info {
  font-size: 0.875rem;
  color: #6b7280;
  font-weight: 500;
}
.dark .section-info {
  color: #A3D1C6;
}

.close-btn {
  background: none;
  border: none;
  font-size: 1.5rem;
  color: #6b7280;
  cursor: pointer;
  padding: 0.5rem;
  border-radius: 8px;
  transition: all 0.2s;
  line-height: 1;
}

.close-btn:hover {
  background: #f3f4f6;
  color: #ef4444;
}

.dark .close-btn:hover {
  background: #374151;
  color: #ef4444;
}

.modal-body {
  flex: 1;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

/* Message Container in Modal */
.messages-container .modal-body .messages-container {
  flex: 1;
  overflow-y: auto;
  padding: 1rem;
  background: #f9fafb;
  margin: 1rem;
  border-radius: 8px;
  border: 1px solid #e5e7eb;
}

.dark .modal-body .messages-container {
  background: #1f2937;
  border-color: #374151;
}

/* Message Bubbles */
.message-bubble {
  margin-bottom: 1rem;
  display: flex;
  flex-direction: column;
}

.message-bubble.sent {
  align-items: flex-end;
}

.message-bubble.received {
  align-items: flex-start;
}

.message-text {
  max-width: 75%;
  padding: 0.75rem 1rem;
  border-radius: 18px;
  background: #3D8D7A;
  color: white;
  word-wrap: break-word;
  margin: 0;
  font-size: 0.875rem;
  line-height: 1.5;
  font-family: 'Inter', sans-serif;
}

.message-bubble.received .message-text {
  background: white;
  color: #1f2937;
  border: 1px solid #e5e7eb;
}

.dark .message-bubble.received .message-text {
  background: #374151;
  color: #A3D1C6;
  border-color: #4b5563;
}

.message-footer {
  margin-top: 0.25rem;
  font-size: 0.75rem;
  color: #6b7280;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.message-time {
  font-size: 0.75rem;
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
  gap: 0.125rem;
  color: #3D8D7A;
  font-size: 0.75rem;
}

.read-time {
  color: #3D8D7A;
  font-size: 0.688rem;
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

/* Message Input Area */
.message-input-area {
  padding: 1rem;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 0.75rem;
  align-items: center;
}

.dark .message-input-area {
  border-top-color: #374151;
}

.attach-file-btn, .send-btn {
  padding: 0.75rem;
  border: none;
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
  flex-shrink: 0;
}

.attach-file-btn {
  background: #B3D8A8;
  color: #1f2937;
}

.attach-file-btn:hover {
  background: #9bc993;
  transform: scale(1.05);
}

.send-btn {
  background: #3D8D7A;
  color: white;
}

.send-btn:hover:not(:disabled) {
  background: #2d6b5a;
  transform: scale(1.05);
}

.send-btn:disabled {
  background: #d1d5db;
  cursor: not-allowed;
  transform: none;
}

.dark .send-btn:disabled {
  background: #4b5563;
}

.message-input {
  flex: 1;
  padding: 0.75rem 1rem;
  border: 1px solid #e5e7eb;
  border-radius: 20px;
  font-size: 0.875rem;
  font-family: 'Inter', sans-serif;
  background: white;
  color: #1f2937;
}

.message-input:focus {
  outline: none;
  border-color: #3D8D7A;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
}

.dark .message-input {
  background: #374151;
  border-color: #4b5563;
  color: #A3D1C6;
}

.dark .message-input:focus {
  border-color: #20c997;
  box-shadow: 0 0 0 3px rgba(32, 201, 151, 0.1);
}

/* Attachments */
.attachments-preview {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  padding: 0.75rem;
  margin-bottom: 0.75rem;
}

.dark .attachments-preview {
  background: #1f2937;
  border-color: #374151;
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
  max-width: 800px;
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

/* Loading Overlay */
.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 2000;
  backdrop-filter: blur(4px);
}

.loading-content {
  background: white;
  padding: 2.5rem;
  border-radius: 16px;
  text-align: center;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
}

.dark .loading-content {
  background: #23272b;
  border: 1px solid #374151;
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 4px solid #f3f4f6;
  border-top: 4px solid #3D8D7A;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 1rem;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.loading-content p {
  margin: 0;
  color: #6b7280;
  font-size: 0.875rem;
  font-family: 'Inter', sans-serif;
}

.dark .loading-content p {
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

/* Loading Overlay */
.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 2000;
}

.loading-content {
  background: white;
  padding: 40px;
  border-radius: 12px;
  text-align: center;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
}

.dark .loading-content {
  background: #2a2a2a;
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 4px solid #f3f3f3;
  border-top: 4px solid #3D8D7A;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 16px;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.loading-content p {
  margin: 0;
  color: #6c757d;
  font-size: 0.9rem;
}

.dark .loading-content p {
  color: #a0a0a0;
}

/* Broadcast History */
.broadcast-history {
  max-width: 800px;
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
</style>
