import { loginByUsername, logout } from '@/api/login'
import { getUserInfo, updateUserInfo } from '@/api/user'
import { getToken, setToken, removeToken } from '@/utils/auth'

const user = {
  state: {
    token: getToken(),
    username: '',
    is_admin: undefined,
    profile: ''
  },

  mutations: {
    SET_TOKEN: (state, token) => {
      state.token = token
    },
    SET_USERNAME: (state, username) => {
      state.username = username
    },
    SET_IS_ADMIN: (state, is_admin) => {
      state.is_admin = is_admin
    },
    SET_PROFILE: (state, profile) => {
      state.profile = profile
    }

  },

  actions: {
    // 用户名登录
    LoginByUsername({ commit }, userInfo) {
      const username = userInfo.username.trim()
      return new Promise((resolve, reject) => {
        loginByUsername(username, userInfo.password).then(response => {
          const token = 'Token ' + response.data.token
          commit('SET_TOKEN', token)
          setToken(token)
          resolve()
        }).catch(error => {
          reject(error)
        })
      })
    },

    // 获取用户信息
    GetUserInfo({ commit }) {
      return new Promise((resolve, reject) => {
        getUserInfo().then(response => {
          commit('SET_USERNAME', response.data.username)
          commit('SET_IS_ADMIN', response.data.is_superuser)
          commit('SET_PROFILE', response.data.profile)
          resolve(response.data)
        }).catch(error => {
          reject(error)
        })
      })
    },

    // 第三方验证登录
    // LoginByThirdparty({ commit, state }, code) {
    //   return new Promise((resolve, reject) => {
    //     commit('SET_CODE', code)
    //     loginByThirdparty(state.status, state.email, state.code).then(response => {
    //       commit('SET_TOKEN', response.data.token)
    //       setToken(response.data.token)
    //       resolve()
    //     }).catch(error => {
    //       reject(error)
    //     })
    //   })
    // },

    // 登出
    LogOut({ commit }) {
      return new Promise((resolve, reject) => {
        logout().then(response => {
          commit('SET_TOKEN', '')
          commit('SET_IS_ADMIN', undefined)
          commit('SET_USERNAME', '')
          commit('SET_PROFILE', '')
          removeToken()
          resolve()
        }).catch(error => {
          reject(error)
        })
      })
    },

    updateProfile({ commit }, profile) {
      return new Promise((resolve, reject) => {
        updateUserInfo(profile).then(response => {
          commit('SET_PROFILE', response.data.profile)
          resolve()
        }).catch(error => {
          reject(error)
        })
      })
    },

    // remove token
    resetToken({ commit }) {
      return new Promise(resolve => {
        commit('SET_TOKEN', '')
        commit('SET_IS_ADMIN', undefined)
        commit('SET_USERNAME', '')
        commit('SET_PROFILE', '')
        removeToken()
        resolve()
      })
    }

  }
}

export default user
