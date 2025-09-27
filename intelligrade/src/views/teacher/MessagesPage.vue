<template>
  <div class="page-container">
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

      <!-- Main Content -->
      <section class="content-section">
        <div class="card-box content-card">
          <!-- Tabs -->
          <div class="tabs">
            <button 
              :class="['tab-btn', { 'active': currentTab === 'students' }]"
              @click="currentTab = 'students'"
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
              @click="currentTab = 'broadcast'"
            >
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M3 11l18-5v12L3 14v-3z"/>
                <path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"/>
              </svg>
              Broadcast Message
            </button>
          </div>

          <!-- Students Tab -->
          <div v-if="currentTab === 'students'" class="tab-content">
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
                    <option v-for="section in mySections" :key="section.id" :value="section.id">
                      {{ section.name }}
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
            </div>

            <div v-else class="students-by-section">
              <div v-for="section in groupedStudents" :key="section.id" class="section-group">
                <div class="section-header">
                  <div class="section-info">
                    <h3 class="section-name">{{ section.name }}</h3>
                    <span class="section-code">{{ section.code }}</span>
                  </div>
                  <div class="section-actions">
                    <span class="student-count">{{ section.students.length }} students</span>
                    <button 
                      class="broadcast-btn" 
                      @click="openBroadcastModal(); broadcastSection = section.id"
                    >
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M3 11l18-5v12L3 14v-3z"/>
                      </svg>
                      Broadcast
                    </button>
                  </div>
                </div>
                
                <div class="students-list">
                  <div 
                    v-for="student in section.students" 
                    :key="`${student.id}-${section.id}`"
                    :class="['student-item', { 'has-unread': student.unread_count > 0 }]"
                    @click="startChatWithStudent(student)"
                  >
                    <div class="student-info">
                      <div class="student-avatar">
                        <span>{{ student.name?.[0] || 'S' }}</span>
                      </div>
                      <div class="student-details">
                        <h4 class="student-name">{{ student.name }}</h4>
                        <p class="student-email">{{ student.email }}</p>
                        <p class="last-message">{{ student.last_message || 'No messages yet' }}</p>
                      </div>
                    </div>
                    <div class="message-status">
                      <span v-if="student.unread_count > 0" class="unread-badge">{{ student.unread_count }}</span>
                      <span class="last-time">{{ formatTime(student.last_message_time) }}</span>
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

          <!-- Broadcast Tab -->
          <div v-else-if="currentTab === 'broadcast'" class="tab-content">
            <div class="broadcast-section">
              <div class="broadcast-header">
                <h3>Send Section Announcement</h3>
                <p>Send a message to all students in a selected section</p>
              </div>
              
              <div class="broadcast-form">
                <div class="form-group">
                  <label>Select Section</label>
                  <select v-model="broadcastSection" class="form-control">
                    <option value="">Choose a section</option>
                    <option v-for="section in mySections" :key="section.id" :value="section.id">
                      {{ section.name }}
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
                
                <div class="broadcast-actions">
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
              <span>{{ activeConversation?.name?.[0] || 'S' }}</span>
            </div>
            <div class="header-details">
              <h2 class="modal-title">{{ activeConversation?.name || 'Student' }}</h2>
              <span class="section-info">{{ activeConversation?.subject_name }}</span>
            </div>
          </div>
        </div>
        <div class="modal-body">
          <div class="messages-container" ref="messagesContainer">
            <div 
              v-for="message in currentMessages" 
              :key="message.id" 
              :class="['message-bubble', { 'sent': message.sender_id === currentUser.id, 'received': message.sender_id !== currentUser.id }]"
            >
              <p class="message-text">{{ message.content }}</p>
              <span class="message-time">{{ formatTime(message.created_at) }}</span>
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
              @keyup.enter="handleSendMessage" 
              placeholder="Type your message to the student..." 
              class="message-input"
            />
            <button class="send-btn" @click="handleSendMessage" :disabled="!newMessage.trim()">
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
          <h2 class="modal-title">Send Section Announcement</h2>
        </div>
        <div class="modal-body">
          <div class="broadcast-form">
            <div class="form-group">
              <label>Select Section</label>
              <select v-model="broadcastSection" class="form-control">
                <option value="">Choose a section</option>
                <option v-for="section in mySections" :key="section.id" :value="section.id">
                  {{ section.name }}
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
          </div>
        </div>
        <div class="modal-footer">
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

    <!-- Loading Overlay -->
    <div v-if="isLoading" class="loading-overlay">
      <div class="loading-content">
        <div class="loading-spinner"></div>
        <p>Loading messages...</p>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref, computed, onMounted, nextTick } from 'vue'
import { useRouter } from 'vue-router'
import { supabase } from '@/supabase.js'

