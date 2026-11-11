import 'bootstrap/dist/css/bootstrap.min.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index.js'

import PrimeVue from 'primevue/config';
import Aura from '@primevue/themes/aura';

import './assets/main.css'

const app = createApp(App)

app.use(PrimeVue, {
    theme: {
        preset: Aura,
        options: {
            darkModeSelector: '.canopy-dark',
        },
    },
});

app.use(router);

app.mount('#app')