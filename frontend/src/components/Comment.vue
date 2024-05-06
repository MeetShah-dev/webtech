<template>
    <v-dialog v-model="showCommentModal" max-width="500">
      <v-card>
        <v-card-title class="headline grey lighten-2">
          Add Comment
          <v-spacer></v-spacer>
          <v-btn icon @click="closeModal">
            <v-icon color="grey darken-1">mdi-close</v-icon>
          </v-btn>
        </v-card-title>
        <v-card-text>
          <v-textarea v-model="comment" label="Your Comment"></v-textarea>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" @click="postComment">Post</v-btn>
          <v-btn color="primary" @click="closeModal">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </template>
  
  <script>
  import axios from 'axios';

  export default {
        props: ['blogId'],
        data() {
            return {
                showCommentModal: false,
                comment: '',
                blogId: null
            };
        },
        methods: {
            async postComment() {
                this.$emit('post-comment', this.comment);
                this.showCommentModal = false; 
                await this.commentBlog(this.comment, this.blogId);
            },
            async closeModal() {
                this.showCommentModal = false;
            },
            async showModal() {
                this.showCommentModal = true;
            },
            async commentBlog(text, blogId) {
                try {
                    const url = import.meta.env.VITE_AUTH_SERVER + '/scheduler/add-comment'; 
                    const response = await axios.post(url, {
                        "text": text,
                        "blog_id": blogId,
                    });
                    return response.data;
                } catch (error) {
                    console.error('Error:', error);
                }
            },

            async test(text) {
                console.log(text)
            }
        }
  };
  </script>  