<template>
    <div class="container py-3">
        <div
            class="d-flex flex-column flex-lg-row 
            align-items-center justify-content-lg-between gap-3"
        >
            
            <router-link
                to="/"
                class="text-decoration-none fw-bold fs-4 text-center"
            >
                Canopy Connect
            </router-link>
            
            <nav aria-label="Main">
                <ul class="nav nav-pills flex-column flex-sm-row flex-wrap
                    justify-content-center align-items-center gap-1">

                    <li class="nav-item">
                        <router-link
                            to="/"
                            class="nav-link"
                            active-class="active"
                        >
                            Home
                        </router-link>
                    </li>

                    <li v-if="isAuthenticated" class="nav-item">
                        <router-link
                            to="/positions"
                            class="nav-link"
                            active-class="active"
                        >
                            Positions
                        </router-link>
                    </li>

                    <li
                        v-if="isAuthenticated && currentUser.role === 'editor'"
                        class="nav-item"
                    >
                        <router-link
                            to="/manage-positions"
                            class="nav-link"
                            active-class="active"
                        >
                            Manage Positions
                        </router-link>
                    </li>

                    <li
                        v-if="isAuthenticated && currentUser.role === 'admin'"
                        class="nav-item"
                    >
                        <router-link
                            to="/admin-dashboard"
                            class="nav-link"
                            active-class="active"
                        >
                            Dashboard
                        </router-link>
                    </li>

                    <li
                    v-if="isAuthenticated && currentUser.role === 'admin'"
                    class="nav-item"
                    >
                        <router-link
                            to="/manage-users"
                            class="nav-link"
                            active-class="active"
                        >
                            Manage Users
                        </router-link>
                    </li>

                    <li v-if="!isAuthenticated" class="nav-item">
                        <router-link
                            to="/register"
                            class="nav-link"
                            active-class="active"
                        >
                            Register
                        </router-link>
                    </li>

                    <li v-if="!isAuthenticated" class="nav-item">
                        <router-link
                            to="/login"
                            class="nav-link"
                            active-class="active"
                        >
                            Login
                        </router-link>
                    </li>

                    <li v-else class="nav-item">
                        <button
                            type="button"
                            class="nav-link"
                            @click="logout"
                        >
                            Logout
                        </button>
                    </li>

                    <li
                        v-if="isAuthenticated && currentUser.role === 'admin'"
                        class="nav-item"
                    >
                        <router-link
                            to="/send-email"
                            class="nav-link"
                            active-class="active"
                        >
                            Send Email
                        </router-link>
                    </li>   

                    <li v-if="isAuthenticated" class="nav-item">
                        <span class="nav-link disabled">
                            {{ currentUser.username }} — {{ currentUser.role }}
                        </span>
                    </li>
                </ul>
            </nav>
        </div>
    </div>
</template>

<script setup>
    import { currentUser, isAuthenticated } from '../auth.js';
    import { useRouter } from 'vue-router';
    import { signOut } from 'firebase/auth';
    import { auth } from '../firebase/init.js';
    
    const router = useRouter();

    const logout = async () => {
        try {
            await signOut(auth);

            currentUser.value = null;
            isAuthenticated.value = false;
            router.push({ name: 'Login' });
        } catch (error) {
            console.error('Logout failed:', error);
        }
    };

</script>