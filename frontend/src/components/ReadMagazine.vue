<script>
import axios from 'axios';
export default {
    data() {
        return {
            links: [
                { text: 'Article Title One', route: '' },
                { text: 'Article Title Two', route: '' },
                { text: 'Article Title Three', route: '' },
                { text: 'Article Title Four', route: '' },
                { text: 'Article Title Five', route: '' },
                { text: 'Article Title Six', route: '' },
            ],
            selectedTab: null,
            comment: '',
            latestMagazine: '',
        };
    },
    async mounted() {
        await this.getBlogs();
    },
    methods: {
        handleLike() {
            alert('Liked!');
        },
        loadArticle(index) {
            // Set the selected tab to trigger the route change and load corresponding article
            this.selectedTab = index;
        },
        postComment() {
            if (this.comment.trim() !== '') {
                console.log('Posting comment:', this.comment);
                this.comment = ''; // Clear the comment input after posting
            }
        },
        async getBlogs() {
            try {
                const url = 'http://54.82.93.84:8000/api/magazine-feed';
                const response = await axios.get(url);
                this.latestMagazine = response.data; // Populate categories array
                console.log('KJBVKSHBFVHBK', response.data);
                return response.data;
            } catch (error) {
                console.error('Error fetching categories:', error);
            }
        },
    },
};
</script>

<template>
    <div class="main">
        <div class="side-container">
            <v-card flat>
                <v-tabs vertical v-model="selectedTab">
                    <v-tab
                        v-for="(link, index) in links"
                        :key="index"
                        @click="loadArticle(index)"
                    >
                        {{ link.text }}
                    </v-tab>
                </v-tabs>
            </v-card>
        </div>

        <div class="content-container">
            <div class="article-view">
                <br />
                <br />
                <br />
                <br />
                <!-- <router-view></router-view> -->
            </div>
            <div class="bottom-container">
                <div class="like-section">
                    <v-btn @click="handleLike"
                        ><v-icon>mdi-thumb-up-outline</v-icon></v-btn
                    >
                </div>

                <div class="comment-section">
                    <h3>Comment</h3>
                    <textarea
                        v-model="comment"
                        placeholder="Enter your comment"
                    ></textarea>
                    <v-btn @click="postComment">Post Comment</v-btn>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.main {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
}

.side-container {
    width: 300px;
}

.content-container {
    margin-top: 20px;
    width: 900px;
    background-color: aquamarine;
}

.bottom-container {
    border: 1px solid black;
    border-radius: 7px;
    background-color: white;
    padding: 10px;
    margin: auto;
    width: 750px;
    align-items: center;
    justify-content: center;
}

.like-section,
.comment-section {
    margin-top: 20px;
}

textarea {
    width: 100%;
    height: 100px;
    margin-bottom: 10px;
}
</style>
