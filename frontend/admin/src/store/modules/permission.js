import { userRouterMap, adminRouterMap, constantRouterMap } from '@/router'

const permission = {
  state: {
    routers: constantRouterMap,
    addRouters: []
  },
  mutations: {
    SET_ROUTERS: (state, routers) => {
      state.addRouters = routers
      state.routers = constantRouterMap.concat(routers)
    }
  },
  actions: {
    GenerateRoutes({ commit }, is_admin) {
      return new Promise(resolve => {
        let accessedRoutes
        if (is_admin) {
          // eslint-disable-next-line no-undef
          accessedRoutes = adminRouterMap
        } else {
          accessedRoutes = userRouterMap
        }
        commit('SET_ROUTERS', accessedRoutes)
        resolve(accessedRoutes)
      })
    }
  }
}

export default permission
