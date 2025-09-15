<template>
  <div class="page-container">
    <div class="bg-decoration">
      <div class="floating-shape shape-1"></div>
      <div class="floating-shape shape-2"></div>
      <div class="floating-shape shape-3"></div>
    </div>
    
    <div class="main-wrapper">
      <!-- Header Section (Uniform Card Style) -->
      <div class="section-header-card">
        <div class="section-header-left">
          <div class="section-header-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
            </svg>
          </div>
          <div>
            <div class="section-header-title">Messages & Notifications</div>
            <div class="section-header-sub">View and manage your messages and announcements</div>
          </div>
        </div>
      </div>

      <section class="content-section">
        <div class="card-box content-card">
          <div class="tabs">
            <button 
              :class="['tab-btn', { 'active': currentTab === 'messages' }]"
              @click="currentTab = 'messages'"
            >
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                <polyline points="22,6 12,13 2,6"/>
              </svg>
              Messages
            </button>
            <button 
              :class="['tab-btn', { 'active': currentTab === 'notifications' }]"
              @click="currentTab = 'notifications'"
            >
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/>
                <path d="M13.73 21a2 2 0 0 1-3.46 0"/>
              </svg>
              Notifications
            </button>
            <button 
              :class="['tab-btn', { 'active': currentTab === 'archived' }]"
              @click="currentTab = 'archived'"
            >
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="20 6 20 10 14 10"/>
                <path d="M4 22h16a2 2 0 0 0 2-2V7.94a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v12.06a2 2 0 0 0 2 2z"/>
                <line x1="14" y1="2" x2="14" y2="10"/>
              </svg>
              Archived
            </button>
          </div>

          <div v-if="currentTab === 'messages'" class="tab-content">
            <div class="section-actions">
              <div class="search-bar">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="search-icon">
                  <circle cx="11" cy="11" r="8"></circle>
                  <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
                <input type="text" v-model="searchQuery" placeholder="Search conversations..." class="search-input" />
              </div>
              <button class="action-btn" @click="markAllAsRead">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <polyline points="20,6 9,17 4,12"/>
                </svg>
                Mark all read
              </button>
            </div>
            
            <div v-if="filteredConversations.length === 0" class="empty-state">
              <div class="empty-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                  <circle cx="12" cy="12" r="10"/>
                  <path d="M8 14s1.5 2 4 2 4-2 4-2"/>
                  <line x1="9" y1="9" x2="9.01" y2="9"/>
                  <line x1="15" y1="9" x2="15.01" y2="9"/>
                </svg>
              </div>
              <p>No messages found</p>
              <span class="empty-subtext">Try searching for another name or check back later.</span>
            </div>
            
            <div v-else class="conversation-list">
              <div 
                v-for="convo in filteredConversations" 
                :key="convo.id" 
               :class="[
    'conversation-item', 
    { 'unread': !convo.read, 'menu-open': activeMessageMenu === convo.id }
  ]"
  @click.stop="openConversationModal(convo)"
              >
                <div class="sender-info">
                  <div class="sender-avatar">
                    <span>{{ convo.sender[0] }}</span>
                  </div>
                  <div class="message-content">
                    <div class="message-header">
                      <p class="sender-name">{{ convo.sender }}</p>
                      <div class="message-indicators">
                        <span v-if="!convo.read" class="unread-dot"></span>
                        <span class="message-time">{{ convo.time }}</span>
                      </div>
                    </div>
                    <p class="last-message">{{ convo.lastMessage }}</p>
                  </div>
                </div>
                <div class="message-options-container">
                    <button class="options-btn" @click.stop="toggleMessageMenu(convo.id)">
                      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="12" r="1"></circle>
                        <circle cx="19" cy="12" r="1"></circle>
                        <circle cx="5" cy="12" r="1"></circle>
                      </svg>
                    </button>
                    <div v-if="activeMessageMenu === convo.id" class="options-menu">
                        <a href="#" @click.stop.prevent="toggleReadStatus(convo.id)">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 12A10 10 0 0 1 12 2a10 10 0 0 0 0 20c3.2 0 6.2-1.3 8.4-3.5L14 14.5V12a2 2 0 1 1 4 0v2.5l6 6c-2.2 2.2-5.4 3.5-8.8 3.5A10 10 0 0 1 2 12a10 10 0 0 1 20 0z"/></svg>
                            {{ convo.read ? 'Mark as Unread' : 'Mark as Read' }}
                        </a>
                        <a href="#" @click.stop.prevent="archiveMessage(convo.id)">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 8V5c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v3m18 0h-16c-1.1 0-2 .9-2 2v7c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zm-8-3v4m-4 0v-4"/></svg>
                            Archive
                        </a>
                        <a href="#" @click.stop.prevent="deleteMessage(convo.id)" class="delete-option">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg>
                            Delete
                        </a>
                    </div>
                </div>
              </div>
            </div>
          </div>

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
                <button 
                  :class="['filter-btn', { 'active': currentFilter === 'important' }]"
                  @click="currentFilter = 'important'"
                >
                  Important
                </button>
              </div>
              <button class="action-btn" @click="clearNotifications">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <polyline points="3,6 5,6 21,6"/>
                  <path d="M19,6v14a2,2,0,0,1-2,2H7a2,2,0,0,1-2-2V6m3,0V4a2,2,0,0,1,2-2h4a2,2,0,0,1,2,2V6"/>
                </svg>
                Clear all
              </button>
            </div>
            
            <div v-if="filteredNotifications.length === 0" class="empty-state">
              <div class="empty-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                  <circle cx="12" cy="12" r="10"/>
                  <path d="M8 14s1.5 2 4 2 4-2 4-2"/>
                  <line x1="9" y1="9" x2="9.01" y2="9"/>
                  <line x1="15" y1="9" x2="15.01" y2="9"/>
                </svg>
              </div>
              <p>No notifications found</p>
              <span class="empty-subtext">You're all up to date with announcements and updates.</span>
            </div>
            
            <div v-else class="notification-list">
              <div 
                v-for="notif in filteredNotifications" 
                :key="notif.id" 
                :class="['notification-item', {'unread': !notif.read, 'important': notif.important}]"
                @click="openNotificationModal(notif)"

                
              >
                <div class="notification-header">
                  <span class="notification-icon">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <circle cx="12" cy="12" r="10"></circle>
                      <line x1="12" y1="16" x2="12" y2="12"></line>
                      <line x1="12" y1="8" x2="12.01" y2="8"></line>
                    </svg>
                  </span>
                  <div class="notification-indicators">
                    <div v-if="notif.important" class="priority-dot"></div>
                    <span v-if="!notif.read" class="unread-label">New</span>
                  </div>
                </div>
                <div class="notification-content">
                  <p class="notif-title">{{ notif.title }}</p>
                  <p class="notif-body">{{ notif.body }}</p>
                </div>
                <div class="notification-footer">
                  <span class="notif-timestamp">{{ notif.time }}</span>
                  <button class="dismiss-btn" @click.stop="dismissNotification(notif.id)">
                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <line x1="18" y1="6" x2="6" y2="18"/>
                      <line x1="6" y1="6" x2="18" y2="18"/>
                    </svg>
                  </button>
                </div>
              </div>
            </div>
          </div>
          
          <div v-else-if="currentTab === 'archived'" class="tab-content">
            <div class="section-actions">
                <p class="section-title">Archived Messages</p>
                <button class="action-btn" @click="unarchiveAll">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M21 8V5c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v3m18 0h-16c-1.1 0-2 .9-2 2v7c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zm-8-3v4m-4 0v-4"/>
                  </svg>
                  Unarchive all
                </button>
            </div>
            <div v-if="archivedConversations.length === 0" class="empty-state">
              <div class="empty-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                  <circle cx="12" cy="12" r="10"/>
                  <path d="M8 14s1.5 2 4 2 4-2 4-2"/>
                  <line x1="9" y1="9" x2="9.01" y2="9"/>
                  <line x1="15" y1="9" x2="15.01" y2="9"/>
                </svg>
              </div>
              <p>No archived messages</p>
              <span class="empty-subtext">Archived conversations will appear here.</span>
            </div>
            <div v-else class="conversation-list">
              <div 
                v-for="convo in archivedConversations" 
                :key="convo.id" 
                class="conversation-item"
                @click.stop="openConversationModal(convo)"
              >
                <div class="sender-info">
                  <div class="sender-avatar">
                    <span>{{ convo.sender[0] }}</span>
                  </div>
                  <div class="message-content">
                    <div class="message-header">
                      <p class="sender-name">{{ convo.sender }}</p>
                      <div class="message-indicators">
                        <span class="message-time">{{ convo.time }}</span>
                      </div>
                    </div>
                    <p class="last-message">{{ convo.lastMessage }}</p>
                  </div>
                </div>
                <div class="message-options-container">
                    <button class="options-btn" @click.stop="toggleMessageMenu(convo.id)">
                      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="12" r="1"></circle>
                        <circle cx="19" cy="12" r="1"></circle>
                        <circle cx="5" cy="12" r="1"></circle>
                      </svg>
                    </button>
                    <div v-if="activeMessageMenu === convo.id" class="options-menu">
                        <a href="#" @click.stop.prevent="unarchiveMessage(convo.id)">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1" ry="1"/></svg>
                            Unarchive
                        </a>
                        <a href="#" @click.stop.prevent="deleteArchived(convo.id)" class="delete-option">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg>
                            Delete
                        </a>
                    </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>

    <div v-if="isModalOpen" class="modal-overlay" @click.self="closeModal">
      <div class="modal-content">
        <div class="modal-header">
          <button @click="closeModal" class="close-btn">&times;</button>
          <div class="header-info">
            <div class="sender-avatar">
              <span>{{ activeConversation.sender[0] }}</span>
            </div>
            <h2 class="modal-title">{{ activeConversation.sender }}</h2>
          </div>
        </div>
        <div class="modal-body">
          <div class="messages-container" ref="messagesContainer">
            <div 
              v-for="message in activeConversation.messages" 
              :key="message.id" 
              :class="['message-bubble', { 'sent': message.sender === 'You', 'received': message.sender !== 'You' }]"
            >
              <p class="message-text">{{ message.text }}</p>
              <span class="message-time">{{ message.time }}</span>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <div class="message-input-area">
            <input 
              type="text" 
              v-model="newMessage" 
              @keyup.enter="sendMessage" 
              placeholder="Type your message..." 
              class="message-input"
            />
            <button class="send-btn" @click="sendMessage">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <line x1="22" y1="2" x2="11" y2="13"></line>
                <polygon points="22 2 15.46 22 11 13 2 9.54 22 2"></polygon>
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, nextTick } from 'vue';
import { useMessaging } from '@/composables/useMessaging.js';

