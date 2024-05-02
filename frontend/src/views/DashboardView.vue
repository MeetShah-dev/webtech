<script>
// import FeedbackApp from '../components/FeedbackApp.vue';
export default {
    components: {
        SideBar: () => import('@/components/SideBar.vue'),
    },
};
</script>

<template>
    <main class="editing">
        <side-bar></side-bar>
        <div class="main-container"></div>
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
