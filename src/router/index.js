import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'
import Workbench from '../components/home/Workbench.vue'
import Project from '../components/project/Project.vue'
import Email from '../components/config/email/Email.vue'
import Env from '../components/config/environment/Env.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect: '/login'
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
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
  mode: 'history', // 模式: hash/history
  base: process.env.BASE_URL,
  routes
})

// 导航守卫，控制一些页面登录才能访问
router.beforeEach((to, from, next) => {
  if (to.path === '/login') { // 当路由为login时就直接下一步操作
    next();
  } else { // 否则就需要判断
    if (sessionStorage.token) { // 如果有用户名就进行下一步操作
      next()
    } else {
      next({ path: '/login' }) // 没有用户名就跳转到login页面
    }
  }
});

export default router