const currentTab = ref('messages');
const currentFilter = ref('all');
const searchQuery = ref('');
const activeMessageMenu = ref(null);
const isModalOpen = ref(false);
const activeConversation = ref(null);
const newMessage = ref('');
const messagesContainer = ref(null);

// Use the messaging composable
const {
  conversations,
  notifications,
  archivedConversations,
  unreadCount,
  isConnected,
  currentUser,
  fetchConversations,
  fetchConversationMessages,
  sendMessage: sendMessageAPI,
  markMessagesAsRead,
  fetchUsers,
  fetchNotifications
} = useMessaging();

const filteredConversations = computed(() => {
  const query = searchQuery.value.toLowerCase();
  if (!query) {
    return conversations.value;
  }
  return conversations.value.filter(convo =>
    convo.sender.toLowerCase().includes(query) ||
    convo.lastMessage.toLowerCase().includes(query)
  );
});

const filteredNotifications = computed(() => {
  if (currentFilter.value === 'unread') {
    return notifications.value.filter(notif => !notif.read);
  } else if (currentFilter.value === 'important') {
    return notifications.value.filter(notif => notif.important);
  } else {
    return notifications.value;
  }
});

const toggleMessageMenu = (id) => {
  activeMessageMenu.value = activeMessageMenu.value === id ? null : id;
};

