import { createApp } from 'vue'
import App from './App.vue'

import { Amplify } from 'aws-amplify';

Amplify.configure({
    Auth: {
        region: 'us-east-1',
        userPoolId: 'us-east-1_Xf2MACMDh',
        userPoolWebClientId: '3ejvl5qniefqloiggpr2n73t12',
    }
});

createApp(App).mount('#app')
