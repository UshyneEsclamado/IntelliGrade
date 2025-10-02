<template>
  <div class="page-container" :class="{ 'dark-mode': isDarkMode }">
    <!-- Background decoration -->
    <div class="bg-decoration">
      <div class="floating-shape shape-1"></div>
      <div class="floating-shape shape-2"></div>
      <div class="floating-shape shape-3"></div>
    </div>
    
    <div class="main-wrapper">
      <!-- Header -->
      <div class="hero-header card-box">
        <div class="header-content">
          <div class="header-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
            </svg>
          </div>
          <h1 class="page-title">Class Messaging Center</h1>
          <p class="page-subtitle">Communicate with your enrolled students and send section announcements.</p>
        </div>
      </div>

      <!-- Debug Info -->
      <div v-if="debugMode" class="debug-info card-box" style="margin-bottom: 1rem; padding: 1rem; background: #f0f0f0;">
        <h4>Debug Info:</h4>
        <p><strong>Auth User ID:</strong> {{ currentUser?.id || 'None' }}</p>
        <p><strong>Teacher Profile ID:</strong> {{ teacherProfile?.id || 'None' }}</p>
        <p><strong>Teacher ID:</strong> {{ currentTeacherId || 'None' }}</p>
        <p><strong>Teacher Name:</strong> {{ teacherProfile?.full_name || 'None' }}</p>
        <p><strong>Contacts Count:</strong> {{ studentContacts.length }}</p>
        <button @click="debugMode = false" style="margin-top: 0.5rem;">Hide Debug</button>
      </div>

      <!-- Main Content -->
      <section class="content-section">
        <div class="card-box content-card">
          <!-- Tabs -->
          <div class="tabs">
            <button 
              :class="['tab-btn', { 'active': currentTab === 'students' }]"
              @click="currentTab = 'students'; showArchive = false"
            >
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
                <circle cx="8.5" cy="7" r="4"/>
                <line x1="20" y1="8" x2="20" y2="14"/>
                <line x1="23" y1="11" x2="17" y2="11"/>
              </svg>
              My Students
            </button>
            <button 
              :class="['tab-btn', { 'active': currentTab === 'broadcast' }]"
              @click="currentTab = 'broadcast'; showBroadcastHistory = false"
            >
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M3 11l18-5v12L3 14v-3z"/>
                <path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"/>
              </svg>
              Broadcast Message
            </button>
            <button 
              :class="['tab-btn', { 'active': showArchive }]"
              @click="currentTab = 'students'; showArchive = true"
            >
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="21 8 21 21 3 21 3 8"></polyline>
                <rect x="1" y="3" width="22" height="5"></rect>
                <line x1="10" y1="12" x2="14" y2="12"></line>
              </svg>
              Archive
            </button>
            <button @click="debugMode = true" class="debug-btn">Debug</button>
          </div>

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
                <div class="action-buttons">
                  <div class="filter-section">
                    <select v-model="selectedSection" class="section-filter">
                      <option value="">All Sections</option>
                      <option v-for="section in uniqueSections" :key="section.section_id" :value="section.section_id">
                        {{ section.section_name }} - {{ section.subject_name }}
                      </option>
                    </select>
                  </div>
                  <button class="action-btn" @click="markAllAsRead">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <polyline points="20,6 9,17 4,12"/>
                    </svg>
                    Mark all read
                  </button>
                </div>
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
                <div v-for="section in groupedStudents" :key="section.section_id" class="section-overview-card">
                  <div class="section-overview-header" @click="viewSectionStudents(section)">
                    <div class="section-overview-icon">
                      <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
                        <path d="M9 22V12h6v10"/>
                      </svg>
                    </div>
                    <div class="section-overview-info">
                      <h3 class="section-overview-title">{{ section.subject_name }}</h3>
                      <p class="section-overview-subtitle">{{ section.section_name }} - {{ section.section_code }}</p>
                      <p class="section-overview-grade">Grade {{ section.grade_level }}</p>
                    </div>
                    <div class="section-overview-stats">
                      <div class="section-overview-count">
                        <span class="count-number">{{ section.students.length }}</span>
                        <span class="count-label">Students</span>
                      </div>
                      <div v-if="section.total_unread > 0" class="section-overview-unread">
                        <span class="unread-number">{{ section.total_unread }}</span>
                        <span class="unread-label">Unread</span>
                      </div>
                    </div>
                    <div class="section-overview-arrow">
                      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <polyline points="9 18 15 12 9 6"></polyline>
                      </svg>
                    </div>
                  </div>
                  <div class="section-overview-actions">
                    <button 
                      class="section-overview-broadcast-btn" 
                      @click.stop="openBroadcastModal(); broadcastSection = section.section_id"
                    >
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M3 11l18-5v12L3 14v-3z"/>
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
      </section>
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
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, nextTick } from 'vue'
import { useRouter } from 'vue-router'
import { supabase } from '@/supabase.js'
import { useDarkMode } from '../../composables/useDarkMode.js'

