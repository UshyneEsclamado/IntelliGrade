<template>
  <div class="dashboard-wrapper">
    <nav class="top-nav">
      <div class="nav-content">
        <div class="nav-left">
          <div class="logo">
            <span class="logo-icon">🎓</span>
            <span class="logo-text">IntelliGrade</span>
          </div>
          <div class="search-container">
            <input 
              type="text" 
              placeholder="Search students, assessments, or classes..." 
              class="search-input"
              v-model="searchQuery"
            >
            <span class="search-icon">🔍</span>
          </div>
        </div>
        
        <div class="nav-right">
          <div class="nav-item notification-dropdown" @click="toggleNotifications">
            <div class="nav-icon">
              🔔
              <span class="notification-badge" v-if="unreadNotifications > 0">{{ unreadNotifications }}</span>
            </div>
            <div class="dropdown-menu notifications-menu" v-show="showNotifications">
              <div class="dropdown-header">
                <h3>Notifications</h3>
                <button class="mark-all-read" @click="markAllNotificationsRead">Mark all as read</button>
              </div>
              <div class="notifications-list">
                <div 
                  v-for="notification in notifications.slice(0, 5)" 
                  :key="notification.id"
                  class="notification-item"
                  :class="{ unread: !notification.read }"
                  @click="handleNotificationClick(notification)"
                >
                  <div class="notification-avatar">{{ notification.avatar }}</div>
                  <div class="notification-content">
                    <p class="notification-text">{{ notification.message }}</p>
                    <span class="notification-time">{{ notification.timeAgo }}</span>
                  </div>
                  <div class="notification-dot" v-if="!notification.read"></div>
                </div>
              </div>
              <div class="dropdown-footer">
                <button class="see-all-btn">See all notifications</button>
              </div>
            </div>
          </div>
  
          <div class="nav-item messages-dropdown" @click="toggleMessages">
            <div class="nav-icon">
              💬
              <span class="message-badge" v-if="unreadMessages > 0">{{ unreadMessages }}</span>
            </div>
            <div class="dropdown-menu messages-menu" v-show="showMessages">
              <div class="dropdown-header">
                <h3>Messages</h3>
                <div class="header-actions">
                  <button class="icon-btn" @click.stop="showCreateClassModal = true">&#x2795;</button>
                </div>
              </div>
              <div class="messages-list">
                <div 
                  v-for="message in recentMessages" 
                  :key="message.id"
                  class="message-item"
                  :class="{ unread: !message.read }"
                  @click="openChatWith(message.sender)"
                >
                  <div class="message-avatar">{{ message.avatar }}</div>
                  <div class="message-content">
                    <div class="message-header">
                      <span class="sender-name">{{ message.sender }}</span>
                      <span class="message-time">{{ message.timeAgo }}</span>
                    </div>
                    <p class="message-preview">{{ message.preview }}</p>
                  </div>
                  <div class="message-dot" v-if="!message.read"></div>
                </div>
              </div>
            </div>
          </div>
  
          <div class="nav-item profile-dropdown" @click="toggleProfile">
            <div class="profile-avatar">&#x1F464;</div>
            <div class="dropdown-menu profile-menu" v-show="showProfile">
              <div class="profile-info">
                <div class="profile-pic">&#x1F464;</div>
                <div>
                  <h4>Prof. Juan Dela Cruz</h4>
                  <p>Mathematics Department</p>
                </div>
              </div>
              <div class="profile-actions">
                <button class="profile-btn">View Profile</button>
                <button class="profile-btn">Settings</button>
                <button class="profile-btn">Help Center</button>
                <button class="profile-btn logout">Log Out</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <div class="dashboard-content">
      <aside class="sidebar">
        <div class="sidebar-section">
          <h3 class="sidebar-title">Quick Actions</h3>
          <div class="quick-actions">
            <button class="action-btn" @click="navigateToMyClasses">
              <span class="action-icon">&#x1F4C1;</span>
              My Classes
            </button>
            <button class="action-btn" @click="scheduleClass">
              <span class="action-icon">&#x23F0;</span>
              Schedule Class
            </button>
            <button class="action-btn" @click="uploadMaterial">
              <span class="action-icon">&#x1F4E4;</span>
              Upload Material
            </button>
          </div>
        </div>
        
        <div class="sidebar-section">
          <h3 class="sidebar-title">
            Reminders 
            <button class="add-reminder" @click="showReminderModal = true">&#x2795;</button>
          </h3>
          <div class="reminders-list">
            <div 
              v-for="reminder in reminders" 
              :key="reminder.id"
              class="reminder-item"
              :class="{ urgent: reminder.urgent, completed: reminder.completed }"
            >
              <div class="reminder-checkbox">
                <input 
                  type="checkbox" 
                  :checked="reminder.completed"
                  @change="toggleReminder(reminder.id)"
                >
              </div>
              <div class="reminder-content">
                <p class="reminder-text">{{ reminder.text }}</p>
                <span class="reminder-date">{{ reminder.dueDate }}</span>
              </div>
            </div>
          </div>
        </div>
  
        <div class="sidebar-section">
          <h3 class="sidebar-title">Today's Schedule</h3>
          <div class="schedule-list">
            <div v-for="event in todaySchedule" :key="event.id" class="schedule-item">
              <div class="schedule-time">{{ event.time }}</div>
              <div class="schedule-details">
                <h4>{{ event.title }}</h4>
                <p>{{ event.location }}</p>
              </div>
            </div>
          </div>
        </div>
      </aside>
  
      <main class="main-content">
        <div class="header-section">
          <div class="welcome-content">
            <h1 class="main-title">Good morning, Prof. Juan! 🌅</h1>
            <p class="welcome-text">You have {{ pendingTasks }} tasks pending and {{ upcomingClasses }} classes today</p>
          </div>
          <div class="quick-stats-grid">
            <div class="stat-card" @click="viewAssessments">
              <div class="stat-icon">&#x1F4C9;</div>
              <div class="stat-info">
                <span class="stat-number">{{ stats.autoGradedCount }}</span>
                <span class="stat-label">Auto Graded</span>
              </div>
            </div>
            <div class="stat-card" @click="viewAnalytics">
              <div class="stat-icon">&#x1F4C8;</div>
              <div class="stat-info">
                <span class="stat-number">{{ stats.averageScore }}%</span>
                <span class="stat-label">Avg Score</span>
              </div>
            </div>
            <div class="stat-card" @click="viewPending">
              <div class="stat-icon">&#x23F1;</div>
              <div class="stat-info">
                <span class="stat-number">{{ assessmentsToGrade.length }}</span>
                <span class="stat-label">Pending</span>
              </div>
            </div>
            <div class="stat-card" @click="viewStudents">
              <div class="stat-icon">&#x1F465;</div>
              <div class="stat-info">
                <span class="stat-number">{{ stats.totalStudents }}</span>
                <span class="stat-label">Students</span>
              </div>
            </div>
          </div>
        </div>
  
        <section class="core-feature">
          <div class="section-header">
            <h2 class="section-title">
              My Classes
            </h2>
          </div>
          <div class="assessments-grid">
            <div v-for="classItem in myClasses" :key="classItem.id" class="class-card">
              <div class="card-header">
                <h3 class="class-title">{{ classItem.subject }}</h3>
                <div class="card-actions-header">
                  <span class="section-tag">Section {{ classItem.section }}</span>
                </div>
              </div>
              <div class="card-content">
                <p class="class-code-label">Class Code:</p>
                <div class="class-code-display">
                  <p>{{ classItem.classCode }}</p>
                  <button class="copy-btn" @click="copyClassCode(classItem.classCode)">
                    <span class="btn-icon">&#x1F4C4;</span>
                  </button>
                </div>
                <div class="class-stats">
                  <div class="stat-item">
                    <span class="stat-number">{{ classItem.students }}</span>
                    <span class="stat-label">Students</span>
                  </div>
                  <div class="stat-item">
                    <span class="stat-number">{{ classItem.assessments }}</span>
                    <span class="stat-label">Assessments</span>
                  </div>
                </div>
              </div>
              <div class="card-actions">
                <button class="secondary-btn" @click="viewClassDetails(classItem.id)">
                  View Details
                </button>
              </div>
            </div>
          </div>
        </section>

        <section class="core-feature">
          <div class="section-header">
            <h2 class="section-title">
              <span class="title-icon">&#x270F;</span>
              Recent Assessments
            </h2>
            <div class="header-actions">
              <button class="filter-btn" @click="showFilters = !showFilters">
                <span class="btn-icon">🔍</span>
                Filter
              </button>
              <button class="primary-btn" @click="uploadAssessment">
                <span class="btn-icon">&#x1F4E4;</span>
                Upload Assessment
              </button>
            </div>
          </div>
          
          <div class="filters-bar" v-show="showFilters">
            <select v-model="selectedSubject" class="filter-select">
              <option value="">All Subjects</option>
              <option value="math">Mathematics</option>
              <option value="science">Science</option>
              <option value="history">History</option>
            </select>
            <select v-model="selectedStatus" class="filter-select">
              <option value="">All Status</option>
              <option value="pending">Pending</option>
              <option value="in-progress">In Progress</option>
              <option value="completed">Completed</option>
            </select>
          </div>
          
          <div class="assessments-grid">
            <div v-for="assessment in filteredAssessments" :key="assessment.id" class="assessment-card">
              <div class="card-header">
                <h3 class="assessment-title">{{ assessment.title }}</h3>
                <div class="card-actions-header">
                  <span class="status-badge" :class="assessment.status.toLowerCase().replace(' ', '-')">
                    {{ assessment.status }}
                  </span>
                  <button class="menu-btn" @click="toggleAssessmentMenu(assessment.id)">⋯</button>
                </div>
              </div>
              <div class="card-content">
                <div class="assessment-meta">
                  <span class="subject-tag">{{ assessment.subject }}</span>
                  <span class="due-date">Due: {{ assessment.dueDate }}</span>
                </div>
                <div class="progress-container">
                  <div class="progress-bar">
                    <div class="progress-fill" :style="{ width: assessment.progress + '%' }"></div>
                  </div>
                  <p class="progress-text">{{ assessment.completed }} of {{ assessment.total }} students completed</p>
                </div>
                <div class="student-avatars">
                  <div class="avatar-group">
                    <span v-for="student in assessment.recentSubmissions.slice(0, 4)" 
                          :key="student" 
                          class="student-avatar">{{ student }}</span>
                    <span v-if="assessment.recentSubmissions.length > 4" class="more-avatars">
                      +{{ assessment.recentSubmissions.length - 4 }}
                    </span>
                  </div>
                </div>
              </div>
              <div class="card-actions">
                <button class="secondary-btn" @click="gradeAssessment(assessment.id)">
                  <span class="btn-icon">&#x26A1;</span>
                  Auto-Grade
                </button>
                <button class="tertiary-btn" @click="viewAssessmentDetails(assessment.id)">
                  View Details
                </button>
                <button class="icon-btn" @click="shareAssessment(assessment.id)" title="Share">
                  &#x1F4E4;
                </button>
              </div>
            </div>
          </div>
        </section>
      </main>

      <section class="activity-feed">
        <div class="section-header">
          <h2 class="section-title">
            <span class="title-icon">&#x1F4C8;</span>
            Live Activity
          </h2>
          <button class="view-all-btn">View All</button>
        </div>
        <div class="activity-list">
          <div v-for="activity in liveActivities" :key="activity.id" class="activity-item">
            <div class="activity-avatar">{{ activity.avatar }}</div>
            <div class="activity-content">
              <p class="activity-text">
                <strong>{{ activity.student }}</strong> {{ activity.action }}
                <span class="activity-target">{{ activity.target }}</span>
              </p>
              <span class="activity-time">{{ activity.timeAgo }}</span>
            </div>
            <div class="activity-score" v-if="activity.score">{{ activity.score }}%</div>
          </div>
        </div>
      </section>
    </div>

    <div class="chat-container">
      <div class="floating-chat" @click="toggleChatBox">
        <div class="chat-icon">💬</div>
        <div class="chat-badge" v-if="unreadMessages > 0">{{ unreadMessages }}</div>
      </div>
      
      <div class="chatbox" :class="{ open: showChatBox }">
        <div class="chatbox-header">
          <h3>Student Chat</h3>
          <div class="chatbox-controls">
            <button class="minimize-btn" @click="minimizeChatBox">−</button>
            <button class="close-btn" @click="closeChatBox">×</button>
          </div>
        </div>
        
        <div class="chat-contacts" v-show="!currentChatUser">
          <div class="search-contacts">
            <input 
              type="text" 
              placeholder="Search students..." 
              v-model="chatSearchQuery"
              class="contact-search"
            >
          </div>
          <div class="contacts-list">
            <div 
              v-for="contact in filteredChatContacts" 
              :key="contact.id"
              class="contact-item"
              @click="startChatWith(contact)"
            >
              <div class="contact-avatar">{{ contact.avatar }}</div>
              <div class="contact-info">
                <h4>{{ contact.name }}</h4>
                <p class="last-message">{{ contact.lastMessage }}</p>
              </div>
              <div class="contact-status">
                <span class="online-indicator" :class="{ online: contact.online }"></span>
                <span class="last-seen">{{ contact.lastSeen }}</span>
              </div>
            </div>
          </div>
        </div>

        <div class="active-chat" v-show="currentChatUser">
          <div class="chat-user-header" @click="backToContacts">
            <span class="back-arrow">&#x2190;</span>
            <div class="chat-user-info">
              <div class="chat-user-avatar">{{ currentChatUser?.avatar }}</div>
              <div>
                <h4>{{ currentChatUser?.name }}</h4>
                <span class="user-status">{{ currentChatUser?.online ? 'Online' : 'Last seen ' + currentChatUser?.lastSeen }}</span>
              </div>
            </div>
          </div>
          
          <div class="chat-messages" ref="chatMessages">
            <div 
              v-for="message in currentChatMessages" 
              :key="message.id"
              class="message"
              :class="{ sent: message.sender === 'teacher', received: message.sender !== 'teacher' }"
            >
              <div class="message-content">
                <p>{{ message.text }}</p>
                <span class="message-time">{{ message.time }}</span>
              </div>
            </div>
          </div>
          
          <div class="chat-input-container">
            <input 
              type="text" 
              placeholder="Type a message..." 
              v-model="newMessage"
              @keyup.enter="sendMessage"
              class="chat-input"
            >
            <button class="send-btn" @click="sendMessage">&#x1F4E4;</button>
          </div>
        </div>
      </div>
    </div>

    <div class="modal-overlay" v-show="showReminderModal" @click="showReminderModal = false">
      <div class="modal" @click.stop>
        <div class="modal-header">
          <h3>Add Reminder</h3>
          <button class="close-modal" @click="showReminderModal = false">×</button>
        </div>
        <div class="modal-content">
          <form @submit.prevent="addReminder">
            <div class="form-group">
              <label>Reminder Text</label>
              <input 
                type="text" 
                v-model="newReminder.text" 
                placeholder="Enter reminder..." 
                required
              >
            </div>
            <div class="form-group">
              <label>Due Date</label>
              <input 
                type="datetime-local" 
                v-model="newReminder.dueDate" 
                required
              >
            </div>
            <div class="form-group">
              <label>
                <input type="checkbox" v-model="newReminder.urgent"> 
                Mark as urgent
              </label>
            </div>
            <div class="modal-actions">
              <button type="button" class="cancel-btn" @click="showReminderModal = false">Cancel</button>
              <button type="submit" class="add-btn">Add Reminder</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "EnhancedTeacherDashboard",
  data() {
    return {
      // UI States
      showNotifications: false,
      showMessages: false,
      showProfile: false,
      showChatBox: false,
      showReminderModal: false,
      showFilters: false,
      
      // Search & Filters
      searchQuery: '',
      selectedSubject: '',
      selectedStatus: '',
      chatSearchQuery: '',
      
      // Chat
      currentChatUser: null,
      newMessage: '',
      
      // Counts
      unreadNotifications: 3,
      unreadMessages: 2,
      pendingTasks: 7,
      upcomingClasses: 3,
      
      // Data
      myClasses: [
        {
          id: 1,
          subject: "Mathematics 101",
          section: "A1-G4",
          classCode: "MATH-A1-2R8",
          students: 32,
          assessments: 5
        },
        {
          id: 2,
          subject: "Science 101",
          section: "B2-F1",
          classCode: "SCIE-B2-X5H",
          students: 25,
          assessments: 3
        }
      ],
      
      assessmentsToGrade: [
        { 
          id: 1, 
          title: "Mathematics Quiz - Algebra", 
          status: "Pending",
          subject: "Mathematics",
          dueDate: "Aug 20, 2025",
          progress: 45,
          completed: 15,
          total: 32,
          recentSubmissions: ['👩', '👨', '👧', '👦', '🧑']
        },
        { 
          id: 2, 
          title: "Science Test - Photosynthesis", 
          status: "In Progress",
          subject: "Science",
          dueDate: "Aug 22, 2025",
          progress: 78,
          completed: 25,
          total: 32,
          recentSubmissions: ['👩', '👨', '👧']
        },
        { 
          id: 3, 
          title: "History Essay - World War II", 
          status: "Pending",
          subject: "History",
          dueDate: "Aug 25, 2025",
          progress: 23,
          completed: 7,
          total: 30,
          recentSubmissions: ['👦', '🧑']
        }
      ],
      
      stats: {
        autoGradedCount: 47,
        averageScore: 78.5,
        totalStudents: 125
      },
      
      notifications: [
        { id: 1, message: "Maria Santos submitted Math Quiz 1", timeAgo: "2m ago", avatar: "👩", read: false },
        { id: 2, message: "Science Test deadline is approaching", timeAgo: "5m ago", avatar: "⏰", read: false },
        { id: 3, message: "New student joined your class", timeAgo: "10m ago", avatar: "🎓", read: false },
        { id: 4, message: "Parent meeting scheduled for tomorrow", timeAgo: "1h ago", avatar: "👨‍👩‍👧‍👦", read: true }
      ],
      
      recentMessages: [
        { 
          id: 1, 
          sender: "Maria Santos", 
          preview: "Professor, I have a question about the homework...", 
          timeAgo: "5m ago", 
          avatar: "👩",
          read: false 
        },
        { 
          id: 2, 
          sender: "John Doe", 
          preview: "Thank you for the explanation!", 
          timeAgo: "1h ago", 
          avatar: "👨",
          read: false 
        }
      ],
      
      reminders: [
        { id: 1, text: "Grade Biology exam papers", dueDate: "Today 3:00 PM", urgent: true, completed: false },
        { id: 2, text: "Prepare presentation for faculty meeting", dueDate: "Tomorrow 9:00 AM", urgent: false, completed: false },
        { id: 3, text: "Submit semester grades", dueDate: "Aug 20, 2025", urgent: true, completed: false },
        { id: 4, text: "Review curriculum updates", dueDate: "Aug 22, 2025", urgent: false, completed: true }
      ],
      
      newReminder: {
        text: '',
        dueDate: '',
        urgent: false
      },
      
      todaySchedule: [
        { id: 1, time: "9:00 AM", title: "Mathematics 101", location: "Room A-204" },
        { id: 2, time: "11:00 AM", title: "Advanced Calculus", location: "Room B-108" },
        { id: 3, time: "2:00 PM", title: "Faculty Meeting", location: "Conference Room" },
        { id: 4, time: "4:00 PM", title: "Student Consultation", location: "Office 305" }
      ],
      
      liveActivities: [
        { id: 1, student: "Maria Santos", action: "submitted", target: "Math Quiz 1", timeAgo: "2m ago", avatar: "👩", score: 95 },
        { id: 2, student: "John Doe", action: "started", target: "Science Lab Report", timeAgo: "5m ago", avatar: "👨" },
        { id: 3, student: "Sarah Kim", action: "completed", target: "History Essay", timeAgo: "8m ago", avatar: "👧", score: 87 },
        { id: 4, student: "Mike Johnson", action: "submitted late", target: "Chemistry Homework", timeAgo: "15m ago", avatar: "👦", score: 78 }
      ],
      
      chatContacts: [
        { 
          id: 1, 
          name: "Maria Santos", 
          avatar: "👩", 
          online: true, 
          lastSeen: "now", 
          lastMessage: "Professor, I have a question about the homework..."
        },
        { 
          id: 2, 
          name: "John Doe", 
          avatar: "👨", 
          online: false, 
          lastSeen: "1h ago", 
          lastMessage: "Thank you for the help!"
        },
        { 
          id: 3, 
          name: "Sarah Kim", 
          avatar: "👧", 
          online: true, 
          lastSeen: "now", 
          lastMessage: "When is the next exam?"
        }
      ],
      
      currentChatMessages: [],
    }
  },
  
  computed: {
    filteredAssessments() {
      return this.assessmentsToGrade.filter(assessment => {
        const subjectMatch = !this.selectedSubject || assessment.subject.toLowerCase().includes(this.selectedSubject);
        const statusMatch = !this.selectedStatus || assessment.status.toLowerCase().replace(' ', '-') === this.selectedStatus;
        return subjectMatch && statusMatch;
      });
    },
    
    filteredChatContacts() {
      if (!this.chatSearchQuery) return this.chatContacts;
      return this.chatContacts.filter(contact => 
        contact.name.toLowerCase().includes(this.chatSearchQuery.toLowerCase())
      );
    }
  },
  
  methods: {
    // Navigation toggles
    toggleNotifications() {
      this.showNotifications = !this.showNotifications;
      this.showMessages = false;
      this.showProfile = false;
    },
    
    toggleMessages() {
      this.showMessages = !this.showMessages;
      this.showNotifications = false;
      this.showProfile = false;
    },
    
    toggleProfile() {
      this.showProfile = !this.showProfile;
      this.showNotifications = false;
      this.showMessages = false;
    },
    
    // Notification actions
    markAllNotificationsRead() {
      this.notifications.forEach(n => n.read = true);
      this.unreadNotifications = 0;
    },
    
    handleNotificationClick(notification) {
      notification.read = true;
      this.unreadNotifications = Math.max(0, this.unreadNotifications - 1);
      // Handle navigation based on notification type
      console.log('Navigate to:', notification.message);
    },
    
    // Chat functions
    toggleChatBox() {
      this.showChatBox = !this.showChatBox;
    },
    
    minimizeChatBox() {
      this.showChatBox = false;
    },
    
    closeChatBox() {
      this.showChatBox = false;
      this.currentChatUser = null;
    },
    
    openChatWith(senderName) {
      const contact = this.chatContacts.find(c => c.name === senderName);
      if (contact) {
        this.startChatWith(contact);
      }
      this.showMessages = false;
    },
    
    startChatWith(contact) {
      this.currentChatUser = contact;
      this.loadChatMessages(contact.id);
      this.showChatBox = true;
    },
    
    backToContacts() {
      this.currentChatUser = null;
    },
    
    loadChatMessages(contactId) {
      // Simulate loading chat messages
      this.currentChatMessages = [
        { id: 1, sender: 'student', text: 'Hello Professor!', time: '10:30 AM' },
        { id: 2, sender: 'teacher', text: 'Hi! How can I help you?', time: '10:32 AM' },
        { id: 3, sender: 'student', text: 'I have a question about the homework.', time: '10:35 AM' }
      ];
      // Scroll to bottom after loading
      this.$nextTick(() => {
        const chatMessages = this.$refs.chatMessages;
        if (chatMessages) {
          chatMessages.scrollTop = chatMessages.scrollHeight;
        }
      });
    },
    
    sendMessage() {
      if (this.newMessage.trim()) {
        this.currentChatMessages.push({
          id: Date.now(),
          sender: 'teacher',
          text: this.newMessage,
          time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
        });
        this.newMessage = '';
        
        // Scroll to bottom
        this.$nextTick(() => {
          const chatMessages = this.$refs.chatMessages;
          if (chatMessages) {
            chatMessages.scrollTop = chatMessages.scrollHeight;
          }
        });
      }
    },
    
    // Reminder functions
    addReminder() {
      if (this.newReminder.text && this.newReminder.dueDate) {
        this.reminders.push({
          id: Date.now(),
          text: this.newReminder.text,
          dueDate: new Date(this.newReminder.dueDate).toLocaleDateString(),
          urgent: this.newReminder.urgent,
          completed: false
        });
        
        this.newReminder = { text: '', dueDate: '', urgent: false };
        this.showReminderModal = false;
      }
    },
    
    toggleReminder(id) {
      const reminder = this.reminders.find(r => r.id === id);
      if (reminder) {
        reminder.completed = !reminder.completed;
      }
    },
    
    // Assessment actions
    uploadAssessment() {
      alert("Opening assessment upload wizard...");
    },
    
    gradeAssessment(id) {
      alert(`Starting auto-grading for assessment ${id}`);
    },
    
    viewAssessmentDetails(id) {
      alert(`Viewing details for assessment ${id}`);
    },
    
    shareAssessment(id) {
      alert(`Sharing assessment ${id}`);
    },
    
    toggleAssessmentMenu(id) {
      console.log(`Toggle menu for assessment ${id}`);
    },
    
    // Navigation actions
    navigateToMyClasses() {
      alert("Navigating to My Classes...");
    },

    createQuiz() {
      alert("Creating new quiz...");
    },
    
    scheduleClass() {
      alert("Opening class scheduler...");
    },
    
    uploadMaterial() {
      alert("Opening material uploader...");
    },
    
    viewAssessments() {
      alert("Navigating to assessments page...");
    },
    
    viewAnalytics() {
      alert("Opening analytics dashboard...");
    },
    
    viewPending() {
      alert("Showing pending tasks...");
    },
    
    viewStudents() {
      alert("Opening student management...");
    },
    
    // Class and Section methods
    copyClassCode(code) {
      if (navigator.clipboard) {
        navigator.clipboard.writeText(code).then(() => {
          alert('Class code copied to clipboard!');
        }).catch(err => {
          console.error('Could not copy text: ', err);
          alert('Failed to copy code. Please copy it manually.');
        });
      } else {
        // Fallback for older browsers
        const el = document.createElement('textarea');
        el.value = code;
        document.body.appendChild(el);
        el.select();
        document.execCommand('copy');
        document.body.removeChild(el);
        alert('Class code copied to clipboard!');
      }
    },

    viewClassDetails(id) {
      alert(`Viewing details for class ${id}`);
    },
    
    // Close dropdowns when clicking outside
    closeDropdowns() {
      this.showNotifications = false;
      this.showMessages = false;
      this.showProfile = false;
    }
  },
  
  mounted() {
    // Close dropdowns when clicking outside
    document.addEventListener('click', (e) => {
      if (!e.target.closest('.nav-item')) {
        this.closeDropdowns();
      }
    });
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

/* General font and background changes */
:root {
  --primary-color: #3D8D7A; /* Dark Green */
  --secondary-color: #B3D8A8; /* Light Muted Green */
  --accent-color: #A3D1C6; /* Light Blue-Green for highlights */
  --background-color: #FBFFE4; /* Light Yellow-White */
  --card-background: #FFFFFF;
  --text-color: #495057;
  --light-text-color: #ADB5BD;
  --border-color: #E9ECEF;
  --shadow-color: rgba(0, 0, 0, 0.08);
}

body {
  font-family: 'Poppins', sans-serif;
  color: var(--text-color);
  background-color: var(--background-color);
}

.dashboard-wrapper {
  background: var(--background-color);
  min-height: 100vh;
  padding: 0;
  display: flex;
  flex-direction: column;
}

/* Top Navigation Bar */
.top-nav {
  background: var(--card-background);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--border-color);
  box-shadow: 0 2px 10px var(--shadow-color);
  width: 100%;
  position: sticky;
  top: 0;
  z-index: 100;
  padding: 1rem 0;
}

