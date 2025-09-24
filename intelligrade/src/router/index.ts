import { createRouter, createWebHistory } from 'vue-router'
import { supabase } from '@/supabase'

// Import all necessary components
import Intro from '@/views/Intro.vue'
import Landing from '@/views/Landing.vue'
import Login from '@/views/Login.vue'
import Signup from '@/views/Signup.vue'
import SignupStudent from '@/views/SignupStudent.vue'
import RoleSelection from '@/views/RoleSelection.vue'
import StudentDashboard from '@/views/StudentDashboard.vue'
import TeacherDashboard from '@/views/TeacherDashboard.vue'
import JoinSection from '@/views/student/JoinSection.vue'

// Teacher Dashboard children components
import DashboardHome from '@/views/teacher/DashboardHome.vue'
import MySubjects from '@/views/teacher/MySubjects.vue'
import MessagesPage from '@/views/teacher/MessagesPage.vue'
import AssessmentResults from '@/views/teacher/AssessmentResults.vue'
import SettingsPage from '@/views/teacher/SettingsPage.vue'
import UploadAssessment from '@/components/UploadAssessment.vue'

// Quiz Management components
import CreateQuiz from '@/views/teacher/CreateQuiz.vue'
import ViewQuizzes from '@/views/teacher/ViewQuizzes.vue'
import Reports from '@/views/teacher/Reports.vue'

// Analytics component
import Analytics from '@/views/teacher/Analytics.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'intro', component: Intro },
    { path: '/landing', name: 'landing', component: Landing },
    { path: '/login', name: 'login', component: Login },
    { path: '/signup', name: 'signup', component: Signup },
    { path: '/signup-student', name: 'signupStudent', component: SignupStudent },
    { path: '/role-selection', name: 'roleSelection', component: RoleSelection },
    { path: '/student-dashboard', name: 'studentDashboard', component: StudentDashboard, meta: { requiresAuth: true } },

    // Add the new route for /email-verified
    {
      path: '/email-verified',
      name: 'EmailVerified',
      component: () => import('../views/EmailVerified.vue')
    },

    // Join Class Routes (Manual Entry from Login) - Updated flow
    {
      path: '/join-class',
      name: 'JoinClass',
      component: JoinSection
    },
    // Other routes...

    // Teacher Dashboard with all routes
    {
      path: '/teacher',
      component: TeacherDashboard,
      meta: { requiresAuth: true, requiresTeacher: true },
      children: [
        // Teacher routes...
      ]
    }
  ]
})

// Navigation Guard
router.beforeEach(async (to, from, next) => {
  // Check if route requires authentication
  if (to.meta.requiresAuth) {
    const { data: { user } } = await supabase.auth.getUser()

    if (!user) {
      // Redirect to login if not authenticated
      next('/login')
      return
    }

    // Check if route requires student role
    if (to.meta.requiresStudent) {
      try {
        const { data: profile, error } = await supabase
          .from('profiles')
          .select('role')
          .eq('id', user.id)
          .single()

        if (error || profile?.role !== 'student') {
          // Redirect to student dashboard if not a student
          next('/student-dashboard')
          return
        }
      } catch (error) {
        console.error('Error checking user role:', error)
        next('/login')
        return
      }
    }

    // Check if route requires teacher role
    if (to.meta.requiresTeacher) {
      try {
        const { data: profile, error } = await supabase
          .from('profiles')
          .select('role')
          .eq('id', user.id)
          .single()

        if (error || profile?.role !== 'teacher') {
          // Redirect to login if not a teacher
          next('/login')
          return
        }
      } catch (error) {
        console.error('Error checking user role:', error)
        next('/login')
        return
      }
    }
  }

  next()
})

export default router
