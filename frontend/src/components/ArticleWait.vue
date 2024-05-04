<script>
import axios from 'axios';

export default {
    name: 'axios-articlewaiting',
    data() {
        return {
            articleItems: null,
            selectedArticle: {
                id: ""
            },
            selectedArticleTitle: "",
            data: '',
            response: '',
            feedback_comment: " ", // Data binding for feedback comment
             // Data binding for the new category input
            feedbackSubmitted: false
            };
         
        
    },
    async mounted() {
        await this.fetchArticles(); // Call the method to fetch categories
    },
    methods: {
        async fetchArticles() {
            try {
                const response = await axios.get("http://18.206.186.97:8000/getReadyPosts");
                this.articleItems = response.data; // Populate categories array
            } catch (error) {
                console.error('Error fetching categories:', error);
            }
        },
        async submitFeedback() {
            try {
                const feedbackData = {
                    blog: this.selectedArticle.id,
                    content: this.feedback_comment
                };
                this.feedbackSubmitted=true
                // Post feedback to the /postfeedback API
                await axios.post("http://18.206.186.97:8000/postFeedback", feedbackData);
                
                // Reset selected article and feedback comment after successful submission
               
                // You may want to add additional logic here, like displaying a success message
            } catch (error) {
                console.error('Error submitting feedback:', error);
                // You can handle errors here, e.g., displaying an error message
            }
        },
        async approveSelectedArticle() {
            try {
             
               
                await axios.put("http://18.206.186.97:8000/approvePost", { id: this.selectedArticle.id });
                alert(`Post ID ${this.selectedArticle.id} is approved.`);
            } catch (error) {
                console.error('Error approving article:', error);
            }
        },

        async rejectSelectedArticle() {
            try {
             
               
                await axios.put("http://18.206.186.97:8000/rejectPost", { id: this.selectedArticle.id });
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
            

        
         
            const response = await axios.get('http://54.82.93.84:8000/api/read-blog-moderation/',
            {params: {'blog':this.selectedArticle.id}
            });
           alert("MERHABALAR" + response.data.content)
            
               // this.selectedArticleTitle = response.data.title;
        },

    }
};
</script>








<template>
    <main class="home">
        <h1>List of Articles to Check</h1>
        <div class="main">
            <div class="article-list">
                <v-list-item 
            v-for="article in articleItems" 
            :key="article.id"
            @click="selectArticle(article)"
             >
   
          <v-list-item-content>{{ article.id }} .th Article:  {{ article.title }}</v-list-item-content>
</v-list-item>
     
            </div>

            <div class="add-feedback">

                <v-container>
                     <div v-if="selectedArticle.id">
                        <p :style="{ 'font-weight': 'bold', 'font-style': 'italic', 'color': 'red' }">
                        You have selected {{ selectedArticle.id }}th Article "{{ selectedArticle.title }}" to give FEEDBACK.
                        </p>
                        <p :style="{ 'font-weight': 'bold', 'color': 'black' }">
                        FEEDBACK
                        </p>
                    </div>
        
                    
                    <v-form ref="form">
                        <v-form ref="form" >
                        <v-textarea
                            width="350px"
                            label="Feedback comment"
                            v-model="feedback_comment"
                        ></v-textarea>
                        <v-btn class="primary" depressed @click="submitFeedback">Submit</v-btn>
                    </v-form>
                        <v-row justify="space-between">
                            <v-btn class="success" depressed :disabled="!feedbackSubmitted" @click="approveSelectedArticle">accept</v-btn>
                            <v-btn class="error" depressed :disabled="!feedbackSubmitted" @click="rejectSelectedArticle">reject</v-btn>
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

.mb-2 {
  margin-bottom: 0.1rem; /* Adjust as needed */
}
main {
    width: 700px;
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