.nav-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 1.5rem;
}

.nav-left {
  display: flex;
  align-items: center;
  gap: 24px;
}

.logo {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 1.2rem;
  font-weight: 700;
}

.logo-text {
  color: var(--primary-color);
  font-weight: 700;
}

.logo-icon {
  font-size: 1.5rem;
}

.search-container {
  position: relative;
}

.search-input {
  width: 350px;
  padding: 10px 40px 10px 16px;
  border: 2px solid var(--border-color);
  border-radius: 25px;
  background: var(--background-color);
  font-size: 0.9rem;
  transition: all 0.3s ease;
}

.search-input:focus {
  outline: none;
  border-color: var(--accent-color);
  background: white;
  box-shadow: 0 0 0 3px rgba(163, 209, 198, 0.5);
}

.search-icon {
  position: absolute;
  right: 16px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--light-text-color);
}

.nav-right {
  display: flex;
  align-items: center;
  gap: 16px;
}

.nav-icon {
  position: relative;
  font-size: 1.5rem;
  padding: 8px;
  border-radius: 50%;
  background: var(--background-color);
  transition: all 0.3s ease;
  cursor: pointer;
}

.nav-icon:hover {
  background: var(--border-color);
  transform: scale(1.1);
}

.profile-avatar {
  font-size: 2rem;
  padding: 4px;
  cursor: pointer;
}

