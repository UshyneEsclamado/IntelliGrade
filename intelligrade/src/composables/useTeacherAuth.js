import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { supabase } from '../supabase.js'

// Global state
const currentUser = ref(null)
const teacherInfo = ref(null)
const isInitialized = ref(false)
const isLoading = ref(false)
const authListener = ref(null)

export function useTeacherAuth() {
  const router = useRouter()

  // Initialize authentication once and reuse
  const initializeAuth = async (force = false) => {
    if (isInitialized.value && !force) {
      return { success: true, user: currentUser.value, teacher: teacherInfo.value }
    }

    if (isLoading.value) {
      // Wait for existing initialization to complete
      return new Promise((resolve) => {
        const checkInit = () => {
          if (!isLoading.value) {
            resolve({ 
              success: isInitialized.value, 
              user: currentUser.value, 
              teacher: teacherInfo.value 
            })
          } else {
            setTimeout(checkInit, 100)
          }
        }
        checkInit()
      })
    }

    isLoading.value = true

    try {
      const { data: { session }, error: sessionError } = await supabase.auth.getSession()
      
      if (sessionError) {
        console.error('Session error:', sessionError)
        throw sessionError
      }
      
      if (!session?.user) {
        console.warn('No active session')
        await router.push('/login')
        return { success: false }
      }
      
      currentUser.value = session.user
      
      // Get profile data
      const { data: profile, error: profileError } = await supabase
        .from('profiles')
        .select('id, role, full_name, email')
        .eq('auth_user_id', session.user.id)
        .single()
      
      if (profileError || !profile) {
        console.error('Profile error:', profileError)
        await router.push('/login')
        return { success: false }
      }

      if (profile.role !== 'teacher') {
        console.warn('User is not a teacher')
        await router.push('/login')
        return { success: false }
      }

      // Get teacher details
      const { data: teacher, error: teacherError } = await supabase
        .from('teachers')
        .select('*')
        .eq('profile_id', profile.id)
        .eq('is_active', true)
        .single()

      if (teacherError || !teacher) {
        console.error('Teacher error:', teacherError)
        await router.push('/login')
        return { success: false }
      }

      teacherInfo.value = { ...teacher, profile }
      isInitialized.value = true
      
      console.log('Teacher authentication initialized:', teacher.id)
      return { success: true, user: currentUser.value, teacher: teacherInfo.value }

    } catch (error) {
      console.error('Authentication error:', error)
      await router.push('/login')
      return { success: false }
    } finally {
      isLoading.value = false
    }
  }

  // Setup auth state listener (only once)
  const setupAuthListener = () => {
    if (authListener.value) {
      return // Already set up
    }
    
    authListener.value = supabase.auth.onAuthStateChange(async (event, session) => {
      console.log('Auth state changed:', event)
      
      if (event === 'SIGNED_OUT' || !session) {
        currentUser.value = null
        teacherInfo.value = null
        isInitialized.value = false
        await router.push('/login')
      } else if (event === 'TOKEN_REFRESHED' && session) {
        // Token refreshed, update user but don't re-fetch everything
        currentUser.value = session.user
      }
    })
  }

  // Get current teacher info without re-initialization
  const getTeacherInfo = () => {
    return {
      user: currentUser.value,
      teacher: teacherInfo.value,
      isInitialized: isInitialized.value,
      isLoading: isLoading.value
    }
  }

  // Reset state on logout
  const resetAuth = () => {
    currentUser.value = null
    teacherInfo.value = null
    isInitialized.value = false
    isLoading.value = false
    
    if (authListener.value) {
      authListener.value.data.subscription.unsubscribe()
      authListener.value = null
    }
  }

  // Computed properties
  const isAuthenticated = computed(() => {
    return isInitialized.value && currentUser.value && teacherInfo.value
  })

  const teacherId = computed(() => {
    return teacherInfo.value?.id || null
  })

  const teacherProfile = computed(() => {
    return teacherInfo.value?.profile || null
  })

  return {
    // State
    currentUser: computed(() => currentUser.value),
    teacherInfo: computed(() => teacherInfo.value),
    isInitialized: computed(() => isInitialized.value),
    isLoading: computed(() => isLoading.value),
    isAuthenticated,
    teacherId,
    teacherProfile,
    
    // Methods
    initializeAuth,
    setupAuthListener,
    getTeacherInfo,
    resetAuth
  }
}