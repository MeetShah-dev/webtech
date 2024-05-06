<template>
    <div>
         <main class="home" v-if="!overlay">
        <nav-bar></nav-bar>
        <div class="main">
            <div class="main-container">
                <h2>
                    <div class="center">
                        {{ magazineTitle }}
                    </div>
                </h2>
                <div v-for="blog in MagazineData.results" :key="blog.id">
                    <div class="blog">
                        <div class="blog-container">
                            <quillEditor id="ql-editor" v-model.lazy="blog.content" ref="myQuillEditor" :options="{ modules: { toolbar: [] }, debug: false, }"/>
                            <div class="blog-info">
                                <small class="like-info" style="margin-right: 20px;">
                                    <v-icon>mdi-thumb-up-outline</v-icon>
                                    <b>{{blog.likes}}</b>  
                                </small>
                                <small class="comment-info" style="margin-right: 20px;">
                                    <v-icon>mdi-comment-outline</v-icon>
                                    <b>{{blog.comments}}</b>
                                </small>
                                <small class="comment-info">
                                    <v-icon>mdi-book-open-page-variant</v-icon>
                                    <b>{{blog.readers}}</b>
                                </small>
                            </div>
                        </div>
                    </div>
                    <div class="center">
                        <div class="main-container-btn">
                            <v-row>
                                <v-btn flat dark color="#114C6E" style="margin-right: 20px;" @click="handleLike(blog.id)">
                                    <v-icon>mdi-thumb-up-outline</v-icon> 
                                    LIKE
                                </v-btn>
                                <v-btn flat dark color="#114C6E" tag="button" style="margin-right: 20px;" @click="handleComment(blog.id)"> <!--@click="readLatestMagazine"-->
                                    <v-icon>mdi-comment-outline</v-icon>
                                    COMMENT
                                </v-btn>
                                <v-btn flat dark color="#114C6E" tag="button" @click="readBlog(blog.id)">
                                    <v-icon>mdi-book-open-page-variant</v-icon>
                                    READ
                                </v-btn>
                            </v-row>
                        </div>
                    </div>
                </div>
                <div class="pagination">
                    <button @click="prevPage" :disabled="currentPage === 1">Prev</button>
                    <button>{{ currentPage }}</button>
                    <button @click="nextPage" :disabled="currentPage === totalPages">Next</button>
                </div>
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
    data() {
        return {
            MagazineData: null,
            // blogs: [
            //     { id:likeClicked: false },
            //     { id: 2, likeClicked: false },
            //     { id: 3, title: 'Blog 3', likeClicked: false }
            // ], // like tracker
            likes: '', // all likes
            blogId: '',
            magazineTitle: '',
            // pagination
            nextPageLink: '',
            prevPageLink: '', 
            currentPage: '',
            itemsPerPage: 10,
            totalPages: '',
            overlay: true
        };
    },
    async created() {
        const queryData = this.$route.query.data;
        if (queryData) {
            this.MagazineData = JSON.parse(queryData);
            const magazineId = this.MagazineData.results[0].magazine
            this.magazineTitle = await this.getMagazineTitle(magazineId);
            this.nextPageLink = this.MagazineData.next;
            this.prevPageLink = this.MagazineData.previous;
            this.currentPage = this.MagazineData?.currentPage ?? 1;
            this.totalPages = Math.ceil(this.MagazineData.count / this.itemsPerPage);
            try {
                for (let i = 0; i < this.MagazineData.results.length; i++) {
                    this.MagazineData.results[i].content = await this.formatBlog(this.MagazineData.results[i]);
                }
            } catch (error) {
                console.error('Error formatting blog content:', error);
            }
        }
    },

    async mounted () {
        await this.getLikes();
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
        this.overlay = false
    },
    components: {
        NavBar: () => import('@/components/NavBar.vue'),
        FooterBar: () => import('@/components/FooterBar.vue'),
        quillEditor,
        Comment,
    },
    methods: {
        async handleLike(blogId) {
            try {
                const url = import.meta.env.VITE_AUTH_SERVER + '/scheduler/update-like-dislike';
                const response = await axios.post(url, {
                    'like_dislike': "true",
                    "blog_id": blogId,
                });
                let liked = false;
                for (var i = 0; i < this.likes.length; i++) {
                    if (userId === this.likes[i].user_id && blogId === this.likes[i].blog_id) { liked = true; }
                }
                if (!liked) {
                    const blogToUpdate = this.MagazineData.results.find(blog => blog.id === blogId);
                    // updating the likes count in the blog object
                    if (blogToUpdate) {
                        blogToUpdate.likes += 1;
                    }
                }
                return response.data;
            } catch (error) {
                console.error('Error:', error);
            }
        },

        async handleComment(blogId) {
            const userId = 8; // get user ID!!!!!!!!!
            this.blogId = blogId;
            this.$refs.Comment.showCommentModal = true;
            // setting new blog id and user id in the comment component to make an api call on comment upload
            this.$refs.Comment.blogId = blogId;
            this.$refs.Comment.userId = userId;
        },

        async incrementCommentCount() {
            const blogToUpdate = this.MagazineData.results.find(blog => blog.id === this.blogId);
            // updating the likes count in the blog object
            if (blogToUpdate) {
                blogToUpdate.comments += 1;
            }
        },
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
                return htmlContent;
            } catch (error) {
                console.error('Error:', error);
            }
        },
        async readBlog(blogId) {
            await this.addReader(blogId);
            const data = await this.getBlog(blogId);
            this.$router.push({ name: 'blog', query: { data: JSON.stringify(data) } });
        },

        async getBlog(blogId) {
            try {
                const url = import.meta.env.VITE_AUTH_SERVER + '/blog/read-blog'; 
                const response = await axios.get(url, {
                    params: { 'blog': blogId } 
                });
                return response.data;
            } catch (error) {
                console.error('Error:', error);
            }
        },

        async addReader(blogId) {
            const url = import.meta.env.VITE_AUTH_SERVER + '/blog/add-reader';
            const response = await axios.post(url, {
                "blog": blogId,
            });
            console.log(response.data);
        },

        async getMagazineTitle(magazineId) {
            try {
                const url = import.meta.env.VITE_ADMIN_SERVER + '/getMagazine'; 
                console.log('}}}}}', url)
                const response = await axios.get(url, {
                    params: {'magazine_id': magazineId}
                });
                console.log(response.data, 'QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ')
                return response.data.title;
            } catch (error) {
                console.error('RAYAN    Error:', error);
            }
        },

        async getLikes() {
            try {
                const url = import.meta.env.VITE_AUTH_SERVER + '/scheduler/get-all-user-likes'; // change for auth api
                const response = await axios.get(url);
                console.log("likes => ", response.data.data);
                this.likes = response.data.data;
                return response.data.data;
            } catch (error) {
                console.error('Error:', error);
            }
        },

        /////////////////////////////////////////////////////////// pagination
        async prevPage() {
            console.log('prev clicked')
            if (this.currentPage > 1) {
                this.currentPage--;
                await this.redirect(this.prevPageLink, this.currentPage); // Fetch data for previous page
            }
        },

        async nextPage() {
            console.log('next clicked')
            if (this.currentPage < this.totalPages) {
                this.currentPage++;
                await this.redirect(this.nextPageLink, this.currentPage); // Fetch data for next page
            }
        },

        async goToPage(page) {
            try {
                this.currentPage = page;
                const url = import.meta.env.VITE_BLOGGING_SERVER + '/blog/magazine-feed/?page=' + String(page); // change for auth api
                await this.redirect(url, this.currentPage);
                return response.data.data;
            } catch (error) {
                console.error('Error:', error);
            }
        },

        async redirect(pageLink, currentPage) {
            try {
                const response = await axios.get(pageLink);
                let magazineData;
                magazineData = response.data;
                magazineData.currentPage = currentPage;
                console.log("response =>>>>>>>>>", response.data)
                this.$router.push({ name: 'magazine view', query: { data: JSON.stringify(response.data) } });
                window.location.reload();
            } catch (e) {
                console.error('error', e)
            }
        },
    },
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

.main-container,
.blog {
    margin: 5px;
    padding: 10px;

    height: 80%;
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

#ql-editor {
    height: 100%;
    width: 100%;
    border-color: none;
}

.pagination {
    margin-top: 20px;
    padding: 40px;
    text-align: center;
}

.pagination button {
    margin: 0 5px;
    padding: 8px 12px;
    background-color: #114C6E;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
}

.pagination button:hover {
    background-color: #0b344c;
}

.pagination button:disabled {
    opacity: 0.5;
    cursor: not-allowed;
}

.pagination .active {
    background-color: #0b344c;
}
</style>