// Dark mode
const { isDarkMode, initDarkMode } = useDarkMode()

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
  initDarkMode()
  
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
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* ================================
   MAIN LAYOUT
   ================================ */
.page-container {
  padding: 2rem 5%;
  font-family: 'Inter', sans-serif;
  min-height: 100vh;
  position: relative;
  overflow-x: hidden;
  background: var(--bg-primary);
}

.bg-decoration {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 0;
}

.floating-shape {
  position: absolute;
  border-radius: 50%;
  opacity: 0.03;
  animation: float 20s ease-in-out infinite;
}

.shape-1 {
  width: 300px;
  height: 300px;
  background: var(--accent-color);
  top: 10%;
  right: 10%;
  animation-delay: 0s;
}

.shape-2 {
  width: 200px;
  height: 200px;
  background: #A3D1C6;
  bottom: 20%;
  left: 5%;
  animation-delay: 7s;
}

.shape-3 {
  width: 150px;
  height: 150px;
  background: #B3D8A8;
  top: 60%;
  right: 40%;
  animation-delay: 14s;
}

@keyframes float {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  33% { transform: translateY(-20px) rotate(120deg); }
  66% { transform: translateY(10px) rotate(240deg); }
}

.main-wrapper {
  max-width: 1000px;
  margin: 0 auto;
  position: relative;
  z-index: 1;
}

/* ================================
   CARD COMPONENTS
   ================================ */