const toggleReadStatus = (id) => {
  const convo = conversations.value.find(c => c.id === id);
  if (convo) {
    convo.read = !convo.read;
  }
  activeMessageMenu.value = null;
};

const archiveMessage = (id) => {
  const convoToArchive = conversations.value.find(convo => convo.id === id);
  if (convoToArchive) {
    archivedConversations.value.unshift(convoToArchive);
    conversations.value = conversations.value.filter(convo => convo.id !== id);
  }
  activeMessageMenu.value = null;
};

const unarchiveMessage = (id) => {
  const convoToUnarchive = archivedConversations.value.find(convo => convo.id === id);
  if (convoToUnarchive) {
    conversations.value.unshift(convoToUnarchive);
    archivedConversations.value = archivedConversations.value.filter(convo => convo.id !== id);
  }
  activeMessageMenu.value = null;
};

const unarchiveAll = () => {
  conversations.value.unshift(...archivedConversations.value);
  archivedConversations.value = [];
  activeMessageMenu.value = null;
};

const deleteMessage = (id) => {
  if (confirm('Are you sure you want to delete this message? This action cannot be undone.')) {
    conversations.value = conversations.value.filter(convo => convo.id !== id);
    console.log(`Deleted message with ID: ${id}`);
  }
  activeMessageMenu.value = null;
};

