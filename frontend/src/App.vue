<template>
    <v-app class="grey lightn-4">
        <!-- <img alt="Surrey Horizon logo" class="logo" src="@/assets/s-h.png" /> -->
        <router-view></router-view>
        <Modal v-if="showModal" :message="message"/>
    </v-app>
</template>

<script>
import Modal from './components/Modal.vue';

export default {
    name: 'App',
    components: { 
        Modal,
    },
    data() {
        return {
            message: 'hello world',
            showModal: false
        }
    },
    mounted() {
        this.$root.$on('show-modal', this.auth)
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
        auth(access_token, userId) {
            console.log('nik zebiiiiiiiiiiiiiiiiiiiiiiiiiii')
            this.showModal = true;
            console.log(access_token, userId)
            // console.log('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@FUNCTION CALLED@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@');

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