.card-box {
  background: var(--card-background);
  backdrop-filter: blur(20px);
  border: 1px solid var(--card-border-color);
  border-radius: 28px;
  padding: 2.5rem;
  box-shadow: 
    0 20px 60px var(--shadow-light),
    0 8px 32px var(--shadow-light),
    0 0 0 1px rgba(255, 255, 255, 0.3);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.card-box:hover {
  transform: translateY(-2px);
  box-shadow: 
    0 25px 70px var(--shadow-medium),
    0 12px 40px var(--shadow-light),
    0 0 0 1px rgba(255, 255, 255, 0.4);
}

/* ================================
   HEADER
   ================================ */
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
  background: linear-gradient(135deg, var(--accent-color) 0%, #A3D1C6 100%);
  border-radius: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  box-shadow: 0 8px 32px var(--shadow-light);
}

.page-title {
  font-size: 2.5rem;
  font-weight: 800;
  color: var(--accent-color);
  margin: 0;
  letter-spacing: -0.02em;
}

.page-subtitle {
  font-size: 1.2rem;
  color: var(--secondary-text-color);
  margin: 0;
  max-width: 600px;
}

/* ================================
   TABS
   ================================ */
.tabs {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
}

.tab-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: var(--bg-accent);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  color: var(--secondary-text-color);
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.tab-btn:hover {
  background: var(--bg-accent-hover);
}

.tab-btn.active {
  background: var(--accent-color);
  color: white;
  box-shadow: 0 4px 12px var(--shadow-light);
}

.tab-btn.active svg {
  color: white;
  stroke: white;
}

/* ================================
   SECTION ACTIONS
   ================================ */
.section-actions {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  gap: 1rem;
  flex-wrap: wrap;
}

.action-buttons {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.search-bar {
  position: relative;
  flex: 1;
  max-width: 400px;
}

.search-icon {
  position: absolute;
  left: 1rem;
  top: 50%;
  transform: translateY(-50%);
  color: var(--secondary-text-color);
}

.search-input {
  width: 100%;
  padding: 0.75rem 1rem 0.75rem 3rem;
  border: 1px solid var(--border-color);
  border-radius: 12px;
  font-size: 1rem;
  background: var(--input-bg);
  color: var(--primary-text-color);
  transition: all 0.2s ease;
}

.search-input:focus {
  outline: none;
  border-color: var(--accent-color);
  box-shadow: 0 0 0 3px var(--shadow-light);
}

.subject-filter {
  padding: 0.75rem 1rem;
  border: 1px solid var(--border-color);
  border-radius: 12px;
  background: var(--card-background);
  color: var(--primary-text-color);
  font-size: 0.9rem;
  min-width: 200px;
}

.action-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1rem;
  background: var(--action-btn-bg);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  color: var(--action-btn-color);
  font-size: 0.9rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
}

.action-btn:hover {
  background: var(--bg-accent-hover);
  transform: translateY(-1px);
}

/* ================================
   STUDENTS SECTION
   ================================ */
.students-by-subject {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.subject-group {
  background: var(--bg-accent);
  border-radius: 20px;
  padding: 1.5rem;
  border: 1px solid var(--border-color);
}

.subject-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid var(--border-color);
}

.subject-info {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.subject-name {
  font-size: 1.2rem;
  font-weight: 700;
  color: var(--accent-color);
  margin: 0;
}

.subject-code {
  background: var(--accent-color);
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 8px;
  font-size: 0.8rem;
  font-weight: 600;
}

.subject-actions {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.student-count {
  font-size: 0.9rem;
  color: var(--secondary-text-color);
  font-weight: 500;
}

.broadcast-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background: linear-gradient(135deg, var(--accent-color) 0%, #A3D1C6 100%);
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.broadcast-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px var(--shadow-light);
}

.students-list {
  background: var(--bg-accent);
  padding: 0;
}

.student-item {
  border-bottom: 1px solid var(--border-color);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 1.5rem;
  background: var(--card-background);
  border: 1px solid var(--card-border-color);
  border-radius: 16px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.student-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px var(--shadow-medium);
}

.student-item.has-unread {
  border-left: 4px solid var(--accent-color);
  background: var(--bg-unread);
}

.student-info {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex: 1;
}

.student-avatar {
  width: 56px;
  height: 56px;
  background: linear-gradient(135deg, #A3D1C6 0%, #B3D8A8 100%);
  color: var(--accent-color);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 1.3rem;
  flex-shrink: 0;
}

.student-details {
  flex: 1;
  min-width: 0;
}

.student-name {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--accent-color);
  margin: 0 0 0.25rem 0;
}

.student-email {
  font-size: 0.9rem;
  color: var(--text-muted);
  margin: 0 0 0.25rem 0;
}

.last-message {
  font-size: 0.9rem;
  color: var(--secondary-text-color);
  margin: 0;
}

.message-status {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.unread-badge {
  background: var(--accent-color);
  color: white;
  border-radius: 50%;
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.8rem;
  font-weight: 600;
}

.last-time {
  font-size: 0.8rem;
  color: var(--text-muted);
}

.chat-icon {
  color: var(--accent-color);
  opacity: 0.7;
  transition: opacity 0.2s ease;
}

.student-item:hover .chat-icon {
  opacity: 1;
  transform: scale(1.1);
}

/* ================================
   BROADCAST SECTION
   ================================ */
.broadcast-section {
  max-width: 600px;
  margin: 0 auto;
}

.broadcast-header {
  text-align: center;
  margin-bottom: 2rem;
}

.broadcast-header h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--accent-color);
  margin-bottom: 0.5rem;
}

.broadcast-header p {
  color: var(--secondary-text-color);
}

.broadcast-form {
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
  color: var(--accent-color);
}

.form-control {
  padding: 0.75rem 1rem;
  border: 1px solid var(--border-color);
  border-radius: 12px;
  background: var(--card-background);
  color: var(--primary-text-color);
  font-size: 1rem;
}

.message-textarea {
  min-height: 120px;
  resize: vertical;
}

.form-control:focus {
  outline: none;
  border-color: var(--accent-color);
  box-shadow: 0 0 0 3px var(--shadow-light);
}

.broadcast-send-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.75rem;
  padding: 1rem 2rem;
  background: linear-gradient(135deg, var(--accent-color) 0%, #A3D1C6 100%);
  color: white;
  border: none;
  border-radius: 12px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  align-self: flex-start;
}

.broadcast-send-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px var(--shadow-medium);
}

.broadcast-send-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  transform: none;
}

