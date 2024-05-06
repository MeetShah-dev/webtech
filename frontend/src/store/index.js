// store/index.js

import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    count: 0
  },
  mutations: {
    increment(state) {
      state.count++;
    }
  },
  actions: {
    incrementNotificationCount({ commit }) {
      commit('increment');
    }
  },
  getters: {
    currentCount: state => state.count
  }
});
