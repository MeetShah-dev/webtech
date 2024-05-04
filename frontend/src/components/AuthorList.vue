<script>
export default {
    name: 'AuthorList',
    data: () => {
        return {};
    },
};
</script>

<template>
    <main class="author-display">
        <h1>List of Authors</h1>
        <div class="main">
            <div class="side-container">
                <ul class="author-list">
                    <li
                        v-for="(link, index) in links"
                        :key="index"
                        @click="loadArticle(index)"
                    >
                        {{ link.text }}
                    </li>
                </ul>
            </div>

            <div class="content-container">
                <div class="article-view">
                    <br />
                    <br />
                    <br />
                    <br />
                </div>
            </div>
        </div>
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
