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
                blogId: null,
                userId: null,
            };
        },
        methods: {
            async postComment() {
                this.$emit('post-comment', this.comment);
                this.showCommentModal = false; 
                await this.commentBlog(this.comment, this.blogId, this.userId);
                console.log("comment posted", this.userId, this.comment, this.blogId)
            },
            async closeModal() {
                this.showCommentModal = false;
            },
            async showModal() {
                this.showCommentModal = true;
            },
            async commentBlog(text, blogId, userId) {
                try {
                    console.log("calling api")
                    const url = import.meta.env.VITE_INTERACTION_SERVER + '/add_comment'; // change for auth api
                    console.log("text: ", text, "blog id: ", blogId, "user id: ", userId)
                    const response = await axios.post(url, {
                        "text": text,
                        "blog_id": blogId,
                        "user_id": userId // USER ID SHOULD NOT BE HARDCODED DELETE AFTER AUTHSERVICE SETUP!!!!!!!!
                    });
                    console.log(response.data);
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