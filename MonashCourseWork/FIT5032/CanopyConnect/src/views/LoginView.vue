<template>
    <div v-if="!isAuthenticated" class="container mt-5">
        <div class="row justify-content-center">
            <div class="col-12 col-sm-10 col-md-8 col-lg-6 col-xl-5 col-xxl-4">
                <h1 class="text-center">Canopy Connect Login</h1>
                <form class="mt-5" @submit.prevent="submitForm">
                    <div class="mb-3">
                        <label for="login-email" class="form-label">Email</label>
                        <input 
                            type="email" 
                            class="form-control" 
                            id="login-email" 
                            v-model="formData.email"
                            autocomplete="username"
                            :aria-invalid="Boolean(errors.email)"
                            aria-describedby="login-email-error"
                            @blur="() => validateEmail(true)"
                            @input="() => validateEmail(false)"
                            required
                        >
                        <div id="login-email-error" class="text-danger" aria-live="polite">
                            {{ errors.email }}
                        </div>
                    </div>
                    <div class="mb-3">
                        <label for="password" class="form-label">Password</label>
                        <input 
                            type="password" 
                            class="form-control" 
                            id="password" 
                            autocomplete="current-password"
                            :aria-invalid="Boolean(errors.password)"
                            aria-describedby="login-password-error"
                            v-model="formData.password"
                            @blur="() => validatePassword(true)"
                            @input="() => validatePassword(false)"
                            required
                        >
                        <div id="login-password-error" class="text-danger" aria-live="polite">
                            {{ errors.password }}
                        </div>

                        <div v-if="loginError" class="text-danger mt-2" role="alert">
                            {{ loginError }}
                        </div>
                    </div>
                    <div class="d-grid gap-2 d-sm-flex justify-content-sm-center mb-3 mt-5">
                        <button 
                            type="submit" 
                            class="btn btn-primary" 
                            :disabled="isGoogleSigningIn">
                            Log In
                        </button>
                        <button
                            type="button"
                            class="btn btn-secondary"
                            @click="clearForm"
                            :disabled="isGoogleSigningIn"
                        >
                            Clear
                        </button>
                    </div>
                    <div class="d-grid mb-3">
                        <button
                            type="button"
                            class="btn btn-outline-primary"
                            :disabled="isGoogleSigningIn"
                            @click="signInWithGoogle"
                        >
                            {{ isGoogleSigningIn ? 'Signing in…' : 'Continue with Google' }}
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
    <div v-else class="container mt-5 text-center">
        <h1>Welcome, {{ currentUser.username }}!</h1>
        <p>Your role is: {{ currentUser.role }}</p>
    </div>
</template>

<script setup>
    import { ref } from 'vue';
    import { currentUser, isAuthenticated, loadUserProfile } from '../auth.js';
    import {
        signInWithEmailAndPassword,
        GoogleAuthProvider,
        signInWithPopup,
    } from 'firebase/auth';
    import { auth, db } from '../firebase/init.js';
    import { useRouter } from 'vue-router';
    import { doc, getDoc, setDoc } from 'firebase/firestore';

    const router = useRouter();

    const googleProvider = new GoogleAuthProvider();

    const formData = ref({
        email: '',
        password: '',
    });

    const errors = ref({
        email: '',
        password: '',
    });

    const loginError = ref('')
    const isGoogleSigningIn = ref(false);

    const signInWithGoogle = async () => {
        if (isGoogleSigningIn.value) return;

        loginError.value = '';
        isGoogleSigningIn.value = true;

        try {
            const credential = await signInWithPopup(auth, googleProvider);
            const user = credential.user;

            if (!user.email) {
                throw new Error('Google did not provide an email address.');
            }

            const profileRef = doc(db, 'users', user.uid);
            const snapshot = await getDoc(profileRef);

            if (!snapshot.exists()) {
                let username = 'Google User';

                if (user.displayName && user.displayName.trim().length >= 3) {
                    username = user.displayName.trim();
                }

                await setDoc(profileRef, {
                    username: username,
                    email: user.email,
                    role: 'viewer',
                });
            }

            const profile = await loadUserProfile(user.uid);

            currentUser.value = profile;
            isAuthenticated.value = true;
            formData.value.password = '';

            await router.push({ name: 'Positions' });
        } catch (error) {
            console.error('Google login or profile setup failed:', error);
            loginError.value =
                'Could not complete Google sign-in. Please try again.';
        } finally {
            isGoogleSigningIn.value = false;
        }
    };

    const submitForm = () => {
        if (isGoogleSigningIn.value) return;
        loginError.value = '';

        validateEmail(true);
        validatePassword(true);

        if (errors.value.email || errors.value.password) {
            return;
        }

        signInWithEmailAndPassword(
            auth,
            formData.value.email.trim(),
            formData.value.password
        )
        .then((credential) => {
            return loadUserProfile(credential.user.uid);
        })
        .then((profile) => {
            currentUser.value = profile;
            isAuthenticated.value = true;
            formData.value.password = '';
            router.push({ name: 'Positions' })
        })
        .catch((error) => {
            console.error('Login or profile loading failed:', error);
            loginError.value = 'Could not complete login. Check your credentials and account profile.';
        });
    };

    const clearForm = () => {
        formData.value = {
            email: '',
            password: '',
        };
        errors.value.email = '';
        errors.value.password = '';
        loginError.value = '';
    };

    const validateEmail = (blur) => {
        const email = formData.value.email.trim();
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if (!email) {
            if (blur) errors.value.email = 'Email must not be empty.';
        } else if (!emailPattern.test(email)) {
            if (blur) errors.value.email = 'Enter a valid email address.';
        } else {
            errors.value.email = '';
        }
    };

    const validatePassword = (blur) => {
        if (!formData.value.password) {
            if (blur) errors.value.password = "Password must not be empty";
        }
        else {
            errors.value.password = null;
        }
    }

</script>
