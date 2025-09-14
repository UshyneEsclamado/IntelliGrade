import { ref, reactive, onMounted, onUnmounted } from 'vue'

const API_BASE_URL = 'http://localhost:8000/api'
const WS_BASE_URL = 'ws://localhost:8000'

export function useMessaging() {
  const conversations = ref([])
  const notifications = ref([])
  const archivedConversations = ref([])
  const unreadCount = ref(0)
  const isConnected = ref(false)
  const currentUser = ref(null)
  
  let websocket = null
  let reconnectAttempts = 0
  const maxReconnectAttempts = 5
  
  // Get auth token from localStorage
  const getAuthToken = () => {
    return localStorage.getItem('access_token')
  }
  
  // Get current user info
  const getCurrentUser = () => {
    const userData = localStorage.getItem('user_data')
    return userData ? JSON.parse(userData) : null
  }
  
  // API calls with authentication
  const apiCall = async (endpoint, options = {}) => {
    const token = getAuthToken()
    const headers = {
      'Content-Type': 'application/json',
      ...(token && { 'Authorization': `Bearer ${token}` }),
      ...options.headers
    }
    
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      ...options,
      headers
    })
    
    if (!response.ok) {
      throw new Error(`API call failed: ${response.statusText}`)
    }
    
    return response.json()
  }
  
  // WebSocket connection
  const connectWebSocket = () => {
    const user = getCurrentUser()
    if (!user) return
    
    try {
      websocket = new WebSocket(`${WS_BASE_URL}/ws/${user.id}`)
      
      websocket.onopen = () => {
        console.log('WebSocket connected')
        isConnected.value = true
        reconnectAttempts = 0
      }
      
      websocket.onmessage = (event) => {
        const data = JSON.parse(event.data)
        handleWebSocketMessage(data)
      }
      
      websocket.onclose = () => {
        console.log('WebSocket disconnected')
        isConnected.value = false
        
        // Attempt to reconnect
        if (reconnectAttempts < maxReconnectAttempts) {
          setTimeout(() => {
            reconnectAttempts++
            connectWebSocket()
          }, 1000 * Math.pow(2, reconnectAttempts))
        }
      }
      
      websocket.onerror = (error) => {
        console.error('WebSocket error:', error)
      }
      
    } catch (error) {
      console.error('Failed to connect WebSocket:', error)
    }
  }
  
  // Handle incoming WebSocket messages
  const handleWebSocketMessage = (data) => {
    switch (data.type) {
      case 'new_message':
        handleNewMessage(data.message)
        break
      case 'message_read':
        handleMessageRead(data)
        break
      default:
        console.log('Unknown message type:', data.type)
    }
  }
  
  // Handle new incoming message
  const handleNewMessage = (message) => {
    const conversationId = message.conversation_id
    
    // Find the conversation and add the message
    const conversation = conversations.value.find(c => c.id === conversationId)
    if (conversation) {
      // Add message to conversation
      if (!conversation.messages) conversation.messages = []
      conversation.messages.push({
        id: message.id,
        text: message.content,
        sender: message.sender_id === getCurrentUser()?.id ? 'You' : conversation.sender,
        time: new Date(message.created_at).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      })
      
      // Update last message
      conversation.lastMessage = message.content
      conversation.time = new Date(message.created_at).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      conversation.read = message.sender_id === getCurrentUser()?.id
      
      // Move conversation to top
      const index = conversations.value.findIndex(c => c.id === conversationId)
      if (index > 0) {
        const [conv] = conversations.value.splice(index, 1)
        conversations.value.unshift(conv)
      }
    }
    
    // Update unread count if message is not from current user
    if (message.sender_id !== getCurrentUser()?.id) {
      unreadCount.value++
    }
  }
  
  // API Functions
  const fetchConversations = async () => {
    try {
      const data = await apiCall('/conversations')
      
      // Transform API data to component format
      conversations.value = data.map(conv => {
        const user = getCurrentUser()
        const otherUser = conv.user1_id === user?.id ? conv.user2 : conv.user1
        
        return {
          id: conv.id,
          sender: otherUser.full_name,
          lastMessage: conv.last_message?.content || 'No messages yet',
          time: conv.last_message ? 
            new Date(conv.last_message.created_at).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }) : 
            new Date(conv.created_at).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
          read: conv.last_message?.sender_id === user?.id || conv.last_message?.is_read || false,
          messages: []
        }
      })
    } catch (error) {
      console.error('Failed to fetch conversations:', error)
    }
  }
  
  const fetchConversationMessages = async (conversationId) => {
    try {
      const messages = await apiCall(`/conversations/${conversationId}/messages`)
      const user = getCurrentUser()
      
      return messages.map(msg => ({
        id: msg.id,
        text: msg.content,
        sender: msg.sender_id === user?.id ? 'You' : msg.sender.full_name,
        time: new Date(msg.created_at).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      }))
    } catch (error) {
      console.error('Failed to fetch messages:', error)
      return []
    }
  }
  
  const sendMessage = async (conversationId, receiverId, content) => {
    if (websocket && websocket.readyState === WebSocket.OPEN) {
      // Send via WebSocket for real-time delivery
      const message = {
        type: 'message',
        conversation_id: conversationId,
        receiver_id: receiverId,
        content: content
      }
      websocket.send(JSON.stringify(message))
    } else {
      // Fallback to REST API
      try {
        await apiCall('/messages', {
          method: 'POST',
          body: JSON.stringify({
            receiver_id: receiverId,
            content: content
          })
        })
      } catch (error) {
        console.error('Failed to send message:', error)
        throw error
      }
    }
  }
  
  const createConversation = async (participantId) => {
    try {
      const conversation = await apiCall('/conversations', {
        method: 'POST',
        body: JSON.stringify({ participant_id: participantId })
      })
      return conversation
    } catch (error) {
      console.error('Failed to create conversation:', error)
      throw error
    }
  }
  
  const markMessagesAsRead = async (conversationId) => {
    if (websocket && websocket.readyState === WebSocket.OPEN) {
      const message = {
        type: 'mark_read',
        conversation_id: conversationId
      }
      websocket.send(JSON.stringify(message))
    }
  }
  
  const fetchUsers = async (role = null) => {
    try {
      const params = role ? `?role=${role}` : ''
      return await apiCall(`/users${params}`)
    } catch (error) {
      console.error('Failed to fetch users:', error)
      return []
    }
  }
  
  const searchUsers = async (query) => {
    try {
      if (!query || query.trim().length < 2) {
        return []
      }
      return await apiCall(`/users/search?query=${encodeURIComponent(query.trim())}`)
    } catch (error) {
      console.error('Failed to search users:', error)
      return []
    }
  }
  
  const createConversationWithUser = async (userId) => {
    try {
      const response = await apiCall('/conversations/create', {
        method: 'POST',
        body: JSON.stringify({ other_user_id: userId })
      })
      
      // Refresh conversations to include the new one
      await fetchConversations()
      
      return response
    } catch (error) {
      console.error('Failed to create conversation:', error)
      throw error
    }
  }
  
  const fetchUnreadCount = async () => {
    try {
      const data = await apiCall('/unread-count')
      unreadCount.value = data.unread_count
    } catch (error) {
      console.error('Failed to fetch unread count:', error)
    }
  }
  
  // Mock notifications for now (can be replaced with real API later)
  const fetchNotifications = () => {
    notifications.value = [
      { id: 1, title: 'Holiday Announcement', body: 'Classes are suspended on Monday due to a public holiday. Regular schedule resumes Tuesday.', time: '2 hours ago', read: false, important: true },
      { id: 2, title: 'Assignment Reminder', body: 'Your research paper for English Literature is due this Friday. Make sure to submit it before 11:59 PM.', time: '1 day ago', read: false, important: true },
      { id: 3, title: 'Grade Posted', body: 'Your midterm exam grade for Mathematics has been posted. Check your student portal for details.', time: '3 days ago', read: true, important: false },
      { id: 4, title: 'Library Notice', body: 'The main library will be closed for maintenance this weekend. Study rooms in Building B remain open.', time: '1 week ago', read: true, important: false },
    ]
  }
  
  // Initialize
  const initialize = () => {
    currentUser.value = getCurrentUser()
    if (currentUser.value) {
      connectWebSocket()
      fetchConversations()
      fetchNotifications()
      fetchUnreadCount()
    }
  }
  
  // Cleanup
  const cleanup = () => {
    if (websocket) {
      websocket.close()
    }
  }
  
  // Lifecycle
  onMounted(() => {
    initialize()
  })
  
  onUnmounted(() => {
    cleanup()
  })
  
  return {
    // State
    conversations,
    notifications,
    archivedConversations,
    unreadCount,
    isConnected,
    currentUser,
    
    // Methods
    fetchConversations,
    fetchConversationMessages,
    sendMessage,
    createConversation,
    markMessagesAsRead,
    fetchUsers,
    searchUsers,
    createConversationWithUser,
    fetchUnreadCount,
    fetchNotifications,
    connectWebSocket,
    cleanup
  }
}