/* ================================
   EMPTY STATE
   ================================ */
.empty-state {
  text-align: center;
  color: var(--secondary-text-color);
  padding: 3rem 2rem;
}

.empty-icon {
  color: var(--border-color);
  margin-bottom: 1rem;
}

.empty-state p {
  font-size: 1.1rem;
  font-weight: 600;
  margin: 0;
  color: var(--secondary-text-color);
}

.empty-subtext {
  font-size: 0.9rem;
  color: var(--text-muted);
  margin-top: 0.5rem;
  display: block;
}

/* ================================
   MODAL
   ================================ */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  backdrop-filter: blur(5px);
}

.modal-content {
  background: #fff;
  border-radius: 20px;
  width: 90%;
  max-width: 600px;
  height: 80vh;
  display: flex;
  flex-direction: column;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);
  overflow: hidden;
}

.modal-header {
  padding: 1.5rem 2rem;
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: white;
  display: flex;
  align-items: center;
  gap: 1.5rem;
  position: relative;
}

.close-btn {
  background: none;
  border: none;
  color: white;
  font-size: 2rem;
  cursor: pointer;
  position: absolute;
  right: 1.5rem;
  top: 1.5rem;
  opacity: 0.8;
  transition: opacity 0.2s ease;
}

.close-btn:hover {
  opacity: 1;
}

.header-info {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.header-details {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.modal-title {
  font-size: 1.5rem;
  font-weight: 700;
  margin: 0;
}

.subject-info {
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.8);
  font-weight: 500;
}

.modal-header .student-avatar {
  background: rgba(255, 255, 255, 0.3);
  width: 48px;
  height: 48px;
  box-shadow: none;
}

.modal-body {
  flex: 1;
  padding: 1.5rem 2rem;
  overflow-y: auto;
  background-color: #f8fcfb;
}

.messages-container {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.message-bubble {
  max-width: 85%;
  padding: 1rem 1.25rem;
  border-radius: 20px;
  line-height: 1.4;
  position: relative;
}

.message-bubble.received {
  background: #e6f1f4;
  color: #333;
  align-self: flex-start;
  border-bottom-left-radius: 4px;
}

.message-bubble.sent {
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: white;
  align-self: flex-end;
  border-bottom-right-radius: 4px;
}

.message-text {
  margin: 0;
  font-size: 1rem;
}

.message-time {
  display: block;
  font-size: 0.75rem;
  margin-top: 0.5rem;
  color: rgba(0, 0, 0, 0.4);
  text-align: right;
}

.message-bubble.sent .message-time {
  color: rgba(255, 255, 255, 0.7);
}

.modal-footer {
  padding: 1.5rem 2rem;
  border-top: 1px solid #eee;
  background-color: #f8fcfb;
}

.message-input-area {
  display: flex;
  gap: 0.75rem;
}

.message-input {
  flex: 1;
  padding: 0.75rem 1.25rem;
  border: 1px solid #ddd;
  border-radius: 20px;
  font-size: 1rem;
}

.message-input:focus {
  outline: none;
  border-color: #3D8D7A;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
}

.send-btn {
  background: #3D8D7A;
  color: white;
  border: none;
  width: 48px;
  height: 48px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
}

.send-btn:hover {
  background: #347c6b;
  transform: scale(1.05);
}

/* ================================
   NEW FEATURES STYLES
   ================================ */

/* Archive Tab Styles */
.archive-header {
  text-align: center;
  margin-bottom: 2rem;
}

.archive-header h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--accent-color);
  margin-bottom: 0.5rem;
}

.archive-header p {
  color: var(--secondary-text-color);
}

.student-item.archived {
  opacity: 0.8;
}

.restore-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background: #3D8D7A;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.restore-btn:hover {
  transform: translateY(-1px);
  background: #2f7063;
}

