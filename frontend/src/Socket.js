import Vue from "vue";
import Modal from './App.vue';
import { EventBus } from "./eventBus";
export default Vue.extend({
    components: {
        Modal,
    },
    methods: {
        authenticateWebSockets(access_token, userId) {
            console.log("websocket authentication test:")
        
            const notificationWebsocket = new WebSocket(
                'ws://' + 
                '35.171.3.193:8001' + 
                '/ws/notification/' + 
                `${userId}` +  
                `/?Authorization=${access_token}`
            ); 
            console.log(notificationWebsocket);
        
            const eventWebsocket = new WebSocket(
                'ws://' + 
                '35.171.3.193:8001' + 
                `/ws/event/?Authorization=${access_token}` 
            );
        
            notificationWebsocket.onmessage = (event) => {
                console.log("Received WebSocket message:", event.data);
                const data = JSON.parse(event.data);
                const notificationMessage = data.message;
                EventBus.$emit('show-modal', notificationMessage);
            };
        
            eventWebsocket.onmessage = (event) => {
                const data = JSON.parse(event.data);
                const eventMessage = data.message;
            };
        },
    }
});

