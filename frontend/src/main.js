import Vue from 'vue';

import App from './App.vue';
import router from './router';
import vuetify from '@/plugins/vuetify';
import axios from 'axios';
import store from './store';
import './assets/main.css';

axios.interceptors.request.use(
    (config) => {
        const token = sessionStorage.getItem('token');
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

axios.interceptors.response.use(
    (response) => {
        return response;
    },
    (error) => {
        if (error.response && error.response.status === 401) {
            sessionStorage.removeItem('token');
            router.push('/login');
            console.error(
                'Session expired or token invalid. Redirecting to login.'
            );
        }
        return Promise.reject(error);
    }
);
new Vue({
    router,
    vuetify,
    store,
    render: (h) => h(App),
}).$mount('#app');