/* Chat Options Menu */
.options-menu-btn {
  background: rgba(255, 255, 255, 0.2);
  border: none;
  color: white;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  position: absolute;
  right: 60px;
  top: 1.5rem;
  transition: all 0.2s ease;
}

.options-menu-btn:hover {
  background: rgba(255, 255, 255, 0.3);
}

.chat-options-menu {
  position: absolute;
  right: 60px;
  top: 4rem;
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  z-index: 100;
  min-width: 180px;
  overflow: hidden;
}

.chat-options-menu button {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  width: 100%;
  padding: 0.75rem 1rem;
  background: white;
  border: none;
  color: #333;
  font-size: 0.9rem;
  cursor: pointer;
  transition: background 0.2s ease;
  text-align: left;
}

.chat-options-menu button:hover {
  background: #f5f5f5;
}

.chat-options-menu button.delete-option {
  color: #dc3545;
}

.chat-options-menu button.delete-option:hover {
  background: #fff5f5;
}

/* Message Attachments */
.message-attachments {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-top: 0.75rem;
}

.attachment-item {
  max-width: 100%;
}

.attachment-image {
  max-width: 250px;
  max-height: 200px;
  border-radius: 12px;
  cursor: pointer;
  transition: transform 0.2s ease;
}

.attachment-image:hover {
  transform: scale(1.02);
}

.attachment-file {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  max-width: 300px;
}

.message-bubble.received .attachment-file {
  background: rgba(0, 0, 0, 0.05);
}

.attachment-file span {
  flex: 1;
  font-size: 0.9rem;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.attachment-actions {
  display: flex;
  gap: 0.25rem;
}

.attachment-btn {
  background: rgba(255, 255, 255, 0.2);
  border: none;
  color: inherit;
  width: 28px;
  height: 28px;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
}

.attachment-btn:hover {
  background: rgba(255, 255, 255, 0.3);
  transform: scale(1.1);
}

/* Message Status Icons */
.message-footer {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 0.5rem;
  margin-top: 0.5rem;
}

.message-status {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  font-size: 0.75rem;
}

.status-sent {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  color: rgba(255, 255, 255, 0.7);
}

.status-read {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  color: #4CAF50;
}

.read-time {
  font-size: 0.7rem;
  margin-left: 0.25rem;
}

.message-bubble.received .message-status {
  display: none;
}

/* Attachment Preview in Input */
.attachments-preview {
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 12px;
  margin-bottom: 1rem;
}

.attachments-preview label {
  display: block;
  font-weight: 600;
  color: var(--accent-color);
  margin-bottom: 0.5rem;
}

.attachment-list,
.attachment-preview-list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
}

.attachment-preview-item {
  position: relative;
  border-radius: 8px;
  overflow: hidden;
  border: 1px solid #ddd;
}

.attachment-preview-image {
  width: 80px;
  height: 80px;
  object-fit: cover;
  display: block;
}

.attachment-preview-file {
  width: 80px;
  height: 80px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: #f0f0f0;
  padding: 0.5rem;
}

.attachment-preview-file span {
  font-size: 0.7rem;
  text-align: center;
  margin-top: 0.25rem;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 70px;
}

.remove-attachment-btn {
  position: absolute;
  top: 4px;
  right: 4px;
  background: rgba(220, 53, 69, 0.9);
  color: white;
  border: none;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
}

.remove-attachment-btn:hover {
  background: #dc3545;
  transform: scale(1.1);
}

/* Attach File Button */
.attach-file-btn {
  background: #e9ecef;
  color: #495057;
  border: none;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
  flex-shrink: 0;
}

.attach-file-btn:hover {
  background: #dee2e6;
  transform: scale(1.05);
}

.attach-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: #6c757d;
  color: white;
  border: none;
  border-radius: 12px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.attach-btn:hover {
  background: #5a6268;
  transform: translateY(-1px);
}

/* Attachment Viewer Modal */
.attachment-viewer {
  background: white;
  border-radius: 20px;
  max-width: 90vw;
  max-height: 90vh;
  position: relative;
  display: flex;
  flex-direction: column;
}

.attachment-viewer .close-btn {
  position: absolute;
  right: 1rem;
  top: 1rem;
  background: rgba(0, 0, 0, 0.5);
  color: white;
  border: none;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  font-size: 1.5rem;
  cursor: pointer;
  z-index: 10;
}

