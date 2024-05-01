<script>
export default {
    name: 'ArticleApproved',
    data: () => {
        return {};
    },
};
</script>

<template>
    <main class="home">
        <h1>List of All Articles</h1>
        <div class="main"></div>
    </main>
</template>

<style scoped>
* {
    margin: 5px;
    padding: 10px;
}
.main {
    width: 100%;
    height: 600px;
    display: flex;
    justify-content: space-around;
}

.main-container {
    width: 50%;
    height: 70%;
    background-color: #ffffff;
    border-radius: 10px;
}

.main-container h2 {
    border-top: solid 1px black;
    border-bottom: solid 1px black;
}

.main-container,
.cover-image {
    height: 80%;
}

.cover-image img {
    display: block;
    margin: auto;
    justify-content: center;
    height: 600px;
    width: auto;
    background-color: black;
}

.main-container-btn {
    display: flex;
    justify-content: space-between;
}
.side-container {
    border-radius: 10px;
    width: 20%;
    height: 70%;
    background-color: #c1e2f4;
}
</style>
