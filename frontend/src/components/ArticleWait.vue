<script>
import axios from 'axios';
import { quillEditor } from 'vue-quill-editor';
import 'quill/dist/quill.snow.css';
export default {
    name: 'axios-articlewaiting',
    data() {
        return {
            articleItems: null,
            selectedArticle: {
                id: '',
            },
            selectedArticleTitle: '',
            data: '',
            response: '',
            feedback_comment: ' ', // Data binding for feedback comment
            // Data binding for the new category input
            latestBlog: '',
            selectedBlog: '',
            feedbackSubmitted: false,
            blog: {
                content: '',
                editorOption: {
                    debug: 'info',
                    readOnly: true,
                    theme: 'snow',
                    modules: {
                        toolbar: [],
                    },
                },
            },
        };
    },
    components: {
        quillEditor,
    },
    async mounted() {
        await this.fetchArticles(); // Call the method to fetch categories
    },
    methods: {
        async fetchArticles() {
            try {
                const response = await axios.get(
                    'http://18.206.186.97:8000/getReadyPosts'
                );
                this.articleItems = response.data; // Populate categories array
            } catch (error) {
                console.error('Error fetching categories:', error);
            }
        },
        async submitFeedback() {
            try {
                const feedbackData = {
                    blog: this.selectedArticle.id,
                    content: this.feedback_comment,
                };
                this.feedbackSubmitted = true;
                // Post feedback to the /postfeedback API
                await axios.post(
                    'http://18.206.186.97:8000/postFeedback',
                    feedbackData
                );

                // Reset selected article and feedback comment after successful submission

                // You may want to add additional logic here, like displaying a success message
            } catch (error) {
                console.error('Error submitting feedback:', error);
                // You can handle errors here, e.g., displaying an error message
            }
        },
        async approveSelectedArticle() {
            try {
                await axios.put('http://18.206.186.97:8000/approvePost', {
                    id: this.selectedArticle.id,
                });
                alert(`Post ID ${this.selectedArticle.id} is approved.`);
            } catch (error) {
                console.error('Error approving article:', error);
            }
        },

        async rejectSelectedArticle() {
            try {
                await axios.put('http://18.206.186.97:8000/rejectPost', {
                    id: this.selectedArticle.id,
                });
                alert(`Post ID ${this.selectedArticle.id} is rejected.`);
            } catch (error) {
                console.error('Error approving article:', error);
            }
        },

        async selectArticle(article) {
            // Set the selected article
            this.selectedArticle = article;
            // let data = JSON.stringify({
            //     blog: 78
            // });
            // let data = {"blog": this.selectedArticle.id}
            //alert("MERHABALAR" + this.selectedArticle.id)
            //console.log(data)

            const response = await axios.get(
                'http://54.82.93.84:8000/api/read-blog-moderation/',
                { params: { blog: this.selectedArticle.id } }
            );
            //alert("MERHABALAR" + response.data.content)

            this.selectedBlog = response.data;

            //this.latestBlog = selectedArticle
            //alert("ddskflkgfldkgflskgled" + this.selectedBlog.files)

            const files = this.selectedBlog.files;

            let htmlContent =
                `<h1>${this.selectedBlog.title}</h1><br>` +
                this.selectedBlog.content;
            //alert("FILE: " + files)
            if (files.length > 0) {
                for (var i = 0; i < files.length; i++) {
                    const uidRegExp = new RegExp(
                        files[i].uid.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'),
                        'g'
                    );
                    const imgTag = `<img src="${files[i].url}" alt="Image">`;
                    htmlContent = htmlContent.replace(uidRegExp, imgTag + ' ');
                    //console.log("HTTTTTTTTT" + htmlContent)
                }
            }
            this.blog.content = htmlContent;

            //alert("xxxxx" + this.blog.content)

            // this.selectedArticleTitle = response.data.title;
        },
    },
};
</script>

<template>
    <main class="home">
        <h1>List of Articles to Check</h1>
        <div class="main">
            <div class="article-list">
                <v-list-item
                    class="pt-0 pb-0 mt-0 mb-0"
                    v-for="article in articleItems"
                    :key="article.id"
                    @click="selectArticle(article)"
                >
                    <v-list-item-content dense
                        >{{ article.id }} .th Article:
                        {{ article.title }}</v-list-item-content
                    >
                </v-list-item>
            </div>

            <div class="add-feedback">
                <v-container>
                    <div v-if="selectedArticle.id">
                        <p
                            :style="{
                                'font-weight': 'bold',
                                'font-style': 'italic',
                                color: 'red',
                            }"
                        >
                            You have selected {{ selectedArticle.id }}th Article
                            "{{ selectedArticle.title }}" to give FEEDBACK.
                        </p>
                    </div>
                    <div class="cover-image">
                        <quillEditor
                            class="pt-0 pb-0 mt-0 mb-0"
                            id="ql-editor"
                            placeholder="Content"
                            v-model.lazy="blog.content"
                            ref="myQuillEditor"
                            :options="blog.editorOption"
                        />
                    </div>
                </v-container>
            </div>
        </div>
        <h1>Feedback</h1>
        <v-form ref="form">
            <v-form ref="form">
                <v-textarea
                    width="350px"
                    label="Feedback comment"
                    v-model="feedback_comment"
                ></v-textarea>
                <v-btn class="primary" depressed @click="submitFeedback"
                    >Submit</v-btn
                >
            </v-form>
            <v-row justify="space-between">
                <v-btn
                    class="success"
                    depressed
                    :disabled="!feedbackSubmitted"
                    @click="approveSelectedArticle"
                    >accept</v-btn
                >
                <v-btn
                    class="error"
                    depressed
                    :disabled="!feedbackSubmitted"
                    @click="rejectSelectedArticle"
                    >reject</v-btn
                >
            </v-row>
        </v-form>
    </main>
</template>

<style scoped>
* {
    margin: 5px;
    padding: 10px;
}

.article-list {
    width: 700px;
}

.add-feedback {
    width: 700px;
    margin: 0;
    padding: 0;
    top: 0;
}
.main {
    margin: 0;
    padding: 0;
    width: 100%;
    display: flex;
    justify-content: space-around;
}

.add-feedback .cover-image {
    margin: 5px;
    padding: 10px;
}

#ql-editor {
    height: 600px;
}
</style>