const router = useRouter()

// ================================
// STATE MANAGEMENT
// ================================

// User authentication
const currentUser = ref(null)

const getCurrentUser = async () => {
  try {
    const { data: { user } } = await supabase.auth.getUser()
    if (!user) {
      await router.push('/login')
      return null
    }
    currentUser.value = user
    return user
  } catch (error) {
    console.error('Error getting current user:', error)
    await router.push('/login')
    return null
  }
}

// UI State
const currentTab = ref('students')
const isModalOpen = ref(false)
const isBroadcastModalOpen = ref(false)
const isLoading = ref(false)

// Search and Filter
const searchQuery = ref('')
const selectedSection = ref('') // Changed from selectedSubject to selectedSection

// Chat State
const selectedChat = ref(null)
const activeConversation = ref(null)
const newMessage = ref('')
const messagesContainer = ref(null)

// Broadcast State
const broadcastMessage = ref('')
const broadcastSection = ref('') // Changed from broadcastSubject to broadcastSection

// Data
const mySections = ref([]) // Changed from mySubjects to mySections
const enrolledStudents = ref([])
const currentMessages = ref([])

// ================================
// COMPUTED PROPERTIES
// ================================

const filteredStudents = computed(() => {
  let students = enrolledStudents.value
  
  // Filter by selected section instead of subject
  if (selectedSection.value) {
    students = students.filter(s => s.section_id === selectedSection.value)
  }
  
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    students = students.filter(s => 
      s.student_name.toLowerCase().includes(query) ||
      s.subject_name.toLowerCase().includes(query) ||
      s.section_name.toLowerCase().includes(query)
    )
  }
  
  return students
})

// Updated grouping logic: Group by section instead of subject
const groupedStudents = computed(() => {
  const sections = {}
  
  filteredStudents.value.forEach(student => {
    const sectionKey = student.section_id // Use section_id as key
    if (!sections[sectionKey]) {
      sections[sectionKey] = {
        id: student.section_id,
        subject_id: student.subject_id,
        name: `${student.subject_name} - ${student.section_name}`, // Show "Filipino - Section A"
        code: student.section_code,
        section_name: student.section_name,
        subject_name: student.subject_name,
        grade_level: student.grade_level,
        students: []
      }
    }
    sections[sectionKey].students.push(student)
  })
  
  return Object.values(sections)
})

// ================================
// DATA LOADING METHODS
// ================================

const loadMySubjectsAndStudents = async () => {
  try {
    if (!currentUser.value) {
      console.error('No authenticated user')
      return
    }
    
    isLoading.value = true
    console.log('Loading subjects and students for teacher:', currentUser.value.id)
    
    // Use the teacher_contacts view we created earlier
    const { data: contacts, error: contactsError } = await supabase
      .from('teacher_contacts')
      .select('*')
      .eq('teacher_id', currentUser.value.id)
    
    if (contactsError) {
      console.error('Error fetching teacher contacts:', contactsError)
      throw contactsError
    }
    
    console.log('Teacher contacts found:', contacts)
    
    if (!contacts || contacts.length === 0) {
      console.log('No enrolled students found')
      enrolledStudents.value = []
      mySections.value = []
      return
    }
    
    // Process the contacts data
    enrolledStudents.value = contacts.map(contact => ({
      id: contact.student_id,
      student_name: contact.student_name,
      student_email: contact.student_email,
      student_number: contact.student_number,
      subject_id: contact.subject_id,
      subject_name: contact.subject_name,
      section_id: contact.section_id,
      section_name: contact.section_name,
      section_code: contact.section_code,
      grade_level: contact.grade_level,
      enrolled_date: contact.enrolled_date,
      last_message_date: contact.last_message_date,
      unread_count: contact.unread_count || 0,
      // For display purposes
      name: contact.student_name,
      email: contact.student_email,
      last_message: null, // We'll load this separately if needed
      last_message_time: contact.last_message_date
    }))
    
    // Extract unique SECTIONS for the filter dropdown (not subjects)
    const sectionsMap = new Map()
    contacts.forEach(contact => {
      if (!sectionsMap.has(contact.section_id)) {
        sectionsMap.set(contact.section_id, {
          id: contact.section_id,
          name: `${contact.subject_name} - ${contact.section_name}`,
          code: contact.section_code,
          subject_name: contact.subject_name,
          section_name: contact.section_name,
          grade_level: contact.grade_level
        })
      }
    })
    
    mySections.value = Array.from(sectionsMap.values())
    
    console.log('Processed students:', enrolledStudents.value)
    console.log('Processed sections:', mySections.value)
    
  } catch (error) {
    console.error('Error loading subjects and students:', error)
    alert('Error loading messaging data. Please check the console for details.')
  } finally {
    isLoading.value = false
  }
}