.notification-badge, .message-badge {
  position: absolute;
  top: -2px;
  right: -2px;
  background: var(--accent-color);
  color: white;
  border-radius: 50%;
  width: 20px;
  height: 20px;
  font-size: 0.7rem;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
}

/* Dropdown Menus */
.dropdown-menu {
  position: absolute;
  top: 100%;
  right: 0;
  background: var(--card-background);
  border-radius: 16px;
  box-shadow: 0 10px 40px var(--shadow-color);
  border: 1px solid var(--border-color);
  min-width: 300px;
  max-height: 400px;
  overflow-y: auto;
  z-index: 1000;
}

.notifications-menu {
  width: 380px;
}

.messages-menu {
  width: 350px;
}

.dropdown-header {
  padding: 16px 20px;
  border-bottom: 1px solid var(--border-color);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.dropdown-header h3 {
  margin: 0;
  color: var(--primary-color);
  font-size: 1.1rem;
}

.mark-all-read, .new-message-btn {
  background: none;
  border: none;
  color: var(--accent-color);
  font-size: 0.8rem;
  cursor: pointer;
  text-decoration: underline;
}

.notifications-list, .messages-list {
  max-height: 300px;
  overflow-y: auto;
}

.notification-item, .message-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 20px;
  border-bottom: 1px solid rgba(163, 209, 198, 0.1);
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
}

