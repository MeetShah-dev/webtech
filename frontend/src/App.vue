<template>
    <v-app class="grey lightn-4">
        <!-- <img alt="Surrey Horizon logo" class="logo" src="@/assets/s-h.png" /> -->
        <router-view></router-view>
        <Modal v-if="showModal" :message="message"/>
    </v-app>
</template>

<script>
import Modal from './components/Modal.vue';
import { EventBus } from './eventBus';
export default {
    name: 'App',
    components: { 
        Modal,
    },
    data() {
        return {
            message: '',
            showModal: false
        }
    },
    mounted() {
        console.log("App.vue mounted, setting up event listener.");
        EventBus.$on('show-modal', this.authMethod);
    },
    watch: {
        $route: {
            immediate: true,
            handler(to) {
                document.title = to.meta.title || 'Surrey Horizon';
            },
        },
    },
    methods: {
        authMethod(message) {
            this.showModal = false; 
            this.$nextTick(() => {
            this.showModal = true; 
            this.message = message; 
            this.$store.dispatch('incrementNotificationCount');
           });
        },
    }
};
</script>
<style scoped>
.logo {
    display: block;
    margin: auto;
    justify-content: center;
    height: 120px;
    width: auto;
}
</style>