.attachment-viewer-content {
  padding: 2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  max-height: 85vh;
}

.viewer-image {
  max-width: 100%;
  max-height: 80vh;
  object-fit: contain;
  border-radius: 12px;
}

.viewer-file {
  text-align: center;
  padding: 2rem;
}

.viewer-file h3 {
  margin: 1rem 0;
  color: #333;
}

.download-viewer-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: #3D8D7A;
  color: white;
  border: none;
  border-radius: 12px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  margin-top: 1rem;
}

.download-viewer-btn:hover {
  background: #2f7063;
  transform: translateY(-2px);
}

/* Broadcast History */
.view-history-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background: #6c757d;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  margin-top: 1rem;
}

.view-history-btn:hover {
  background: #5a6268;
  transform: translateY(-1px);
}

.back-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background: #6c757d;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  margin-bottom: 1rem;
}

.back-btn:hover {
  background: #5a6268;
}

.broadcast-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.broadcast-item {
  background: var(--card-background);
  border: 1px solid var(--border-color);
  border-radius: 16px;
  padding: 1.5rem;
  transition: all 0.2s ease;
}

.broadcast-item:hover {
  box-shadow: 0 4px 12px var(--shadow-light);
}

.broadcast-item-header {
  display: flex;
  justify-content: space-between;
  align-items: start;
  margin-bottom: 1rem;
}

.broadcast-info h4 {
  font-size: 1.2rem;
  font-weight: 600;
  color: var(--primary-text-color);
  margin: 0 0 0.5rem 0;
  line-height: 1.4;
}

.broadcast-meta {
  display: block;
  font-size: 0.85rem;
  color: var(--secondary-text-color);
  margin-bottom: 0.25rem;
}

.broadcast-date {
  display: block;
  font-size: 0.8rem;
  color: var(--text-muted);
}

.broadcast-options {
  position: relative;
}

.options-btn {
  background: transparent;
  border: 1px solid var(--border-color);
  color: var(--secondary-text-color);
  width: 36px;
  height: 36px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
}

.options-btn:hover {
  background: var(--bg-accent);
}

.options-menu {
  position: absolute;
  right: 0;
  top: 40px;
  background: white;
  border: 1px solid var(--border-color);
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  z-index: 100;
  min-width: 150px;
  overflow: hidden;
}

.options-menu button {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  width: 100%;
  padding: 0.75rem 1rem;
  background: white;
  border: none;
  color: #333;
  font-size: 0.85rem;
  cursor: pointer;
  transition: background 0.2s ease;
  text-align: left;
}

.options-menu button:hover {
  background: #f5f5f5;
}

.options-menu button.delete-option {
  color: #dc3545;
}

.options-menu button.delete-option:hover {
  background: #fff5f5;
}

.broadcast-content p {
  margin: 0 0 1rem 0;
  line-height: 1.6;
  color: var(--primary-text-color);
}

.broadcast-attachments {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin-top: 1rem;
}

.broadcast-attachment-image {
  width: 120px;
  height: 120px;
  object-fit: cover;
  border-radius: 8px;
  cursor: pointer;
  transition: transform 0.2s ease;
}

.broadcast-attachment-image:hover {
  transform: scale(1.05);
}

.broadcast-attachment-file {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem;
  background: var(--bg-accent);
  border-radius: 8px;
  border: 1px solid var(--border-color);
}

/* ================================
   SECTION OVERVIEW CARDS
   ================================ */
.sections-overview {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 1.5rem;
}

.section-overview-card {
  background: var(--card-background);
  border: 1px solid var(--border-color);
  border-radius: 20px;
  overflow: hidden;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px var(--shadow-light);
}

.section-overview-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px var(--shadow-medium);
}

.section-overview-header {
  display: flex;
  align-items: center;
  padding: 2rem;
  cursor: pointer;
  gap: 1.5rem;
}

