import Vue from 'vue';
import VueRouter from 'vue-router';
import HomeView from '../views/HomeView.vue';
import LoginPage from '@/views/LoginPage.vue';
import AuthorPage from '@/views/AuthorPage.vue';
import MagazineView from '@/views/MagazineView.vue';
import EmptyPage from '@/views/EmptyPage.vue';

Vue.use(VueRouter);

const router = new VueRouter({
    mode: 'history',
    base: import.meta.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomeView,
        },
        {
            path: '/dashboard',
            name: 'dashboard',
            component: () => import('../views/DashboardView.vue'),
        },
        {
            path: '/login',
            name: 'login',
            component: LoginPage,
        },
        {
            path: '/author-page',
            name: 'author',
            component: AuthorPage,
        },
        {
            path: '/read-magazine',
            name: 'magazine view',
            component: MagazineView,
        },
        {
            path: '*',
            component: EmptyPage,
        },
    ],
});

export default router;
