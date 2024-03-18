import { createApp } from 'vue'
import App from './App.vue'

import { Amplify } from 'aws-amplify';

Amplify.configure({
    Auth: {
        region: 'REPLACE_ME',
        userPoolId: 'REPLACE_ME',
        userPoolWebClientId: 'REPLACE_ME',
    }
});

createApp(App).mount('#app')