.notification-item:hover, .message-item:hover {
  background: var(--background-color);
}

.notification-item.unread, .message-item.unread {
  background: rgba(163, 209, 198, 0.05);
}

.notification-avatar, .message-avatar {
  font-size: 1.5rem;
  flex-shrink: 0;
}

.notification-content, .message-content {
  flex: 1;
}

.notification-text, .message-preview {
  margin: 0;
  font-size: 0.9rem;
  color: var(--text-color);
  line-height: 1.4;
}

.notification-time, .message-time {
  font-size: 0.75rem;
  color: var(--light-text-color);
}

.notification-dot, .message-dot {
  width: 8px;
  height: 8px;
  background: var(--primary-color);
  border-radius: 50%;
  flex-shrink: 0;
}

.message-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 4px;
}

.sender-name {
  font-weight: 600;
  color: var(--primary-color);
  font-size: 0.9rem;
}

.dropdown-footer {
  padding: 12px 20px;
  text-align: center;
  border-top: 1px solid var(--border-color);
}

.see-all-btn {
  background: none;
  border: none;
  color: var(--accent-color);
  font-weight: 600;
  cursor: pointer;
}

/* Profile Menu */
.profile-menu {
  width: 250px;
}

.profile-info {
  padding: 20px;
  display: flex;
  align-items: center;
  gap: 12px;
  border-bottom: 1px solid var(--border-color);
}

