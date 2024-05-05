import Vue from 'vue';
import VueRouter from 'vue-router';
import HomeView from '../views/HomeView.vue';
import LoginPage from '@/views/LoginPage.vue';
import AuthorPage from '@/views/AuthorPage.vue';
import MagazineView from '@/views/MagazineView.vue';
import EmptyPage from '@/views/EmptyPage.vue';
import axios from 'axios'
Vue.use(VueRouter);
// Authentication Guard
const requireAuthHome = (to, from, next) => {
    // Attempt to parse and set user data if coming with URL parameters
    const urlParams = new URLSearchParams(window.location.search);
    const user = urlParams.get('user');
    const token = urlParams.get('token');

    if (user && token) {
        try {
            const parsedUser = JSON.parse(decodeURIComponent(user));
            sessionStorage.setItem('user', JSON.stringify(parsedUser));
            sessionStorage.setItem('token', token);
            next();  // Continue to the route
        } catch (error) {
            console.error('Failed to parse user data:', error);
            next('/login');  // Redirect to login if parsing fails
        }
    } else {
        requireAuth(to, from, next)
    }
};


const requireAuth = async (to, from, next) => {
    const token = sessionStorage.getItem('token');
    if (!token) {
        next('/login');
        return;
    }
    try {
        const result = await verifyToken(token);
        if (result.isValid) {
            next();
        } else {
            sessionStorage.clear(); // Clear session storage
            next('/login');
        }
    } catch (error) {
        console.error('Error verifying token:', error);
        sessionStorage.clear();
        next('/login');
    }
};


const ifAuthenticated = (to, from, next) => {
    const user = sessionStorage.getItem('user');
    if (user) {
        if (to.path === '/login') {
            next(from.fullPath || '/');
        } else {
            next();
        }
    } else {
        next();
    }
};


function verifyToken(accessToken) {
    const url = `https://www.googleapis.com/oauth2/v3/tokeninfo?access_token=${accessToken}`;
    return axios.get(url)
        .then(response => {
            if (response.data && response.data.aud) {
                return { isValid: true, data: response.data };
            }
            return { isValid: false };
        })
        .catch(error => {
            console.error("Token verification failed:", error);
            return { isValid: false };
        });
}
const router = new VueRouter({
    mode: 'history',
    base: import.meta.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomeView,
            beforeEnter: requireAuthHome
        },
        {
            path: '/dashboard',
            name: 'dashboard',
            component: () => import('../views/DashboardView.vue'),
            beforeEnter: requireAuth
        },
        {
            path: '/editing',
            name: 'editing',
            component: () => import('../views/EditingView.vue'),
            beforeEnter: requireAuth
        },
        {
            path: '/login',
            name: 'login',
            component: LoginPage,
            beforeEnter: ifAuthenticated

        },
        {
            path: '/author-page',
            name: 'author',
            component: AuthorPage,
            beforeEnter: requireAuth
        },
        {
            path: '/read-magazine',
            name: 'magazine view',
            component: MagazineView,
            beforeEnter: requireAuth

        },
        {
            path: '*',
            component: EmptyPage,
            beforeEnter: requireAuth

        },
        {
            path: '/dashboard/create-article',
            name: 'CreateBlog',
            component: () => import('../components/ArticleCreation.vue'),
            beforeEnter: requireAuth

        },
    ],
});


export default router;
