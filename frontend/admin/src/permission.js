import router from './router'
import store from './store'
import { Message } from 'element-ui'
import NProgress from 'nprogress' // progress bar
import 'nprogress/nprogress.css'// progress bar style
import { getToken } from '@/utils/auth' // getToken from cookie

NProgress.configure({ showSpinner: false })// NProgress Configuration

const whiteList = ['/login', '/auth-redirect']// no redirect whitelist

router.beforeEach(async(to, from, next) => {
  NProgress.start() // start progress bar
  if (getToken()) { // determine if there has token
    /* has token*/
    if (to.path === '/login') {
      next({ path: '/' })
      NProgress.done() // if current page is dashboard will not trigger	afterEach hook, so manually handle it
    } else {
      if (store.getters.is_admin === undefined) { // 判断当前用户是否已拉取完user_info信息
        try {
          const { is_superuser } = await store.dispatch('GetUserInfo')

          if (is_superuser) {
            store.dispatch('getAllUsers')
          }

          // generate accessible routes map based on roles
          const accessRoutes = await store.dispatch('GenerateRoutes', is_superuser)

          // dynamically add accessible routes
          router.addRoutes(accessRoutes)

          next({ ...to, replace: true })
        } catch (err) {
          // remove token and go to login page to re-login
          await store.dispatch('resetToken')
          Message.error(JSON.stringify(err.msg) || 'Has Error')
          next(`/login?redirect=${to.path}`)
          NProgress.done()
        }
      } else {
        // 没有动态改变权限的需求可直接next() 删除下方权限判断 ↓
        next()
        // 可删 ↑
      }
    }
  } else {
    /* has no token*/
    if (whiteList.indexOf(to.path) !== -1) { // 在免登录白名单，直接进入
      next()
    } else {
      next(`/login?redirect=${to.path}`) // 否则全部重定向到登录页
      NProgress.done() // if current page is login will not trigger afterEach hook, so manually handle it
    }
  }
})

router.afterEach(() => {
  NProgress.done() // finish progress bar
})
