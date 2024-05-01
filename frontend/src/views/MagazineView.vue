<template>
    <div class="main-container">
        <div class="side-container">
            <v-list>
                <v-list-tile v-for="link in links" :key="link.text">
                    <router-link :to="link.route" tag="div">
                        <v-list-tile-content>
                            <v-list-tile-title>{{
                                link.text
                            }}</v-list-tile-title>
                        </v-list-tile-content>
                    </router-link>
                </v-list-tile>
            </v-list>
        </div>
        <div class="content-container">
            <div class="article-view">
                <router-view></router-view>
            </div>
            <div class="like-section">
                <h3>Like Section</h3>
                <v-btn @click="handleLike">Like</v-btn>
            </div>

            <!-- Comment Section -->
            <div class="comment-section">
                <h3>Comment Section</h3>
                <!-- Your comment component can go here -->
                <textarea
                    v-model="comment"
                    placeholder="Enter your comment"
                ></textarea>
                <v-btn @click="postComment">Post Comment</v-btn>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            links: [
                { text: 'Article Title One', route: '/article/1' },
                { text: 'Article Title Two', route: '/article/2' },
                { text: 'Article Title Three', route: '/article/3' },
                { text: 'Article Title Four', route: '/article/4' },
                { text: 'Article Title Five', route: '/article/5' },
                { text: 'Article Title Six', route: '/article/6' },
            ],
            comment: '', // Store user's comment
        };
    },
    methods: {
        handleLike() {
            alert('Liked!');
        },
        postComment() {
            if (this.comment.trim() !== '') {
                console.log('Posting comment:', this.comment);
                this.comment = '';
            }
        },
    },
};
</script>

<style scoped>
.main-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 1000px;
}

.side-container {
    height: 1000px;
    width: 20%;
    padding: 10px;
    background-color: #c1e2f4;
}

.content-container {
    height: 1000px;
    width: 70%;
    padding: 10px;
    background-color: #114c6e;
    color: #fff;
}

.like-section,
.comment-section {
    margin-top: 20px;
    padding: 10px;
    border-top: 1px solid #fff;
}

textarea {
    width: 100%;
    height: 100px;
    margin-bottom: 10px;
}
</style>
