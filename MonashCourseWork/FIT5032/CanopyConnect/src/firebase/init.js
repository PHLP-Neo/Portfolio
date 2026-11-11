import { initializeApp } from 'firebase/app'
import { getFirestore } from 'firebase/firestore'
import { getAuth } from 'firebase/auth'
import { getFunctions } from 'firebase/functions';

const firebaseConfig = {
    apiKey: "AIzaSyDAT_M7oabkXbomyajXItLy0Ufz88nF8Xs",
    authDomain: "canopy-connect-16c1a.firebaseapp.com",
    projectId: "canopy-connect-16c1a",
    storageBucket: "canopy-connect-16c1a.firebasestorage.app",
    messagingSenderId: "738009309765",
    appId: "1:738009309765:web:817aa366281e9ba22cb92c"
  };

const firebaseApp = initializeApp(firebaseConfig)

export const auth = getAuth(firebaseApp)
export const db = getFirestore(firebaseApp)

export const functions = getFunctions(
  firebaseApp,
  'australia-southeast2'
);