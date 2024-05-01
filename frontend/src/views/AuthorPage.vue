<script>
export default {};
</script>

<template>
    <div class="author-page">
        <div class="main-container"></div>
        <div class="side-container"></div>
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
