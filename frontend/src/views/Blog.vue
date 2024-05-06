<template>
    <div>
        <main class="home" v-if="!overlay">
        <nav-bar></nav-bar>
        <div class="main">
            <div class="main-container">
                <div class="blog">
                    <div class="blog-container">
                        <quillEditor id="ql-editor" v-model.lazy="blogData.content" ref="myQuillEditor" :options="{ modules: { toolbar: [] }, debug: false, }"/>
                        <div class="blog-info">
                            <small class="like-info" style="margin-right: 20px;">
                                <v-icon>mdi-thumb-up-outline</v-icon>
                                <b>{{blogData.likes}}</b>  
                            </small>
                            <small class="comment-info" style="margin-right: 20px;">
                                <v-icon>mdi-comment-outline</v-icon>
                                <b>{{blogData.comments}}</b>
                            </small>
                            <small class="comment-info">
                                <v-icon>mdi-book-open-page-variant</v-icon>
                                <b>{{blogData.readers}}</b>
                            </small>
                        </div>
                    </div>
                </div>
                <div class="center">
                    <div class="main-container-btn">
                        <v-row>
                            <v-btn flat dark color="#114C6E" style="margin-right: 20px;" @click="handleLike(blogData.id)" 
                            :style="{ 'pointer-events': likeClicked ? 'none' : 'auto' }">
                                <v-icon>mdi-thumb-up-outline</v-icon> 
                                LIKE
                            </v-btn>
                            <v-btn flat dark color="#114C6E" tag="button" style="margin-right: 20px;" @click="handleComment(blogData.id)"> <!--@click="readLatestMagazine"-->
                                <v-icon>mdi-comment-outline</v-icon>
                                COMMENT
                            </v-btn>
                        </v-row>
                    </div>
                    
                </div>
                <div class="comments-section">
                    <h3>Comments</h3>
                    <div v-if="blogComments.length === 0">No comments yet.</div>
                    <div v-else>
                        <div v-for="(comment, index) in blogComments" :key="index" class="comment-item">
                            <div class="comment-header">{{ comment.date_time }}</div>
                            <div class="comment-body">{{ comment.text }}</div>
                        </div>
                    </div>
                </div>
                <br>
            </div>
        </div>
        <div class="comment-modal">
            <Comment ref="Comment" @post-comment="incrementCommentCount"/>
        </div>
    </main>
    <v-overlay :opacity="1" :value="overlay" v-if="overlay">
      <v-progress-circular indeterminate size="64">
        Loading...
      </v-progress-circular>
    </v-overlay>
    </div>
   
</template>
<script>
import axios from 'axios'; 
import 'quill/dist/quill.snow.css';
import { quillEditor } from 'vue-quill-editor';
import Comment from '@/components/Comment.vue';

