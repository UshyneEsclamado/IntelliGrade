import { ref, computed } from 'vue'
import { supabase } from '../supabase.js'
import { useTeacherAuth } from './useTeacherAuth.js'

// Global state with caching
const subjects = ref([])
const subjectsCache = ref(null)
const lastFetchTime = ref(0)
const isLoadingSubjects = ref(false)
const CACHE_DURATION = 30000 // 30 seconds

// Dashboard stats cache
const dashboardStats = ref({
  totalClasses: 0,
  gradedToday: 0,
  pendingReviews: 0,
  assessmentsToGrade: []
})
const dashboardStatsCache = ref(null)
const lastDashboardFetch = ref(0)

export function useTeacherData() {
  const { teacherId, isAuthenticated } = useTeacherAuth()

  // Fetch subjects with caching
  const fetchSubjects = async (forceRefresh = false) => {
    if (!isAuthenticated.value || !teacherId.value) {
      console.warn('Cannot fetch subjects: not authenticated')
      return { success: false, data: [] }
    }

    const now = Date.now()
    const timeSinceLastFetch = now - lastFetchTime.value

    // Return cached data if available and not expired
    if (!forceRefresh && subjectsCache.value && timeSinceLastFetch < CACHE_DURATION) {
      console.log('Using cached subjects data')
      subjects.value = subjectsCache.value
      return { success: true, data: subjects.value, fromCache: true }
    }

    // Prevent multiple simultaneous requests
    if (isLoadingSubjects.value) {
      return new Promise((resolve) => {
        const checkLoading = () => {
          if (!isLoadingSubjects.value) {
            resolve({ success: true, data: subjects.value, fromCache: true })
          } else {
            setTimeout(checkLoading, 100)
          }
        }
        checkLoading()
      })
    }

    isLoadingSubjects.value = true

    try {
      console.log('Fetching subjects from database...')
      
      const { data: subjectsData, error } = await supabase
        .from('subjects')
        .select(`
          id,
          name,
          grade_level,
          description,
          teacher_id,
          is_active,
          created_at,
          sections (
            id,
            name,
            section_code,
            max_students,
            current_enrollment,
            is_active,
            created_at
          )
        `)
        .eq('teacher_id', teacherId.value)
        .eq('is_active', true)
        .order('created_at', { ascending: false })

      if (error) {
        console.error('Error fetching subjects:', error)
        return { success: false, data: [], error }
      }

      // Process and cache the data
      const processedSubjects = (subjectsData || []).map(subject => ({
        ...subject,
        sections: (subject.sections || [])
          .filter(section => section.is_active)
          .sort((a, b) => a.name.localeCompare(b.name)),
        expanded: false
      }))

      subjects.value = processedSubjects
      subjectsCache.value = processedSubjects
      lastFetchTime.value = now

      console.log(`Fetched ${processedSubjects.length} subjects`)
      return { success: true, data: subjects.value, fromCache: false }

    } catch (error) {
      console.error('Unexpected error fetching subjects:', error)
      return { success: false, data: [], error }
    } finally {
      isLoadingSubjects.value = false
    }
  }

  // Fetch dashboard stats with caching
  const fetchDashboardStats = async (forceRefresh = false) => {
    if (!isAuthenticated.value || !teacherId.value) {
      return { success: false, data: dashboardStats.value }
    }

    const now = Date.now()
    const timeSinceLastFetch = now - lastDashboardFetch.value

    // Return cached data if available and not expired
    if (!forceRefresh && dashboardStatsCache.value && timeSinceLastFetch < CACHE_DURATION) {
      console.log('Using cached dashboard stats')
      dashboardStats.value = dashboardStatsCache.value
      return { success: true, data: dashboardStats.value, fromCache: true }
    }

    try {
      console.log('Fetching dashboard stats...')
      
      // Get total classes (subjects with active sections)
      const { data: subjectsData } = await supabase
        .from('subjects')
        .select('id, sections(id)')
        .eq('teacher_id', teacherId.value)
        .eq('is_active', true)

      const totalClasses = subjectsData?.reduce((count, subject) => {
        return count + (subject.sections?.length || 0)
      }, 0) || 0

      // Get assessments to grade (mock data for now)
      const assessmentsToGrade = []

      const stats = {
        totalClasses,
        gradedToday: 0, // TODO: Calculate based on actual grading data
        pendingReviews: 0, // TODO: Calculate based on actual review data
        assessmentsToGrade
      }

      dashboardStats.value = stats
      dashboardStatsCache.value = stats
      lastDashboardFetch.value = now

      return { success: true, data: stats, fromCache: false }

    } catch (error) {
      console.error('Error fetching dashboard stats:', error)
      return { success: false, data: dashboardStats.value, error }
    }
  }

  // Clear cache when data changes
  const invalidateSubjectsCache = () => {
    subjectsCache.value = null
    lastFetchTime.value = 0
  }

  const invalidateDashboardCache = () => {
    dashboardStatsCache.value = null
    lastDashboardFetch.value = 0
  }

  // Auto-refresh data when tab becomes visible
  const setupAutoRefresh = () => {
    const handleVisibilityChange = () => {
      if (document.visibilityState === 'visible' && isAuthenticated.value) {
        const timeSinceLastFetch = Date.now() - lastFetchTime.value
        if (timeSinceLastFetch > CACHE_DURATION) {
          fetchSubjects(true)
        }
      }
    }

    document.addEventListener('visibilitychange', handleVisibilityChange)
    
    return () => {
      document.removeEventListener('visibilitychange', handleVisibilityChange)
    }
  }

  // Get cached data without making requests
  const getCachedSubjects = () => {
    return subjects.value
  }

  const getCachedDashboardStats = () => {
    return dashboardStats.value
  }

  // Computed properties
  const hasSubjects = computed(() => {
    return subjects.value && subjects.value.length > 0
  })

  const totalSubjects = computed(() => {
    return subjects.value?.length || 0
  })

  const totalSections = computed(() => {
    return subjects.value?.reduce((count, subject) => {
      return count + (subject.sections?.length || 0)
    }, 0) || 0
  })

  return {
    // State
    subjects: computed(() => subjects.value),
    dashboardStats: computed(() => dashboardStats.value),
    isLoadingSubjects: computed(() => isLoadingSubjects.value),
    hasSubjects,
    totalSubjects,
    totalSections,

    // Methods
    fetchSubjects,
    fetchDashboardStats,
    getCachedSubjects,
    getCachedDashboardStats,
    invalidateSubjectsCache,
    invalidateDashboardCache,
    setupAutoRefresh
  }
}