const deleteArchived = (id) => {
  if (confirm('Are you sure you want to permanently delete this archived message?')) {
    archivedConversations.value = archivedConversations.value.filter(convo => convo.id !== id);
    console.log(`Permanently deleted archived message with ID: ${id}`);
  }
  activeMessageMenu.value = null;
};

const markAllAsRead = () => {
  conversations.value = conversations.value.map(convo => ({ ...convo, read: true }));
};

const clearNotifications = () => {
  notifications.value = [];
};

const openConversationModal = async (convo) => {
  activeConversation.value = convo;
  isModalOpen.value = true;
  convo.read = true;
  
  // Fetch messages for this conversation if not already loaded
  if (!convo.messages || convo.messages.length === 0) {
    try {
      const messages = await fetchConversationMessages(convo.id);
      convo.messages = messages;
    } catch (error) {
      console.error('Failed to load messages:', error);
    }
  }
  
  // Mark messages as read
  markMessagesAsRead(convo.id);
  
  // Wait for the modal to render, then scroll to the bottom
  nextTick(() => {
    if (messagesContainer.value) {
      messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight;
    }
  });
};

const closeModal = () => {
  isModalOpen.value = false;
  activeConversation.value = null;
  newMessage.value = '';
  activeMessageMenu.value = null;
};

const sendMessage = async () => {
  if (newMessage.value.trim() === '' || !activeConversation.value) return;

  const messageText = newMessage.value.trim();
  const conversation = activeConversation.value;
  
  // Find receiver ID (the other participant in conversation)
  const receiverId = getOtherParticipantId(conversation);
  
  try {
    // Add message optimistically to UI
    const optimisticMessage = {
      id: Date.now(), // Temporary ID
      text: messageText,
      sender: 'You',
      time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    };
    
    if (!conversation.messages) conversation.messages = [];
    conversation.messages.push(optimisticMessage);
    conversation.lastMessage = messageText;
    newMessage.value = '';
    
    // Scroll to bottom
    nextTick(() => {
      if (messagesContainer.value) {
        messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight;
      }
    });
    
    // Send message via API
    await sendMessageAPI(conversation.id, receiverId, messageText);
    
  } catch (error) {
    console.error('Failed to send message:', error);
    // Remove optimistic message on error
    if (conversation.messages) {
      conversation.messages = conversation.messages.filter(msg => msg.id !== optimisticMessage.id);
    }
  }
};