.profile-pic {
  font-size: 2.5rem;
}

.profile-info h4 {
  margin: 0 0 4px 0;
  color: var(--primary-color);
  font-size: 1rem;
}

.profile-info p {
  margin: 0;
  font-size: 0.8rem;
  color: var(--light-text-color);
}

.profile-actions {
  padding: 8px 0;
}

.profile-btn {
  width: 100%;
  padding: 12px 20px;
  background: none;
  border: none;
  text-align: left;
  cursor: pointer;
  font-size: 0.9rem;
  color: var(--text-color);
  transition: all 0.3s ease;
}

.profile-btn:hover {
  background: var(--background-color);
  color: var(--primary-color);
}

.profile-btn.logout {
  color: #DC3545; /* A standard red for log out */
  border-top: 1px solid var(--border-color);
}

/* Dashboard Content */
.dashboard-content {
  display: grid;
  grid-template-columns: minmax(280px, 20%) 1fr 320px;
  gap: 2rem;
  flex: 1;
  width: 100%;
  box-sizing: border-box;
  max-width: 1400px;
  margin: 0 auto;
  padding: 1.5rem;
}

/* Sidebar */
.sidebar {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  position: sticky;
  top: calc(80px + 1.5rem);
  height: calc(100vh - 80px - 3rem);
  overflow-y: auto;
}

