import { initializeApp } from "firebase/app";
import { getAuth, GoogleAuthProvider } from "firebase/auth";
import { getFirestore } from "firebase/firestore";
import { getAnalytics, isSupported } from "firebase/analytics";

const firebaseConfig = {
  apiKey: import.meta.env.VITE_FIREBASE_API_KEY,
  authDomain: import.meta.env.VITE_FIREBASE_AUTH_DOMAIN,
  projectId: import.meta.env.VITE_FIREBASE_PROJECT_ID,
  storageBucket: import.meta.env.VITE_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: import.meta.env.VITE_FIREBASE_MESSAGING_SENDER_ID,
  appId: import.meta.env.VITE_FIREBASE_APP_ID,
  measurementId: import.meta.env.VITE_FIREBASE_MEASUREMENT_ID
};

// Only initialize Firebase if we have a valid config
const hasValidConfig = firebaseConfig.apiKey && firebaseConfig.projectId;

let app = null;
let auth = null;
let db = null;
let analytics = null;
let googleProvider = null;

if (hasValidConfig) {
  try {
    app = initializeApp(firebaseConfig);
    auth = getAuth(app);
    db = getFirestore(app);
    googleProvider = new GoogleAuthProvider();
    
    // Analytics requires browser support check
    isSupported().then((supported) => {
      if (supported) {
        analytics = getAnalytics(app);
      }
    }).catch(() => {});
  } catch (e) {
    console.warn('Firebase initialization failed:', e.message);
  }
} else {
  console.warn('Firebase config not found. Running without Firebase services.');
}

// Safe analytics logger that works even when analytics is null
export const safeLogEvent = (eventName, params) => {
  if (analytics) {
    import('firebase/analytics').then(({ logEvent }) => {
      logEvent(analytics, eventName, params);
    });
  }
};

export { auth, db, analytics, googleProvider };
export default app;
