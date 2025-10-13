import { createRouter, createWebHistory } from 'vue-router'
import { supabase } from '../supabase.js'

// Import views that actually exist
import Login from '../views/Login.vue'
import RoleSelection from '../views/RoleSelection.vue'
import EmailVerified from '../views/EmailVerified.vue'
import Signup from '../views/Signup.vue'
import SignupStudent from '../views/SignupStudent.vue'
import Landing from '../views/Landing.vue'
import Intro from '../views/Intro.vue'

// Dashboard views
import TeacherDashboard from '../views/TeacherDashboard.vue'
import StudentDashboard from '../views/StudentDashboard.vue'

// Teacher subfolder components that actually exist
import Analytics from '../views/teacher/Analytics.vue'
import AssessmentRes from '../views/teacher/AssessmentResults.vue'
import ClassCodeEntry from '../views/teacher/ClassCodeEntry.vue'
import CreateQuiz from '../views/teacher/CreateQuiz.vue'
import DashboardHome from '../views/teacher/DashboardHome.vue'
import GradeManagement from '../views/teacher/GradeManagement.vue'
import MessagesPage from '../views/teacher/MessagesPage.vue'
import MySubjects from '../views/teacher/MySubjects.vue'
import SectionCode from '../views/teacher/SectionCode.vue'
import SectionSelection from '../views/teacher/SectionSelection.vue'
import SettingsPage from '../views/teacher/SettingsPage.vue'
import UploadAssessment from '../views/teacher/UploadAssessment.vue'
import AssessmentHistory from '../views/teacher/AssessmentHistory.vue'
import AssessmentDetails from '../views/teacher/AssessmentDetails.vue'
import ViewQuizzes from '../views/teacher/ViewQuizzes.vue'
import ViewStudents from '../views/teacher/ViewStudents.vue'

// Student subfolder components
import Subjects from '../views/student/Subjects.vue'
import Messages from '../views/student/Messages.vue'
import TakeQuiz from '../views/student/TakeQuiz.vue'

const routes = [
  {
    path: '/',
    name: 'Intro',
    component: Intro
  },
  {
    path: '/landing',
    name: 'Landing',
    component: Landing
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/signup-student',
    name: 'SignupStudent',
    component: SignupStudent
  },
  {
    path: '/role-selection',
    name: 'RoleSelection',
    component: RoleSelection
  },
  {
    path: '/email-verified',
    name: 'EmailVerified',
    component: EmailVerified
  },
  // Teacher Dashboard Routes
  {
    path: '/teacher',
    name: 'TeacherLayout',
    component: TeacherDashboard,
    meta: { requiresAuth: true, role: 'teacher' },
    children: [
      {
        path: '',
        redirect: 'dashboard'
      },
      {
        path: 'dashboard',
        name: 'TeacherDashboardHome',
        component: DashboardHome
      },
      {
        path: 'subjects',
        name: 'MySubjects',
        component: MySubjects
      },
      {
        path: 'analytics',
        name: 'Analytics',
        component: Analytics
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
        path: 'upload-assessment',
        name: 'UploadAssessment',
        component: UploadAssessment,
        meta: { requiresAuth: true, role: 'teacher' }
      },
      {
        path: 'assessment-history',
        name: 'AssessmentHistory',
        component: AssessmentHistory,
        meta: { requiresAuth: true, role: 'teacher' }
      },
      {
        path: 'assessment-details/:id',
        name: 'AssessmentDetails',
        component: AssessmentDetails,
        meta: { requiresAuth: true, role: 'teacher' }
      },
      {
        path: 'assessment-results',
        name: 'AssessmentRes',
        component: AssessmentRes
      },
      {
        path: 'class-code-entry',
        name: 'ClassCodeEntry',
        component: ClassCodeEntry
      },
      {
        path: 'create-quiz/:subjectId/:sectionId',
        name: 'CreateQuiz',
        component: CreateQuiz
      },
      {
        path: 'grade-management/:subjectId/:sectionId',
        name: 'GradeManagement',
        component: GradeManagement
      },
      {
        path: 'section-code',
        name: 'SectionCode',
        component: SectionCode
      },
      {
        path: 'section-selection',
        name: 'SectionSelection',
        component: SectionSelection
      },
      {
        path: 'view-quizzes/:subjectId/:sectionId',
        name: 'ViewQuizzes',
        component: ViewQuizzes
      },
      {
        path: 'view-students/:subjectId/:sectionId',
        name: 'ViewStudents',
        component: ViewStudents
      }
    ]
  },
  // Student Dashboard Routes
  {
    path: '/student',
    name: 'StudentLayout',
    component: StudentDashboard,
    meta: { requiresAuth: true, role: 'student' },
    children: [
      {
        path: '',
        redirect: 'dashboard'
      },
      {
        path: 'dashboard',
        name: 'StudentDashboardHome',
        component: StudentDashboard
      },
      {
        path: 'subjects',
        name: 'StudentSubjects',
        component: Subjects
      },
      {
        path: 'messages',
        name: 'StudentMessages',
        component: Messages
      }
    ]
  },
  // TakeQuiz Route - UPDATED with both subjectId and sectionId
  {
    path: '/student/take-quiz/:subjectId/:sectionId',
    name: 'TakeQuiz',
    component: TakeQuiz,
    meta: { requiresAuth: true, role: 'student' }
  },
  // Legacy student dashboard route (for backward compatibility)
  {
    path: '/student-dashboard',
    redirect: '/student/dashboard'
  },
  // Forgot/Reset Password routes
  {
    path: '/forgot-password',
    name: 'ForgotPassword',
    component: () => import('../views/ForgotPassword.vue')
  },
  {
    path: '/reset-password',
    name: 'ResetPassword',
    component: () => import('../views/ResetPassword.vue')
  },
  // Catch-all redirect to Intro
  {
    path: '/:pathMatch(.*)*',
    redirect: '/'
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// Navigation guard
router.beforeEach(async (to, from, next) => {
  console.log('=== ROUTER NAVIGATION ===')
  console.log('Going to:', to.path)
  console.log('Coming from:', from.path)
  console.log('Route meta:', to.meta)
  
  if (to.meta.requiresAuth) {
    try {
      const { data: { session }, error } = await supabase.auth.getSession()
      
      if (error || !session) {
        console.log('No valid session, redirecting to login')
        next('/login')
        return
      }

      console.log('Valid session found for user:', session.user.email)

      // Check user role if required
      if (to.meta.role) {
        console.log('Checking user role requirement:', to.meta.role)
        
        const { data: profile, error: profileError } = await supabase
          .from('profiles')
          .select('role')
          .eq('auth_user_id', session.user.id)
          .single()

        if (profileError) {
          console.error('Profile fetch error:', profileError)
          next('/login')
          return
        }

        console.log('User profile role:', profile?.role)

        if (!profile || profile.role !== to.meta.role) {
          console.log('Role mismatch or no profile')
          if (profile?.role === 'student') {
            console.log('Redirecting to student dashboard')
            next('/student/dashboard')
          } else if (profile?.role === 'teacher') {
            console.log('Redirecting to teacher dashboard')
            next('/teacher/dashboard')
          } else {
            console.log('No valid role, redirecting to login')
            next('/login')
          }
          return
        }
      }
      
      console.log('Authorization successful, proceeding to:', to.path)
      next()
    } catch (error) {
      console.error('Auth check error:', error)
      next('/login')
    }
  } else {
    console.log('No auth required, proceeding to:', to.path)
    next()
  }
})

export default router