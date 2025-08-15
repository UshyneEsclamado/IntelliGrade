import { createRouter, createWebHistory } from 'vue-router'

import Intro from '@/views/Intro.vue'
import Login from '@/views/Login.vue'
import Signup from '@/views/Signup.vue'
import SignupStudent from '@/views/SignupStudent.vue'
import RoleSelection from '@/views/RoleSelection.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'intro', component: Intro },
    { path: '/login', name: 'login', component: Login },
    { path: '/signup', name: 'signup', component: Signup },
    { path: '/signup-student', name: 'signupStudent', component: SignupStudent },
    { path: '/role-selection', name: 'roleSelection', component: RoleSelection }
  ]
})

export default router