.sidebar-section {
  background: var(--card-background);
  border-radius: 16px;
  padding: 20px;
  border: 1px solid var(--border-color);
  box-shadow: 0 4px 15px var(--shadow-color);
  flex: 1;
}

.sidebar-title {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 0 0 16px 0;
  color: var(--primary-color);
  font-size: 1.1rem;
  font-weight: 600;
}

.add-reminder {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: var(--secondary-color);
  color: white;
  border: none;
  cursor: pointer;
  font-size: 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.quick-actions {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.action-btn {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  background: var(--background-color);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 0.9rem;
  color: var(--text-color);
}

.action-btn:hover {
  background: var(--border-color);
  transform: none;
  box-shadow: 0 2px 8px var(--shadow-color);
}

.action-icon {
  font-size: 1.2rem;
}

.reminders-list, .schedule-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.reminder-item {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 12px;
  background: var(--background-color);
  border-radius: 12px;
  border-left: 4px solid var(--border-color);
  transition: all 0.3s ease;
}

.reminder-item.urgent {
  border-left-color: #FFC107; /* A standard yellow for urgency */
}

.reminder-item.completed {
  opacity: 0.6;
  text-decoration: line-through;
}

.reminder-checkbox input {
  margin: 0;
  cursor: pointer;
}

.reminder-content {
  flex: 1;
}

.reminder-text {
  margin: 0 0 4px 0;
  font-size: 0.9rem;
  color: var(--text-color);
}

.reminder-date {
  font-size: 0.8rem;
  color: var(--light-text-color);
}

.schedule-item {
  display: flex;
  gap: 12px;
  padding: 12px;
  background: var(--background-color);
  border-radius: 12px;
  border-left: 4px solid var(--secondary-color);
}

.schedule-time {
  font-weight: 600;
  color: var(--primary-color);
  font-size: 0.8rem;
  min-width: 60px;
}

.schedule-details h4 {
  margin: 0 0 2px 0;
  font-size: 0.9rem;
  color: var(--primary-color);
}

.schedule-details p {
  margin: 0;
  font-size: 0.8rem;
  color: var(--light-text-color);
}

/* Main Content */
.main-content {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  width: 100%;
}

/* Header Section */
.header-section {
  margin-bottom: 8px;
}

.welcome-content {
  text-align: left;
  margin-bottom: 24px;
}

.main-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: var(--primary-color);
  margin: 0 0 8px 0;
}

.welcome-text {
  font-size: 1rem;
  color: var(--text-color);
}

/* Stats Grid */
.quick-stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 1rem;
}

.stat-card {
  background: var(--card-background);
  padding: 24px;
  border-radius: 16px;
  border: 1px solid var(--border-color);
  box-shadow: 0 4px 15px var(--shadow-color);
  display: flex;
  align-items: center;
  gap: 16px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.stat-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
}

.stat-icon {
  font-size: 2.5rem;
  flex-shrink: 0;
  color: var(--secondary-color);
}

.stat-info {
  display: flex;
  flex-direction: column;
}

.stat-number {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--primary-color);
}

.stat-label {
  font-size: 0.9rem;
  color: var(--light-text-color);
}

/* Core Feature Section */
.core-feature {
  background: var(--card-background);
  border-radius: 16px;
  padding: 24px;
  border: 1px solid var(--border-color);
  box-shadow: 0 4px 15px var(--shadow-color);
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.section-title {
  display: flex;
  align-items: center;
  gap: 10px;
  margin: 0;
  font-size: 1.5rem;
  color: var(--primary-color);
}

.title-icon {
  font-size: 1.8rem;
  color: var(--secondary-color);
}

.header-actions {
  display: flex;
  gap: 12px;
}

.filter-btn, .primary-btn {
  padding: 10px 18px;
  border-radius: 25px;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.primary-btn {
  background: var(--primary-color);
  color: white;
  border: 1px solid var(--primary-color);
}

.primary-btn:hover {
  background: var(--secondary-color);
  border-color: var(--secondary-color);
}

.filter-btn {
  background: none;
  border: 1px solid var(--border-color);
  color: var(--text-color);
}

.filter-btn:hover {
  background: var(--background-color);
  color: var(--primary-color);
}

.btn-icon {
  font-size: 1.1rem;
}

.filters-bar {
  display: flex;
  gap: 1rem;
  margin-bottom: 20px;
}

.filter-select {
  padding: 8px 12px;
  border-radius: 8px;
  border: 1px solid var(--border-color);
  background: var(--background-color);
  color: var(--text-color);
}

.assessments-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}

.assessment-card {
  background: var(--card-background);
  border-radius: 16px;
  padding: 24px;
  border: 1px solid var(--border-color);
  box-shadow: 0 4px 15px var(--shadow-color);
  display: flex;
  flex-direction: column;
  transition: all 0.3s ease;
}

.assessment-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.assessment-title, .class-title {
  font-size: 1.2rem;
  font-weight: 600;
  color: var(--primary-color);
  margin: 0;
  transition: all 0.3s ease;
}

.card-actions-header {
  display: flex;
  align-items: center;
  gap: 8px;
}

.status-badge, .section-tag {
  font-size: 0.75rem;
  font-weight: 700;
  padding: 4px 8px;
  border-radius: 12px;
  text-transform: uppercase;
}

.status-badge.pending {
  background: #FFC107;
  color: #FFFFFF;
}

.status-badge.in-progress {
  background: var(--accent-color);
  color: var(--primary-color);
}

.status-badge.completed {
  background: var(--secondary-color);
  color: var(--primary-color);
}

.section-tag {
  background: var(--secondary-color);
  color: var(--primary-color);
}

.menu-btn {
  background: none;
  border: none;
  font-size: 1.2rem;
  color: var(--light-text-color);
  cursor: pointer;
}

.card-content {
  flex: 1;
}

.assessment-meta {
  display: flex;
  gap: 12px;
  font-size: 0.85rem;
  margin-bottom: 12px;
}

.subject-tag, .due-date {
  color: var(--light-text-color);
}

.progress-container {
  margin-bottom: 12px;
}

.progress-bar {
  width: 100%;
  height: 8px;
  background: var(--border-color);
  border-radius: 4px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: var(--secondary-color);
  border-radius: 4px;
  transition: width 0.5s ease;
}

.progress-text {
  font-size: 0.8rem;
  color: var(--light-text-color);
  margin: 4px 0 0;
}

.student-avatars {
  display: flex;
  align-items: center;
  margin-bottom: 16px;
}

.avatar-group {
  display: flex;
  align-items: center;
}

.student-avatar {
  width: 30px;
  height: 30px;
  background: rgba(163, 209, 198, 0.5);
  color: var(--primary-color);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1rem;
  margin-right: -10px;
  border: 2px solid var(--card-background);
}

.more-avatars {
  width: 30px;
  height: 30px;
  background: rgba(163, 209, 198, 0.2);
  color: var(--secondary-color);
  font-size: 0.8rem;
  font-weight: 600;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-left: 10px;
}

.card-actions {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: auto;
  padding-top: 16px;
  border-top: 1px solid var(--border-color);
}

.secondary-btn, .tertiary-btn, .icon-btn {
  padding: 8px 16px;
  border-radius: 20px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.secondary-btn {
  background: var(--background-color);
  color: var(--secondary-color);
  border: 1px solid var(--border-color);
  display: flex;
  align-items: center;
  gap: 8px;
}

.secondary-btn:hover {
  background: var(--border-color);
}

.tertiary-btn {
  background: none;
  border: 1px solid var(--border-color);
  color: var(--text-color);
}

.tertiary-btn:hover {
  background: var(--background-color);
}

.icon-btn {
  background: none;
  border: none;
  font-size: 1.5rem;
  color: var(--light-text-color);
}

.icon-btn:hover {
  color: var(--secondary-color);
}

/* NEW STYLES FOR CLASS CARD */
.class-card {
  background: var(--card-background);
  border-radius: 16px;
  padding: 24px;
  border: 1px solid var(--border-color);
  box-shadow: 0 4px 15px var(--shadow-color);
  display: flex;
  flex-direction: column;
  transition: all 0.3s ease;
}

.class-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
}

.class-card .card-content {
  display: flex;
  flex-direction: column;
  flex: 1;
}

.class-code-label {
  font-size: 0.8rem;
  color: var(--light-text-color);
  margin: 0;
}

.class-code-display {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 15px;
  background-color: var(--background-color);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  margin-top: 8px;
  margin-bottom: 16px;
}

.class-code-display p {
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--primary-color);
  margin: 0;
  user-select: all;
}