.section-overview-icon {
  width: 60px;
  height: 60px;
  background: linear-gradient(135deg, var(--accent-color) 0%, #A3D1C6 100%);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
}

.section-overview-info {
  flex: 1;
  min-width: 0;
}

.section-overview-title {
  font-size: 1.3rem;
  font-weight: 700;
  color: var(--accent-color);
  margin: 0 0 0.5rem 0;
}

.section-overview-subtitle {
  font-size: 1rem;
  color: var(--secondary-text-color);
  margin: 0 0 0.25rem 0;
}

.section-overview-grade {
  font-size: 0.9rem;
  color: var(--text-muted);
  margin: 0;
}

.section-overview-stats {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  align-items: center;
}

.section-overview-count {
  text-align: center;
}

.count-number {
  display: block;
  font-size: 2rem;
  font-weight: 800;
  color: var(--accent-color);
  line-height: 1;
}

.count-label {
  font-size: 0.8rem;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.section-overview-unread {
  background: #ff6b6b;
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  text-align: center;
}

.unread-number {
  display: block;
  font-weight: 700;
  font-size: 0.9rem;
}

.unread-label {
  font-size: 0.7rem;
  text-transform: uppercase;
}

.section-overview-arrow {
  color: var(--text-muted);
  transition: transform 0.2s ease;
}

.section-overview-card:hover .section-overview-arrow {
  transform: translateX(4px);
}

.section-overview-actions {
  padding: 0 2rem 2rem 2rem;
}

.section-overview-broadcast-btn {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.75rem;
  padding: 1rem;
  background: linear-gradient(135deg, var(--accent-color) 0%, #A3D1C6 100%);
  color: white;
  border: none;
  border-radius: 12px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.section-overview-broadcast-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px var(--shadow-medium);
}

/* ================================
   SECTION STUDENTS VIEW
   ================================ */
.section-students-view {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.section-students-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding: 1.5rem 0;
  border-bottom: 1px solid var(--border-color);
}

.back-to-sections-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1rem;
  background: var(--bg-accent);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  color: var(--secondary-text-color);
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.back-to-sections-btn:hover {
  background: var(--bg-accent-hover);
  transform: translateY(-1px);
}

.section-students-info {
  flex: 1;
  text-align: center;
}

.section-students-info h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--accent-color);
  margin: 0 0 0.5rem 0;
}

.section-students-meta {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.section-broadcast-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: linear-gradient(135deg, var(--accent-color) 0%, #A3D1C6 100%);
  color: white;
  border: none;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.section-broadcast-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px var(--shadow-medium);
}

.section-students-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 1.5rem;
}

.section-student-item {
  background: var(--card-background);
  border: 1px solid var(--border-color);
  border-radius: 16px;
  padding: 1.5rem;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.section-student-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px var(--shadow-medium);
}

.section-student-item.has-unread {
  border-left: 4px solid var(--accent-color);
  background: var(--bg-unread);
}

.section-student-info {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex: 1;
}

.section-student-avatar {
  width: 56px;
  height: 56px;
  background: linear-gradient(135deg, #A3D1C6 0%, #B3D8A8 100%);
  color: var(--accent-color);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 1.3rem;
  flex-shrink: 0;
}

.section-student-details {
  flex: 1;
  min-width: 0;
}

.section-student-name {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--accent-color);
  margin: 0 0 0.25rem 0;
}

.section-student-email {
  font-size: 0.9rem;
  color: var(--text-muted);
  margin: 0 0 0.25rem 0;
}

.section-student-id {
  font-size: 0.85rem;
  color: var(--secondary-text-color);
  margin: 0 0 0.25rem 0;
}

.section-last-message {
  font-size: 0.9rem;
  color: var(--secondary-text-color);
  margin: 0;
}

.section-message-status {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
}

.section-unread-badge {
  background: var(--accent-color);
  color: white;
  border-radius: 50%;
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.8rem;
  font-weight: 600;
}

.section-last-time {
  font-size: 0.8rem;
  color: var(--text-muted);
}

.section-chat-icon {
  color: var(--accent-color);
  opacity: 0.7;
  transition: all 0.2s ease;
}

.section-student-item:hover .section-chat-icon {
  opacity: 1;
  transform: scale(1.1);
}

/* ================================
   BROADCAST SECTIONS OVERVIEW
   ================================ */
.broadcast-sections-overview {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 1.5rem;
}

.broadcast-section-card {
  background: var(--card-background);
  border: 1px solid var(--border-color);
  border-radius: 20px;
  overflow: hidden;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px var(--shadow-light);
}

.broadcast-section-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px var(--shadow-medium);
}

