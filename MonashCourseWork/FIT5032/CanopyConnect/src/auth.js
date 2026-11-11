import { ref } from 'vue'
import { onAuthStateChanged } from 'firebase/auth';
import { auth, db } from './firebase/init.js';
import { doc, getDoc } from 'firebase/firestore';

export const currentUser = ref(null)

export const isAuthenticated = ref(false)

export const loadUserProfile = (uid) => {
    return getDoc(doc(db, 'users', uid))
        .then((snapshot) => {
            if (!snapshot.exists()) {
                throw new Error('User profile not found.');
            }

            return {
                id: uid,
                username: snapshot.data().username,
                email: snapshot.data().email,
                role: snapshot.data().role,
            };
        });
};

export const authReady = new Promise((resolve, reject) => {
    onAuthStateChanged(
        auth,
        (user) => {
            if (!user) {
                currentUser.value = null;
                isAuthenticated.value = false;
                resolve();
                return;
            }

            loadUserProfile(user.uid)
                .then((profile) => {
                    if (auth.currentUser) {
                        if (auth.currentUser.uid === user.uid) {
                            currentUser.value = profile;
                            isAuthenticated.value = true;
                        }
                    }

                    resolve();
                })
                .catch((error) => {
                    if (auth.currentUser) {
                        if (auth.currentUser.uid === user.uid) {
                            currentUser.value = null;
                            isAuthenticated.value = false;
                        }
                    }

                    console.error('Profile restoration failed:', error);
                    resolve();
                });
        },
        reject
    );
});