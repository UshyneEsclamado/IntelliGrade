
<template>
  <div class="messages-container">
    <!-- Global Loading Overlay -->
    <div v-if="isInitialLoading" class="loading-overlay">
      <div class="loading-spinner">
        <div class="spinner"></div>
        <p>Loading your messages...</p>
      </div>
    </div>

    <!-- Header Section (Uniform Card Style) -->
    <div class="section-header-card minimal-header-card">
      <div class="section-header-left">
        <div class="section-header-icon minimal-header-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
          </svg>
        </div>
        <div>
          <div class="section-header-title minimal-header-title">Messages</div>
          <div class="section-header-sub minimal-header-sub">Chat with your enrolled teachers and view announcements</div>
        </div>
      </div>
    </div>

    <!-- Filter and Search -->
    <div class="controls-section">
      <div class="search-box">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
          <path d="M9.5,3A6.5,6.5 0 0,1 16,9.5C16,11.11 15.41,12.59 14.44,13.73L14.71,14H15.5L20.5,19L19,20.5L14,15.5V14.71L13.73,14.44C12.59,15.41 11.11,16 9.5,16A6.5,6.5 0 0,1 3,9.5A6.5,6.5 0 0,1 9.5,3M9.5,5C7,5 5,7 5,9.5C5,12 7,14 9.5,14C12,14 14,12 14,9.5C14,7 12,5 9.5,5Z" />
        </svg>
        <input 
          type="text" 
          v-model="searchQuery" 
          placeholder="Search teachers or subjects..."
          class="search-input"
        />
      </div>
      <div class="filter-tabs">
        <button 
          :class="['filter-tab', { 'active': currentTab === 'teachers' }]"
          @click="currentTab = 'teachers'; showArchive = false"
        >
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
            <circle cx="12" cy="7" r="4"/>
          </svg>
          My Teachers
        </button>
        <button 
          :class="['filter-tab', { 'active': currentTab === 'archive' }]"
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
          :class="['filter-tab', { 'active': currentTab === 'notifications' }]"
          @click="currentTab = 'notifications'; showArchive = false"
        >
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/>
            <path d="M13.73 21a2 2 0 0 1-3.46 0"/>
          </svg>
          Notifications
          <span v-if="unreadNotificationsCount > 0" class="notification-badge">{{ unreadNotificationsCount }}</span>
        </button>
      </div>
    </div>

    <!-- Main Content Area -->
    <div class="content-area">
      <!-- Teachers Tab -->
      <div v-if="currentTab === 'teachers' || currentTab === 'archive'" class="tab-content">

        <!-- Loading State -->
        <div v-if="isLoadingTeachers" class="loading-state">
          <div class="loading-spinner-small">
            <div class="spinner"></div>
          </div>
          <p>Loading teachers...</p>
        </div>

        <!-- Empty state when no deleted conversations -->
        <div v-else-if="filteredTeachers.length === 0 && !hasDeletedConversations" class="empty-state">
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

        <!-- Teachers Grid -->
        <div v-else class="teachers-grid">
          <div v-for="subject in groupedTeachers" :key="(subject as any).id" class="subject-section">
            <div class="subject-section-header">
              <h3 class="subject-section-name">{{ (subject as any).name }}</h3>
              <span class="subject-section-code">{{ (subject as any).code }}</span>
            </div>
            
            <div class="teachers-cards">
              <div 
                v-for="teacher in (subject as any).teachers" 
                :key="`${teacher.id}-${teacher.section_id}`"
                :class="['teacher-card', { 'has-unread': teacher.unread_count > 0 }]"
                @click="startChatWithTeacher(teacher)"
              >
                <div class="teacher-card-header">
                  <div class="teacher-card-left">
                    <div class="teacher-avatar">
                      <span>{{ teacher.teacher_name?.[0] || 'T' }}</span>
                      <span v-if="teacherPresence[teacher.id]?.is_online" class="online-indicator" title="Online now"></span>
                    </div>
                    <div class="teacher-info">
                      <h4 class="teacher-name">{{ teacher.teacher_name }}</h4>
                      <p class="teacher-email">{{ teacher.email }}</p>
                      <p class="presence-status">{{ getPresenceStatus(teacher.id) }}</p>
                    </div>
                  </div>
                  <div class="teacher-card-right">
                    <button 
                      class="options-btn" 
                      @click.stop="toggleTeacherOptions(`${teacher.id}-${teacher.section_id}`)"
                      :title="'More options'"
                    >
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M12,16A2,2 0 0,1 14,18A2,2 0 0,1 12,20A2,2 0 0,1 10,18A2,2 0 0,1 12,16M12,10A2,2 0 0,1 14,12A2,2 0 0,1 12,14A2,2 0 0,1 10,12A2,2 0 0,1 12,10M12,4A2,2 0 0,1 14,6A2,2 0 0,1 12,8A2,2 0 0,1 10,6A2,2 0 0,1 12,4Z" />
                      </svg>
                    </button>
                    <div v-if="activeTeacherOptionsId === `${teacher.id}-${teacher.section_id}`" class="options-dropdown" @click.stop>
                      <button @click.stop="archiveConversation(teacher); activeTeacherOptionsId = null" class="dropdown-item">
                        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                          <polyline points="21 8 21 21 3 21 3 8"></polyline>
                          <rect x="1" y="3" width="22" height="5"></rect>
                          <line x1="10" y1="12" x2="14" y2="12"></line>
                        </svg>
                        {{ teacher.archived ? 'Unarchive' : 'Archive' }}
                      </button>
                      <button @click.stop="deleteConversation(teacher); activeTeacherOptionsId = null" class="dropdown-item delete-option">
                        <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                          <polyline points="3 6 5 6 21 6"></polyline>
                          <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
                        </svg>
                        Delete
                      </button>
                    </div>
                  </div>
                </div>
                
                <div class="teacher-card-body">
                  <p class="last-message">{{ teacher.last_message || 'Start a conversation' }}</p>
                  <span v-if="teacher.last_message_time" class="last-message-time">{{ formatTime(teacher.last_message_time) }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Notifications Tab -->
      <div v-else-if="currentTab === 'notifications'" class="tab-content">
        <div class="notifications-actions">
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
          <button class="action-btn" @click="clearNotifications" v-if="unreadNotificationsCount > 0">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="20,6 9,17 4,12"/>
            </svg>
            Mark all read
          </button>
        </div>
        
        <!-- Loading State for Notifications -->
        <div v-if="isLoadingNotifications" class="loading-state">
          <div class="loading-spinner-small">
            <div class="spinner"></div>
          </div>
          <p>Loading notifications...</p>
        </div>
        
        <div v-else-if="Object.keys(groupedBroadcasts).length === 0" class="empty-state">
          <div class="empty-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
              <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/>
              <path d="M13.73 21a2 2 0 0 1-3.46 0"/>
            </svg>
          </div>
          <p>No announcements found</p>
          <span class="empty-subtext">Class announcements and notifications will appear here.</span>
        </div>
        
        <div v-else class="notifications-grid">
          <div 
            v-for="(group, key) in groupedBroadcasts" 
            :key="key" 
            class="notification-card"
            @click="openBroadcastGroup(group)"
          >
            <div class="notification-card-header">
              <div class="notification-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
                </svg>
              </div>
              <div class="notification-card-right">
                <span class="notification-count">{{ (group as any).announcements.length }}</span>
                <span v-if="(group as any).announcements.some((a: any) => !a.is_read)" class="unread-dot"></span>
              </div>
            </div>
            <div class="notification-card-body">
              <h3 class="notification-title">{{ (group as any).section }}: {{ (group as any).subject }}</h3>
              <p class="notification-teacher">Teacher: {{ (group as any).teacher }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Chat Modal -->
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
          <!-- Loading Messages -->
          <div v-if="isLoadingMessages" class="loading-messages">
            <div class="loading-spinner-small">
              <div class="spinner"></div>
            </div>
            <p>Loading conversation...</p>
          </div>

          <!-- Messages Container -->
          <div v-else class="messages-container" ref="messagesContainer">
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
            <div v-if="currentMessages.length === 0 && !isLoadingMessages" class="no-messages">
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
            <button class="attach-btn" @click="($refs.fileInput as HTMLInputElement)?.click()" :disabled="isSendingMessage">
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
              :disabled="isSendingMessage"
            />
            <button class="send-btn" @click="sendMessage" :disabled="(!newMessage.trim() && !selectedFile) || isSendingMessage">
              <svg v-if="!isSendingMessage" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <line x1="22" y1="2" x2="11" y2="13"></line>
                <polygon points="22 2 15.46 22 11 13 2 9.54 22 2"></polygon>
              </svg>
              <div v-else class="button-spinner"></div>
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

<script setup lang="ts">
defineOptions({ name: 'StudentMessages' })
import { ref, computed, onMounted, onUnmounted, nextTick, watch } from 'vue'
import { useRoute } from 'vue-router'
import { supabase } from '@/supabase.js'

// Watch for route changes
const route = useRoute()
watch(() => route.fullPath, () => {
  loadEnrolledSubjectsAndTeachers()
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

// Loading states
const isInitialLoading = ref(true)
const isLoadingTeachers = ref(false)
const isLoadingNotifications = ref(false)
const isLoadingMessages = ref(false)
const isSendingMessage = ref(false)

const activeTeacherOptionsId = ref(null)
const showArchive = ref(false)
const selectedFile = ref(null)
const previewFile = ref(null)
const deletedConversationKeys = ref(new Set())

// Real-time subscriptions
let messageChannel = null
let presenceChannel = null

// Data
const enrolledSubjects = ref([])
const enrolledTeachers = ref([])
const notifications = ref([])
const currentMessages = ref([])
const currentUser = ref(null)
const currentStudentId = ref(null)
const teacherPresence = ref({})

// ================================
// COMPUTED PROPERTIES
// ================================

const unreadNotificationsCount = computed(() => {
  return notifications.value.filter(n => !n.is_read).length
})

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

// ================================
// FILE UPLOAD FUNCTIONS
// ================================

const uploadFileToStorage = async (file, folder = 'message-attachments') => {
  try {
    const fileExt = file.name.split('.').pop()
    const fileName = `${Date.now()}-${Math.random().toString(36).substring(7)}.${fileExt}`
    const filePath = `${folder}/${fileName}`
    
    const { error } = await supabase.storage
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
// HANDLER METHODS
// ================================

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
    }
  }
  
  isBroadcastModalOpen.value = true
}

const closeBroadcastModal = () => {
  isBroadcastModalOpen.value = false
  selectedBroadcastGroup.value = null
}

const openAnnouncementDetail = async (announcement) => {
  selectedAnnouncement.value = announcement
  await loadAnnouncementAttachments(announcement.notification_id)
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
  } catch (err) {
    console.error('Error loading announcement attachments:', err)
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
    
    announcement.is_read = true
    
    const notificationIndex = notifications.value.findIndex(n => n.notification_id === announcement.notification_id)
    if (notificationIndex !== -1) {
      notifications.value[notificationIndex].is_read = true
    }
    
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

// ================================
// AUTHENTICATION METHODS
// ================================

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

// ================================
// DATA LOADING METHODS
// ================================

const loadEnrolledSubjectsAndTeachers = async () => {
  try {
    if (!currentStudentId.value) {
      console.error('No student ID available')
      return
    }
    
    isLoadingTeachers.value = true
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
        .eq('message_type', 'direct')
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
    isLoadingTeachers.value = false
  }
}

const loadNotifications = async () => {
  try {
    if (!currentStudentId.value) return
    
    isLoadingNotifications.value = true
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
    
    const messageIds = messages.map(m => m.id)
    const { data: attachments } = await supabase
      .from('message_attachments')
      .select('*')
      .in('message_id', messageIds)
    
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
  } finally {
    isLoadingNotifications.value = false
  }
}

// ================================
// CHAT METHODS
// ================================

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
    
    isLoadingMessages.value = true
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
      isLoadingMessages.value = false
      return
    }
    
    const messageIds = messages.map(m => m.id)
    const { data: attachments } = await supabase
      .from('message_attachments')
      .select('*')
      .in('message_id', messageIds)
    
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
  } finally {
    isLoadingMessages.value = false
  }
}

const sendMessage = async () => {
  if ((!newMessage.value.trim() && !selectedFile.value) || !activeTeacher.value || !currentStudentId.value || isSendingMessage.value) return
  
  const messageText = newMessage.value.trim()
  const fileToUpload = selectedFile.value
  
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
    isSendingMessage.value = true
    
    let uploadedAttachment = null
    if (fileToUpload) {
      uploadedAttachment = await uploadFileToStorage(fileToUpload)
    }
    
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
    
    if (uploadedAttachment) {
      await saveMessageAttachments(newMsg.id, [uploadedAttachment])
    }
    
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
    isSendingMessage.value = false
  }
}

