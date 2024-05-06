import Vue from 'vue';

import App from './App.vue';
import router from './router';
import vuetify from '@/plugins/vuetify';
import axios from 'axios';
import store from './store';
import './assets/main.css';
// Request interceptor to add the auth token header to requests
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

// Response interceptor to handle errors globally
axios.interceptors.response.use(
    (response) => {
        return response;
    },
    (error) => {
        if (error.response && error.response.status === 401) {
            // If the API returns a 401 error, assume the token is invalid or expired
            // Clear the session and redirect to login
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
    render: (h) => h(App),
}).$mount('#app');
