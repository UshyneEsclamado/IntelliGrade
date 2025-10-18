<template>
  <div class="messages-container">
    <!-- Simple Header matching Home.vue -->
    <div class="header-card">
      <div class="header-content">
        <div class="header-left">
          <div class="header-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
            </svg>
          </div>
          <div>
            <h1 class="header-title">Messages</h1>
            <p class="header-subtitle">Chat with your enrolled teachers and view announcements</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Main Content Card matching Home.vue -->
    <div class="content-card">
      <div class="card-header">
        <h3>Messages</h3>
        <p class="card-desc">Connect with your teachers and stay updated with announcements</p>
        <div class="tabs">
          <button 
            :class="['tab-btn', { 'active': currentTab === 'teachers' }]"
            @click="currentTab = 'teachers'; showArchive = false"
          >
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
              <circle cx="12" cy="7" r="4"/>
            </svg>
            My Teachers
          </button>
          <button 
            :class="['tab-btn', { 'active': currentTab === 'archive' }]"
            @click="currentTab = 'archive'; showArchive = true"
          >
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="21 8 21 21 3 21 3 8"></polyline>
              <rect x="1" y="3" width="22" height="5"></rect>
              <line x1="10" y1="12" x2="14" y2="12"></line>
            </svg>
            Archive
          </button>
          <button 
            :class="['tab-btn', { 'active': currentTab === 'notifications' }]"
              @click="currentTab = 'notifications'; showArchive = false"
            >
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/>
                <path d="M13.73 21a2 2 0 0 1-3.46 0"/>
              </svg>
              Notifications
          </button>
          </div>

          <!-- Teachers Tab -->
          <div v-if="currentTab === 'teachers' || currentTab === 'archive'" class="tab-content">
            <div class="section-actions">
              <div class="search-bar">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="search-icon">
                  <circle cx="11" cy="11" r="8"></circle>
                  <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
                <input type="text" v-model="searchQuery" placeholder="Search teachers or subjects..." class="search-input" />
              </div>
              <!-- Subject filter dropdown removed as requested -->
            </div>

            <!-- Empty state when no deleted conversations -->
            <div v-if="filteredTeachers.length === 0 && !hasDeletedConversations" class="empty-state">
              <div class="empty-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
                  <circle cx="12" cy="7" r="4"/>
                </svg>
              </div>
              <p>{{ showArchive ? 'No archived conversations' : 'No teachers found' }}</p>
              <span class="empty-subtext">{{ showArchive ? 'Archived conversations will appear here.' : 'Teachers from your enrolled subjects will appear here.' }}</span>
            </div>

            <!-- Show Available Teachers when conversations are deleted -->
            <div v-else-if="filteredTeachers.length === 0 && hasDeletedConversations" class="deleted-state">
              <div class="deleted-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
                  <circle cx="12" cy="7" r="4"/>
                </svg>
              </div>
              <p>You deleted all conversations</p>
              <span class="deleted-subtext">Your enrolled teachers are still available. Click below to see them again.</span>
              <button @click="showAvailableTeachers" class="show-teachers-btn">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                  <circle cx="12" cy="12" r="3"></circle>
                </svg>
                Show Available Teachers
              </button>
            </div>

            <!-- Teachers list -->
            <div v-else class="teachers-by-subject">
              <div v-for="subject in groupedTeachers" :key="subject.id" class="subject-group">
                <div class="subject-header">
                  <h3 class="subject-name">{{ subject.name }}</h3>
                  <span class="subject-code">{{ subject.code }}</span>
                </div>
                
                <div class="teachers-list">
                  <div 
                    v-for="teacher in subject.teachers" 
                    :key="`${teacher.id}-${teacher.section_id}`"
                    :class="['teacher-item', { 'has-unread': teacher.unread_count > 0 }]"
                  >
                    <div class="teacher-info" @click="startChatWithTeacher(teacher)">
                      <div class="teacher-avatar">
                        <span>{{ teacher.teacher_name?.[0] || 'T' }}</span>
                      </div>
                      <div class="teacher-details">
                        <h4 class="teacher-name">{{ teacher.teacher_name }}</h4>
                        <p class="teacher-email">{{ teacher.email }}</p>
                        <p class="last-message">{{ teacher.last_message || 'Start a conversation' }}</p>
                      </div>
                    </div>
                    <div class="message-status">
                      <div class="status-info">
                        <span v-if="teacher.unread_count > 0" class="unread-badge">{{ teacher.unread_count }}</span>
                      </div>
                      <div class="options-wrapper">
                        <button class="options-btn" @click.stop="toggleTeacherOptions(`${teacher.id}-${teacher.section_id}`)">
                          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <circle cx="12" cy="12" r="1"/>
                            <circle cx="12" cy="5" r="1"/>
                            <circle cx="12" cy="19" r="1"/>
                          </svg>
                        </button>
                        <div v-if="activeTeacherOptionsId === `${teacher.id}-${teacher.section_id}`" class="options-menu" @click.stop>
                          <a href="#" @click.prevent="archiveConversation(teacher); activeTeacherOptionsId = null">
                            <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                              <polyline points="21 8 21 21 3 21 3 8"></polyline>
                              <rect x="1" y="3" width="22" height="5"></rect>
                              <line x1="10" y1="12" x2="14" y2="12"></line>
                            </svg>
                            {{ teacher.archived ? 'Unarchive' : 'Archive' }}
                          </a>
                          <a href="#" @click.prevent="deleteConversation(teacher); activeTeacherOptionsId = null" class="delete-option">
                            <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                              <polyline points="3 6 5 6 21 6"></polyline>
                              <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
                            </svg>
                            Delete
                          </a>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Notifications Tab -->
          <div v-else-if="currentTab === 'notifications'" class="tab-content">
            <div class="section-actions">
              <div class="notification-filters">
                <button 
                  :class="['filter-btn', { 'active': currentFilter === 'all' }]"
                  @click="currentFilter = 'all'"
                >
                  All
                </button>
                <button 
                  :class="['filter-btn', { 'active': currentFilter === 'unread' }]"
                  @click="currentFilter = 'unread'"
                >
                  Unread
                </button>
              </div>
              <button class="action-btn" @click="clearNotifications">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <polyline points="20,6 9,17 4,12"/>
                </svg>
                Mark all read
              </button>
            </div>
            
            <div v-if="Object.keys(groupedBroadcasts).length === 0" class="empty-state">
              <div class="empty-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/>
                  <path d="M13.73 21a2 2 0 0 1-3.46 0"/>
                </svg>
              </div>
              <p>No announcements found</p>
              <span class="empty-subtext">Class announcements and notifications will appear here.</span>
            </div>
            
            <div v-else class="broadcast-groups">
              <div 
                v-for="(group, key) in groupedBroadcasts" 
                :key="key" 
                class="broadcast-group"
                @click="openBroadcastGroup(group)"
              >
                <div class="broadcast-group-header">
                  <div class="broadcast-icon">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
                    </svg>
                  </div>
                  <div class="broadcast-info">
                    <h3 class="broadcast-title">{{ group.section }}: {{ group.subject }}</h3>
                    <p class="broadcast-teacher">Teacher: {{ group.teacher }}</p>
                  </div>
                  <div class="broadcast-count">
                    <span class="count-badge">{{ group.announcements.length }}</span>
                    <span v-if="group.announcements.some(a => !a.is_read)" class="unread-indicator"></span>
                  </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>    <!-- Chat Modal -->
    <div v-if="isModalOpen" class="modal-overlay" @click.self="closeModal">
      <div class="modal-content">
        <div class="modal-header">
          <div class="header-info">
            <div class="teacher-avatar-chat">
              <span>{{ activeTeacher?.teacher_name?.[0] || 'T' }}</span>
            </div>
            <div class="header-details">
              <h2 class="modal-title">{{ activeTeacher?.teacher_name }}</h2>
              <span class="subject-info">{{ activeTeacher?.subject_name }}</span>
            </div>
          </div>
          <button @click="closeModal" class="close-btn">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="18" y1="6" x2="6" y2="18"></line>
              <line x1="6" y1="6" x2="18" y2="18"></line>
            </svg>
          </button>
        </div>
        <div class="modal-body">
          <div class="messages-container" ref="messagesContainer">
            <div 
              v-for="message in currentMessages" 
              :key="message.id" 
              :class="['message-bubble', { 'sent': message.sender_id === currentStudentId, 'received': message.sender_id !== currentStudentId }]"
            >
              <div v-if="message.attachments && message.attachments.length > 0" class="message-attachments">
                <div v-for="(attachment, idx) in message.attachments" :key="idx" class="attachment">
                  <img v-if="attachment.type === 'image'" :src="attachment.url" :alt="attachment.name" class="attachment-image" @click="viewAttachment(attachment)" />
                  <div v-else class="attachment-file" @click="downloadAttachment(attachment)">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"></path>
                      <polyline points="13 2 13 9 20 9"></polyline>
                    </svg>
                    <span>{{ attachment.name }}</span>
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                      <polyline points="7 10 12 15 17 10"></polyline>
                      <line x1="12" y1="15" x2="12" y2="3"></line>
                    </svg>
                  </div>
                </div>
              </div>
              
              <p v-if="message.content" class="message-text">{{ message.content }}</p>
              
              <div class="message-footer">
                <span class="message-time">{{ formatTime(message.sent_at) }}</span>
                <span v-if="message.sender_id === currentStudentId" class="message-status">
                  <svg v-if="!message.is_read" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="20 6 9 17 4 12"></polyline>
                  </svg>
                  <svg v-else xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="20 6 9 17 4 12"></polyline>
                    <polyline points="20 6 9 17 4 12" transform="translate(4, 0)"></polyline>
                  </svg>
                  <span v-if="message.is_read && message.read_at" class="read-time">Read {{ formatTime(message.read_at) }}</span>
                </span>
              </div>
            </div>
            <div v-if="currentMessages.length === 0" class="no-messages">
              <p>No messages yet. Start the conversation!</p>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <div v-if="selectedFile" class="file-preview">
            <div class="preview-content">
              <img v-if="previewFile" :src="previewFile" alt="Preview" class="preview-image" />
              <div v-else class="preview-file">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"></path>
                  <polyline points="13 2 13 9 20 9"></polyline>
                </svg>
                <span>{{ selectedFile.name }}</span>
              </div>
              <button @click="removeFile" class="remove-file-btn">
                <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <line x1="18" y1="6" x2="6" y2="18"></line>
                  <line x1="6" y1="6" x2="18" y2="18"></line>
                </svg>
              </button>
            </div>
          </div>
          
          <div class="message-input-area">
            <input 
              type="file" 
              ref="fileInput" 
              @change="handleFileSelect" 
              style="display: none" 
              accept="image/*,.pdf,.doc,.docx,.txt"
            />
            <button class="attach-btn" @click="$refs.fileInput.click()">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="m21.44 11.05-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48"></path>
              </svg>
            </button>
            <input 
              type="text" 
              v-model="newMessage" 
              @keyup.enter="sendMessage" 
              placeholder="Type your message to your teacher..." 
              class="message-input"
            />
            <button class="send-btn" @click="sendMessage" :disabled="!newMessage.trim() && !selectedFile">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <line x1="22" y1="2" x2="11" y2="13"></line>
                <polygon points="22 2 15.46 22 11 13 2 9.54 22 2"></polygon>
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Broadcast Modal -->
    <div v-if="isBroadcastModalOpen" class="modal-overlay" @click.self="closeBroadcastModal">
      <div class="modal-content">
        <div class="modal-header">
          <button @click="closeBroadcastModal" class="close-btn">&times;</button>
          <div class="header-info">
            <div class="broadcast-icon-large">
              <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
              </svg>
            </div>
            <div class="header-details">
              <h2 class="modal-title">{{ selectedBroadcastGroup?.section }}: {{ selectedBroadcastGroup?.subject }}</h2>
              <span class="subject-info">Teacher: {{ selectedBroadcastGroup?.teacher }}</span>
            </div>
          </div>
        </div>
        <div class="modal-body">
          <div class="broadcast-list">
            <div 
              v-for="announcement in selectedBroadcastGroup?.announcements || []" 
              :key="announcement.notification_id"
              :class="['broadcast-item', { 'unread': !announcement.is_read }]"
              @click="openAnnouncementDetail(announcement)"
            >
              <div class="broadcast-item-header">
                <h3 class="broadcast-item-title">{{ announcement.title }}</h3>
                <span v-if="!announcement.is_read" class="unread-label">New</span>
              </div>
              <p class="broadcast-item-body">{{ announcement.body }}</p>
              <div class="broadcast-item-footer">
                <span class="broadcast-item-time">{{ formatTime(announcement.created_at) }}</span>
                <div v-if="announcement.has_attachments || (announcement.attachments && announcement.attachments.length > 0)" class="attachment-indicator">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="m21.44 11.05-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48"/>
                  </svg>
                  <span>{{ announcement.attachments?.length || 0 }} attachments</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Announcement Detail Modal -->
    <div v-if="isAnnouncementDetailOpen" class="modal-overlay" @click.self="closeAnnouncementDetail">
      <div class="modal-content announcement-detail-modal">
        <div class="modal-header">
          <button @click="closeAnnouncementDetail" class="close-btn">&times;</button>
          <div class="header-info">
            <div class="announcement-icon">
              <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/>
                <path d="M13.73 21a2 2 0 0 1-3.46 0"/>
              </svg>
            </div>
            <div class="header-details">
              <h2 class="modal-title">Class Announcement</h2>
              <span class="subject-info">{{ selectedAnnouncement?.subject_name }} - {{ selectedAnnouncement?.section_name }}</span>
            </div>
          </div>
        </div>
        <div class="modal-body announcement-detail-body">
          <div v-if="selectedAnnouncement" class="announcement-content">
            <!-- Announcement Header -->
            <div class="announcement-header">
              <h3 class="announcement-title">{{ selectedAnnouncement.title }}</h3>
              <div class="announcement-meta">
                <div class="teacher-info">
                  <span class="teacher-name">Teacher: {{ selectedAnnouncement.teacher_name }}</span>
                </div>
                <div class="announcement-date">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="12" cy="12" r="10"/>
                    <polyline points="12 6 12 12 16 14"/>
                  </svg>
                  <span>{{ formatFullDate(selectedAnnouncement.created_at) }}</span>
                </div>
              </div>
            </div>

            <!-- Announcement Body -->
            <div class="announcement-body">
              <p class="announcement-text">{{ selectedAnnouncement.body }}</p>
            </div>

            <!-- Attachments Section -->
            <div v-if="selectedAnnouncement.attachments && selectedAnnouncement.attachments.length > 0" class="announcement-attachments">
              <h4 class="attachments-title">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="m21.44 11.05-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48"></path>
                </svg>
                Attachments ({{ selectedAnnouncement.attachments.length }})
              </h4>
              <div class="attachments-grid">
                <div 
                  v-for="(attachment, idx) in selectedAnnouncement.attachments" 
                  :key="idx" 
                  class="attachment-item"
                >
                  <!-- Image Attachments -->
                  <div v-if="attachment.type === 'image'" class="attachment-image-container">
                    <img 
                      :src="attachment.url" 
                      :alt="attachment.name" 
                      class="attachment-image-large" 
                      @click="viewAttachment(attachment)"
                    />
                    <div class="attachment-overlay">
                      <button @click="viewAttachment(attachment)" class="view-btn">
                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                          <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/>
                          <circle cx="12" cy="12" r="3"/>
                        </svg>
                        View
                      </button>
                      <button @click="downloadAttachment(attachment)" class="download-btn">
                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                          <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
                          <polyline points="7 10 12 15 17 10"/>
                          <line x1="12" y1="15" x2="12" y2="3"/>
                        </svg>
                        Download
                      </button>
                    </div>
                  </div>

                  <!-- File Attachments -->
                  <div v-else class="attachment-file-large" @click="downloadAttachment(attachment)">
                    <div class="file-icon">
                      <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/>
                        <polyline points="13 2 13 9 20 9"/>
                      </svg>
                    </div>
                    <div class="file-info">
                      <span class="file-name">{{ attachment.name }}</span>
                      <span class="file-size">{{ formatFileSize(attachment.size) }}</span>
                    </div>
                    <button class="download-file-btn" @click.stop="downloadAttachment(attachment)">
                      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
                        <polyline points="7 10 12 15 17 10"/>
                        <line x1="12" y1="15" x2="12" y2="3"/>
                      </svg>
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button @click="closeAnnouncementDetail" class="close-detail-btn">
            Close
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, nextTick, watch } from 'vue'
import { useRoute } from 'vue-router'
import { supabase } from '@/supabase.js'

