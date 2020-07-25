import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/views/layout/Layout'

/** note: Submenu only appear when children.length>=1
 *  detail see  https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 **/

/**
* hidden: true                   if `hidden:true` will not show in the sidebar(default is false)
* alwaysShow: true               if set true, will always show the root menu, whatever its child routes length
*                                if not set alwaysShow, only more than one route under the children
*                                it will becomes nested mode, otherwise not show the root menu
* redirect: noredirect           if `redirect:noredirect` will no redirect in the breadcrumb
* name:'router-name'             the name is used by <keep-alive> (must set!!!)
* meta : {
    perms: ['GET /aaa','POST /bbb']     will control the page perms (you can set multiple perms)
    title: 'title'               the name show in submenu and breadcrumb (recommend set)
    icon: 'svg-name'             the icon show in the sidebar,
    noCache: true                if true ,the page will no be cached(default is false)
  }
**/
export const constantRouterMap = [
  {
    path: '/redirect',
    component: Layout,
    hidden: true,
    children: [
      {
        path: '/redirect/:path*',
        component: () => import('@/views/redirect/index')
      }
    ]
  },
  {
    path: '/login',
    component: () => import('@/views/login/index'),
    hidden: true
  },
  {
    path: '/auth-redirect',
    component: () => import('@/views/login/authredirect'),
    hidden: true
  },
  {
    path: '/404',
    component: () => import('@/views/errorPage/404'),
    hidden: true
  },
  {
    path: '/401',
    component: () => import('@/views/errorPage/401'),
    hidden: true
  },
  {
    path: '',
    component: Layout,
    redirect: 'dashboard',
    children: [
      {
        path: 'dashboard',
        component: () => import('@/views/dashboard/index'),
        name: 'Dashboard',
        meta: { title: '首页', icon: 'dashboard', affix: true }
      }
    ]
  }
]

export default new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRouterMap
})

export const userRouterMap = [
  { path: '*', redirect: '/404', hidden: true }
]

export const adminRouterMap = [
  {
    path: '/admin/category',
    component: Layout,
    redirect: '/admin/category/list',
    alwaysShow: true,
    name: 'storeAdminManage',
    meta: {
      title: '分类管理',
      icon: 'chart'
    },
    children: [
      {
        path: 'list',
        component: () => import('@/views/category/list'),
        name: 'categoryList',
        meta: {
          title: '分类列表',
          noCache: true
        }
      },
      {
        path: 'single',
        component: () => import('@/views/category/single'),
        name: 'categoryEdit',
        meta: {
          title: '新建分类',
          noCache: true
        }
      }
    ]
  },
  {
    path: '/admin/forecast',
    component: Layout,
    redirect: '/admin/forecast/list',
    alwaysShow: true,
    name: 'forecastAdminManage',
    meta: {
      title: '预报管理',
      icon: 'guide'
    },
    children: [
      {
        path: 'list',
        component: () => import('@/views/forecast/admin_list'),
        name: 'forecastList',
        meta: {
          title: '预报列表',
          noCache: true
        }
      },
      {
        path: 'handle',
        component: () => import('@/views/forecast/admin_handle'),
        name: 'forecastAdminHandle',
        meta: {
          title: '入库扫描',
          noCache: true
        }
      },
      {
        path: 'create',
        component: () => import('@/views/forecast/admin_create'),
        name: 'forecastAdminCreate',
        meta: {
          title: '未预报入库',
          noCache: true
        }
      },
      {
        path: 'edit',
        component: () => import('@/views/forecast/admin_update'),
        name: 'forecastAdminUpdate',
        meta: {
          title: '预报更新',
          noCache: true
        },
        hidden: true
      }
    ]
  },
  {
    path: '/admin/user',
    component: Layout,
    redirect: '/admin/user/list',
    alwaysShow: true,
    name: 'userManage',
    meta: {
      title: '用户管理',
      icon: 'guide'
    },
    children: [

      {
        path: 'list',
        component: () => import('@/views/user/admin-user-list'),
        name: 'list',
        meta: {
          title: '用户列表',
          noCache: true
        }
      },
      {
        path: 'files',
        component: () => import('@/views/user/admin-files'),
        name: 'files',
        meta: {
          title: '用户文件',
          noCache: true
        }
      }
    ]
  }
]
