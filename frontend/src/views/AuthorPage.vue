<script>
import AuthorList from '../components/AuthorList.vue';
export default {
    data() {
        return {
            links: [
                { text: 'Author 1', route: '' },
                { text: 'Author 1', route: '' },
                { text: 'Author 1', route: '' },
                { text: 'Author 1', route: '' },
                { text: 'Author 1', route: '' },
                { text: 'Author 1', route: '' },
            ],
            selectedTab: null,
        };
    },
    components: {
        NavBar: () => import('@/components/NavBar.vue'),
        AuthorList,
    },
};
</script>

<template>
    <div class="main">
        <nav-bar></nav-bar>
        <author-list></author-list>
    </div>
</template>

<style scoped>
* {
    margin: 5px;
    padding: 10px;
}

.author-page {
    margin: auto;
    padding: 10px;
    display: flex;
    height: 800px;
    width: 100%;
}

.main-container {
    width: 80%;
    height: max-content;
    background-color: #114c6e;
}

.main-container-btn {
    display: flex;
    justify-content: space-between;
}
.side-container {
    padding: 0;
    width: 20%;
    background-color: #c1e2f4;
}
</style>
