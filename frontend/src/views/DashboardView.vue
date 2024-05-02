<script>
// import FeedbackApp from '../components/FeedbackApp.vue';
import axios from 'axios';
export default {
    components: {
        SideBar: () => import('@/components/SideBar.vue'),
    },
    name: 'axios-category',
    mounted() {
        // Example headers
        const headers = {
            Accept: 'application/json',
            // Add any other headers you need here
        };

        // Example GET request with headers
        axios
            .get('http://localhost:8083/getAllCategories', { headers })
            .then((response) => {
                this.responseData = response.data;
                console.log(this.responseData); // Print the response data to the console
                console.log('CCCCC'); // Print the response data to the console
            })
            .catch((error) => {
                console.error('Error fetching data:', error);
            });
    },
    methods: {
        validate() {
            this.$refs.form.validate();
        },
        reset() {
            this.$refs.form.reset();
        },
        resetValidation() {
            this.$refs.form.resetValidation();
        },
    },
};
</script>

<template>
    <main class="editing">
        <side-bar></side-bar>
        <div class="main-container"></div>
        <div class="side-container"></div>
    </main>
</template>

<style scoped>
* {
    margin: 5px;
    padding: 10px;
}

.editing {
    margin-left: 350px;
    margin-right: 0px;
    /* margin: auto; */
    padding: 10px;
    display: flex;
    height: 800px;
    width: 90%;
    /* align-items: center; */
    justify-content: space-between;
}

.main-container {
    /* margin: 10px; */
    padding: 10px;
    height: max-content;
}

.main-container-btn {
    display: flex;
    justify-content: space-between;
}
.side-container {
    padding: 0;
    width: 30%;
    height: 100%;
    background-color: #c1e2f4;
}
</style>