const loadConversationMessages = async (studentId, sectionId) => {
  try {
    if (!currentUser.value) return
    
    console.log('Loading messages between teacher and student:', { 
      teacherId: currentUser.value.id, 
      studentId, 
      sectionId 
    })
    
    // Load messages using the teacher_messages view
    const { data: messages, error: messagesError } = await supabase
      .from('teacher_messages')
      .select('*')
      .eq('section_id', sectionId)
      .or(`and(sender_id.eq.${currentUser.value.id},recipient_id.eq.${studentId}),and(sender_id.eq.${studentId},recipient_id.eq.${currentUser.value.id})`)
      .order('sent_at', { ascending: true })
    
    if (messagesError) {
      console.error('Error loading messages:', messagesError)
      throw messagesError
    }
    
    console.log('Messages loaded:', messages)
    
    // Format messages for display
    currentMessages.value = (messages || []).map(msg => ({
      id: msg.id,
      sender_id: msg.sender_id,
      recipient_id: msg.recipient_id,
      content: msg.message_text,
      created_at: msg.sent_at,
      is_read: msg.is_read,
      message_type: msg.message_type,
      sender_name: msg.sender_name,
      recipient_name: msg.recipient_name
    }))
    
    // Mark messages as read
    if (messages && messages.length > 0) {
      await markConversationAsRead(sectionId, studentId)
    }
    
  } catch (error) {
    console.error('Error loading conversation messages:', error)
  }
}

const markConversationAsRead = async (sectionId, studentId) => {
  try {
    const { error } = await supabase.rpc('mark_conversation_read', {
      p_section_id: sectionId,
      p_other_user_id: studentId,
      p_current_user_id: currentUser.value.id
    })
    
    if (error) {
      console.error('Error marking conversation as read:', error)
    } else {
      // Update local unread count
      const student = enrolledStudents.value.find(s => s.id === studentId && s.section_id === sectionId)
      if (student) {
        student.unread_count = 0
      }
    }
  } catch (error) {
    console.error('Error marking conversation as read:', error)
  }
}

// ================================
// CHAT METHODS
// ================================

const startChatWithStudent = async (student) => {
  console.log('Starting chat with student:', student)
  
  activeConversation.value = {
    ...student,
    name: student.student_name || student.name,
    email: student.student_email || student.email,
    subject_name: student.subject_name // Include section context in modal
  }
  
  selectedChat.value = student
  isModalOpen.value = true
  
  // Load messages for this conversation
  await loadConversationMessages(student.id, student.section_id)
  
  // Scroll to bottom of messages
  await nextTick()
  if (messagesContainer.value) {
    messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
  }
}

const handleSendMessage = async () => {
  if (!newMessage.value.trim() || !activeConversation.value || !currentUser.value) return
  
  const messageText = newMessage.value.trim()
  const tempMessage = {
    id: 'temp-' + Date.now(),
    sender_id: currentUser.value.id,
    recipient_id: activeConversation.value.id,
    content: messageText,
    created_at: new Date().toISOString(),
    is_read: false,
    message_type: 'direct'
  }
  
  // Add temporary message to display
  currentMessages.value.push(tempMessage)
  newMessage.value = ''
  
  // Scroll to bottom
  await nextTick()
  if (messagesContainer.value) {
    messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
  }
  
  try {
    // Send the message to the database
    const { data: sentMessage, error: sendError } = await supabase
      .from('messages')
      .insert({
        section_id: activeConversation.value.section_id,
        sender_id: currentUser.value.id,
        recipient_id: activeConversation.value.id,
        message_text: messageText,
        message_type: 'direct'
      })
      .select()
      .single()
    
    if (sendError) {
      console.error('Error sending message:', sendError)
      throw sendError
    }
    
    console.log('Message sent successfully:', sentMessage)
    
    // Replace temporary message with real message
    const tempIndex = currentMessages.value.findIndex(m => m.id === tempMessage.id)
    if (tempIndex !== -1) {
      currentMessages.value[tempIndex] = {
        id: sentMessage.id,
        sender_id: sentMessage.sender_id,
        recipient_id: sentMessage.recipient_id,
        content: sentMessage.message_text,
        created_at: sentMessage.sent_at,
        is_read: sentMessage.is_read,
        message_type: sentMessage.message_type
      }
    }
    
  } catch (error) {
    console.error('Failed to send message:', error)
    
    // Remove temporary message on error
    const tempIndex = currentMessages.value.findIndex(m => m.id === tempMessage.id)
    if (tempIndex !== -1) {
      currentMessages.value.splice(tempIndex, 1)
    }
    
    alert('Failed to send message. Please try again.')
  }
}

