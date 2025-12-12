import { ref, onMounted } from 'vue'
import { useTeacherAuth } from '../../composables/useTeacherAuth.js'

export default {
  setup() {
    const { isAuthenticated, teacherInfo } = useTeacherAuth()
    
    // Only load component-specific data if authenticated
    const loadComponentData = async () => {
      if (!isAuthenticated.value) {
        console.warn('Component not authenticated, skipping data load')
        return
      }
      
      // Component-specific data loading logic here
      console.log('Loading component data for teacher:', teacherInfo.value?.id)
    }
    
    onMounted(async () => {
      if (isAuthenticated.value) {
        await loadComponentData()
      }
    })
    
    return {
      isAuthenticated,
      teacherInfo,
      loadComponentData
    }
  }
}