// Watch for route changes
const route = useRoute()
watch(() => route.fullPath, () => {
  loadSections()
})

// State management
const currentTab = ref('teachers')
const currentFilter = ref('all')
const searchQuery = ref('')
const selectedSubject = ref('')
const isModalOpen = ref(false)
const isBroadcastModalOpen = ref(false)
const isAnnouncementDetailOpen = ref(false)
const selectedAnnouncement = ref(null)
const activeTeacher = ref(null)
const selectedBroadcastGroup = ref(null)
const newMessage = ref('')
const messagesContainer = ref(null)
const fileInput = ref(null)
const isLoading = ref(false)
const activeTeacherOptionsId = ref(null)
const showArchive = ref(false)
const selectedFile = ref(null)
const previewFile = ref(null)
const deletedConversationKeys = ref(new Set())

// Real-time subscriptions
let messageChannel = null

// Data
const enrolledSubjects = ref([])
const enrolledTeachers = ref([])
const notifications = ref([])
const currentMessages = ref([])
const currentUser = ref(null)
const currentStudentId = ref(null)

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
    
    // Return the file info object (inside the function)
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

// Computed properties
const hasDeletedConversations = computed(() => {
  return deletedConversationKeys.value.size > 0 && filteredTeachers.value.length === 0 && !showArchive.value
})

const filteredTeachers = computed(() => {
  let teachers = enrolledTeachers.value.filter(t => showArchive.value ? t.archived : !t.archived)
  
  if (selectedSubject.value) {
    teachers = teachers.filter(t => t.subject_id === parseInt(selectedSubject.value))
  }
  
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    teachers = teachers.filter(t => 
      t.teacher_name.toLowerCase().includes(query) ||
      t.subject_name.toLowerCase().includes(query)
    )
  }
  
  return teachers
})

const groupedTeachers = computed(() => {
  const subjects = {}
  
  filteredTeachers.value.forEach(teacher => {
    const subjectId = teacher.subject_id
    if (!subjects[subjectId]) {
      subjects[subjectId] = {
        id: subjectId,
        name: teacher.subject_name,
        code: teacher.section_code,
        teachers: []
      }
    }
    subjects[subjectId].teachers.push(teacher)
  })
  
  return Object.values(subjects)
})

