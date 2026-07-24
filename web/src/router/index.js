import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Scripts from '../views/Scripts.vue'
import ScriptDetail from '../views/ScriptDetail.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/scripts',
    name: 'Scripts',
    component: Scripts
  },
  {
    path: '/scripts/:id',
    name: 'ScriptDetail',
    component: ScriptDetail
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior() {
    return { top: 0 }
  }
})

export default router