const closeModal = () => {
  isModalOpen.value = false
  activeConversation.value = null
  selectedChat.value = null
  currentMessages.value = []
}

// ================================
// BROADCAST METHODS
// ================================

const openBroadcastModal = () => {
  isBroadcastModalOpen.value = true
  broadcastMessage.value = ''
  broadcastSection.value = '' // Changed from broadcastSubject
}

const closeBroadcastModal = () => {
  isBroadcastModalOpen.value = false
  broadcastMessage.value = ''
  broadcastSection.value = ''
}

// Updated broadcast logic to work with individual sections
const sendBroadcastMessage = async () => {
  if (!broadcastMessage.value.trim() || !broadcastSection.value || !currentUser.value) return
  
  try {
    isLoading.value = true
    
    // Send broadcast message to the specific section only
    const { data: sentMessage, error: sendError } = await supabase
      .from('messages')
      .insert({
        section_id: broadcastSection.value, // Specific section ID
        sender_id: currentUser.value.id,
        recipient_id: null, // null for broadcast
        message_text: broadcastMessage.value.trim(),
        message_type: 'announcement'
      })
      .select()
      .single()
    
    if (sendError) {
      console.error('Error sending broadcast message:', sendError)
      throw sendError
    }
    
    console.log('Broadcast message sent successfully:', sentMessage)
    
    // Get section info for confirmation message
    const selectedSectionInfo = mySections.value.find(s => s.id === broadcastSection.value)
    const sectionName = selectedSectionInfo ? selectedSectionInfo.name : 'Selected Section'
    
    closeBroadcastModal()
    alert(`Broadcast message sent successfully to all students in ${sectionName}!`)
    
  } catch (error) {
    console.error('Error sending broadcast message:', error)
    alert('Failed to send broadcast message. Please try again.')
  } finally {
    isLoading.value = false
  }
}

// ================================
// UTILITY METHODS
// ================================

const markAllAsRead = async () => {
  try {
    if (!currentUser.value) return
    
    // This would mark all messages sent to the teacher as read
    const { error } = await supabase
      .from('messages')
      .update({ 
        is_read: true, 
        read_at: new Date().toISOString() 
      })
      .eq('recipient_id', currentUser.value.id)
      .eq('is_read', false)
    
    if (error) {
      console.error('Error marking all messages as read:', error)
      return
    }
    
    // Update local state
    enrolledStudents.value.forEach(student => {
      student.unread_count = 0
    })
    
  } catch (error) {
    console.error('Error marking all as read:', error)
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

// ================================
// AUTHENTICATION & LIFECYCLE
// ================================

const setupAuthListener = () => {
  supabase.auth.onAuthStateChange(async (event, session) => {
    if (event === 'SIGNED_OUT' || !session) {
      currentUser.value = null
      enrolledStudents.value = []
      mySections.value = []
      await router.push('/login')
      return
    }
    
    if (event === 'SIGNED_IN' && session?.user) {
      currentUser.value = session.user
      await loadMySubjectsAndStudents()
    }
  })
}

onMounted(async () => {
  console.log('Teacher messages component mounted')
  
  // Setup auth listener
  setupAuthListener()
  
  // Get current user and load data
  const user = await getCurrentUser()
  if (user) {
    console.log('Authenticated user found:', user.email)
    await loadMySubjectsAndStudents()
  } else {
    console.error('No authenticated user found')
  }
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
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.student-item {
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
  border-color: var(--border-color-hover);
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
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, #A3D1C6 0%, #B3D8A8 100%);
  color: var(--accent-color);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 1.2rem;
  box-shadow: 0 4px 12px var(--shadow-light);
}

.student-details {
  flex: 1;
  min-width: 0;
}

.student-name {
  font-weight: 700;
  color: var(--accent-color);
  margin: 0 0 0.25rem 0;
  font-size: 1.1rem;
}

.student-email {
  font-size: 0.85rem;
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
  font-size: 0.85rem;
  color: var(--text-muted);
}

.chat-icon {
  color: var(--accent-color);
  opacity: 0.7;
  transition: opacity 0.2s ease;
}

.student-item:hover .chat-icon {
  opacity: 1;
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
  box-shadow: 0 8px 25px var(--shadow-medium);
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
   RESPONSIVE
   ================================ */
@media (max-width: 768px) {
  .page-container {
    padding: 1rem;
  }
  
  .card-box {
    padding: 1.5rem;
    border-radius: 20px;
  }
  
  .page-title {
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
  
  .subject-actions {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.5rem;
  }
  
  .student-item {
    padding: 1rem;
  }
}

@media (max-width: 480px) {
  .last-message {
    -webkit-line-clamp: 1;
    line-clamp: 1;
  }
}
</style>