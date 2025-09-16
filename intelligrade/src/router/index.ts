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
import JoinClassAuth from '@/views/JoinClassAuth.vue'
import ClassCodeEntry from '@/views/ClassCodeEntry.vue' // Add this import

// Teacher Dashboard children components
import DashboardHome from '@/views/teacher/DashboardHome.vue'
import MySubjects from '@/views/teacher/MySubjects.vue' // Add this import
import MessagesPage from '@/views/MessagesPage.vue'
import AssessmentResults from '@/views/teacher/AssessmentResults.vue'
import CreateQuiz from '@/views/teacher/CreateQuiz.vue'
import SettingsPage from '@/views/SettingsPage.vue'
import UploadAssessment from '@/components/UploadAssessment.vue'

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
    
    // Join Class Routes (Manual Entry from Login)
    {
      path: '/join-class',
      name: 'JoinClassAuth',
      component: JoinClassAuth
    },
    {
      path: '/join-class/enter-code',
      name: 'ClassCodeEntry',
      component: ClassCodeEntry,
      meta: { requiresAuth: true, requiresStudent: true }
    },
    {
      path: '/join-class/select-section',
      name: 'SectionSelection',
      component: () => import('@/views/SectionSelection.vue'),
      meta: { requiresAuth: true, requiresStudent: true }
    },

    // Link-based joining routes (Fixed to match teacher-generated URLs)
    {
      path: '/join-class/:classCode',
      name: 'JoinClass',
      component: JoinClassAuth,
      props: true
    },
    {
      path: '/join-section/:classCode/:sectionCode',
      name: 'JoinSpecificSection',
      component: JoinClassAuth,
      props: true,
      meta: { skipSectionSelection: true }
    },
    
    // Section code input page
    {
      path: '/join-class/section-code',
      name: 'SectionCode',
      component: () => import('@/views/SectionCode.vue'),
      meta: { requiresAuth: true, requiresStudent: true }
    },

    {
      path: '/teacher',
      component: TeacherDashboard,
      meta: { requiresAuth: true },
      children: [
        {
          path: '',
          redirect: 'dashboard'
        },
        {
          path: 'dashboard',
          name: 'DashboardHome',
          component: DashboardHome
        },
        {
          path: 'subjects',
          name: 'MySubjects',
          component: MySubjects
        },
        {
          path: 'messages',
          name: 'MessagesPage',
          component: MessagesPage
        },
        {
          path: 'settings', 
          name: 'SettingsPage',
          component: SettingsPage
        },
        {
          path: 'assessments/:id/results',
          name: 'AssessmentResults',
          component: AssessmentResults,
          props: true
        },
        {
          path: 'create-quiz/:subjectId',
          name: 'CreateQuiz',
          component: CreateQuiz,
          props: true
        },
        // New route for uploading assessments
        {
          path: 'upload-assessment',
          name: 'UploadAssessment',
          component: UploadAssessment,
        }
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
  }

  next()
})

export default router