const groupedBroadcasts = computed(() => {
  const groups = {}
  let notifs = notifications.value
  
  if (currentFilter.value === 'unread') {
    notifs = notifs.filter(n => !n.is_read)
  }
  
  notifs.forEach(notif => {
    const key = `${notif.section_name}: ${notif.subject_name}`
    if (!groups[key]) {
      groups[key] = {
        section: notif.section_name,
        subject: notif.subject_name,
        teacher: notif.teacher_name,
        announcements: []
      }
    }
    groups[key].announcements.push(notif)
  })
  
  return groups
})

// Handler methods
const toggleTeacherOptions = (teacherId) => {
  activeTeacherOptionsId.value = activeTeacherOptionsId.value === teacherId ? null : teacherId
}

const archiveConversation = (teacher) => {
  enrolledTeachers.value = enrolledTeachers.value.map(t => 
    (t.id === teacher.id && t.section_id === teacher.section_id) 
      ? { ...t, archived: !t.archived } 
      : t
  )
  activeTeacherOptionsId.value = null
}

const deleteConversation = async (teacher) => {
  if (!confirm(`Are you sure you want to delete the conversation with Teacher: ${teacher.teacher_name}?\n\nNote: All messages will be permanently deleted, but you can still message this teacher again.`)) {
    return
  }
  
  try {
    const { error } = await supabase
      .from('messages')
      .delete()
      .eq('section_id', teacher.section_id)
      .or(`and(sender_id.eq.${currentStudentId.value},recipient_id.eq.${teacher.id}),and(sender_id.eq.${teacher.id},recipient_id.eq.${currentStudentId.value})`)
    
    if (error) throw error
    
    deletedConversationKeys.value.add(`${teacher.id}-${teacher.section_id}`)
    
    enrolledTeachers.value = enrolledTeachers.value.filter(t => 
      !(t.id === teacher.id && t.section_id === teacher.section_id)
    )
    activeTeacherOptionsId.value = null
    
    console.log('Conversation deleted. Teacher can be restored.')
    
  } catch (error) {
    console.error('Error deleting conversation:', error)
    alert('Failed to delete conversation. Please try again.')
  }
}

const showAvailableTeachers = () => {
  deletedConversationKeys.value.clear()
  loadEnrolledSubjectsAndTeachers()
}

const handleFileSelect = (event) => {
  const file = event.target.files[0]
  if (!file) return
  
  selectedFile.value = file
  
  if (file.type.startsWith('image/')) {
    const reader = new FileReader()
    reader.onload = (e) => {
      previewFile.value = e.target.result
    }
    reader.readAsDataURL(file)
  } else {
    previewFile.value = null
  }
}

const removeFile = () => {
  selectedFile.value = null
  previewFile.value = null
  if (fileInput.value) {
    fileInput.value.value = ''
  }
}

const viewAttachment = (attachment) => {
  window.open(attachment.url, '_blank')
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

const openBroadcastGroup = async (group) => {
  selectedBroadcastGroup.value = group
  
  console.log('Opening broadcast group:', group)
  
  // Load attachments for all announcements in this group
  for (const announcement of group.announcements) {
    if (!announcement.attachments || announcement.attachments.length === 0) {
      console.log('Loading attachments for announcement:', announcement.notification_id)
      try {
        const { data: attachments, error } = await supabase
          .from('message_attachments')
          .select('*')
          .eq('message_id', announcement.notification_id)
        
        if (error) throw error
        
        if (attachments && attachments.length > 0) {
          announcement.attachments = attachments.map(att => ({
            name: att.file_name,
            url: att.file_url,
            type: att.file_type,
            size: att.file_size,
            path: att.file_path
          }))
          announcement.has_attachments = true
          console.log('Loaded attachments for announcement:', announcement.attachments)
        } else {
          announcement.attachments = []
          announcement.has_attachments = false
        }
      } catch (error) {
        console.error('Error loading attachments for announcement:', error)
        announcement.attachments = []
        announcement.has_attachments = false
      }
    } else {
      console.log('Announcement already has attachments:', announcement.attachments)
    }
  }
  
  isBroadcastModalOpen.value = true
}

const closeBroadcastModal = () => {
  isBroadcastModalOpen.value = false
  selectedBroadcastGroup.value = null
}

// New methods for announcement detail
const openAnnouncementDetail = async (announcement) => {
  selectedAnnouncement.value = announcement
  // Always fetch attachments from DB for reliability
  await loadAnnouncementAttachments(announcement.notification_id)
  // Mark as read
  await markBroadcastAsRead(announcement)
  isAnnouncementDetailOpen.value = true
}

const closeAnnouncementDetail = () => {
  isAnnouncementDetailOpen.value = false
  selectedAnnouncement.value = null
}

const loadAnnouncementAttachments = async (messageId) => {
  try {
    const { data: attachments, error } = await supabase
      .from('message_attachments')
      .select('*')
      .eq('message_id', messageId)
    if (error) throw error
    if (attachments && attachments.length > 0) {
      selectedAnnouncement.value.attachments = attachments.map(att => ({
        name: att.file_name,
        url: att.file_url,
        type: att.file_type,
        size: att.file_size,
        path: att.file_path
      }))
      selectedAnnouncement.value.has_attachments = true
    } else {
      selectedAnnouncement.value.attachments = []
      selectedAnnouncement.value.has_attachments = false
    }
  } catch (error) {
    selectedAnnouncement.value.attachments = []
    selectedAnnouncement.value.has_attachments = false
  }
}

const formatFileSize = (bytes) => {
  if (!bytes) return '0 B'
  
  const k = 1024
  const sizes = ['B', 'KB', 'MB', 'GB']
  const i = Math.floor(Math.log(bytes) / Math.log(k))
  
  return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i]
}

