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
import ForgotPassword from '../views/ForgotPassword.vue'
import ResetPassword from '../views/ResetPassword.vue'

// Dashboard views
import TeacherDashboard from '../views/TeacherDashboard.vue'
import StudentDashboard from '../views/StudentDashboard.vue'

// Teacher subfolder components that actually exist
import Analytics from '../views/teacher/Analytics.vue'
import AssessmentRes from '../views/teacher/AssessmentResults.vue'
import ClassCodeEntry from '../views/teacher/ClassCodeEntry.vue'
import CreateQuiz from '../views/teacher/CreateQuiz.vue'
import EditQuiz from '../views/teacher/EditQuiz.vue'
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
import Gradebook from '../views/teacher/Gradebook.vue'

// Student subfolder components - FIXED: Removed duplicates
import Home from '../views/student/Home.vue'
import Subjects from '../views/student/Subjects.vue'
import Messages from '../views/student/Messages.vue'
import Calendar from '../views/student/Calendar.vue'
import Settings from '../views/student/Settings.vue'
import TakeQuiz from '../views/student/TakeQuiz.vue'
import StudentGrades from '../views/student/Grades.vue'

const routes = [
  {
    path: '/',
    name: 'Intro',
    component: Intro,
    meta: { public: true }
  },
  {
    path: '/landing',
    name: 'Landing',
    component: Landing,
    meta: { public: true }
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: { 
      public: true,
      guestOnly: true
    }
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup,
    meta: { 
      public: true,
      guestOnly: true
    }
  },
  {
    path: '/signup-student',
    name: 'SignupStudent',
    component: SignupStudent,
    meta: { 
      public: true,
      guestOnly: true
    }
  },
  {
    path: '/role-selection',
    name: 'RoleSelection',
    component: RoleSelection,
    meta: { 
      public: true,
      guestOnly: true
    }
  },
  {
    path: '/email-verified',
    name: 'EmailVerified',
    component: EmailVerified,
    meta: { public: true }
  },
  {
    path: '/forgot-password',
    name: 'ForgotPassword',
    component: ForgotPassword,
    meta: { public: true }
  },
  {
    path: '/reset-password',
    name: 'ResetPassword',
    component: ResetPassword,
    meta: { public: true }
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
        path: 'edit-quiz/:quizId',
        name: 'EditQuiz',
        component: EditQuiz,
        meta: { requiresAuth: true, role: 'teacher' }
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
      },
      {
        path: 'gradebook',
        name: 'TeacherGradebook',
        component: Gradebook,
        meta: { requiresAuth: true, role: 'teacher' }
      }
    ]
  },
  // Student Dashboard Routes - FIXED: Removed duplicate calendar route
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
        component: Home
      },
      {
        path: 'subjects',
        name: 'StudentSubjects',
        component: Subjects
      },
      {
        path: 'calendar',
        name: 'StudentCalendar',
        component: Calendar
      },
      {
        path: 'messages',
        name: 'StudentMessages',
        component: Messages
      },
      {
        path: 'settings',
        name: 'StudentSettings',
        component: Settings
      },
      {
        path: 'take-quiz/:subjectId/:sectionId',
        name: 'TakeQuiz',
        component: TakeQuiz
      },
      {
        path: 'grades/:subjectId/:sectionId',
        name: 'StudentGrades',
        component: StudentGrades
      }
    ]
  },
  // Legacy student dashboard route (for backward compatibility)
  {
    path: '/student-dashboard',
    redirect: '/student/dashboard'
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

// Enhanced Navigation Guard with Better Error Handling and Refresh Support
router.beforeEach(async (to, from, next) => {
  console.log('=== ROUTER NAVIGATION START ===')
  console.log('From:', from.path)
  console.log('To:', to.path)
  console.log('Route meta:', to.meta)
  
  try {
    // Get current session with retry logic for refresh scenarios
    let session = null
    let sessionError = null
    
    // Try to get session, with retry on refresh
    for (let attempt = 0; attempt < 3; attempt++) {
      const result = await supabase.auth.getSession()
      session = result.data?.session
      sessionError = result.error
      
      if (!sessionError && session) {
        break // Success
      }
      
      if (attempt < 2) {
        console.log(`Session attempt ${attempt + 1} failed, retrying...`)
        await new Promise(resolve => setTimeout(resolve, 100)) // Small delay
      }
    }
    
    if (sessionError) {
      console.error('Session error after retries:', sessionError)
      // Only sign out on authentication errors, not network errors
      if (sessionError.message?.includes('Invalid') || sessionError.message?.includes('Expired')) {
        await supabase.auth.signOut()
      }
    }

    const isAuthenticated = !!session?.user
    console.log('Is authenticated:', isAuthenticated)

    // Allow access to guest-only routes even when authenticated
    // Users can visit login/signup pages to logout or switch accounts

    // Handle routes that require authentication
    if (to.meta.requiresAuth) {
      if (!isAuthenticated) {
        console.log('Authentication required but not authenticated')
        console.log('→ Redirecting to login')
        next('/login')
        return
      }

      console.log('Valid session found for user:', session.user.email)

      // Handle role-based access with better error handling
      if (to.meta.role) {
        console.log('Checking role requirement:', to.meta.role)
        
        try {
          const { data: profile, error: profileError } = await supabase
            .from('profiles')
            .select('role')
            .eq('auth_user_id', session.user.id)
            .single()

          if (profileError) {
            console.error('Profile fetch error:', profileError)
            // Don't immediately sign out - might be a temporary network issue
            // Allow access and let the component handle it
            console.log('→ Profile error, but allowing navigation (component will handle)')
            next()
            return
          }

          if (!profile) {
            console.error('No profile found for authenticated user')
            console.log('→ No profile found, redirecting to role selection')
            next('/role-selection')
            return
          }

          console.log('User profile role:', profile.role)

          if (profile.role !== to.meta.role) {
            console.log('Role mismatch! Required:', to.meta.role, 'Got:', profile.role)
            // Redirect to appropriate dashboard based on actual role
            const redirectPath = profile.role === 'student' 
              ? '/student/dashboard' 
              : '/teacher/dashboard'
            console.log('→ Redirecting to correct dashboard:', redirectPath)
            next(redirectPath)
            return
          }

          console.log('✓ Role check passed')
        } catch (roleError) {
          console.error('Role check error:', roleError)
          // Allow navigation to continue, let component handle the auth state
          console.log('→ Role check failed, but allowing navigation')
          next()
          return
        }
      }
      
      console.log('✓ Authorization successful, proceeding to:', to.path)
      next()
      return
    }

    // Public routes - no restrictions
    console.log('Public route, no auth required')
    next()

  } catch (error) {
    console.error('=== NAVIGATION GUARD ERROR ===')
    console.error('Error details:', error)
    
    // On any error, be more forgiving for protected routes
    if (to.meta.requiresAuth) {
      console.log('→ Error on protected route, but being more forgiving')
      // Only redirect to login on authentication-specific errors
      if (error.message?.includes('Invalid') || error.message?.includes('Expired') || error.message?.includes('JWT')) {
        console.log('→ Authentication error detected, redirecting to login')
        try {
          await supabase.auth.signOut()
        } catch (signOutError) {
          console.error('Sign out error:', signOutError)
        }
        next('/login')
      } else {
        // For network or other errors, allow navigation and let component handle
        console.log('→ Non-auth error, allowing navigation')
        next()
      }
    } else {
      // Allow access to public routes even on error
      console.log('→ Error on public route, allowing access')
      next()
    }
  }
})

export default router