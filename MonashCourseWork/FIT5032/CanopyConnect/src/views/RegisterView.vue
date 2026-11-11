<template>
    <div class="container mt-5">
        <div class="row justify-content-center">
            <div class="col-12 col-sm-10 col-md-8 col-lg-6 col-xl-5 col-xxl-4">
                <h1 class="text-center">Join Canopy Connect</h1>

                <div
                    v-if="registrationError"
                    class="alert alert-danger"
                    role="alert"
                >
                    {{ registrationError }}
                </div>

                <form
                    class="mt-4"
                    @submit.prevent="registerUser"
                >
                    <div class="mb-3">
                            <label for="register-username" class="form-label">
                            Username
                        </label>

                        <input
                            id="register-username"
                            v-model="formData.username"
                            type="text"
                            class="form-control"
                            required
                            minlength="3"
                            autocomplete="username"
                            :aria-invalid="Boolean(errors.username)"
                            aria-describedby="register-username-error"
                            @blur="() => validateUsername(true)"
                            @input="() => validateUsername(false)"
                        >

                        <div
                            id="register-username-error"
                            class="text-danger"
                            aria-live="polite"
                        >
                            {{ errors.username }}
                        </div>
                    </div>



                    <div class="mb-3">
                        <label for="register-email" class="form-label">
                            Email
                        </label>

                        <input
                            id="register-email"
                            v-model="formData.email"
                            type="email"
                            class="form-control"
                            autocomplete="email"
                            required
                            :aria-invalid="Boolean(errors.email)"
                            aria-describedby="register-email-error"
                            @blur="() => validateEmail(true)"
                            @input="() => validateEmail(false)"
                        >

                        <div
                            id="register-email-error"
                            class="text-danger"
                            aria-live="polite"
                        >
                            {{ errors.email }}
                        </div>
                    </div>


                    
                    <div class="mb-3">
                        <label for="register-password" class="form-label">
                            Password
                        </label>

                        <input
                            id="register-password"
                            v-model="formData.password"
                            type="password"
                            class="form-control"
                            required
                            minlength="8"
                            autocomplete="new-password"
                            :aria-invalid="Boolean(errors.password)"
                            aria-describedby="register-password-error"
                            @blur="() => validatePassword(true)"
                            @input="() => validatePassword(false)"
                        >

                        <div
                            id="register-password-error"
                            class="text-danger"
                            aria-live="polite"
                        >
                            {{ errors.password }}
                        </div>
                    </div>

                    <div class="mb-3">
                        <label
                            for="confirm-password"
                            class="form-label"
                        >
                            Confirm password
                        </label>

                        <input
                            id="confirm-password"
                            v-model="formData.confirmPassword"
                            type="password"
                            class="form-control"
                            required
                            autocomplete="new-password"
                            :aria-invalid="Boolean(errors.confirmPassword)"
                            aria-describedby="confirm-password-error"
                            @blur="() => validateConfirmPassword(true)"
                            @input="() => validateConfirmPassword(false)"
                        >

                        <div
                            id="confirm-password-error"
                            class="text-danger"
                            aria-live="polite"
                        >
                            {{ errors.confirmPassword }}
                        </div>
                    </div>

                    <div class="d-grid gap-2 d-sm-flex">


                        <button
                            type="submit"
                            class="btn btn-primary"
                            :disabled="isRegistering"
                        >
                            {{ isRegistering ? 'Creating account…' : 'Register' }}
                        </button>

                        <button
                            type="button"
                            class="btn btn-secondary"
                            @click="clearForm"
                            :disabled="isRegistering"
                        >
                            Clear
                        </button>
                    </div>

                </form>
            </div>
        </div>
    </div>
</template>

<script setup>
    import { ref } from 'vue';
    import { createUserWithEmailAndPassword, signOut } from 'firebase/auth';
    import { useRouter } from 'vue-router';
    import { auth, db } from '../firebase/init.js';
    import { doc, setDoc } from 'firebase/firestore';

    const router = useRouter();

    const formData = ref({
        username: '',
        email: '',
        password: '',
        confirmPassword: '',
    });

    const errors = ref({
        username: '',
        email: '',
        password: '',
        confirmPassword: '',
    });

    // const successMessage = ref('');
    const registrationError = ref('');
    const isRegistering = ref(false);

    const registerUser = async () => {
        if (isRegistering.value) return;

        // successMessage.value = '';
        registrationError.value = '';

        validateUsername(true);
        validateEmail(true);
        validatePassword(true);
        validateConfirmPassword(true);

        if (
            errors.value.username ||
            errors.value.email ||
            errors.value.password ||
            errors.value.confirmPassword
        ) {
            return;
        }

        isRegistering.value = true;

        let accountCreated = false;

        try {
            const credential = await createUserWithEmailAndPassword(
                auth,
                formData.value.email.trim(),
                formData.value.password
            );

            accountCreated = true;

            await setDoc(doc(db, 'users', credential.user.uid), {
                username: formData.value.username.trim(),
                email: credential.user.email,
                role: 'viewer',
            });

            await signOut(auth);
            clearForm();
            router.push({ name: 'Login' });

        } catch (error) {

            if (accountCreated) {
                registrationError.value =
                    'Your account was created, but setup could not finish. Please do not register again.';
                console.error('Account setup failed:', error);
            } else if (error.code === 'auth/email-already-in-use') {
                registrationError.value = 'This email is already registered.';
            } else if (error.code === 'auth/weak-password') {
                registrationError.value = 'Your password does not meet the account requirements.';
            } else {
                registrationError.value = 'Registration failed. Please try again.';
            }
        } finally {
            isRegistering.value = false;
        }
    };

    const clearForm = () => {
        formData.value = {
            username: '',
            email: '',
            password: '',
            confirmPassword: '',
        };

        errors.value.username = '';
        errors.value.email = '';
        errors.value.password = '';
        errors.value.confirmPassword = '';
        // successMessage.value = '';
        registrationError.value = '';
    };

    const validateUsername = (blur) => {
        if (!formData.value.username.trim()) {
            if (blur) {
            errors.value.username = 'Username must not be empty.';
            }
        } else if (formData.value.username.trim().length < 3) {
            if (blur) {
            errors.value.username =
                'Username must contain at least 3 characters.';
            }
        } else {
            errors.value.username = '';
        }
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
        if (formData.value.password.length < 8) {
            if (blur) {
                errors.value.password = 'Password must contain at least 8 characters.';
            }
        } else {
            errors.value.password = '';
        }
    }

    const validateConfirmPassword = (blur) => {
        if (formData.value.confirmPassword !== formData.value.password) {
            if (blur) {
                errors.value.confirmPassword = 'The passwords do not match.';
            }
        } else {
            errors.value.confirmPassword = '';
        }
    }
</script>