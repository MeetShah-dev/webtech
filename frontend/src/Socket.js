import Vue from "vue";
import Modal from './App.vue';

export default Vue.extend({
    components: {
        Modal,
    },
    methods: {
        auth(access_token, userId) {
            console.log(access_token, userId)
            console.log('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@FUNCTION CALLED@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@');
            this.$root.$emit('show-modal', 'notificationMessage');
        },
        authenticateWebSockets(access_token, userId) {
            console.log("websocket authentication test:")
        
            notificationWebsocket = new WebSocket(
                'ws://' + 
                '35.171.3.193:8001' + 
                // import.meta.env.VITE_NOTIFICATION_SERVER +
                '/ws/notification/' + 
                `${userId}` +  
                `/?Authorization=${access_token}`
            ); 
            console.log(notificationWebsocket);
        
            eventWebsocket = new WebSocket(
                'ws://' + 
                '35.171.3.193:8001' + 
                // import.meta.env.VITE_NOTIFICATION_SERVER +
                `/ws/event/?Authorization=${access_token}` 
            );
        
            notificationWebsocket.onmessage = (event) => {
                console.log("Received WebSocket message:", event.data);
                const data = JSON.parse(event.data);
                const notificationMessage = data.message;
                this.$root.$emit('show-modal', notificationMessage);
            };
        
            eventWebsocket.onmessage = (event) => {
                const data = JSON.parse(event.data);
                const eventMessage = data.message;
            };
        },
    }
});