.class-stats {
  display: flex;
  gap: 20px;
}

.stat-item {
  display: flex;
  flex-direction: column;
}

.stat-item .stat-number {
  font-size: 1.2rem;
  color: var(--primary-color);
  font-weight: 700;
}

.stat-item .stat-label {
  font-size: 0.8rem;
  color: var(--light-text-color);
}

.class-card .card-actions {
  justify-content: center;
}

.class-card .secondary-btn {
  width: 100%;
  justify-content: center;
}

/* Live Activity */
.activity-feed {
  background: var(--card-background);
  border-radius: 16px;
  padding: 24px;
  border: 1px solid var(--border-color);
  box-shadow: 0 4px 15px var(--shadow-color);
  height: calc(100vh - 80px - 3rem);
  overflow-y: auto;
  position: sticky;
  top: calc(80px + 1.5rem);
}

.activity-feed .section-header {
  margin-bottom: 12px;
}

.activity-feed .section-title {
  font-size: 1.2rem;
  margin: 0;
}

.activity-feed .view-all-btn {
  background: none;
  border: none;
  color: var(--secondary-color);
  font-size: 0.8rem;
  text-decoration: underline;
  cursor: pointer;
}

.activity-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.activity-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px;
  background: var(--background-color);
  border-radius: 12px;
  transition: all 0.3s ease;
}

.activity-item:hover {
  background: var(--border-color);
}

.activity-avatar {
  font-size: 1.5rem;
  flex-shrink: 0;
}

.activity-content {
  flex: 1;
}

.activity-text {
  margin: 0;
  font-size: 0.9rem;
  line-height: 1.4;
  color: var(--text-color);
}

.activity-target {
  font-style: italic;
  font-weight: 600;
  color: var(--primary-color);
}

.activity-time {
  font-size: 0.75rem;
  color: var(--light-text-color);
}

.activity-score {
  font-size: 1rem;
  font-weight: 700;
  color: var(--secondary-color);
  flex-shrink: 0;
}

/* Chat Container */
.chat-container {
  position: fixed;
  bottom: 1.5rem;
  right: 1.5rem;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 1.5rem;
  z-index: 1000;
}

.floating-chat {
  position: relative;
  width: 60px;
  height: 60px;
  background: var(--primary-color);
  border-radius: 50%;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.floating-chat:hover {
  transform: translateY(-4px);
}

.chat-icon {
  font-size: 2rem;
  color: white;
}

.chat-badge {
  position: absolute;
  top: -4px;
  right: -4px;
  background: #DC3545; /* A standard red for new messages */
  color: white;
  border-radius: 50%;
  width: 24px;
  height: 24px;
  font-size: 0.8rem;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
}

/* Chat Box */
.chatbox {
  width: 350px;
  height: 450px;
  background: var(--card-background);
  border-radius: 16px;
  box-shadow: 0 10px 40px var(--shadow-color);
  border: 1px solid var(--border-color);
  display: flex;
  flex-direction: column;
  position: absolute;
  right: 0;
  bottom: 70px;
  opacity: 0;
  visibility: hidden;
  transform: translateY(20px);
  transition: transform 0.3s ease-in-out, opacity 0.3s ease-in-out, visibility 0.3s;
}

.chatbox.open {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}

.chatbox-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 20px;
  background: var(--primary-color);
  color: white;
  border-top-left-radius: 16px;
  border-top-right-radius: 16px;
}

.chatbox-header h3 {
  margin: 0;
  font-size: 1rem;
}

.chatbox-controls {
  display: flex;
  gap: 8px;
}

.minimize-btn, .close-btn {
  background: none;
  border: none;
  color: white;
  font-size: 1.2rem;
  cursor: pointer;
}

/* Chat Contacts */
.chat-contacts {
  display: flex;
  flex-direction: column;
  flex: 1;
  overflow-y: auto;
}

.search-contacts {
  padding: 12px 20px;
  border-bottom: 1px solid var(--border-color);
}

.contact-search {
  width: 100%;
  padding: 8px 12px;
  border-radius: 20px;
  border: 1px solid var(--border-color);
  font-size: 0.9rem;
}

.contacts-list {
  flex: 1;
  overflow-y: auto;
}

.contact-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 20px;
  border-bottom: 1px solid var(--border-color);
  cursor: pointer;
  transition: all 0.3s ease;
}

.contact-item:hover {
  background: var(--background-color);
}