export default {
    data: () => {
        return {
            magazines: [],
            LatestMagazineBlogs: [],
            archivedMagazineData: [],
            blogData: null,
            blogComments: null,
            likes: null,
            likeClicked: false,
            blog: {
                content: '',
                editorOption: {
                    debug: 'info',
                    readOnly: true,
                    theme: 'snow',
                    modules: {
                        toolbar: [] 
                    }
                },
            },
            overlay: true
        };
    },
    async created() {
        const queryData = this.$route.query.data;
        if (queryData) {
            this.blogData = JSON.parse(queryData);
            console.log(this.blogData)
            console.log(this.blogData.comments)
            try {
                this.blogData.content = await this.formatBlog(this.blogData);
                console.log(this.blogData)
            } catch (error) {
                console.error('Error formatting blog content:', error);
            }
        }
    },
    components: {
        NavBar: () => import('@/components/NavBar.vue'),
        FooterBar: () => import('@/components/FooterBar.vue'),
        quillEditor,
        Comment,
    },
    async mounted() {
        await this.getComments(); 
        await this.getLikes();
        this.overlay = false;
    },
    methods: {
        async formatBlog(blog) {
            try {
                const files = blog.files;
                let htmlContent = `<h1>${blog.title}</h1><br>` + blog.content; 
                if (files.length > 0) {
                    for (var i = 0; i < files.length; i++) {
                        const uidRegExp = new RegExp(files[i].uid.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'g');
                        const imgTag = `<img src="${files[i].url}" alt="Image">`;
                        htmlContent = htmlContent.replace(uidRegExp, imgTag + ' ');
                    }
                }
                console.log(htmlContent)
                return htmlContent;
            } catch (error) {
                console.error('Error:', error);
            }
        },

        async getComments() {
            try {
                const url = import.meta.env.VITE_AUTH_SERVER + '/scheduler/get-all-comments';
                console.log('URLLLLL', url)
                const response = await axios.get(url);
                const comments = await this.getBlogComments(this.blogData.id, response.data.data);
                this.blogComments = comments;
                return response.data.data;
            } catch (error) {
                console.error('Error:', error);
            }
        },

        async getBlogComments(blogId, comments) {
            try {
                for (var i = 0; i < comments.length; i++) {
                    if (!(blogId === comments[i].blog_id)) { 
                        comments.splice(i, 1);
                        i--;
                    }
                }
                return comments;
            } catch (e) {
                console.error('Error:', e)
            }
        },


        async handleLike(blogId) {
            this.likeClicked = true;
            try {
                const url = import.meta.env.VITE_AUTH_SERVER + '/scheduler/update_like_dislike';
                const response = await axios.post(url, {
                    'like_dislike': "true",
                    "blog_id": blogId,
                });
                let liked = false;
                for (var i = 0; i < this.likes.length; i++) {
                    if (userId === this.likes[i].user_id && blogId === this.likes[i].blog_id) { liked = true; }
                }
                if (!liked) {
                    this.blogData.likes += 1;
                }
                return response.data;
            } catch (error) {
                console.error('Error:', error);
            }
        },

        async handleComment(blogId) {
            const parsedUser = JSON.parse(decodeURIComponent(sessionStorage.getItem('user')));
            this.blogId = blogId;
            this.$refs.Comment.showCommentModal = true;
            this.$refs.Comment.blogId = blogId;
            this.$refs.Comment.userId = parsedUser.id;
        },

        async incrementCommentCount() {
            this.blogData.comments += 1;
        },

        async getLikes() {
            try {
                const url = import.meta.env.VITE_AUTH_SERVER + '/scheduler/get-all-user-likes'; 
                const response = await axios.get(url);
                this.likes = response.data.data;
                return response.data.data;
            } catch (error) {
                console.error('Error:', error);
            }
        },
    }
};
</script>
<style scoped>
.main {
    margin: 5px;
    padding: 10px;

    width: 100%;
    height: 1000px;
    display: flex;
    justify-content: space-around;
}

.main-container {
    margin: 5px;
    padding: 10px;

    width: 70%;
    height: 70%;
    background-color: #ffffff;
    border-radius: 10px;
}

.main-container h2 {
    margin: 5px;
    padding: 10px;

    border-top: solid 1px black;
    border-bottom: solid 1px black;
}

.main-container { 
    margin: 5px;
    padding: 10px;

    height: 100%;
} 

.container {
    display: flex;
    flex-direction: row;
}
.blog {
    margin: 5px;
    padding: 10px;
    flex: 1; 
}
#ql-editor {
    height: 100%; 
    width: 100%; 
    border-color: none;
}

.center {
    display: flex;
    justify-content: center;
    align-items: center;
}

.blog img {
    margin: 5px;
    padding: 10px;

    display: block;
    margin: auto;
    justify-content: center;
    height: 600px;
    width: auto;
    background-color: black;
}

.main-container-btn {
    margin: 20px;
    margin-bottom: 50px;
    padding: 10px;

    display: flex;
    justify-content: space-between;
}

.blog-container {
    padding: 20px;
    border: none;
    background-color: rgb(245, 239, 239);
}

.blog-info {
    padding: 20px;
}

.comment-info, .like-info {
    cursor: pointer;
}

.comment-info:hover .v-icon,
.comment-info:hover .b,
.like-info:hover .v-icon,
.like-info:hover .b {
    cursor: pointer;
    color: rgb(93, 93, 216);
    transition: color 0.3s;
}


.comments-section {
  margin-top: 20px;
}

.comment-item {
  margin-bottom: 15px;
  border: 1px solid #ccc;
  padding: 10px;
  border-radius: 5px;
}

.comment-header {
  font-weight: bold;
}

.comment-body {
  margin-top: 5px;
}
</style>