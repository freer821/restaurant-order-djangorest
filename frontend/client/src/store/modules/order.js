import {calcCartGoodId } from '@/utils/cart'

const state = {
	order: undefined,
}

const mutations = {
	SET_ORDER: (state, order) => {
		state.order = order
	},
	CLEAR_ORDER: (state) => {
		state.order = undefined
	}
}

const actions = {
	setOrder({commit}, order) {
		commit('SET_ORDER', order);
	},
	clearOrder({commit}) {
		commit('CLEAR_ORDER');
	}

}

export default {
	namespaced: true,
	state,
	mutations,
	actions
}