.broadcast-section-header {
  display: flex;
  align-items: center;
  padding: 2rem;
  cursor: pointer;
  gap: 1.5rem;
}

.broadcast-section-icon {
  width: 60px;
  height: 60px;
  background: linear-gradient(135deg, #ff6b6b 0%, #ff8e8e 100%);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
}

.broadcast-section-info {
  flex: 1;
  min-width: 0;
}

.broadcast-section-title {
  font-size: 1.3rem;
  font-weight: 700;
  color: var(--accent-color);
  margin: 0 0 0.5rem 0;
}

.broadcast-section-subtitle {
  font-size: 1rem;
  color: var(--secondary-text-color);
  margin: 0 0 0.25rem 0;
}

.broadcast-section-grade {
  font-size: 0.9rem;
  color: var(--text-muted);
  margin: 0;
}

.broadcast-section-stats {
  display: flex;
  align-items: center;
}

.broadcast-section-count {
  text-align: center;
}

.broadcast-count-number {
  display: block;
  font-size: 2rem;
  font-weight: 800;
  color: #ff6b6b;
  line-height: 1;
}

.broadcast-count-label {
  font-size: 0.8rem;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.broadcast-section-arrow {
  color: var(--text-muted);
  transition: transform 0.2s ease;
}

.broadcast-section-card:hover .broadcast-section-arrow {
  transform: translateX(4px);
}

/* ================================
   BROADCAST MESSAGES VIEW
   ================================ */
.broadcast-messages-view {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.broadcast-messages-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding: 1.5rem 0;
  border-bottom: 1px solid var(--border-color);
}

.back-to-history-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1rem;
  background: var(--bg-accent);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  color: var(--secondary-text-color);
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.back-to-history-btn:hover {
  background: var(--bg-accent-hover);
  transform: translateY(-1px);
}

.broadcast-messages-info {
  flex: 1;
  text-align: center;
}

.broadcast-messages-info h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--accent-color);
  margin: 0 0 0.5rem 0;
}

.broadcast-messages-info p {
  color: var(--secondary-text-color);
  margin: 0 0 0.25rem 0;
}

.broadcast-count {
  font-size: 0.9rem;
  color: var(--text-muted);
}

.exit-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1rem;
  background: #dc3545;
  color: white;
  border: none;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.exit-btn:hover {
  background: #c82333;
  transform: translateY(-1px);
}

.broadcast-messages-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.broadcast-message-item {
  background: var(--card-background);
  border: 1px solid var(--border-color);
  border-radius: 16px;
  padding: 1.5rem;
  transition: all 0.2s ease;
}

.broadcast-message-item:hover {
  box-shadow: 0 4px 12px var(--shadow-light);
}

.broadcast-message-header {
  display: flex;
  justify-content: space-between;
  align-items: start;
  margin-bottom: 1rem;
}

.broadcast-message-info h4 {
  font-size: 1.2rem;
  font-weight: 600;
  color: var(--primary-text-color);
  margin: 0 0 0.5rem 0;
  line-height: 1.4;
}

.broadcast-message-date {
  font-size: 0.85rem;
  color: var(--text-muted);
}

.broadcast-message-attachments {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  margin-top: 1rem;
}

.broadcast-message-attachment-image {
  width: 100px;
  height: 100px;
  object-fit: cover;
  border-radius: 8px;
  cursor: pointer;
  transition: transform 0.2s ease;
}

.broadcast-message-attachment-image:hover {
  transform: scale(1.05);
}

.broadcast-message-attachment-file {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem;
  background: var(--bg-accent);
  border-radius: 8px;
  border: 1px solid var(--border-color);
}

/* ================================
   CANCEL BUTTON STYLES
   ================================ */
.cancel-broadcast-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: #6c757d;
  color: white;
  border: none;
  border-radius: 12px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.cancel-broadcast-btn:hover {
  background: #5a6268;
  transform: translateY(-1px);
}

.broadcast-actions {
  display: flex;
  gap: 1rem;
  align-items: center;
  flex-wrap: wrap;
}
</style>