const markMessagesAsRead = async (teacherId, sectionId) => {
  try {
    if (!currentStudentId.value) return
    
    console.log('Marking messages as read:', { teacherId, sectionId })
    
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
    
    currentMessages.value.forEach(m => {
      if (m.sender_id === teacherId && !m.is_read) {
        m.is_read = true
        m.read_at = new Date().toISOString()
      }
    })
    
    const teacherIndex = enrolledTeachers.value.findIndex(t => 
      t.id === teacherId && t.section_id === sectionId
    )
    if (teacherIndex !== -1) {
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

// ================================
// REAL-TIME METHODS
// ================================

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
          
          await loadEnrolledSubjectsAndTeachers()
          
          if (isModalOpen.value && 
              activeTeacher.value && 
              newMessageData.section_id === activeTeacher.value.section_id &&
              newMessageData.sender_id === activeTeacher.value.id) {
            
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

// ================================
// UTILITY METHODS
// ================================

const scrollToBottom = () => {
  if (messagesContainer.value) {
    messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
  }
}

const formatTime = (dateString) => {
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

// ================================
// PRESENCE STATUS METHODS
// ================================

const getPresenceStatus = (teacherId) => {
  const presence = teacherPresence.value[teacherId]
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
  if (!currentStudentId.value) return
  
  const teacherIds = [...new Set(enrolledTeachers.value.map(t => t.id))]
  
  if (teacherIds.length === 0) return
  
  const { data: presenceData, error } = await supabase
    .from('user_presence')
    .select('*')
    .in('user_id', teacherIds)
  
  if (error) {
    console.error('Error fetching teacher presence:', error)
    return
  }
  
  if (presenceData) {
    presenceData.forEach(p => {
      teacherPresence.value[p.user_id] = {
        is_online: p.is_online,
        last_seen: p.last_seen
      }
    })
  }
  
  presenceChannel = supabase
    .channel('teacher-presence-tracking')
    .on(
      'postgres_changes',
      {
        event: '*',
        schema: 'public',
        table: 'user_presence',
        filter: `user_id=in.(${teacherIds.join(',')})`
      },
      (payload) => {
        console.log('Presence update received:', payload)
        
        const userId = (payload.new as { user_id?: string })?.user_id || (payload.old as { user_id?: string })?.user_id
        
        if (payload.eventType === 'DELETE') {
          if (teacherPresence.value[userId]) {
            teacherPresence.value[userId].is_online = false
          }
        } else if (payload.new) {
          teacherPresence.value[userId] = {
            is_online: payload.new.is_online,
            last_seen: payload.new.last_seen
          }
        }
      }
    )
    .subscribe()
  
  console.log('Presence tracking setup complete for', teacherIds.length, 'teachers')
}

const updateStudentPresence = async (isOnline) => {
  if (!currentUser.value) return
  
  try {
    const { error } = await supabase
      .from('user_presence')
      .upsert({
        user_id: currentUser.value.id,
        is_online: isOnline,
        last_seen: new Date().toISOString()
      }, {
        onConflict: 'user_id'
      })
    
    if (error) throw error
  } catch (error) {
    console.error('Error updating student presence:', error)
  }
}

// ================================
// LIFECYCLE
// ================================

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
    
    isInitialLoading.value = false
    
    setupRealTimeSubscriptions()
    await setupPresenceTracking()
    await updateStudentPresence(true)
  } else {
    console.error('Authentication failed or user is not a student')
    isInitialLoading.value = false
  }
})

onUnmounted(() => {
  cleanupRealTimeSubscriptions()
  if (presenceChannel) {
    presenceChannel.unsubscribe()
    presenceChannel = null
  }
  updateStudentPresence(false)
  document.removeEventListener('click', handleClickOutside)
})
</script>


<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

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

/* Header Section (Uniform Card Style) */
.section-header-card {
  background: white;
  border-radius: 16px;
  padding: 1.5rem 2.5rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
  border: 2px solid #A3D1C6;
  width: 100%;
  max-width: none;
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
  border-color: #A3D1C6;
  box-shadow: 0 0 0 3px rgba(163, 209, 198, 0.1);
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


  .filter-tabs {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 0.5rem;
    width: 100%;
    flex: 1 1 100%;
    overflow-x: auto;
    padding-bottom: 0.25rem;
    flex-wrap: nowrap;
  background: none;
  }

  .filter-tab {
    flex: 1 1 0;
    min-width: 0;
    padding: 0.75rem 0.5rem;
    font-size: 0.85rem;
    border-radius: 10px;
    white-space: nowrap;
    height: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-color: #20c997;
  }

/* Content Area */
.content-area {
  min-height: 400px;
}

.tab-content {
  width: 100%;
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

.empty-icon {
  margin-bottom: 1.5rem;
  color: #A3D1C6;
}
.dark .empty-icon {
  color: #20c997;
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

.deleted-state {
  text-align: center;
  padding: 4rem 2rem;
}

.deleted-icon {
  margin-bottom: 1.5rem;
  color: #A3D1C6;
}
.dark .deleted-icon {
  color: #20c997;
}

.show-teachers-btn {
  margin-top: 1.5rem;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.875rem 1.5rem;
  background: #A3D1C6;
  color: white;
  border: none;
  border-radius: 10px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}
.dark .show-teachers-btn {
  background: #20c997;
}

.show-teachers-btn:hover {
  background: #87C5B8;
  transform: translateY(-1px);
}
.dark .show-teachers-btn:hover {
  background: #17a085;
}

/* Teachers Grid */
.teachers-grid {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.subject-section {
  background: white;
  border-radius: 16px;
  padding: 1.5rem;
  border: 2px solid #e9ecef;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}
.dark .subject-section {
  background: #23272b;
  border-color: #495057;
}

.subject-section-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1.5rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid #e9ecef;
}
.dark .subject-section-header {
  border-bottom-color: #495057;
}

.subject-section-name {
  font-size: 1.25rem;
  font-weight: 700;
  color: #2c3e50;
  margin: 0;
}
.dark .subject-section-name {
  color: #ffffff;
}

.subject-section-code {
  font-size: 0.875rem;
  font-weight: 600;
  color: #A3D1C6;
  background: rgba(163, 209, 198, 0.1);
  padding: 0.25rem 0.75rem;
  border-radius: 6px;
}
.dark .subject-section-code {
  color: #20c997;
  background: rgba(32, 201, 151, 0.1);
}

.teachers-cards {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.teacher-card {
  background: white;
  border: 2px solid #e9ecef;
  border-radius: 12px;
  padding: 1.25rem;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  transform: translateY(0);
}
.dark .teacher-card {
  background: #2c3135;
  border-color: #495057;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}

.teacher-card:hover {
  border-color: #A3D1C6;
  transform: translateY(-4px);
  box-shadow: 0 8px 25px rgba(163, 209, 198, 0.25);
}
.dark .teacher-card:hover {
  border-color: #20c997;
  box-shadow: 0 8px 25px rgba(32, 201, 151, 0.25);
}

.teacher-card.has-unread {
  border-color: #A3D1C6;
  background: rgba(163, 209, 198, 0.05);
}
.dark .teacher-card.has-unread {
  border-color: #20c997;
  background: rgba(32, 201, 151, 0.05);
}

.teacher-card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 0.75rem;
}

.teacher-card-left {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  flex: 1;
}

.teacher-avatar {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, #A3D1C6 0%, #87C5B8 100%);
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 600;
  font-size: 1rem;
  flex-shrink: 0;
  position: relative;
}
.dark .teacher-avatar {
  background: linear-gradient(135deg, #20c997 0%, #17a085 100%);
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
  border-color: #23272b;
}

@keyframes pulse-online {
  0%, 100% {
    box-shadow: 0 0 0 2px rgba(40, 167, 69, 0.3);
  }
  50% {
    box-shadow: 0 0 0 4px rgba(40, 167, 69, 0.1);
  }
}

.teacher-info {
  flex: 1;
  min-width: 0;
}

.teacher-name {
  font-size: 1rem;
  font-weight: 600;
  color: #2c3e50;
  margin: 0 0 0.25rem 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.dark .teacher-name {
  color: #ffffff;
}

.teacher-email {
  font-size: 0.8rem;
  color: #6c757d;
  margin: 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.dark .teacher-email {
  color: #adb5bd;
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

.teacher-card-right {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex-shrink: 0;
}

.unread-badge {
  background: #dc3545;
  color: white;
  font-size: 0.75rem;
  font-weight: 700;
  padding: 0.25rem 0.5rem;
  border-radius: 6px;
  min-width: 20px;
  text-align: center;
}

.unread-indicator {
  position: relative;
}

.unread-count {
  background: #dc3545;
  color: white;
  font-size: 0.75rem;
  font-weight: 700;
  padding: 0.25rem 0.5rem;
  border-radius: 6px;
  min-width: 20px;
  text-align: center;
}

.teacher-card-right {
  position: relative;
}

.options-btn {
  width: 28px;
  height: 28px;
  background: transparent;
  border: 1px solid #e9ecef;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: #6c757d;
  transition: all 0.2s ease;
}
.dark .options-btn {
  border-color: #495057;
  color: #adb5bd;
}

.options-btn:hover {
  background: #e9ecef;
  color: #495057;
}
.dark .options-btn:hover {
  background: #495057;
  color: #ffffff;
}

.teacher-card-body {
  margin-top: 0.5rem;
}

.last-message {
  font-size: 0.85rem;
  color: #495057;
  font-style: italic;
  margin: 0;
  line-height: 1.4;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.dark .last-message {
  color: #ced4da;
}

.options-dropdown {
  position: absolute;
  top: 100%;
  right: 0;
  background: white;
  border: 1px solid #e9ecef;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  z-index: 1000;
  min-width: 150px;
  overflow: hidden;
}
.dark .options-dropdown {
  background: #2c3135;
  border-color: #495057;
}

.dropdown-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  width: 100%;
  padding: 0.75rem 1rem;
  background: none;
  border: none;
  text-align: left;
  cursor: pointer;
  color: #495057;
  font-size: 0.875rem;
  transition: background-color 0.2s ease;
}
.dark .dropdown-item {
  color: #ffffff;
}

.dropdown-item:hover {
  background: #f8f9fa;
}
.dark .dropdown-item:hover {
  background: #495057;
}

.dropdown-item.delete-option {
  color: #dc3545;
}
.dropdown-item.delete-option:hover {
  background: #fee;
}
.dark .dropdown-item.delete-option:hover {
  background: rgba(220, 53, 69, 0.1);
}

.teacher-card-body {
  margin-top: 1rem;
}

.teacher-name {
  font-size: 1.125rem;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 0.25rem;
}
.dark .teacher-name {
  color: #ffffff;
}

.teacher-email {
  font-size: 0.875rem;
  color: #6c757d;
  margin-bottom: 0.5rem;
}
.dark .teacher-email {
  color: #adb5bd;
}

.last-message {
  font-size: 0.875rem;
  color: #495057;
  font-style: italic;
}
.dark .last-message {
  color: #ced4da;
}

/* Notifications */
.notifications-actions {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1.5rem;
  padding: 1rem;
  background: white;
  border-radius: 12px;
  border: 2px solid #e9ecef;
}
.dark .notifications-actions {
  background: #23272b;
  border-color: #495057;
}

.notification-filters {
  display: flex;
  gap: 0.5rem;
}

.filter-btn {
  padding: 0.5rem 1rem;
  border: 1px solid #e9ecef;
  background: white;
  color: #6c757d;
  border-radius: 8px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
}
.dark .filter-btn {
  background: #2c3135;
  border-color: #495057;
  color: #adb5bd;
}

.filter-btn:hover {
  border-color: #A3D1C6;
}
.dark .filter-btn:hover {
  border-color: #20c997;
}

.filter-btn.active {
  background: #A3D1C6;
  border-color: #A3D1C6;
  color: white;
}
.dark .filter-btn.active {
  background: #20c997;
  border-color: #20c997;
}

.action-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background: #A3D1C6;
  color: white;
  border: none;
  border-radius: 8px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
}
.dark .action-btn {
  background: #20c997;
}

.action-btn:hover {
  background: #87C5B8;
}
.dark .action-btn:hover {
  background: #17a085;
}

.notifications-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 1.5rem;
}

.notification-card {
  background: white;
  border: 2px solid #e9ecef;
  border-radius: 12px;
  padding: 1.5rem;
  cursor: pointer;
  transition: all 0.2s ease;
}
.dark .notification-card {
  background: #23272b;
  border-color: #495057;
}

.notification-card:hover {
  border-color: #A3D1C6;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(163, 209, 198, 0.15);
}
.dark .notification-card:hover {
  border-color: #20c997;
  box-shadow: 0 4px 12px rgba(32, 201, 151, 0.15);
}

.notification-card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1rem;
}

.notification-icon {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, #A3D1C6 0%, #87C5B8 100%);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}
.dark .notification-icon {
  background: linear-gradient(135deg, #20c997 0%, #17a085 100%);
}

.notification-card-right {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.notification-count {
  background: #A3D1C6;
  color: white;
  font-size: 0.75rem;
  font-weight: 700;
  padding: 0.25rem 0.5rem;
  border-radius: 6px;
  min-width: 24px;
  text-align: center;
}
.dark .notification-count {
  background: #20c997;
}

.unread-dot {
  width: 8px;
  height: 8px;
  background: #dc3545;
  border-radius: 50%;
}

.notification-card-body {
  margin-top: 1rem;
}

.notification-title {
  font-size: 1.125rem;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 0.5rem;
}
.dark .notification-title {
  color: #ffffff;
}

.notification-teacher {
  font-size: 0.875rem;
  color: #6c757d;
}
.dark .notification-teacher {
  color: #adb5bd;
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
  width: 90%;
  max-width: 600px;
  max-height: 80vh;
  overflow: hidden;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
  display: flex;
  flex-direction: column;
}
.dark .modal-content {
  background: #23272b;
  border: 1px solid #495057;
}

.modal-header {
  padding: 1.25rem 1.5rem;
  border-bottom: 1px solid #e9ecef;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: #f8f9fa;
}
.dark .modal-header {
  background: #2c3135;
  border-bottom-color: #495057;
}

.header-info {
  display: flex;
  align-items: center;
  gap: 0.875rem;
}

.teacher-avatar-chat {
  width: 36px;
  height: 36px;
  background: linear-gradient(135deg, #A3D1C6 0%, #87C5B8 100%);
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 600;
  font-size: 1rem;
}
.dark .teacher-avatar-chat {
  background: linear-gradient(135deg, #20c997 0%, #17a085 100%);
}

.header-details {
  display: flex;
  flex-direction: column;
}

.modal-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: #2c3e50;
  margin: 0;
}
.dark .modal-title {
  color: #ffffff;
}

.subject-info {
  font-size: 0.875rem;
  color: #6c757d;
}
.dark .subject-info {
  color: #adb5bd;
}

.close-btn {
  width: 36px;
  height: 36px;
  background: #e9ecef;
  border: none;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: #6c757d;
  transition: all 0.2s ease;
}
.dark .close-btn {
  background: #495057;
  color: #adb5bd;
}

.close-btn:hover {
  background: #dc3545;
  color: white;
}

.modal-body {
  flex: 1;
  padding: 1.5rem;
  overflow-y: auto;
}

.messages-container {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  max-height: 400px;
  overflow-y: auto;
}

.message-bubble {
  max-width: 80%;
  padding: 0.875rem 1.125rem;
  border-radius: 16px;
  word-wrap: break-word;
}

.message-bubble.received {
  align-self: flex-start;
  background: #e9ecef;
  color: #495057;
  border-bottom-left-radius: 4px;
}
.dark .message-bubble.received {
  background: #495057;
  color: #ffffff;
}

.message-bubble.sent {
  align-self: flex-end;
  background: #A3D1C6;
  color: white;
  border-bottom-right-radius: 4px;
}
.dark .message-bubble.sent {
  background: #20c997;
}

.message-text {
  font-size: 0.9rem;
  line-height: 1.4;
}

.message-time {
  font-size: 0.75rem;
  opacity: 0.7;
  margin-top: 0.25rem;
  text-align: right;
}

.message-bubble.sent .message-time {
  text-align: left;
}

/* Message Attachments */
.message-attachments {
  margin-bottom: 0.5rem;
}

.attachment {
  margin-bottom: 0.5rem;
}

.attachment-image {
  max-width: 200px;
  max-height: 150px;
  border-radius: 8px;
  cursor: pointer;
  object-fit: cover;
  border: 1px solid rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease;
}

.attachment-image:hover {
  transform: scale(1.02);
}

.attachment-file {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem;
  background: rgba(0, 0, 0, 0.05);
  border-radius: 8px;
  cursor: pointer;
  font-size: 0.85rem;
  color: #495057;
  max-width: 250px;
}
.dark .attachment-file {
  background: rgba(255, 255, 255, 0.1);
  color: #ffffff;
}

.attachment-file:hover {
  background: rgba(0, 0, 0, 0.1);
}
.dark .attachment-file:hover {
  background: rgba(255, 255, 255, 0.15);
}

.modal-footer {
  padding: 1.5rem;
  border-top: 1px solid #e9ecef;
  background: #f8f9fa;
}
.dark .modal-footer {
  background: #2c3135;
  border-top-color: #495057;
}

.message-input-area {
  display: flex;
  gap: 0.75rem;
  align-items: flex-end;
}

.attach-btn {
  width: 40px;
  height: 40px;
  background: #e9ecef;
  border: none;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: #6c757d;
  transition: all 0.2s ease;
}
.dark .attach-btn {
  background: #495057;
  color: #adb5bd;
}

.attach-btn:hover {
  background: #A3D1C6;
  color: white;
}
.dark .attach-btn:hover {
  background: #20c997;
}

.attach-btn:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(163, 209, 198, 0.3);
}
.dark .attach-btn:focus {
  box-shadow: 0 0 0 3px rgba(32, 201, 151, 0.3);
}

.message-input {
  flex: 1;
  padding: 0.875rem 1rem;
  border: 2px solid #e9ecef;
  border-radius: 10px;
  font-size: 0.9rem;
  resize: none;
  min-height: 40px;
  max-height: 120px;
}
.dark .message-input {
  background: #2c3135;
  border-color: #495057;
  color: #ffffff;
}

.message-input:focus {
  outline: none;
  border-color: #A3D1C6;
  box-shadow: 0 0 0 3px rgba(163, 209, 198, 0.1);
}
.dark .message-input:focus {
  border-color: #20c997;
  box-shadow: 0 0 0 3px rgba(32, 201, 151, 0.1);
}

.send-btn {
  width: 40px;
  height: 40px;
  background: #A3D1C6;
  border: none;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: white;
  transition: all 0.2s ease;
}
.dark .send-btn {
  background: #20c997;
}

.send-btn:hover {
  background: #87C5B8;
  transform: scale(1.05);
}
.dark .send-btn:hover {
  background: #17a085;
}

.send-btn:disabled {
  background: #e9ecef;
  cursor: not-allowed;
  transform: none;
}
.dark .send-btn:disabled {
  background: #495057;
}

/* Responsive Design */
@media (max-width: 1024px) {
  .teachers-cards {
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
  }
  
  .notifications-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
  }
}

@media (max-width: 768px) {
  .messages-container {
    padding: 0;
    min-height: calc(100vh - 150px);
  }
  
  /* Header mobile optimization */
  .section-header-card {
    margin: 0.5rem;
    margin-bottom: 1rem;
    padding: 1rem;
    border-radius: 12px;
    width: calc(100vw - 1rem);
    max-width: 100vw;
    box-sizing: border-box;
  }
  
  .section-header-left {
    gap: 0.75rem;
  }
  
  .section-header-icon {
    width: 50px;
    height: 50px;
    border-radius: 12px;
  }
  
  .section-header-title {
    font-size: 1.25rem;
    margin-bottom: 0.25rem;
  }
  
  .section-header-sub {
    font-size: 0.9rem;
  }
  
  /* Controls section mobile optimization */
  .controls-section {
    margin: 0.5rem;
    margin-bottom: 1rem;
    flex-direction: row;
    align-items: center;
    gap: 0.5rem;
    padding: 1rem;
    border-radius: 12px;
    width: calc(100vw - 1rem);
    max-width: 100vw;
    box-sizing: border-box;
  }
  
  .search-box {
    min-width: 120px;
    width: 45%;
    flex: 1 1 45%;
  }
  
  .search-input {
    padding: 0.875rem 1rem 0.875rem 2.5rem;
    font-size: 1rem;
    border-radius: 12px;
  }
  
  .filter-tabs {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    gap: 0.25rem;
    width: 55%;
    flex: 1 1 55%;
    overflow-x: auto;
    padding-bottom: 0.25rem;
    flex-wrap: nowrap;
  }
  .filter-tab {
    height: 48px;
    display: flex;
    align-items: center;
  }
  
  .filter-tab {
    padding: 0.75rem 1rem;
    font-size: 0.85rem;
    border-radius: 10px;
    white-space: nowrap;
    min-width: auto;
  }
  
  /* Content area mobile optimization */
  .content-area {
    margin: 0 1rem;
  }
  
  .teachers-cards {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
  
  .notifications-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
  
  /* Subject sections mobile layout */
  .subject-section {
    margin-bottom: 0.25rem;
    border-radius: 12px;
    padding: 0.75rem;
  }
  
  .subject-section-header {
    padding: 1rem 0 0.75rem 0;
    margin-bottom: 0.75rem;
  }
  
  .subject-section-name {
    font-size: 1.1rem;
    margin-bottom: 0.25rem;
  }
  
  .subject-section-code {
    font-size: 0.8rem;
    padding: 0.35rem 0.75rem;
    border-radius: 8px;
  }
  
  .teachers-cards {
    gap: 0.5rem;
  }
  
  /* Teacher card mobile optimization */
  .teacher-card {
    padding: 0.75rem;
    border-radius: 12px;
    position: relative;
  }
  
  .teacher-info {
    gap: 0.75rem;
  }
  
  .teacher-avatar {
    width: 50px;
    height: 50px;
    border-radius: 12px;
  }
  
  .teacher-name {
    font-size: 1rem;
    margin-bottom: 0.25rem;
  }
  
  .teacher-email {
    font-size: 0.8rem;
  }
  
  .teacher-status {
    gap: 0.75rem;
    flex-direction: column;
    align-items: flex-end;
  }
  
  .unread-count {
    padding: 0.35rem 0.75rem;
    font-size: 0.75rem;
    border-radius: 8px;
    min-width: 24px;
    height: 24px;
  }
  
  .teacher-options {
    width: 40px;
    height: 40px;
    border-radius: 10px;
  }
  
  .teacher-options-menu {
    position: fixed;
    bottom: 1rem;
    left: 1rem;
    right: 1rem;
    top: auto;
    transform: none;
    border-radius: 16px;
    max-height: 50vh;
    overflow-y: auto;
  }
  
  .teacher-option {
    padding: 1rem;
    font-size: 0.95rem;
    min-height: 56px;
    border-radius: 12px;
  }
  
  /* Notification cards mobile optimization */
  .notification-card {
    padding: 1rem;
    border-radius: 12px;
  }
  
  .notification-header {
    gap: 0.75rem;
    margin-bottom: 0.75rem;
  }
  
  .notification-sender {
    font-size: 0.95rem;
    margin-bottom: 0.25rem;
  }
  
  .notification-subject {
    font-size: 0.8rem;
  }
  
  .notification-preview {
    font-size: 0.85rem;
    margin-bottom: 0.75rem;
  }
  
  .notification-time {
    font-size: 0.75rem;
  }
  
  /* Empty states mobile optimization */
  .empty-state {
    padding: 2rem 1rem;
    margin: 1rem;
    border-radius: 16px;
  }
  
  .empty-icon {
    width: 80px;
    height: 80px;
    margin-bottom: 1rem;
  }
  
  .empty-state p {
    font-size: 0.9rem;
    margin-bottom: 0.5rem;
  }
  
  .empty-subtext {
    font-size: 0.8rem;
  }
  
  .deleted-state {
    margin: 1rem;
    padding: 1.5rem 1rem;
    border-radius: 16px;
  }
  
  .show-teachers-btn {
    padding: 0.875rem 1.25rem;
    font-size: 0.9rem;
    border-radius: 12px;
  }
  
  /* Modal mobile optimization */
  .modal-overlay {
    padding: 1rem;
  }
  
  .modal-content {
    width: 100%;
    max-width: none;
    margin: 0;
    border-radius: 16px;
    max-height: 85vh;
    overflow-y: auto;
  }
  
  .modal-header {
    padding: 1.25rem;
    border-radius: 16px 16px 0 0;
  }
  
  .modal-title {
    font-size: 1.1rem;
  }
  
  .modal-close {
    width: 40px;
    height: 40px;
    border-radius: 10px;
  }
  
  .modal-body {
    padding: 1.25rem;
    max-height: 60vh;
    overflow-y: auto;
  }
  
  .chat-header {
    padding: 1rem;
    border-radius: 12px 12px 0 0;
  }
  
  .chat-teacher-info {
    gap: 0.75rem;
  }
  
  .chat-teacher-avatar {
    width: 45px;
    height: 45px;
    border-radius: 10px;
  }
  
  .chat-teacher-name {
    font-size: 1rem;
  }
  
  .chat-teacher-status {
    font-size: 0.8rem;
  }
  
  .messages-area {
    height: 300px;
    padding: 1rem;
  }
  
  .message-bubble {
    max-width: 85%;
    padding: 0.875rem 1rem;
    border-radius: 16px;
    margin-bottom: 0.75rem;
  }
  
  .message-text {
    font-size: 0.9rem;
    line-height: 1.5;
  }
  
  .message-time {
    font-size: 0.7rem;
    margin-top: 0.25rem;
  }
  
  .message-input-area {
    padding: 1rem;
    border-radius: 0 0 12px 12px;
  }
  
  .message-input-container {
    gap: 0.75rem;
  }
  
  .message-input {
    padding: 0.875rem 1rem;
    font-size: 0.95rem;
    border-radius: 12px;
  }
  
  .send-btn,
  .attach-btn {
    width: 44px;
    height: 44px;
    border-radius: 10px;
  }
  
  /* Broadcast modal mobile optimization */
  .broadcast-modal {
    border-radius: 16px;
  }
  
  .broadcast-header {
    padding: 1.25rem;
    border-radius: 16px 16px 0 0;
  }
  
  .broadcast-group-name {
    font-size: 1.1rem;
  }
  
  .broadcast-announcements {
    padding: 1rem;
    max-height: 50vh;
    overflow-y: auto;
  }
  
  .announcement-item {
    padding: 1rem;
    border-radius: 12px;
    margin-bottom: 0.875rem;
  }
  
  .announcement-header {
    margin-bottom: 0.75rem;
  }
  
  .announcement-title {
    font-size: 0.95rem;
    margin-bottom: 0.25rem;
  }
  
  .announcement-date {
    font-size: 0.75rem;
  }
  
  .announcement-content {
    font-size: 0.85rem;
    margin-bottom: 0.75rem;
  }
  
  .announcement-actions {
    gap: 0.5rem;
  }
  
  .view-details-btn {
    padding: 0.5rem 0.875rem;
    font-size: 0.8rem;
    border-radius: 8px;
  }
}

@media (max-width: 480px) {
  /* Extra small mobile optimizations */
  .section-header-card {
    margin: 0.75rem;
    padding: 0.875rem;
  }
  
  .section-header-icon {
    width: 45px;
    height: 45px;
  }
  
  .section-header-title {
    font-size: 1.125rem;
  }
  
  .controls-section {
    margin: 0 0.75rem 1.25rem 0.75rem;
    padding: 0.875rem;
  }
  
  .content-area {
    margin: 0 0.75rem;
  }
  
  .filter-tabs {
    flex-wrap: wrap;
    gap: 0.375rem;
  }
  
  .filter-tab {
    padding: 0.625rem 0.875rem;
    font-size: 0.8rem;
  }
  
  .teacher-card {
    padding: 0.875rem;
  }
  
  .teacher-avatar {
    width: 45px;
    height: 45px;
  }
  
  .teacher-name {
    font-size: 0.95rem;
  }
  
  .teacher-email {
    font-size: 0.75rem;
  }
  
  .notification-card {
    padding: 0.875rem;
  }
  
  .empty-state {
    margin: 0.75rem;
    padding: 1.5rem 0.875rem;
  }
  
  .empty-icon {
    width: 70px;
    height: 70px;
  }
  
  .modal-header,
  .modal-body,
  .chat-header,
  .messages-area,
  .message-input-area {
    padding: 1rem;
  }
  
  .message-bubble {
    max-width: 90%;
    padding: 0.75rem 0.875rem;
  }
  
  .broadcast-header,
  .broadcast-announcements {
    padding: 1rem;
  }
  
  .announcement-item {
    padding: 0.875rem;
  }
  
  /* Touch optimization for small screens */
  .teacher-options,
  .modal-close,
  .send-btn,
  .attach-btn {
    width: 44px;
    height: 44px;
  }
  
  .unread-count {
    min-width: 22px;
    height: 22px;
    font-size: 0.7rem;
  }
}

/* iPhone 12 Pro specific optimizations */
@media (max-width: 390px) {
  .section-header-card {
    margin: 0.5rem;
  }
  
  .controls-section {
    margin: 0 0.5rem 1rem 0.5rem;
  }
  
  .content-area {
    margin: 0 0.5rem;
  }
  
  .empty-state,
  .deleted-state {
    margin: 0.5rem;
  }
  
  .teacher-options-menu {
    left: 0.5rem;
    right: 0.5rem;
  }
  
  .modal-overlay {
    padding: 0.5rem;
  }
  
  .message-bubble {
    max-width: 95%;
  }
}

/* ADD THESE STYLES TO YOUR EXISTING <style scoped> SECTION */

/* Loading Overlay */
.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(251, 255, 228, 0.95);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
}
.dark .loading-overlay {
  background: rgba(24, 28, 32, 0.95);
}

.loading-spinner {
  text-align: center;
}

.loading-spinner p {
  margin-top: 1rem;
  font-size: 1.1rem;
  color: #2c3e50;
  font-weight: 500;
}
.dark .loading-spinner p {
  color: #ffffff;
}

.spinner {
  width: 50px;
  height: 50px;
  border: 4px solid #e9ecef;
  border-top-color: #A3D1C6;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
  margin: 0 auto;
}
.dark .spinner {
  border-color: #495057;
  border-top-color: #20c997;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.loading-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 3rem 2rem;
  color: #6c757d;
}
.dark .loading-state {
  color: #adb5bd;
}

.loading-spinner-small {
  margin-bottom: 1rem;
}

.loading-spinner-small .spinner {
  width: 40px;
  height: 40px;
  border-width: 3px;
}

.loading-state p {
  font-size: 1rem;
  color: #495057;
}
.dark .loading-state p {
  color: #ced4da;
}

.loading-messages {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 4rem 2rem;
  min-height: 300px;
}

.loading-messages p {
  margin-top: 1rem;
  font-size: 1rem;
  color: #6c757d;
}
.dark .loading-messages p {
  color: #adb5bd;
}

.button-spinner {
  width: 16px;
  height: 16px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top-color: white;
  border-radius: 50%;
  animation: spin 0.6s linear infinite;
}

/* Notification Badge */
.notification-badge {
  background: #dc3545;
  color: white;
  font-size: 0.7rem;
  font-weight: 700;
  padding: 0.2rem 0.4rem;
  border-radius: 10px;
  min-width: 18px;
  text-align: center;
  margin-left: 0.25rem;
}

/* Last Message Time */
.last-message-time {
  display: block;
  font-size: 0.75rem;
  color: #6c757d;
  margin-top: 0.25rem;
  font-style: normal;
}
.dark .last-message-time {
  color: #adb5bd;
}
</style>