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
        <h1>List of Articles to Check</h1>
        <div class="main">
            <div class="article-list">
                <br />
                <br />
                <br />
                <br />
                <br />
            </div>
            <div class="add-feedback">
                <v-container>
                    <v-form ref="form" v-model="valid" lazy-validation>
                        <v-textarea
                            width="350px"
                            label="Feedback comment"
                            v-model="feedback_comment"
                        ></v-textarea>
                        <v-row align="center" justify="space-between">
                            <v-btn class="primary" depressed>submit</v-btn>
                        </v-row>
                        <v-row align="center" justify="space-between">
                            <v-btn class="success" depressed>accept</v-btn>
                            <v-btn class="error" depressed>reject</v-btn>
                        </v-row>
                    </v-form>
                </v-container>
            </div>
        </div>
    </main>
</template>

<style scoped>
* {
    margin: 5px;
    padding: 10px;
}

main {
    width: 900px;
}

/* .main {
    width: 100%;
    height: 600px;
    display: flex;
    justify-content: space-around;
} */

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
