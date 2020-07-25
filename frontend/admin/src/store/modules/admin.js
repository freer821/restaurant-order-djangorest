import { getAllUsers } from '@/api/user'

const admin = {
  state: {
    current_user: 'all',
    all_users: []
  },

  mutations: {
    SET_CURRENT_HANDLER: (state, current_user) => {
      state.current_user = current_user
    },
    SET_ALL_USERS: (state, all_users) => {
      state.all_users = all_users
    }
  },

  actions: {
    changeCurrentUser({ commit }, current_user) {
      commit('SET_CURRENT_HANDLER', current_user)
    },
    getAllUsers({ commit }) {
      return new Promise((resolve, reject) => {
        getAllUsers().then(response => {
          commit('SET_ALL_USERS', response.data.results)
          resolve(response.data)
        }).catch(error => {
          reject(error)
        })
      })
    }
  }
}

export default admin
