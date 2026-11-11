import { createRouter, createWebHistory } from 'vue-router'
import { currentUser, isAuthenticated, authReady } from '../auth.js'

import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import PositionsView from '../views/PositionsView.vue'
import AccessDeniedView from '../views/AccessDeniedView.vue'
import ManagePositionsView from '../views/ManagePositionsView.vue'
import ManageUsersView from '../views/ManageUsersView.vue'
import RegisterView from '../views/RegisterView.vue'
import SendEmailView from '../views/SendEmailView.vue';
import AdminDashboardView from '../views/AdminDashboardView.vue';

const routes = [
    {
        path: '/',
        name: 'Home',
        component: HomeView,
    },
    {
        path: '/login',
        name: 'Login',
        component: LoginView,
    },
    {
        path: '/positions',
        name: 'Positions',
        component: PositionsView,
        meta: {
            requiresAuth: true,
        },
    },
    {
        path: '/access-denied',
        name: 'AccessDenied',
        component: AccessDeniedView,
    },
    {
        path: '/manage-positions',
        name: 'ManagePositions',
        component: ManagePositionsView,
        meta: {
            requiresAuth: true,
        },
        beforeEnter: (to, from, next) => {
            if (currentUser.value && currentUser.value.role === 'editor') {
                next()
            } else {
                next({ name: 'AccessDenied' })
            }
        },
    },
    {
        path: '/manage-users',
        name: 'ManageUsers',
        component: ManageUsersView,
        meta: {
            requiresAuth: true,
        },
        beforeEnter: (to, from, next) => {
            if (currentUser.value && currentUser.value.role === 'admin') {
                next()
            } else {
                next({ name: 'AccessDenied' })
            }
        },
    },
    {
        path: '/register',
        name: 'Register',
        component: RegisterView,
    },
    {
        path: '/send-email',
        name: 'SendEmail',
        component: SendEmailView,
        meta: {
            requiresAuth: true,
        },
        beforeEnter: (to, from, next) => {
            if (currentUser.value && currentUser.value.role === 'admin') {
                next();
            } else {
                next({ name: 'AccessDenied' });
            }
        },
    },
    {
        path: '/admin-dashboard',
        name: 'AdminDashboard',
        component: AdminDashboardView,
        meta: {
            requiresAuth: true,
        },
        beforeEnter: (to, from, next) => {
            if (currentUser.value && currentUser.value.role === 'admin') {
                next();
            } else {
                next({ name: 'AccessDenied' });
            }
        },
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

router.beforeEach(async (to, from, next) => {
    await authReady;

    if (to.meta.requiresAuth && !isAuthenticated.value) {
        next({ name: 'Login' });
    } else {
        next();
    }
});

const pageTitles = {
    Home: 'Home',
    Login: 'Login',
    Register: 'Register',
    Positions: 'Volunteer Positions',
    ManagePositions: 'Manage Positions',
    ManageUsers: 'Manage Users',
    SendEmail: 'Send Volunteer Information',
    AdminDashboard: 'Admin Dashboard',
    AccessDenied: 'Access Denied',
};

router.afterEach((to, from, failure) => {
    if (failure) return;

    const title = pageTitles[to.name];

    document.title = title
        ? title + ' | Canopy Connect'
        : 'Canopy Connect Melbourne';
});

export default router