import Vue from 'vue'
import VueRouter from 'vue-router'
import Workbench from '../components/home/Workbench.vue'
import Project from '../components/project/Project.vue'
import Email from '../components/config/email/Email.vue'
import Env from '../components/config/environment/Env.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Workbench',
    component: Workbench
  },
  {
    path: '/project',
    name: 'Project',
    component: Project
  },
  {
    path: '/env',
    name: 'Env',
    component: Env
  },
  {
    path: '/email',
    name: 'Email',
    component: Email
  }
]

const router = new VueRouter({
  mode: 'hash', // 模式: hash/history
  base: process.env.BASE_URL,
  routes
})

export default router