const getOtherParticipantId = (conversation) => {
  // This would need to be determined based on conversation structure
  // For now, we'll need to store participant IDs in the conversation object
  return conversation.otherParticipantId || 1; // Fallback
};

const openNotificationModal = (notif) => {
  console.log('Opening notification modal for:', notif);
  notif.read = true;
};

const dismissNotification = (id) => {
  notifications.value = notifications.value.filter(notif => notif.id !== id);
};

onMounted(() => {
  // Close menu when clicking outside
  window.addEventListener('click', (e) => {
    if (!e.target.closest('.message-options-container') && activeMessageMenu.value) {
      activeMessageMenu.value = null;
    }
  });
});
</script>

<style scoped>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* Main Page Styling */
.page-container {
  padding: 2rem 5%;
  font-family: 'Inter', sans-serif;
  min-height: 100vh;
  position: relative;
  overflow-x: hidden;
  background: linear-gradient(135deg, #f8fffe 0%, #f0f7f4 100%);
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
  background: #3D8D7A;
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

.card-box {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(61, 141, 122, 0.08);
  border-radius: 28px;
  padding: 2.5rem;
  box-shadow: 
    0 20px 60px rgba(61, 141, 122, 0.05),
    0 8px 32px rgba(61, 141, 122, 0.03),
    0 0 0 1px rgba(255, 255, 255, 0.3);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.card-box:hover {
  transform: translateY(-2px);
  box-shadow: 
    0 25px 70px rgba(61, 141, 122, 0.08),
    0 12px 40px rgba(61, 141, 122, 0.05),
    0 0 0 1px rgba(255, 255, 255, 0.4);
}



/* --- Header card style to match Settings.vue/Subjects.vue --- */
.section-header-card {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  background: #fff;
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
  color: #fff;
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

.content-section {
  display: flex;
  justify-content: center;
  width: 100%;
}

.content-card {
  width: 100%;
}

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
  background: #f0f7f4;
  border: 1px solid rgba(61, 141, 122, 0.1);
  border-radius: 12px;
  color: #777;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.tab-btn:hover {
  background: #e6f0ed;
}

.tab-btn.active {
  background: #3D8D7A;
  color: white;
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.2);
}

.tab-btn.active svg {
  color: white;
  stroke: white;
}

.tab-content {
  padding-top: 1rem;
}

.section-actions {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  gap: 1rem;
  flex-wrap: wrap;
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
  color: #999;
}

.search-input {
  width: 100%;
  padding: 0.75rem 1rem 0.75rem 3rem;
  border: 1px solid #e0e0e0;
  border-radius: 12px;
  font-size: 1rem;
  transition: all 0.2s ease;
}

.search-input:focus {
  outline: none;
  border-color: #3D8D7A;
  box-shadow: 0 0 0 3px rgba(61, 141, 122, 0.1);
}

.action-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1rem;
  background: rgba(61, 141, 122, 0.05);
  border: 1px solid rgba(61, 141, 122, 0.1);
  border-radius: 12px;
  color: #3D8D7A;
  font-size: 0.9rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
}

.action-btn:hover {
  background: rgba(61, 141, 122, 0.1);
  transform: translateY(-1px);
}

.empty-state {
  text-align: center;
  color: #888;
  padding: 3rem 2rem;
}

.empty-icon {
  color: #ccc;
  margin-bottom: 1rem;
}

.empty-state p {
  font-size: 1.1rem;
  font-weight: 600;
  margin: 0;
  color: #666;
}

.empty-subtext {
  font-size: 0.9rem;
  color: #999;
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
  background: linear-gradient(135deg, rgba(251, 255, 228, 0.8) 0%, rgba(255, 255, 255, 0.9) 100%);
  border: 1px solid rgba(61, 141, 122, 0.08);
  border-radius: 20px;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
}

.conversation-item.unread {
  background: linear-gradient(135deg, #e8fffb 0%, #f0fdfc 100%);
  border-color: #A3D1C6;
}

.notification-item.unread {
  background: linear-gradient(135deg, #e8fffb 0%, #f0fdfc 100%);
  border-color: #A3D1C6;
}

.notification-item.important {
  background: linear-gradient(135deg, #fff3e0 0%, #fffbf0 100%);
  border-color: #ffc107;
}

.conversation-item:hover,
.notification-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 40px rgba(61, 141, 122, 0.12);
  border-color: rgba(61, 141, 122, 0.15);
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
  color: #3D8D7A;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 1.2rem;
  flex-shrink: 0;
  box-shadow: 0 4px 16px rgba(61, 141, 122, 0.1);
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
  color: #3D8D7A;
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
  background: #3D8D7A;
  border-radius: 50%;
  flex-shrink: 0;
}

.message-time {
  font-size: 0.85rem;
  color: #999;
  font-weight: 500;
}

.last-message {
  font-size: 0.95rem;
  color: #666;
  margin: 0;
  line-height: 1.4;
  display: -webkit-box;
  -webkit-line-clamp: 2;
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
  color: #999;
  cursor: pointer;
  padding: 0.5rem;
  transition: color 0.2s ease;
}

.options-btn:hover {
  color: #3D8D7A;
}

.options-menu {
  position: absolute;
  top: 100%;
  right: 0;
  background-color: white;
  border: 1px solid #e0e0e0;
  border-radius: 12px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.1);
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
    color: #555;
    text-decoration: none;
    border-radius: 8px;
    transition: background-color 0.2s ease, color 0.2s ease;
}

.options-menu a:hover {
    background-color: #f0f7f4;
    color: #3D8D7A;
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
  border: 1px solid #e0e0e0;
  border-radius: 12px;
  color: #777;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
}

.filter-btn:hover {
  background: #f0f0f0;
}

.filter-btn.active {
  background: #3D8D7A;
  border-color: #3D8D7A;
  color: white;
  box-shadow: 0 4px 12px rgba(61, 141, 122, 0.2);
}

.notification-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.notification-icon {
  color: #3D8D7A;
  background: rgba(61, 141, 122, 0.1);
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
  color: white;
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
  position: relative;
}

.modal-header {
  padding: 1.5rem 2rem;
  background: linear-gradient(135deg, #3D8D7A 0%, #A3D1C6 100%);
  color: white;
  display: flex;
  align-items: center;
  gap: 1.5rem;
  position: relative;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.modal-header .close-btn {
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

.modal-header .close-btn:hover {
  opacity: 1;
}

.header-info {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.modal-header .sender-avatar {
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
  filter: drop-shadow(0 4px 8px rgba(0,0,0,0.05));
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
  position: sticky;
  bottom: 0;
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

/* Responsive Styles */
@media (max-width: 768px) {
  .page-container {
    padding: 1rem;
  }
  
  .card-box {
    padding: 1.5rem;
    border-radius: 20px;
  }
  
  .hero-header h1 {
    font-size: 2rem;
  }
  
  .header-icon {
    width: 64px;
    height: 64px;
  }
  
  .tab-btn {
    padding: 0.5rem 1rem;
  }

  .section-actions {
    flex-direction: column;
    align-items: stretch;
    gap: 1rem;
  }
  
  .search-bar {
    max-width: none;
  }
  
  .conversation-item,
  .notification-item {
    padding: 1rem;
  }
  
  .sender-avatar {
    width: 48px;
    height: 48px;
  }
}

@media (max-width: 480px) {
  .last-message {
    -webkit-line-clamp: 1;
  }
}
</style> 