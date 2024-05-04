<script>
export default {
    name: 'Home-view',
    data: () => {
        return {};
    },
    components: {
        NavBar: () => import('@/components/NavBar.vue'),
        FooterBar: () => import('@/components/FooterBar.vue'),
    },
};
</script>

<template>
    <main class="home">
        <nav-bar></nav-bar>
        <h1>Homepage</h1>
        <div class="main">
            <div class="side-container">
                <h2>Magazine Archives</h2>
            </div>
            <div class="main-container">
                <h2>Latest Issue</h2>
                <div class="cover-image">
                    <!-- <img src="@/assets/Capture.png" alt="Magazine Cover" /> -->
                </div>
                <div class="main-container-btn">
                    <!--linking to catalogue page-->
                    <v-row align="center" justify="space-between">
                        <v-btn flat dark color="#114C6E"
                            >View more issues >></v-btn
                        >
                        <v-btn
                            flat
                            dark
                            color="#114C6E"
                            to="/read-magazine"
                            tag="button"
                            >Read Magazine</v-btn
                        ></v-row
                    >
                </div>
            </div>
            <div class="side-container">
                <h2>Empty placeholder (To be deleted)</h2>
            </div>
        </div>
        <footer-bar></footer-bar>
    </main>
</template>

<style scoped>
* {
    margin: 5px;
    padding: 10px;
}
.main {
    width: 100%;
    height: 1000px;
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