.contact-avatar {
  font-size: 1.5rem;
  flex-shrink: 0;
}

.contact-info {
  flex: 1;
}

.contact-info h4 {
  margin: 0 0 4px 0;
  font-size: 0.9rem;
  color: var(--primary-color);
}

.last-message {
  margin: 0;
  font-size: 0.8rem;
  color: var(--light-text-color);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.contact-status {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 4px;
}

.online-indicator {
  width: 10px;
  height: 10px;
  background: gray;
  border-radius: 50%;
}

.online-indicator.online {
  background: #80C478;
}

.last-seen {
  font-size: 0.7rem;
  color: var(--light-text-color);
}

/* Active Chat */
.active-chat {
  display: flex;
  flex-direction: column;
  flex: 1;
}

.chat-user-header {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 20px;
  border-bottom: 1px solid var(--border-color);
  cursor: pointer;
}

.back-arrow {
  font-size: 1.5rem;
  color: var(--secondary-color);
  transition: transform 0.2s ease;
}

.back-arrow:hover {
  transform: translateX(-4px);
}

.chat-user-info {
  display: flex;
  align-items: center;
  gap: 12px;
}

.chat-user-avatar {
  font-size: 1.5rem;
}

.chat-messages {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.message {
  max-width: 80%;
  padding: 10px 15px;
  border-radius: 20px;
}

.message.sent {
  background: var(--primary-color);
  color: white;
  align-self: flex-end;
  border-bottom-right-radius: 4px;
}

.message.received {
  background: var(--background-color);
  color: var(--text-color);
  align-self: flex-start;
  border-bottom-left-radius: 4px;
}

.message-content {
  display: flex;
  flex-direction: column;
}

.message p {
  margin: 0;
}

.message-time {
  font-size: 0.7rem;
  align-self: flex-end;
  color: rgba(255, 255, 255, 0.7);
  margin-top: 4px;
}

.message.received .message-time {
  color: var(--light-text-color);
}

.chat-input-container {
  padding: 12px 20px;
  border-top: 1px solid var(--border-color);
  display: flex;
  align-items: center;
  gap: 10px;
}

.chat-input {
  flex: 1;
  padding: 8px 16px;
  border-radius: 20px;
  border: 1px solid var(--border-color);
}

.send-btn {
  background: var(--accent-color);
  color: white;
  border: none;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  font-size: 1.2rem;
  cursor: pointer;
}

/* Modal */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 2000;
  transition: all 0.3s ease;
}

.modal {
  background: var(--card-background);
  border-radius: 16px;
  box-shadow: 0 10px 40px var(--shadow-color);
  width: 400px;
  max-width: 90%;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  border-bottom: 1px solid var(--border-color);
}

.modal-header h3 {
  margin: 0;
  color: var(--primary-color);
}

.close-modal {
  background: none;
  border: none;
  font-size: 1.5rem;
  color: var(--secondary-color);
  cursor: pointer;
}

.modal-content {
  padding: 20px;
}

.form-group {
  margin-bottom: 16px;
}

.form-group label {
  display: block;
  font-size: 0.9rem;
  color: var(--text-color);
  margin-bottom: 8px;
}

.form-group input {
  width: 100%;
  padding: 10px;
  border-radius: 8px;
  border: 1px solid var(--border-color);
}

.modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
}

.cancel-btn, .add-btn {
  padding: 10px 20px;
  border-radius: 25px;
  font-weight: 600;
  cursor: pointer;
}

.cancel-btn {
  background: none;
  border: 1px solid var(--border-color);
  color: var(--text-color);
}

.add-btn {
  background: var(--primary-color);
  color: white;
  border: none;
}

/* Scrollbar Styling */
::-webkit-scrollbar {
  width: 6px;
  background-color: transparent;
}

::-webkit-scrollbar-track {
  background: rgba(61, 141, 122, 0.1);
  border-radius: 3px;
}

::-webkit-scrollbar-thumb {
  background: rgba(61, 141, 122, 0.3);
  border-radius: 3px;
}

::-webkit-scrollbar-thumb:hover {
  background: rgba(61, 141, 122, 0.5);
}

/* Animations */
@keyframes slideIn {
  from {
    transform: translateY(-10px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.assessment-card, .activity-item, .reminder-item, .contact-item {
  animation: slideIn 0.3s ease;
}

.notification-item, .message-item {
  animation: fadeIn 0.3s ease;
}

/* Focus states for accessibility */
button:focus, input:focus, select:focus {
  outline: 2px solid var(--secondary-color);
  outline-offset: 2px;
}

/* Hover effects for better UX */
.assessment-card:hover .assessment-title {
  color: var(--primary-color);
}

/* ============================
    RESPONSIVE DESIGN 
   ============================ */

/* For tablets and smaller desktops */
@media screen and (max-width: 1200px) {
  .dashboard-content {
    grid-template-columns: 1fr;
    padding: 1rem;
    gap: 1rem;
  }

  .sidebar, .activity-feed {
    position: static;
    height: auto;
    overflow-y: visible;
  }
  
  .sidebar-section, .core-feature, .activity-feed {
      margin-bottom: 1.5rem;
  }

  .nav-left {
    gap: 16px;
  }

  .search-input {
    width: 250px;
  }
}

/* For mobile devices */
@media screen and (max-width: 768px) {
  .nav-content {
    flex-wrap: wrap;
    gap: 1rem;
    padding: 0 1rem;
  }

  .nav-left {
    width: 100%;
    justify-content: space-between;
    gap: 0;
  }

  .search-container {
    order: 1;
    width: 100%;
  }

  .search-input {
    width: 100%;
  }

  .nav-right {
    width: 100%;
    justify-content: space-around;
    gap: 0;
  }

  .dashboard-content {
    padding: 1rem;
  }

  .main-title {
    font-size: 2rem;
  }

  .quick-stats-grid {
    grid-template-columns: 1fr 1fr;
  }
  
  .card-actions {
      flex-direction: column;
      align-items: stretch;
      gap: 10px;
  }

  .secondary-btn, .tertiary-btn, .icon-btn {
      width: 100%;
      text-align: center;
      justify-content: center;
  }
  
  .icon-btn {
      padding: 10px;
  }
}

/* Hide some elements on very small screens to save space */
@media screen and (max-width: 480px) {
  .logo-text {
    display: none;
  }
  
  .welcome-content .welcome-text {
      font-size: 0.9rem;
  }

  .stat-card {
    flex-direction: column;
    text-align: center;
  }
  
  .stat-info {
      align-items: center;
  }
  
  .chatbox {
      width: 90%;
      height: 70vh;
      bottom: 20px;
      right: 50%;
      transform: translateX(50%);
  }
}
</style>