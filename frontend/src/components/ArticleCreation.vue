<template>
    <main class="editing">
        <v-container>
            <h2>Add a New Article</h2>
            <v-form ref="form" @submit.prevent="submitForm">
                <v-select v-model="blog.categoryItems" :items="categoryItems" item-text="name" item-value="id" hint="Pick one category at least" label="Categories*"
                        multiple persistent-hint></v-select>
                <v-text-field label="Title*" v-model="blog.title"></v-text-field>
                <quillEditor placeholder="Content" v-model.lazy="blog.content" ref="myQuillEditor"
                    :options="blog.editorOption" />
                <v-text-field label="Keywords" v-model="blog.keywords" hint="Separate keywords by a comma"></v-text-field>
                <v-checkbox v-model="blog.draft" label="Save as draft"></v-checkbox>
                <v-btn type="submit">Submit</v-btn>
            </v-form>
            <Success ref="Success"></Success>
        </v-container>
    </main>
</template>
<script>
import axios from 'axios'; 
import { v4 as uuidv4 } from 'uuid';
import 'quill/dist/quill.snow.css';
import { quillEditor } from 'vue-quill-editor';
import Success from '@/components/Success.vue';

export default {
    name: 'CreateBlog',
    components: {
        quillEditor,
        Success
    },
    data() {
        return {
            blog: {
                title: '',
                content: '', 
                categories: [],
                keywords: '',
                draft: false,
                editorOption: {
                    debug: 'info',
                    placeholder: 'Share your thoughts with us...',
                    theme: 'snow',
                },
            },
            categories: [],
            categoryItems: '',
            formData: new FormData(), 
        };
    },
    async mounted() {
        await this.fetchCategories();
        await this.getLikes();
    },

    methods: {
        async submitForm() {
            const title = this.blog.title;
            const content = await this.blogParser(this.blog.content);
            const isDraft = this.blog.draft;
            const category_ids = JSON.stringify(this.blog.categoryItems);
            const keywords = JSON.stringify(this.blog.keywords.split(','))
            const parsedUser = JSON.parse(decodeURIComponent(sessionStorage.getItem('user')));

            this.formData.append('user', parsedUser.id); 
            this.formData.append('title', title);
            this.formData.append('content', content);
            this.formData.append('is_draft', isDraft);
            this.formData.append('category_ids', category_ids);
            this.formData.append('keywords', keywords);
            try {
                // const url = import.meta.env.VITE_BLOGGING_SERVER + '/api/create-blog/';
                const url = 'api/blog/create-blog/';
                const response = await axios.post(url, this.formData);
                console.log(response.data);
            } catch (error) {
                console.error('Error:', error);
            }
            await this.showMessage();
            await this.resetInputFields();
        },
        
        async fetchCategories() {
              try {
                    const url = import.meta.env.VITE_AUTH_SERVER + '/admin/all-categories';
                    const response = await axios.get(url);
                    this.categoryItems = response.data; 
                    return response.data;
              } catch (error) {
                    console.error('Error fetching categories:', error);
              }
        },

        async blogParser(htmlContent) {
            /*****************************************************************************************
            This function parses the HTML in the editor to convert base64 images to files and assign 
            each file a UUID as a placeholder in the text so that the blog order can be maintained.
            ******************************************************************************************/
            const div = document.createElement('div');
            div.innerHTML = htmlContent;
            const images = div.querySelectorAll('img');
            var file_placeholders = [];
            var i = 1;
            for (const img of images) {
                const uuid = uuidv4();
                file_placeholders.push({[`file${i}`]: uuid});
                const span = document.createElement('span');
                span.textContent = uuid;
                img.parentNode.replaceChild(span, img);
                const src = img.src;
                const response = await fetch(src);
                const blob = await response.blob();
                const file = new File([blob], `image-${i}.png`, { type: 'image/png' });
                this.formData.append(`file${i}`, file);
                i++;
            }
            this.formData.append('file_placeholders', JSON.stringify(file_placeholders));
            return div.innerHTML;
        },

        async resetInputFields() {
            this.blog.title = '';
            this.blog.content = '';
            this.blog.categoryItems = [];
            this.blog.keywords = '';
            this.blog.draft = false;
            this.formData = new FormData();
        },

        async showMessage() {
            this.$refs.Success.dialogVisible = true;
        },

    }
}
</script> 
<style>
.ql-editor {
    height: 72vh;
}
</style>