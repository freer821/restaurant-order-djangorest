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
  {
    path: '/forecast',
    component: Layout,
    redirect: '/forecast/list',
    alwaysShow: true,
    name: 'forecastManage',
    meta: {
      title: '预报管理',
      icon: 'guide'
    },
    children: [
      {
        path: 'single-create',
        component: () => import('@/views/forecast/create'),
        name: 'singleCreate',
        meta: {
          title: '创建预报',
          noCache: true
        }
      },
      {
        path: 'excel-upload',
        component: () => import('@/views/forecast/excel-upload'),
        name: 'excelUpload',
        meta: {
          title: '批量导入',
          noCache: true
        }
      },
      {
        path: 'edit',
        component: () => import('@/views/forecast/edit'),
        name: 'edit',
        hidden: true,
        meta: {
          title: '预报修改',
          noCache: true
        }
      },
      {
        path: 'forecastList',
        component: () => import('@/views/forecast/list'),
        name: 'forecastList',
        meta: {
          title: '预报列表',
          noCache: true
        }
      }
    ]
  },
  {
    path: '/warehouse',
    component: Layout,
    redirect: '/warehouse/list',
    alwaysShow: true,
    name: 'storeManage',
    meta: {
      title: '库存管理',
      icon: 'chart'
    },
    children: [
      {
        path: 'list',
        component: () => import('@/views/warehouse/list'),
        name: 'storeList',
        meta: {
          title: '库存列表',
          noCache: true
        }
      },
      {
        path: 'product',
        component: () => import('@/views/warehouse/product_list'),
        name: 'productList',
        hidden: true,
        meta: {
          title: '库存详情',
          noCache: true
        }
      }
    ]
  },
  {
    path: '/chuku',
    component: Layout,
    redirect: '/chuku/list',
    alwaysShow: true,
    name: 'chukuManage',
    meta: {
      title: '出库管理',
      icon: 'guide'
    },
    children: [
      {
        path: 'single-create',
        component: () => import('@/views/chuku/create'),
        name: 'singleCreate',
        meta: {
          title: '出库预报',
          noCache: true
        }
      },
      {
        path: 'edit',
        component: () => import('@/views/chuku/edit'),
        name: 'edit',
        hidden: true,
        meta: {
          title: '出库修改',
          noCache: true
        }
      },
      {
        path: 'list',
        component: () => import('@/views/chuku/admin-list'),
        name: 'list',
        meta: {
          title: '出库列表',
          noCache: true
        }
      }
    ]
  },
  {
    path: '/profile',
    component: Layout,
    redirect: '/profile/info',
    name: 'profileManage',
    meta: {
      title: '个人中心',
      icon: 'chart'
    },
    children: [

      {
        path: 'info',
        component: () => import('@/views/profile/notice'),
        name: 'profileInfo',
        meta: {
          title: '账户信息',
          noCache: true
        }
      },
      {
        path: 'password',
        component: () => import('@/views/profile/password'),
        name: 'profilePassword',
        meta: {
          title: '修改密码',
          noCache: true
        }
      },
      {
        path: 'files',
        component: () => import('@/views/user/files'),
        name: 'files',
        meta: {
          title: '用户文件',
          noCache: true
        }
      }
    ]
  },
  { path: '*', redirect: '/404', hidden: true }
]

export const adminRouterMap = [
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
        name: 'forecastAdminList',
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
    path: '/admin/warehouse',
    component: Layout,
    redirect: '/admin/warehouse/list',
    alwaysShow: true,
    name: 'storeAdminManage',
    meta: {
      title: '库存管理',
      icon: 'chart'
    },
    children: [
      {
        path: 'list',
        component: () => import('@/views/warehouse/admin_list'),
        name: 'storeAdminList',
        meta: {
          title: '库存列表',
          noCache: true
        }
      },
      {
        path: 'check',
        component: () => import('@/views/warehouse/admin_check'),
        name: 'storeAdminCheck',
        meta: {
          title: '检修',
          noCache: true
        }
      },
      {
        path: 'checkdetail',
        component: () => import('@/views/warehouse/admin_check_detail'),
        name: 'storeAdminCheckDetail',
        hidden: true,
        meta: {
          title: '检修 - 详细录入',
          noCache: true
        }
      },
      {
        path: 'product',
        component: () => import('@/views/warehouse/admin_product_list'),
        name: 'storeAdminProduct',
        hidden: true,
        meta: {
          title: '商品库存详情',
          noCache: true
        }
      }
    ]
  },
  {
    path: '/admin/chuku',
    component: Layout,
    redirect: '/admin/chuku/list',
    alwaysShow: true,
    name: 'chukuManage',
    meta: {
      title: '出库管理',
      icon: 'guide'
    },
    children: [
      {
        path: 'create',
        component: () => import('@/views/chuku/admin-create'),
        name: 'create',
        meta: {
          title: '出库预报',
          noCache: true
        }
      },
      {
        path: 'edit',
        component: () => import('@/views/chuku/admin-edit'),
        name: 'edit',
        hidden: true,
        meta: {
          title: '出库修改',
          noCache: true
        }
      },
      {
        path: 'list',
        component: () => import('@/views/chuku/admin-list'),
        name: 'list',
        meta: {
          title: '出库列表',
          noCache: true
        }
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