const formatFullDate = (dateString) => {
  if (!dateString) return ''
  
  const date = new Date(dateString)
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

const markBroadcastAsRead = async (announcement) => {
  if (announcement.is_read) return
  
  try {
    const { error } = await supabase
      .from('messages')
      .update({ is_read: true })
      .eq('id', announcement.notification_id)
    
    if (error) throw error
    
    // Update local state
    announcement.is_read = true
    
    // Update notifications array
    const notificationIndex = notifications.value.findIndex(n => n.notification_id === announcement.notification_id)
    if (notificationIndex !== -1) {
      notifications.value[notificationIndex].is_read = true
    }
    
    // Update selectedBroadcastGroup if it exists
    if (selectedBroadcastGroup.value) {
      const groupAnnouncement = selectedBroadcastGroup.value.announcements.find(a => a.notification_id === announcement.notification_id)
      if (groupAnnouncement) {
        groupAnnouncement.is_read = true
      }
    }
    
    console.log('Broadcast marked as read:', announcement.notification_id)
    
  } catch (error) {
    console.error('Error marking broadcast as read:', error)
  }
}

const handleClickOutside = (event) => {
  const optionsMenu = document.querySelector('.options-menu')
  const optionsBtn = event.target.closest('.options-btn')
  
  if (optionsMenu && !optionsMenu.contains(event.target) && !optionsBtn) {
    activeTeacherOptionsId.value = null
  }
}

// Authentication methods
const getCurrentUser = async () => {
  try {
    const { data: { user }, error: authError } = await supabase.auth.getUser()
    if (authError) throw authError
    
    if (!user) {
      console.error('No authenticated user found')
      return null
    }
    
    const { data: profile, error: profileError } = await supabase
      .from('profiles')
      .select('id, auth_user_id, role, full_name, email')
      .eq('auth_user_id', user.id)
      .single()
    
    if (profileError) throw profileError
    
    if (!profile || profile.role !== 'student') {
      console.error('User is not a student or profile not found')
      return null
    }
    
    const { data: studentData, error: studentError } = await supabase
      .from('students')
      .select('id')
      .eq('profile_id', profile.id)
      .single()
    
    if (studentError) throw studentError
    
    currentUser.value = user
    currentStudentId.value = studentData.id
    
    console.log('Student authenticated:', profile.full_name)
    console.log('Student ID:', studentData.id)
    
    return { authUser: user, studentId: studentData.id, profile: profile }
    
  } catch (error) {
    console.error('Error getting current user:', error)
    return null
  }
}

// Data loading methods
const loadEnrolledSubjectsAndTeachers = async () => {
  try {
    if (!currentStudentId.value) {
      console.error('No student ID available')
      return
    }
    
    isLoading.value = true
    console.log('Loading subjects and teachers for student:', currentStudentId.value)
    
    const { data: enrollments, error: enrollError } = await supabase
      .from('enrollments')
      .select('section_id')
      .eq('student_id', currentStudentId.value)
      .eq('status', 'active')
    
    if (enrollError) {
      console.error('Error fetching enrollments:', enrollError)
      throw enrollError
    }
    
    console.log('Enrollments found:', enrollments)
    
    if (!enrollments || enrollments.length === 0) {
      console.log('No enrollments found for this student')
      enrolledSubjects.value = []
      enrolledTeachers.value = []
      return
    }
    
    const sectionIds = enrollments.map(e => e.section_id)
    
    console.log('Fetching sections for IDs:', sectionIds)
    const { data: sections, error: sectionsError } = await supabase
      .from('sections')
      .select(`
        id,
        name,
        section_code,
        subject_id
      `)
      .in('id', sectionIds)
    
    if (sectionsError) {
      console.error('Error fetching sections:', sectionsError)
      throw sectionsError
    }
    
    console.log('Sections found:', sections)
    
    if (!sections || sections.length === 0) {
      enrolledSubjects.value = []
      enrolledTeachers.value = []
      return
    }
    
    const subjectIds = [...new Set(sections.map(s => s.subject_id))]
    const { data: subjects, error: subjectsError } = await supabase
      .from('subjects')
      .select('id, name, teacher_id')
      .in('id', subjectIds)
    
    if (subjectsError) throw subjectsError
    
    const teacherIds = [...new Set(subjects.map(s => s.teacher_id))]
    const { data: teachers, error: teachersError } = await supabase
      .from('teachers')
      .select('id, full_name, email')
      .in('id', teacherIds)
    
    if (teachersError) throw teachersError
    
    console.log('Subjects:', subjects)
    console.log('Teachers:', teachers)
    
    const processedSubjects = []
    const processedTeachers = []
    const subjectMap = new Map()
    
    const subjectsDataMap = new Map(subjects.map(s => [s.id, s]))
    const teachersDataMap = new Map(teachers.map(t => [t.id, t]))
    
    for (const section of sections) {
      const subject = subjectsDataMap.get(section.subject_id)
      if (!subject) continue
      
      const teacher = teachersDataMap.get(subject.teacher_id)
      if (!teacher) continue
      
      if (!subjectMap.has(subject.id)) {
        processedSubjects.push({
          id: subject.id,
          name: subject.name,
          code: section.section_code
        })
        subjectMap.set(subject.id, true)
      }
      
      const { count: unreadCount } = await supabase
        .from('messages')
        .select('*', { count: 'exact', head: true })
        .eq('section_id', section.id)
        .eq('sender_id', teacher.id)
        .eq('recipient_id', currentStudentId.value)
        .eq('message_type', 'direct')
        .eq('is_read', false)
      
      const { data: lastMsgData } = await supabase
        .from('messages')
        .select('message_text, sent_at')
        .eq('section_id', section.id)
        .or(`and(sender_id.eq.${currentStudentId.value},recipient_id.eq.${teacher.id}),and(sender_id.eq.${teacher.id},recipient_id.eq.${currentStudentId.value})`)
        .order('sent_at', { ascending: false })
        .limit(1)
      
      const lastMsg = lastMsgData && lastMsgData.length > 0 ? lastMsgData[0] : null
      
      processedTeachers.push({
        id: teacher.id,
        teacher_name: teacher.full_name,
        email: teacher.email,
        subject_id: subject.id,
        subject_name: subject.name,
        section_id: section.id,
        section_name: section.name,
        section_code: section.section_code,
        unread_count: unreadCount || 0,
        last_message: lastMsg?.message_text || null,
        last_message_time: lastMsg?.sent_at || null,
        name: teacher.full_name,
        archived: false
      })
    }
    
    enrolledSubjects.value = processedSubjects
    enrolledTeachers.value = processedTeachers
    
    console.log('Processed subjects:', processedSubjects)
    console.log('Processed teachers:', processedTeachers)
    
  } catch (error) {
    console.error('Error loading enrolled data:', error)
    alert('Error loading messaging data. Please check console for details.')
  } finally {
    isLoading.value = false
  }
}

const loadNotifications = async () => {
  try {
    if (!currentStudentId.value) return
    
    console.log('Loading notifications for student:', currentStudentId.value)
    
    const { data: enrollments } = await supabase
      .from('enrollments')
      .select('section_id')
      .eq('student_id', currentStudentId.value)
      .eq('status', 'active')
    
    if (!enrollments || enrollments.length === 0) {
      notifications.value = []
      return
    }
    
    const sectionIds = enrollments.map(e => e.section_id)
    
    const { data: messages, error } = await supabase
      .from('messages')
      .select('*')
      .in('section_id', sectionIds)
      .eq('message_type', 'announcement')
      .order('sent_at', { ascending: false })
    
    if (error) throw error
    
    if (!messages || messages.length === 0) {
      notifications.value = []
      return
    }
    
    // Load attachments for all messages
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
    
    const { data: sections } = await supabase
      .from('sections')
      .select('id, name, subject_id')
      .in('id', sectionIds)
    
    const sectionMap = new Map(sections?.map(s => [s.id, s]) || [])
    
    const subjectIds = [...new Set(sections?.map(s => s.subject_id) || [])]
    const { data: subjects } = await supabase
      .from('subjects')
      .select('id, name')
      .in('id', subjectIds)
    
    const subjectMap = new Map(subjects?.map(s => [s.id, s]) || [])
    
    const senderIds = [...new Set(messages.map(m => m.sender_id))]
    const { data: senders } = await supabase
      .from('teachers')
      .select('id, full_name')
      .in('id', senderIds)
    
    const senderMap = new Map(senders?.map(s => [s.id, s]) || [])
    
    notifications.value = messages.map(msg => {
      const section = sectionMap.get(msg.section_id)
      const subject = section ? subjectMap.get(section.subject_id) : null
      const sender = senderMap.get(msg.sender_id)
      const messageAttachments = attachmentsMap[msg.id] || []
      
      return {
        notification_id: msg.id,
        title: 'Class Announcement',
        body: msg.message_text,
        created_at: msg.sent_at,
        is_read: msg.is_read,
        notification_type: 'announcement',
        teacher_name: sender?.full_name,
        subject_name: subject?.name,
        section_name: section?.name,
        has_attachments: messageAttachments.length > 0,
        attachments: messageAttachments
      }
    })
    
    console.log('Loaded notifications with attachments:', notifications.value)
    
  } catch (error) {
    console.error('Error loading notifications:', error)
  }
}

// Chat methods
const startChatWithTeacher = async (teacher) => {
  console.log('Starting chat with teacher:', teacher)
  
  activeTeacher.value = {
    ...teacher,
    id: teacher.id,
    teacher_name: teacher.teacher_name,
    subject_name: teacher.subject_name,
    section_id: teacher.section_id
  }
  
  isModalOpen.value = true
  await nextTick()
  
  await loadConversationMessages(teacher.id, teacher.section_id)
  
  await nextTick()
  scrollToBottom()
}

const loadConversationMessages = async (teacherId, sectionId) => {
  try {
    if (!currentStudentId.value) return
    
    console.log('Loading messages between student and teacher:', { 
      studentId: currentStudentId.value, 
      teacherId, 
      sectionId 
    })
    
    currentMessages.value = []
    
    const { data: messages, error } = await supabase
      .from('messages')
      .select('*')
      .eq('section_id', sectionId)
      .eq('message_type', 'direct')
      .or(`and(sender_id.eq.${currentStudentId.value},recipient_id.eq.${teacherId}),and(sender_id.eq.${teacherId},recipient_id.eq.${currentStudentId.value})`)
      .order('sent_at', { ascending: true })
    
    if (error) {
      console.error('Error fetching messages:', error)
      throw error
    }
    
    console.log('Raw messages from database:', messages)
    
    if (!messages || messages.length === 0) {
      console.log('No messages found in database')
      currentMessages.value = []
      return
    }
    
    // Load attachments for all messages
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
    
    currentMessages.value = messages.map(msg => ({
      id: msg.id,
      sender_id: msg.sender_id,
      recipient_id: msg.recipient_id,
      content: msg.message_text,
      sent_at: msg.sent_at,
      is_read: msg.is_read,
      read_at: msg.read_at,
      message_type: 'direct',
      attachments: attachmentsMap[msg.id] || []
    }))
    
    console.log('Processed messages with attachments:', currentMessages.value)
    
    await nextTick()
    await markMessagesAsRead(teacherId, sectionId)
    
  } catch (error) {
    console.error('Error loading conversation messages:', error)
    currentMessages.value = []
  }
}

const sendMessage = async () => {
  if ((!newMessage.value.trim() && !selectedFile.value) || !activeTeacher.value || !currentStudentId.value) return
  
  const messageText = newMessage.value.trim()
  const fileToUpload = selectedFile.value
  
  // Create temporary message for UI
  const tempMessage = {
    id: 'temp-' + Date.now(),
    sender_id: currentStudentId.value,
    recipient_id: activeTeacher.value.id,
    content: messageText || '📎 Attachment',
    sent_at: new Date().toISOString(),
    is_read: false,
    read_at: null,
    message_type: 'direct',
    attachments: fileToUpload ? [{
      name: fileToUpload.name,
      url: previewFile.value,
      type: fileToUpload.type.startsWith('image/') ? 'image' : 'file'
    }] : []
  }
  
  currentMessages.value.push(tempMessage)
  newMessage.value = ''
  removeFile()
  
  await nextTick()
  scrollToBottom()
  
  try {
    isLoading.value = true
    
    // Upload file first if exists
    let uploadedAttachment = null
    if (fileToUpload) {
      uploadedAttachment = await uploadFileToStorage(fileToUpload)
    }
    
    // Insert message
    const { data: newMsg, error: sendError } = await supabase
      .from('messages')
      .insert({
        section_id: activeTeacher.value.section_id,
        sender_id: currentStudentId.value,
        recipient_id: activeTeacher.value.id,
        message_text: messageText || '📎 Attachment',
        message_type: 'direct',
        is_read: false
      })
      .select()
      .single()
    
    if (sendError) throw sendError
    
    console.log('Message sent successfully:', newMsg)
    
    // Save attachments to database if exists
    if (uploadedAttachment) {
      await saveMessageAttachments(newMsg.id, [uploadedAttachment])
    }
    
    // Update temp message with real data
    const tempIndex = currentMessages.value.findIndex(m => m.id === tempMessage.id)
    if (tempIndex !== -1) {
      currentMessages.value[tempIndex] = {
        id: newMsg.id,
        sender_id: newMsg.sender_id,
        recipient_id: newMsg.recipient_id,
        content: newMsg.message_text,
        sent_at: newMsg.sent_at,
        is_read: newMsg.is_read,
        read_at: newMsg.read_at,
        message_type: newMsg.message_type,
        attachments: uploadedAttachment ? [{
          name: uploadedAttachment.name,
          url: uploadedAttachment.url,
          type: uploadedAttachment.type,
          size: uploadedAttachment.size
        }] : []
      }
    }
    
    await loadEnrolledSubjectsAndTeachers()
    
  } catch (error) {
    console.error('Failed to send message:', error)
    
    const tempIndex = currentMessages.value.findIndex(m => m.id === tempMessage.id)
    if (tempIndex !== -1) {
      currentMessages.value.splice(tempIndex, 1)
    }
    
    alert('Failed to send message. Please try again.')
  } finally {
    isLoading.value = false
  }
}

const markMessagesAsRead = async (teacherId, sectionId) => {
  try {
    if (!currentStudentId.value) return
    
    console.log('Marking messages as read:', { teacherId, sectionId })
    
    // First, update the database
    const { data: updatedMessages, error } = await supabase
      .from('messages')
      .update({ is_read: true, read_at: new Date().toISOString() })
      .eq('section_id', sectionId)
      .eq('sender_id', teacherId)
      .eq('recipient_id', currentStudentId.value)
      .eq('message_type', 'direct')
      .eq('is_read', false)
      .select()
    
    if (error) throw error
    
    console.log('Database updated, affected rows:', updatedMessages?.length || 0)
    
    // Update local message state
    currentMessages.value.forEach(m => {
      if (m.sender_id === teacherId && !m.is_read) {
        m.is_read = true
        m.read_at = new Date().toISOString()
      }
    })
    
    // IMMEDIATE: Update the specific teacher's unread count to 0
    const teacherIndex = enrolledTeachers.value.findIndex(t => 
      t.id === teacherId && t.section_id === sectionId
    )
    if (teacherIndex !== -1) {
      // Force Vue reactivity by creating a new array
      enrolledTeachers.value = enrolledTeachers.value.map((teacher, index) => {
        if (index === teacherIndex) {
          console.log(`Immediately reset unread count to 0 for teacher ${teacher.teacher_name}`)
          return { ...teacher, unread_count: 0 }
        }
        return teacher
      })
    }
    
    console.log('Messages marked as read and UI updated')
    
  } catch (error) {
    console.error('Error marking messages as read:', error)
  }
}

const closeModal = () => {
  isModalOpen.value = false
  activeTeacher.value = null
  currentMessages.value = []
  removeFile()
}

const clearNotifications = async () => {
  try {
    if (!currentStudentId.value) return
    
    console.log('Marking all notifications as read')
    
    const unreadIds = notifications.value
      .filter(n => !n.is_read)
      .map(n => n.notification_id)
    
    if (unreadIds.length === 0) return
    
    const { error } = await supabase
      .from('messages')
      .update({ is_read: true })
      .in('id', unreadIds)
    
    if (error) throw error
    
    notifications.value.forEach(n => {
      n.is_read = true
    })
    
  } catch (error) {
    console.error('Error clearing notifications:', error)
  }
}

// Real-time methods
const setupRealTimeSubscriptions = () => {
  if (!currentStudentId.value) return
  
  console.log('Setting up real-time subscriptions for student messages')
  
  messageChannel = supabase
    .channel('student-messages-realtime')
    .on(
      'postgres_changes',
      {
        event: 'INSERT',
        schema: 'public',
        table: 'messages'
      },
      async (payload) => {
        console.log('New message received:', payload.new)
        
        const newMessageData = payload.new
        
        if (newMessageData.message_type === 'announcement') {
          await loadNotifications()
          return
        }
        
        if (newMessageData.recipient_id === currentStudentId.value && 
            newMessageData.message_type === 'direct') {
          
          // Reload teacher list to update unread counts
          await loadEnrolledSubjectsAndTeachers()
          
          if (isModalOpen.value && 
              activeTeacher.value && 
              newMessageData.section_id === activeTeacher.value.section_id &&
              newMessageData.sender_id === activeTeacher.value.id) {
            
            // Load attachments for the new message
            const { data: attachments } = await supabase
              .from('message_attachments')
              .select('*')
              .eq('message_id', newMessageData.id)
            
            const processedAttachments = attachments ? attachments.map(att => ({
              name: att.file_name,
              url: att.file_url,
              type: att.file_type,
              size: att.file_size,
              path: att.file_path
            })) : []
            
            console.log('Loaded attachments for new message:', processedAttachments)
            
            currentMessages.value.push({
              id: newMessageData.id,
              sender_id: newMessageData.sender_id,
              recipient_id: newMessageData.recipient_id,
              content: newMessageData.message_text,
              sent_at: newMessageData.sent_at,
              is_read: newMessageData.is_read,
              read_at: newMessageData.read_at,
              message_type: newMessageData.message_type,
              attachments: processedAttachments
            })
            
            console.log('Message added with attachments:', processedAttachments)
            
            await nextTick()
            scrollToBottom()
            
            // Mark as read and immediately update teacher's unread count
            await markMessagesAsRead(newMessageData.sender_id, newMessageData.section_id)
          }
        }
      }
    )
    .on(
      'postgres_changes',
      {
        event: 'UPDATE',
        schema: 'public',
        table: 'messages'
      },
      async (payload) => {
        console.log('Message updated:', payload.new)
        
        if (isModalOpen.value && activeTeacher.value) {
          const messageIndex = currentMessages.value.findIndex(m => m.id === payload.new.id)
          if (messageIndex !== -1) {
            currentMessages.value[messageIndex].is_read = payload.new.is_read
            currentMessages.value[messageIndex].read_at = payload.new.read_at
          }
        }
        
        await loadEnrolledSubjectsAndTeachers()
      }
    )
    .on(
      'postgres_changes',
      {
        event: 'INSERT',
        schema: 'public',
        table: 'message_attachments'
      },
      async (payload) => {
        console.log('New attachment received:', payload.new)
        
        // If we're viewing the conversation and a new attachment is added
        if (isModalOpen.value && activeTeacher.value) {
          const messageIndex = currentMessages.value.findIndex(m => m.id === payload.new.message_id)
          if (messageIndex !== -1) {
            const newAttachment = {
              name: payload.new.file_name,
              url: payload.new.file_url,
              type: payload.new.file_type,
              size: payload.new.file_size,
              path: payload.new.file_path
            }
            
            if (!currentMessages.value[messageIndex].attachments) {
              currentMessages.value[messageIndex].attachments = []
            }
            
            currentMessages.value[messageIndex].attachments.push(newAttachment)
            console.log('Attachment added to message:', newAttachment)
          }
        }
      }
    )
    .subscribe()
}

const cleanupRealTimeSubscriptions = () => {
  if (messageChannel) {
    messageChannel.unsubscribe()
    messageChannel = null
  }
}

// Utility methods
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

// Lifecycle
onMounted(async () => {
  console.log('Student messages component mounted')
  
  document.addEventListener('click', handleClickOutside)
  
  const userData = await getCurrentUser()
  if (userData) {
    console.log('Student authenticated:', userData.profile.full_name)
    
    await Promise.all([
      loadEnrolledSubjectsAndTeachers(),
      loadNotifications()
    ])
    
    setupRealTimeSubscriptions()
  } else {
    console.error('Authentication failed or user is not a student')
  }
})

onUnmounted(() => {
  cleanupRealTimeSubscriptions()
  document.removeEventListener('click', handleClickOutside)
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Main Container */
.messages-container {
  min-height: 100vh;
  background: #FBFFE4;
  padding: 1.5rem;
  font-family: 'Inter', sans-serif;
}
.dark .messages-container {
  background: #181c20;
}

/* Header matching Home.vue */
.header-card {
  background: white;
  border-radius: 16px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
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

.header-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1f2937;
  margin-bottom: 0.25rem;
}
.dark .header-title {
  color: #A3D1C6;
}

.header-subtitle {
  font-size: 0.875rem;
  color: #6b7280;
}
.dark .header-subtitle {
  color: #A3D1C6;
}

/* Content Card matching Home.vue */
.content-card {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
  display: flex;
  flex-direction: column;
  border: 2px solid #A3D1C6;
}
.dark .content-card {
  background: #23272b;
  border: 2px solid #20c997;
  box-shadow: 0 2px 8px rgba(0,0,0,0.25);
}

.card-header {
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

.card-desc {
  font-size: 0.813rem;
  color: #6b7280;
  margin-bottom: 1rem;
}
.dark .card-desc {
  color: #A3D1C6;
}

/* Tab Content */
.tab-content {
  padding: 0;
  background: white;
  overflow-y: auto;
  flex: 1;
}
.dark .tab-content {
  background: #23272b;
}

.tabs {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.tab-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  border: none;
  background: #FBFFE4;
  border: 1px solid #A3D1C6;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.2s;
  font-family: 'Inter', sans-serif;
  font-size: 0.875rem;
  font-weight: 500;
  color: #6b7280;
}
.dark .tab-btn {
  background: #23272b;
  border-color: #20c997;
  color: #A3D1C6;
}

.tab-btn:hover {
  background: #A3D1C6;
  color: #181c20;
  border-color: #3D8D7A;
}
.dark .tab-btn:hover {
  background: #A3D1C6;
  color: #23272b;
  border-color: #20c997;
}

.tab-btn.active {
  background: #3D8D7A;
  color: white;
  border-color: #3D8D7A;
  box-shadow: 0 2px 8px rgba(61, 141, 122, 0.2);
}
.dark .tab-btn.active {
  background: #20c997;
  color: #181c20;
  border-color: #20c997;
}

.tab-content {
  padding: 1.5rem;
}

.dark .tab-content {
  background: #2a2d35;
}

/* Section Actions */
.section-actions {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
  gap: 1rem;
  flex-wrap: wrap;
  padding: 0 1.5rem;
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
  color: #3D8D7A;
}
.dark .search-icon {
  color: #A3D1C6;
}

.search-input {
  width: 100%;
  padding: 0.75rem 1rem 0.75rem 3rem;
  border: 1px solid #A3D1C6;
  border-radius: 12px;
  font-size: 0.875rem;
  background: white;
  color: #1f2937;
  transition: all 0.2s ease;
  font-family: 'Inter', sans-serif;
}
.dark .search-input {
  background: #23272b;
  border-color: #20c997;
  color: #A3D1C6;
}

.search-input:focus {
  outline: none;
  border-color: #3D8D7A;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
}
.dark .search-input:focus {
  border-color: #20c997;
  box-shadow: 0 0 0 3px rgba(32, 201, 151, 0.1);
}

/* Empty States */
.empty-state, .deleted-state {
  text-align: center;
  padding: 3rem 2rem;
  color: #9ca3af;
}
.dark .empty-state, .dark .deleted-state {
  color: #A3D1C6;
}

.empty-icon, .deleted-icon {
  margin-bottom: 1rem;
  color: #3D8D7A;
}
.dark .empty-icon, .dark .deleted-icon {
  color: #A3D1C6;
}

.empty-state p, .deleted-state p {
  font-size: 0.875rem;
  margin: 0;
}

.show-teachers-btn {
  margin-top: 1.5rem;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: #3D8D7A;
  color: white;
  border: none;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  font-family: 'Inter', sans-serif;
}
.dark .show-teachers-btn {
  background: #20c997;
  color: #181c20;
}

.show-teachers-btn:hover {
  background: #2f6b5c;
  transform: translateY(-1px);
}
.dark .show-teachers-btn:hover {
  background: #0ea770;
}

/* Teachers List matching Home.vue assessment pattern */
.teachers-by-subject {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  padding: 1.5rem;
}

.subject-group {
  background: #FBFFE4;
  border: 1px solid #A3D1C6;
  border-radius: 12px;
  padding: 1.25rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}
.dark .subject-group {
  background: #23272b;
  border-color: #20c997;
  box-shadow: 0 2px 8px rgba(0,0,0,0.25);
}

.subject-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
  padding-bottom: 0.75rem;
  border-bottom: 1px solid #A3D1C6;
}
.dark .subject-header {
  border-bottom-color: #20c997;
}

.subject-name {
  font-size: 1.125rem;
  font-weight: 600;
  color: #1f2937;
  margin: 0;
}
.dark .subject-name {
  color: #A3D1C6;
}

.subject-code {
  font-size: 0.813rem;
  font-weight: 500;
  color: #3D8D7A;
  background: #d1fae5;
  padding: 0.25rem 0.75rem;
  border-radius: 8px;
  border: 1px solid #10b981;
}
.dark .subject-code {
  background: #022c22;
  color: #34d399;
  border-color: #059669;
}

.teachers-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}



.teacher-item {
  background: #FBFFE4;
  border-radius: 10px;
  padding: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: all 0.2s;
  border: 1px solid #A3D1C6;
  margin-bottom: 0.75rem;
  cursor: pointer;
}
.dark .teacher-item {
  background: #23272b;
  border-color: #20c997;
}

.teacher-item:hover {
  background: #A3D1C6;
  border-color: #3D8D7A;
}
.dark .teacher-item:hover {
  background: #23272b;
  border-color: #A3D1C6;
}

.teacher-item.has-unread {
  border-color: #3D8D7A;
  border-width: 2px;
}
.dark .teacher-item.has-unread {
  border-color: #20c997;
  border-width: 2px;
}

.teacher-info {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex: 1;
  min-width: 0;
}

.teacher-avatar {
  width: 48px;
  height: 48px;
  background: #3D8D7A;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 600;
  font-size: 1.1rem;
  flex-shrink: 0;
}
.dark .teacher-avatar {
  background: #20c997;
  color: #181c20;
}

.teacher-details {
  flex: 1;
  min-width: 0;
}

.teacher-name {
  font-size: 0.938rem;
  font-weight: 600;
  color: #1f2937;
  margin-bottom: 0.25rem;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.dark .teacher-name {
  color: #A3D1C6;
}

.teacher-email {
  font-size: 0.813rem;
  color: #6b7280;
  margin-bottom: 0.25rem;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.dark .teacher-email {
  color: #A3D1C6;
}

.message-status {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.last-time {
  font-size: 0.875rem;
  font-weight: 600;
  color: #1f2937;
}
.dark .last-time {
  color: #A3D1C6;
}

.unread-badge {
  padding: 0.25rem 0.75rem;
  border-radius: 6px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  white-space: nowrap;
  background: #fef3c7;
  color: #d97706;
  border: 1px solid #fbbf24;
}
.dark .unread-badge {
  background: #451a03;
  color: #fbbf24;
  border-color: #d97706;
}

.options-wrapper {
  position: relative;
}

.options-btn {
  padding: 0.3rem;
  background: transparent;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  color: var(--text-secondary);
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}

.options-btn:hover {
  background: var(--bg-accent);
  color: var(--text-accent);
}

.options-menu {
  position: absolute;
  top: 100%;
  right: 0;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  box-shadow: 0 4px 12px var(--shadow-color);
  padding: 0.25rem;
  min-width: 140px;
  z-index: 1000;
  margin-top: 0.25rem;
}

.options-menu a {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 0.75rem;
  color: var(--text-primary);
  text-decoration: none;
  border-radius: 6px;
  transition: background-color 0.2s ease;
  font-size: 0.875rem;
  font-weight: 400;
}

.options-menu a:hover {
  background: var(--bg-accent);
}

.options-menu a.delete-option {
  color: #ef4444;
}

.options-menu a.delete-option:hover {
  background: rgba(239, 68, 68, 0.1);
}

.options-wrapper {
  position: relative;
}

.options-btn {
  padding: 0.5rem;
  background: transparent;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  color: #6b7280;
  transition: all 0.2s ease;
}

.dark .options-btn {
  color: #9ca3af;
}

.options-btn:hover {
  background: #f3f4f6;
  color: #3D8D7A;
}

.dark .options-btn:hover {
  background: #374151;
  color: #A3D1C6;
}

.action-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1rem;
  background: var(--bg-accent);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  color: var(--text-accent);
  font-size: 0.9rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
}

.action-btn:hover {
  background: var(--bg-accent-hover);
  transform: translateY(-1px);
}

.empty-state {
  text-align: center;
  color: var(--text-muted);
  padding: 3rem 2rem;
}

.empty-icon {
  color: var(--text-muted);
  margin-bottom: 1rem;
}

.empty-state p {
  font-size: 1.1rem;
  font-weight: 600;
  margin: 0;
  color: var(--text-secondary);
}

.empty-subtext {
  font-size: 0.9rem;
  color: var(--text-muted);
  margin-top: 0.5rem;
  display: block;
}

.conversation-item {
  overflow: visible;
  position: relative; /* Add this */
  z-index: 10;        /* Add this */
}

.conversation-item.menu-open {
  z-index: 10000;
}

.conversation-list,
.notification-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.conversation-item,
.notification-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  background: linear-gradient(135deg, var(--bg-accent) 0%, var(--bg-card) 100%);
  border: 1px solid var(--border-color);
  border-radius: 20px;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
}

.conversation-item.unread {
  background: linear-gradient(135deg, var(--bg-unread) 0%, var(--bg-card) 100%);
  border-color: var(--border-color-hover);
}

.notification-item.unread {
  background: linear-gradient(135deg, var(--bg-unread) 0%, var(--bg-card) 100%);
  border-color: var(--border-color-hover);
}

.notification-item.important {
  background: linear-gradient(135deg, var(--bg-important) 0%, var(--bg-card) 100%);
  border-color: #ffc107;
}

.conversation-item:hover,
.notification-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 40px var(--shadow-medium);
  border-color: var(--border-color-hover);
}

.sender-info {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex: 1;
}

.sender-avatar {
  position: relative;
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, #A3D1C6 0%, #B3D8A8 100%);
  color: var(--text-accent);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 1.2rem;
  flex-shrink: 0;
  box-shadow: 0 4px 16px var(--shadow-light);
}

.message-content {
  flex: 1;
  min-width: 0;
}

.message-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.5rem;
}

.sender-name {
  font-weight: 700;
  color: var(--text-accent);
  margin: 0;
  font-size: 1.1rem;
}

.message-indicators {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.unread-dot {
  width: 8px;
  height: 8px;
  background: var(--text-accent);
  border-radius: 50%;
  flex-shrink: 0;
}

.message-time {
  font-size: 0.85rem;
  color: var(--text-muted);
  font-weight: 500;
}

.last-message {
  font-size: 0.95rem;
  color: var(--text-secondary);
  margin: 0;
  line-height: 1.4;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.message-options-container {
  position: relative;
  z-index: 20;
}

.options-btn {
  background: none;
  border: none;
  color: var(--text-muted);
  cursor: pointer;
  padding: 0.5rem;
  transition: color 0.2s ease;
}

.options-btn:hover {
  color: var(--text-accent);
}

.options-menu {
  position: absolute;
  top: 100%;
  right: 0;
  background-color: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  box-shadow: 0 8px 24px var(--shadow-medium);
  padding: 0.5rem;
  display: flex;
  flex-direction: column;
  width: 200px;
  z-index: 9999;
  margin-top: 10px;
}

.options-menu a {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.75rem 1rem;
    color: var(--text-secondary);
    text-decoration: none;
    border-radius: 8px;
    transition: background-color 0.2s ease, color 0.2s ease;
}

.options-menu a:hover {
    background-color: var(--bg-accent);
    color: var(--text-accent);
}

.options-menu a.delete-option {
    color: #ff6b6b;
}

.options-menu a.delete-option:hover {
    background-color: rgba(255, 107, 107, 0.1);
    color: #ff6b6b;
}

.notification-filters {
  display: flex;
  gap: 0.5rem;
}

.filter-btn {
  padding: 0.5rem 1rem;
  background: transparent;
  border: 1px solid var(--border-color);
  border-radius: 12px;
  color: var(--text-muted);
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
}

.filter-btn:hover {
  background: var(--bg-accent);
}

.filter-btn.active {
  background: var(--text-accent);
  border-color: var(--text-accent);
  color: var(--text-inverse);
  box-shadow: 0 4px 12px var(--shadow-medium);
}

.notification-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.notification-icon {
  color: var(--text-accent);
  background: var(--bg-accent);
  padding: 8px;
  border-radius: 12px;
}

.notification-indicators {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.priority-dot {
  width: 8px;
  height: 8px;
  background: linear-gradient(135deg, #ff6b6b 0%, #ffa500 100%);
  border-radius: 50%;
  box-shadow: 0 0 8px rgba(255, 107, 107, 0.3);
}

.unread-label {
  background: #3D8D7A;
  color: var(--text-inverse);
  font-size: 0.75rem;
  font-weight: 600;
  padding: 0.25rem 0.75rem;
  border-radius: 8px;
}

.notif-title {
  font-weight: 700;
  color: #3D8D7A;
  margin: 0 0 0.5rem 0;
  font-size: 1.1rem;
}

.notif-body {
  font-size: 0.95rem;
  color: #555;
  margin: 0;
  line-height: 1.5;
}

.notification-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid rgba(61, 141, 122, 0.05);
}

.notif-timestamp {
  font-size: 0.8rem;
  color: #999;
  font-weight: 500;
}

.dismiss-btn {
  width: 28px;
  height: 28px;
  background: rgba(255, 107, 107, 0.1);
  border: none;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #ff6b6b;
  cursor: pointer;
  transition: all 0.2s ease;
  opacity: 0.7;
}

.dismiss-btn:hover {
  background: rgba(255, 107, 107, 0.2);
  opacity: 1;
  transform: scale(1.1);
}

/* Modal Styles */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  backdrop-filter: blur(8px);
}

.modal-content {
  background: var(--bg-card);
  border-radius: 16px;
  width: 95%;
  max-width: 500px;
  height: 85vh;
  display: flex;
  flex-direction: column;
  box-shadow: 0 8px 32px var(--shadow-color);
  overflow: hidden;
  border: 2px solid var(--border-color);
}

.modal-header {
  padding: 1rem 1.25rem;
  background: var(--text-accent);
  color: white;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid var(--border-color);
}

.header-info {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  flex: 1;
}

.teacher-avatar-chat {
  width: 40px;
  height: 40px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 600;
  font-size: 1.1rem;
  flex-shrink: 0;
  border: 1px solid rgba(255, 255, 255, 0.3);
}

.header-details {
  flex: 1;
  min-width: 0;
}

.modal-title {
  font-size: 1rem;
  font-weight: 600;
  margin: 0 0 0.2rem 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.subject-info {
  font-size: 0.875rem;
  opacity: 0.9;
  font-weight: 400;
}

.close-btn {
  background: rgba(255, 255, 255, 0.1);
  border: none;
  color: white;
  cursor: pointer;
  padding: 0.5rem;
  border-radius: 8px;
  transition: background-color 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}

.close-btn:hover {
  background: rgba(255, 255, 255, 0.2);
}

.header-info {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.modal-header .teacher-avatar {
  background: rgba(255, 255, 255, 0.3);
  width: 48px;
  height: 48px;
  box-shadow: none;
}

.modal-title {
  font-size: 1.5rem;
  font-weight: 700;
  margin: 0;
}

.modal-body {
  flex: 1;
  padding: 1rem;
  overflow-y: auto;
  background: var(--bg-accent);
}

.messages-container {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  padding: 0.5rem;
}

.message-bubble {
  max-width: 75%;
  padding: 0.75rem 1rem;
  border-radius: 16px;
  line-height: 1.4;
  position: relative;
  font-size: 0.9rem;
  box-shadow: 0 1px 4px var(--shadow-color);
}

.message-bubble.received {
  background: var(--bg-card);
  color: var(--text-primary);
  align-self: flex-start;
  border: 1px solid var(--border-color);
  border-bottom-left-radius: 4px;
  box-shadow: 0 1px 4px var(--shadow-color);
}

.message-bubble.sent {
  background: var(--text-accent);
  color: white;
  align-self: flex-end;
  border-bottom-right-radius: 4px;
  box-shadow: 0 2px 8px var(--shadow-color);
}

.message-text {
  margin: 0;
  font-weight: 400;
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
  padding: 1rem;
  border-top: 1px solid var(--border-color);
  background: var(--bg-card);
}

.message-input-area {
  display: flex;
  gap: 0.5rem;
  align-items: center;
}

.attach-btn {
  background: transparent;
  border: 1px solid var(--border-color);
  color: var(--text-accent);
  padding: 0.6rem;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  outline: none;
}

.attach-btn:hover {
  background: var(--bg-accent);
  color: var(--text-accent);
  border-color: var(--text-accent);
  box-shadow: 0 0 0 2px var(--shadow-color);
}

.attach-btn:focus {
  background: var(--bg-accent);
  color: var(--text-accent);
  outline: 2px solid var(--text-accent);
  box-shadow: 0 0 0 3px var(--shadow-color);
}

.message-input {
  flex: 1;
  padding: 0.75rem 1rem;
  border: 1px solid var(--border-color);
  border-radius: 12px;
  font-size: 0.9rem;
  background: var(--bg-card);
  color: var(--text-primary);
  font-family: 'Inter', sans-serif;
  transition: border-color 0.2s ease;
}

.message-input:focus {
  outline: none;
  border-color: var(--text-accent);
  box-shadow: 0 0 0 3px var(--shadow-color);
}

.send-btn {
  background: var(--text-accent);
  color: white;
  border: none;
  width: 40px;
  height: 40px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
}

.send-btn:hover {
  background: #2f6b5c;
  transform: scale(1.05);
  box-shadow: 0 4px 12px var(--shadow-color);
}

.send-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  transform: none;
}

/* Add new styles for the updated layout */
.subject-filter {
  padding: 0.75rem 1rem;
  border: 1px solid var(--border-color);
  border-radius: 12px;
  background: var(--bg-card);
  color: var(--text-primary);
  font-size: 0.9rem;
  min-width: 150px;
}

.teachers-by-subject {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.subject-group {
  background: var(--bg-accent);
  border-radius: 12px;
  padding: 1.2rem;
  border: 1px solid var(--border-color);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}

.subject-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 0.9rem;
  padding-bottom: 0.8rem;
  border-bottom: 1px solid var(--border-color);
}

.subject-name {
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--text-accent);
  margin: 0;
  letter-spacing: -0.02em;
}

.subject-code {
  background: #64748b;
  color: white;
  padding: 0.25rem 0.7rem;
  border-radius: 8px;
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.02em;
}

.teachers-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.teacher-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 1.2rem;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}

.teacher-item:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  border-color: #cbd5e1;
}

.teacher-item.has-unread {
  border-left: 4px solid var(--text-accent);
  background: var(--bg-unread);
}

.teacher-info {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex: 1;
}

.teacher-avatar {
  width: 42px;
  height: 42px;
  background: linear-gradient(135deg, #e2e8f0 0%, #cbd5e1 100%);
  color: #475569;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 0.95rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  border: 2px solid #f8fafc;
}

.dark .teacher-avatar {
  background: linear-gradient(135deg, #374151 0%, #4b5563 100%);
  color: #e5e7eb;
  border: 2px solid #1f2937;
}

.teacher-details {
  flex: 1;
  min-width: 0;
}

.teacher-name {
  font-weight: 600;
  color: var(--text-accent);
  margin: 0 0 0.1rem 0;
  font-size: 0.95rem;
  letter-spacing: -0.01em;
}

.message-status {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 0.3rem;
}

.unread-status {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.15rem;
}

.unread-badge {
  background: var(--text-accent);
  color: var(--text-inverse);
  border-radius: 50%;
  width: 20px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.7rem;
  font-weight: 600;
}

.unread-text {
  font-size: 0.75rem;
  color: var(--text-accent);
  font-weight: 600;
  text-align: center;
  white-space: nowrap;
}

.last-time {
  font-size: 0.85rem;
  color: var(--text-muted);
}

.chat-icon {
  color: var(--text-accent);
  opacity: 0.7;
  transition: opacity 0.2s ease;
}

.teacher-item:hover .chat-icon {
  opacity: 1;
}

.notification-source {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.source-info {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.source-name {
  font-weight: 600;
  color: var(--text-accent);
  font-size: 0.9rem;
}

.source-subject {
  font-size: 0.8rem;
  color: var(--text-muted);
}

.notification-item.class-announcement {
  border-left: 4px solid #4A9B8E;
  background: linear-gradient(135deg, rgba(74, 155, 142, 0.05) 0%, var(--bg-card) 100%);
}

.header-details {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.subject-info {
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.8);
  font-weight: 500;
}

/* Archive and Options Styling */
.options-wrapper {
  position: relative;
}

.options-menu {
  position: absolute;
  top: 100%;
  right: 0;
  background-color: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  box-shadow: 0 8px 24px var(--shadow-medium);
  padding: 0.5rem;
  display: flex;
  flex-direction: column;
  min-width: 180px;
  z-index: 9999;
  margin-top: 8px;
}

.options-menu a {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem 1rem;
  color: var(--text-secondary);
  text-decoration: none;
  border-radius: 8px;
  transition: background-color 0.2s ease, color 0.2s ease;
  font-size: 0.9rem;
}

.options-menu a:hover {
  background-color: var(--bg-accent);
  color: var(--text-accent);
}

.options-menu a.delete-option {
  color: #ff6b6b;
}

.options-menu a.delete-option:hover {
  background-color: rgba(255, 107, 107, 0.1);
  color: #ff6b6b;
}

/* File Upload and Attachments */
.file-preview {
  padding: 1rem;
  background: var(--bg-accent);
  border-top: 1px solid var(--border-color);
}

.preview-content {
  display: flex;
  align-items: center;
  gap: 1rem;
  background: var(--bg-card);
  padding: 0.75rem;
  border-radius: 12px;
  position: relative;
}

.preview-image {
  max-width: 100px;
  max-height: 100px;
  border-radius: 8px;
  object-fit: cover;
}

.preview-file {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: var(--text-secondary);
  flex: 1;
}

.preview-file svg {
  color: var(--text-accent);
}

.remove-file-btn {
  position: absolute;
  top: 0.5rem;
  right: 0.5rem;
  background: rgba(255, 107, 107, 0.9);
  color: white;
  border: none;
  border-radius: 50%;
  width: 28px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
}

.remove-file-btn:hover {
  background: #ff5252;
  transform: scale(1.1);
}

.attach-btn {
  background: var(--bg-accent);
  color: var(--text-accent);
  border: 1px solid var(--border-color);
  width: 44px;
  height: 44px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
}

.attach-btn:hover {
  background: var(--bg-accent-hover);
  transform: scale(1.05);
}

.message-attachments {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-bottom: 0.5rem;
}

.attachment {
  display: inline-block;
}

.attachment-image {
  max-width: 250px;
  max-height: 250px;
  border-radius: 12px;
  cursor: pointer;
  transition: transform 0.2s ease;
}

.attachment-image:hover {
  transform: scale(1.02);
}

.attachment-file {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1rem;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.2s ease;
  color: inherit;
}

.message-bubble.sent .attachment-file {
  background: rgba(255, 255, 255, 0.2);
}

.message-bubble.received .attachment-file {
  background: rgba(0, 0, 0, 0.05);
}

.attachment-file:hover {
  background: rgba(255, 255, 255, 0.25);
  transform: translateY(-1px);
}

.attachment-file span {
  font-size: 0.9rem;
}

/* Message Status and Read Receipts */
.message-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.5rem;
  margin-top: 0.5rem;
}

.message-status {
  display: flex;
  align-items: center;
  gap: 0.25rem;
}

.message-status svg {
  width: 14px;
  height: 14px;
}

.read-time {
  font-size: 0.7rem;
  margin-left: 0.25rem;
}

.message-bubble.sent .message-status {
  color: rgba(255, 255, 255, 0.7);
}

.message-bubble.received .message-status {
  color: rgba(0, 0, 0, 0.4);
}

/* Broadcast Groups */
.broadcast-groups {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.broadcast-group {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 20px;
  padding: 1.5rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.broadcast-group:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px var(--shadow-medium);
  border-color: var(--border-color-hover);
}

.broadcast-group-header {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.broadcast-icon {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, #4A9B8E 0%, #3D8D7A 100%);
  color: white;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.broadcast-icon-large {
  width: 56px;
  height: 56px;
  background: linear-gradient(135deg, #4A9B8E 0%, #3D8D7A 100%);
  color: white;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.broadcast-info {
  flex: 1;
}

.broadcast-title {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--text-accent);
  margin: 0 0 0.25rem 0;
}

.broadcast-teacher {
  font-size: 0.9rem;
  color: var(--text-secondary);
  margin: 0;
}

.broadcast-count {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.count-badge {
  background: var(--text-accent);
  color: var(--text-inverse);
  font-weight: 600;
  font-size: 0.85rem;
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  min-width: 28px;
  text-align: center;
}

.unread-indicator {
  width: 10px;
  height: 10px;
  background: #ff6b6b;
  border-radius: 50%;
  box-shadow: 0 0 8px rgba(255, 107, 107, 0.5);
}

/* Broadcast List Modal */
.broadcast-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.broadcast-item {
  background: var(--bg-accent);
  border: 1px solid var(--border-color);
  border-radius: 16px;
  padding: 1.5rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.broadcast-item:hover {
  background: var(--bg-card);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px var(--shadow-light);
}

.broadcast-item.unread {
  background: var(--bg-unread);
  border-left: 4px solid var(--text-accent);
}

.broadcast-item-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.75rem;
}

.broadcast-item-title {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--text-accent);
  margin: 0;
}

.broadcast-item-body {
  font-size: 0.95rem;
  color: var(--text-secondary);
  line-height: 1.5;
  margin: 0 0 0.75rem 0;
}

.broadcast-item-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 0.75rem;
  border-top: 1px solid var(--border-color);
}

.broadcast-item-time {
  font-size: 0.85rem;
  color: var(--text-muted);
}

.attachment-indicator {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.8rem;
  color: var(--text-accent);
  background: rgba(61, 141, 122, 0.1);
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  font-weight: 500;
}

/* Teacher Email Styling */
.teacher-email {
  font-size: 0.8rem;
  color: var(--text-muted);
  margin: 0;
  opacity: 0.8;
}

/* No Messages State */
.no-messages {
  text-align: center;
  padding: 3rem 2rem;
  color: var(--text-muted);
}

.no-messages p {
  font-size: 1rem;
  margin: 0;
}

/* ================================
   ANNOUNCEMENT DETAIL MODAL
   ================================ */

.announcement-detail-modal {
  max-width: 800px;
  width: 95%;
  height: 85vh;
}

.announcement-detail_body {
  padding: 2rem;
}

.announcement-content {
  max-width: 100%;
  margin: 0 auto;
}

.announcement-header {
  margin-bottom: 2rem;
  padding-bottom: 1.5rem;
  border-bottom: 2px solid var(--border-color);
}

.announcement-title {
  font-size: 1.8rem;
  font-weight: 700;
  color: var(--text-accent);
  margin: 0 0 1rem 0;
  line-height: 1.3;
}

.announcement-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1rem;
}

.teacher-info {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.teacher-name {
  font-size: 1rem;
  font-weight: 600;
  color: var(--text-secondary);
}

.announcement-date {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.9rem;
  color: var(--text-muted);
}

.announcement-body {
  margin-bottom: 2rem;
}

.announcement-text {
  font-size: 1.1rem;
  line-height: 1.6;
  color: var(--text-primary);
  margin: 0;
  white-space: pre-wrap;
}

.announcement-attachments {
  margin-top: 2rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--border-color);
}

.attachments-title {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 1.5rem;
  color: var(--text-accent);
  font-size: 1.2rem;
  font-weight: 600;
}

.attachments-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}

.attachment-item {
  border: 1px solid var(--border-color);
  border-radius: 12px;
  overflow: hidden;
  transition: all 0.2s ease;
  background: var(--bg-card);
}

.attachment-item:hover {
  border-color: var(--border-color-hover);
  box-shadow: 0 4px 12px var(--shadow-light);
  transform: translateY(-2px);
}

.attachment-image-container {
  position: relative;
  overflow: hidden;
}

.attachment-image-large {
  width: 100%;
  height: 200px;
  object-fit: cover;
  cursor: pointer;
  transition: transform 0.2s ease;
}

.attachment-image-large:hover {
  transform: scale(1.05);
}

.attachment-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(transparent, rgba(0, 0, 0, 0.7));
  padding: 1rem;
  display: flex;
  gap: 0.5rem;
  opacity: 0;
  transition: opacity 0.2s ease;
}

.attachment-image-container:hover .attachment-overlay {
  opacity: 1;
}

.view-btn,
.download-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background: rgba(255, 255, 255, 0.9);
  color: var(--text-accent);
  border: none;
  border-radius: 8px;
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.view-btn:hover,
.download-btn:hover {
  background: white;
  transform: translateY(-1px);
}

.attachment-file-large {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1.5rem;
  cursor: pointer;
  transition: all 0.2s ease;
  background: var(--bg-card);
}

.attachment-file-large:hover {
  background: var(--bg-accent);
}

.file-icon {
  width: 56px;
  height: 56px;
  background: var(--bg-accent);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--text-accent);
  flex-shrink: 0;
}

.file-info {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  min-width: 0;
}

.file-name {
  font-weight: 600;
  color: var(--text-primary);
  word-break: break-word;
  font-size: 1rem;
}

.file-size {
  font-size: 0.85rem;
  color: var(--text-muted);
}

.download-file-btn {
  background: var(--text-accent);
  color: white;
  border: none;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
  flex-shrink: 0;
}

.download-file-btn:hover {
  background: #2f7063;
  transform: scale(1.1);
}

.announcement-icon {
  width: 56px;
  height: 56px;
  background: linear-gradient(135deg, #4A9B8E 0%, #3D8D7A 100%);
  color: white;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.close-detail-btn {
  background: var(--text-accent);
  color: white;
  border: none;
  padding: 0.75rem 2rem;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.close-detail-btn:hover {
  background: #2f7063;
  transform: translateY(-1px);
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .announcement-detail-modal {
    width: 98%;
    height: 90vh;
  }
  
  .announcement-detail_body {
    padding: 1rem;
  }
  
  .attachments-grid {
    grid-template-columns: 1fr;
  }
  
  .announcement-meta {
    flex-direction: column;
    align-items: flex-start;
  }
}
</style>