const admin = {
  state: {
    current_handler: 'All'
  },

  mutations: {
    SET_CURRENT_HANDLER: (state, current_handler) => {
      state.current_handler = current_handler
    }
  },

  actions: {
    changeCurrentHandler({ commit }, new_hanlder) {
      commit('SET_CURRENT_HANDLER', new_hanlder)
    }
  }
}

export default admin
