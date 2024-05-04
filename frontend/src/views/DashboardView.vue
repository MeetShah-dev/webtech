<script>
export default {
    components: {
        NavBar: () => import('@/components/NavBar.vue'),
        SideBar: () => import('@/components/SideBar.vue'),
    },
};
</script>

<template>
    <div class="main">
        <nav-bar></nav-bar>
        <h1>Dashboard</h1>
        <main class="editing">
            <side-bar></side-bar>
            <!-- <div class="main-container"></div> -->
        </main>
    </div>
</template>

<style scoped>
.main {
    margin-left: 350px;
    width: 1500px;
}

.editing {
    margin-right: 0px;
    padding: 10px;
    display: flex;
    height: 800px;
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
