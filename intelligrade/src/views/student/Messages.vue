<template>
  <div class="page-container">
    <div class="bg-decoration">
      <div class="floating-shape shape-1"></div>
      <div class="floating-shape shape-2"></div>
      <div class="floating-shape shape-3"></div>
    </div>
    
    <div class="main-wrapper">
      <!-- Header Section -->
      <div class="section-header-card">
        <div class="section-header-left">
          <div class="section-header-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
            </svg>
          </div>
          <div>
          <div class="section-header-title">Messages</div>
            <div class="section-header-sub">Chat with your enrolled teachers and view announcements</div>
          </div>
        </div>
      </div>

      <section class="content-section">
        <div class="card-box content-card">
          <div class="tabs">
            <button 
              :class="['tab-btn', { 'active': currentTab === 'teachers' }]"
              @click="currentTab = 'teachers'"
            >
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
                <circle cx="12" cy="7" r="4"/>
              </svg>
              My Teachers
            </button>
            <button 
              :class="['tab-btn', { 'active': currentTab === 'notifications' }]"
              @click="currentTab = 'notifications'"
            >
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/>
                <path d="M13.73 21a2 2 0 0 1-3.46 0"/>
              </svg>
              Class Announcements
            </button>
          </div>

          <!-- Teachers Tab -->
          <div v-if="currentTab === 'teachers'" class="tab-content">
            <div class="section-actions">
              <div class="search-bar">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="search-icon">
                  <circle cx="11" cy="11" r="8"></circle>
                  <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
                <input type="text" v-model="searchQuery" placeholder="Search teachers or subjects..." class="search-input" />
              </div>
              <div class="filter-section">
                <select v-model="selectedSubject" class="subject-filter">
                  <option value="">All Subjects</option>
                  <option v-for="subject in enrolledSubjects" :key="subject.id" :value="subject.id">
                    {{ subject.name }}
                  </option>
                </select>
              </div>
            </div>

            <!-- Enrolled Teachers by Subject -->
            <div v-if="filteredTeachers.length === 0" class="empty-state">
              <div class="empty-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
                  <circle cx="12" cy="7" r="4"/>
                </svg>
              </div>
              <p>No teachers found</p>
              <span class="empty-subtext">Teachers from your enrolled subjects will appear here.</span>
            </div>

            <div v-else class="teachers-by-subject">
              <div v-for="subject in groupedTeachers" :key="subject.id" class="subject-group">
                <div class="subject-header">
                  <h3 class="subject-name">{{ subject.name }}</h3>
                  <span class="subject-code">{{ subject.code }}</span>
                </div>
                
                <div class="teachers-list">
                  <div 
                    v-for="teacher in subject.teachers" 
                    :key="teacher.id"
                    :class="['teacher-item', { 'has-unread': teacher.unread_count > 0 }]"
                    @click="startChatWithTeacher(teacher)"
                  >
                    <div class="teacher-info">
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
                      <span v-if="teacher.unread_count > 0" class="unread-badge">{{ teacher.unread_count }}</span>
                      <span class="last-time">{{ formatTime(teacher.last_message_time) }}</span>
                      <div class="chat-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                          <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
                        </svg>
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
                <button 
                  :class="['filter-btn', { 'active': currentFilter === 'class' }]"
                  @click="currentFilter = 'class'"
                >
                  Class Announcements
                </button>
              </div>
              <button class="action-btn" @click="clearNotifications">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <polyline points="20,6 9,17 4,12"/>
                </svg>
                Mark all read
              </button>
            </div>
            
            <div v-if="filteredNotifications.length === 0" class="empty-state">
              <div class="empty-icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/>
                  <path d="M13.73 21a2 2 0 0 1-3.46 0"/>
                </svg>
              </div>
              <p>No announcements found</p>
              <span class="empty-subtext">Class announcements and notifications will appear here.</span>
            </div>
            
            <div v-else class="notification-list">
              <div 
                v-for="notif in filteredNotifications" 
                :key="notif.notification_id" 
                :class="['notification-item', {'unread': !notif.is_read, 'class-announcement': notif.notification_type === 'announcement'}]"
                @click="openNotificationModal(notif)"
              >
                <div class="notification-header">
                  <div class="notification-source">
                    <span class="notification-icon">
                      <svg v-if="notif.notification_type === 'announcement'" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
                      </svg>
                      <svg v-else xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="12" r="10"></circle>
                        <line x1="12" y1="16" x2="12" y2="12"></line>
                        <line x1="12" y1="8" x2="12.01" y2="8"></line>
                      </svg>
                    </span>
                    <div class="source-info">
                      <span class="source-name">{{ notif.teacher_name || 'System' }}</span>
                      <span class="source-subject">{{ notif.subject_name || 'General' }}</span>
                    </div>
                  </div>
                  <div class="notification-indicators">
                    <span v-if="!notif.is_read" class="unread-label">New</span>
                  </div>
                </div>
                <div class="notification-content">
                  <p class="notif-title">{{ notif.title || notif.body }}</p>
                  <p class="notif-body">{{ notif.body }}</p>
                </div>
                <div class="notification-footer">
                  <span class="notif-timestamp">{{ formatTime(notif.created_at) }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>

    <!-- Chat Modal -->
    <div v-if="isModalOpen" class="modal-overlay" @click.self="closeModal">
      <div class="modal-content">
        <div class="modal-header">
          <button @click="closeModal" class="close-btn">&times;</button>
          <div class="header-info">
            <div class="teacher-avatar">
              <span>{{ activeTeacher?.teacher_name?.[0] || 'T' }}</span>
            </div>
            <div class="header-details">
              <h2 class="modal-title">{{ activeTeacher?.teacher_name }}</h2>
              <span class="subject-info">{{ activeTeacher?.subject_name }}</span>
            </div>
          </div>
        </div>
        <div class="modal-body">
          <div class="messages-container" ref="messagesContainer">
            <div 
              v-for="message in currentMessages" 
              :key="message.id" 
              :class="['message-bubble', { 'sent': message.sender_id === currentStudentId, 'received': message.sender_id !== currentStudentId }]"
            >
              <p class="message-text">{{ message.content }}</p>
              <span class="message-time">{{ formatTime(message.sent_at) }}</span>
            </div>
            <div v-if="currentMessages.length === 0" class="no-messages">
              <p>No messages yet. Start the conversation!</p>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <div class="message-input-area">
            <input 
              type="text" 
              v-model="newMessage" 
              @keyup.enter="sendMessage" 
              placeholder="Type your message to your teacher..." 
              class="message-input"
            />
            <button class="send-btn" @click="sendMessage" :disabled="!newMessage.trim()">
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
import { ref, computed, onMounted, onUnmounted, nextTick } from 'vue'
import { supabase } from '@/supabase.js'

// State management
const currentTab = ref('teachers')
const currentFilter = ref('all')
const searchQuery = ref('')
const selectedSubject = ref('')
const isModalOpen = ref(false)
const activeTeacher = ref(null)
const newMessage = ref('')
const messagesContainer = ref(null)
const isLoading = ref(false)

// Real-time subscriptions
let messageChannel = null

// Data
const enrolledSubjects = ref([])
const enrolledTeachers = ref([])
const notifications = ref([])
const currentMessages = ref([])
const currentUser = ref(null)
const currentStudentId = ref(null)

// Computed properties
const filteredTeachers = computed(() => {
  let teachers = enrolledTeachers.value
  
  if (selectedSubject.value) {
    teachers = teachers.filter(t => t.subject_id === selectedSubject.value)
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

const filteredNotifications = computed(() => {
  let notifs = notifications.value
  
  if (currentFilter.value === 'unread') {
    notifs = notifs.filter(n => !n.is_read)
  } else if (currentFilter.value === 'class') {
    notifs = notifs.filter(n => n.notification_type === 'announcement')
  }
  
  return notifs
})

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

// Data loading methods - FIXED for your database schema
const loadEnrolledSubjectsAndTeachers = async () => {
  try {
    if (!currentStudentId.value) {
      console.error('No student ID available')
      return
    }
    
    isLoading.value = true
    console.log('Loading subjects and teachers for student:', currentStudentId.value)
    
    // Step 1: Get enrollments
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
    
    // Step 2: Get sections - FIXED: using 'name' instead of 'section_name'
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
      console.error('DETAILED sections error:', JSON.stringify(sectionsError, null, 2))
      console.error('Error message:', sectionsError.message)
      console.error('Error details:', sectionsError.details)
      console.error('Error hint:', sectionsError.hint)
      throw sectionsError
    }
    
    console.log('Sections found:', sections)
    
    if (!sections || sections.length === 0) {
      enrolledSubjects.value = []
      enrolledTeachers.value = []
      return
    }
    
    // Step 3: Get subjects - FIXED: getting teacher_id from subjects
    const subjectIds = [...new Set(sections.map(s => s.subject_id))]
    const { data: subjects, error: subjectsError } = await supabase
      .from('subjects')
      .select('id, name, teacher_id')
      .in('id', subjectIds)
    
    if (subjectsError) throw subjectsError
    
    // Step 4: Get teachers - FIXED: from teachers table, not profiles
    const teacherIds = [...new Set(subjects.map(s => s.teacher_id))]
    const { data: teachers, error: teachersError } = await supabase
      .from('teachers')
      .select('id, full_name, email')
      .in('id', teacherIds)
    
    if (teachersError) throw teachersError
    
    console.log('Subjects:', subjects)
    console.log('Teachers:', teachers)
    
    // Process the data
    const processedSubjects = []
    const processedTeachers = []
    const subjectMap = new Map()
    
    // Create maps for easy lookup
    const subjectsDataMap = new Map(subjects.map(s => [s.id, s]))
    const teachersDataMap = new Map(teachers.map(t => [t.id, t]))
    
    for (const section of sections) {
      const subject = subjectsDataMap.get(section.subject_id)
      if (!subject) continue
      
      const teacher = teachersDataMap.get(subject.teacher_id)
      if (!teacher) continue
      
      // Add subject if not exists
      if (!subjectMap.has(subject.id)) {
        processedSubjects.push({
          id: subject.id,
          name: subject.name,
          code: section.section_code
        })
        subjectMap.set(subject.id, true)
      }
      
      // Get unread count
      const { count: unreadCount } = await supabase
        .from('messages')
        .select('*', { count: 'exact', head: true })
        .eq('section_id', section.id)
        .eq('sender_id', teacher.id)
        .eq('recipient_id', currentStudentId.value)
        .eq('is_read', false)
      
      // Get last message
      const { data: lastMsgData } = await supabase
        .from('messages')
        .select('message_text, sent_at')
        .eq('section_id', section.id)
        .or(`and(sender_id.eq.${currentStudentId.value},recipient_id.eq.${teacher.id}),and(sender_id.eq.${teacher.id},recipient_id.eq.${currentStudentId.value})`)
        .order('sent_at', { ascending: false })
        .limit(1)
      
      const lastMsg = lastMsgData && lastMsgData.length > 0 ? lastMsgData[0] : null
      
      // Add teacher
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
        name: teacher.full_name
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
    
    const { data: sections } = await supabase
      .from('sections')
      .select('id, subject_id')
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
      
      return {
        notification_id: msg.id,
        title: 'Class Announcement',
        body: msg.message_text,
        created_at: msg.sent_at,
        is_read: msg.is_read,
        notification_type: 'announcement',
        teacher_name: sender?.full_name,
        subject_name: subject?.name
      }
    })
    
    console.log('Loaded notifications:', notifications.value)
    
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
    
    const { data: messages, error } = await supabase
      .from('messages')
      .select('*')
      .eq('section_id', sectionId)
      .eq('message_type', 'direct')
      .or(`and(sender_id.eq.${currentStudentId.value},recipient_id.eq.${teacherId}),and(sender_id.eq.${teacherId},recipient_id.eq.${currentStudentId.value})`)
      .order('sent_at', { ascending: true })
    
    if (error) throw error
    
    currentMessages.value = (messages || []).map(msg => ({
      id: msg.id,
      sender_id: msg.sender_id,
      recipient_id: msg.recipient_id,
      content: msg.message_text,
      sent_at: msg.sent_at,
      is_read: msg.is_read,
      message_type: 'direct'
    }))
    
    console.log('Loaded messages:', currentMessages.value)
    
    await markMessagesAsRead(teacherId, sectionId)
    
  } catch (error) {
    console.error('Error loading conversation messages:', error)
  }
}

const sendMessage = async () => {
  if (!newMessage.value.trim() || !activeTeacher.value || !currentStudentId.value) return
  
  const messageText = newMessage.value.trim()
  const tempMessage = {
    id: 'temp-' + Date.now(),
    sender_id: currentStudentId.value,
    recipient_id: activeTeacher.value.id,
    content: messageText,
    sent_at: new Date().toISOString(),
    is_read: false,
    message_type: 'direct'
  }
  
  currentMessages.value.push(tempMessage)
  newMessage.value = ''
  
  await nextTick()
  scrollToBottom()
  
  try {
    const { data: newMsg, error: sendError } = await supabase
      .from('messages')
      .insert({
        section_id: activeTeacher.value.section_id,
        sender_id: currentStudentId.value,
        recipient_id: activeTeacher.value.id,
        message_text: messageText,
        message_type: 'direct',
        is_read: false
      })
      .select()
      .single()
    
    if (sendError) throw sendError
    
    console.log('Message sent successfully:', newMsg)
    
    const tempIndex = currentMessages.value.findIndex(m => m.id === tempMessage.id)
    if (tempIndex !== -1) {
      currentMessages.value[tempIndex] = {
        id: newMsg.id,
        sender_id: newMsg.sender_id,
        recipient_id: newMsg.recipient_id,
        content: newMsg.message_text,
        sent_at: newMsg.sent_at,
        is_read: newMsg.is_read,
        message_type: newMsg.message_type
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
  }
}

const markMessagesAsRead = async (teacherId, sectionId) => {
  try {
    if (!currentStudentId.value) return
    
    console.log('Marking messages as read:', { teacherId, sectionId })
    
    const { error } = await supabase
      .from('messages')
      .update({ is_read: true })
      .eq('section_id', sectionId)
      .eq('sender_id', teacherId)
      .eq('recipient_id', currentStudentId.value)
      .eq('is_read', false)
    
    if (error) throw error
    
    currentMessages.value.forEach(m => {
      if (m.sender_id === teacherId && !m.is_read) {
        m.is_read = true
      }
    })
    
    const teacher = enrolledTeachers.value.find(t => 
      t.id === teacherId && t.section_id === sectionId
    )
    if (teacher) {
      teacher.unread_count = 0
    }
    
  } catch (error) {
    console.error('Error marking messages as read:', error)
  }
}

const closeModal = () => {
  isModalOpen.value = false
  activeTeacher.value = null
  currentMessages.value = []
}

// Notification methods
const openNotificationModal = async (notif) => {
  try {
    console.log('Marking notification as read:', notif)
    
    await supabase
      .from('messages')
      .update({ is_read: true })
      .eq('id', notif.notification_id)
    
    notif.is_read = true
    
  } catch (error) {
    console.error('Error marking notification as read:', error)
  }
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
        
        if (newMessageData.recipient_id === currentStudentId.value || 
            newMessageData.message_type === 'announcement') {
          
          await loadEnrolledSubjectsAndTeachers()
          await loadNotifications()
          
          if (isModalOpen.value && activeTeacher.value && 
              newMessageData.section_id === activeTeacher.value.section_id &&
              newMessageData.sender_id === activeTeacher.value.id &&
              newMessageData.message_type === 'direct') {
            
            currentMessages.value.push({
              id: newMessageData.id,
              sender_id: newMessageData.sender_id,
              recipient_id: newMessageData.recipient_id,
              content: newMessageData.message_text,
              sent_at: newMessageData.sent_at,
              is_read: newMessageData.is_read,
              message_type: newMessageData.message_type
            })
            
            await nextTick()
            scrollToBottom()
            
            await supabase
              .from('messages')
              .update({ is_read: true })
              .eq('id', newMessageData.id)
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
      async () => {
        await loadEnrolledSubjectsAndTeachers()
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
})
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
  background: linear-gradient(135deg, var(--bg-primary) 0%, var(--bg-secondary) 100%);
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
  background: var(--bg-card);
  backdrop-filter: blur(20px);
  border: 1px solid var(--border-color);
  border-radius: 28px;
  padding: 2.5rem;
  box-shadow: 
    0 20px 60px var(--shadow-light),
    0 8px 32px var(--shadow-medium),
    0 0 0 1px rgba(255, 255, 255, 0.3);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.card-box:hover {
  transform: translateY(-2px);
  box-shadow: 
    0 25px 70px var(--shadow-medium),
    0 12px 40px var(--shadow-strong),
    0 0 0 1px rgba(255, 255, 255, 0.4);
}



/* --- Header card style to match Settings.vue/Subjects.vue --- */
.section-header-card {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  background: var(--bg-card);
  border-radius: 28px;
  box-shadow: 0 8px 32px var(--shadow-medium);
  border: 1.5px solid var(--border-color-hover);
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
  color: var(--text-accent);
  margin-bottom: 0.18rem;
  letter-spacing: -0.01em;
}
.section-header-sub {
  font-size: 1.15rem;
  color: var(--text-secondary);
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
  background: var(--bg-accent);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  color: var(--text-muted);
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.tab-btn:hover {
  background: var(--bg-accent-hover);
}

.tab-btn.active {
  background: var(--text-accent);
  color: var(--text-inverse);
  box-shadow: 0 4px 12px var(--shadow-medium);
}

.tab-btn.active svg {
  color: var(--text-inverse);
  stroke: var(--text-inverse);
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
  border: 1px solid var(--border-color);
  border-radius: 12px;
  font-size: 1rem;
  background: var(--bg-card);
  color: var(--text-primary);
  transition: all 0.2s ease;
}

.search-input:focus {
  outline: none;
  border-color: var(--text-accent);
  box-shadow: 0 0 0 3px var(--shadow-light);
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
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  backdrop-filter: blur(5px);
}

.modal-content {
  background: var(--card-background);
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
  color: var(--text-inverse);
  display: flex;
  align-items: center;
  gap: 1.5rem;
  position: relative;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.modal-header .close-btn {
  background: none;
  border: none;
  color: var(--text-inverse);
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
  color: var(--text-inverse);
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
  color: var(--text-inverse);
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

.subject-name {
  font-size: 1.2rem;
  font-weight: 700;
  color: var(--text-accent);
  margin: 0;
}

.subject-code {
  background: var(--text-accent);
  color: var(--text-inverse);
  padding: 0.25rem 0.75rem;
  border-radius: 8px;
  font-size: 0.8rem;
  font-weight: 600;
}

.teachers-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.teacher-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 1.5rem;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 16px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.teacher-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px var(--shadow-medium);
  border-color: var(--border-color-hover);
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
  box-shadow: 0 4px 12px var(--shadow-light);
}

.teacher-details {
  flex: 1;
  min-width: 0;
}

.teacher-name {
  font-weight: 700;
  color: var(--text-accent);
  margin: 0 0 0.25rem 0;
  font-size: 1.1rem;
}

.message-status {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.unread-badge {
  background: var(--text-accent);
  color: var(--text-inverse);
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

/* Keep existing styles and add these new ones */
/* ... (keep all the existing styles from the original file) ... */
</style>