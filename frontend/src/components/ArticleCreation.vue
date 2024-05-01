<script>
import axios from 'axios'; // Import Axios library
import { v4 as uuidv4 } from 'uuid';
import 'quill/dist/quill.snow.css';
import { quillEditor } from 'vue-quill-editor';
// import { Button, Input, Select } from 'iview';

export default {
    name: 'CreateBlog',
    components: {
        // Button,
        // Input,
        // Select,
        quillEditor,
    },
    data() {
        return {
            blog: {
                // valid: true,
                // name: '',
                // nameRules: [
                //     (v) => !!v || 'Name is required',
                //     (v) =>
                //         (v && v.length <= 10) ||
                //         'Name must be less than 10 characters',
                // ],
                // email: '',
                // emailRules: [
                //     (v) => !!v || 'E-mail is required',
                //     (v) => /.+@.+\..+/.test(v) || 'E-mail must be valid',
                // ],
                title: '',
                title_rules: [],

                content: '',
                content_rules: [],
                editorOption: {
                    debug: 'info',
                    placeholder: 'Type your post here...',
                    readOnly: true,
                    theme: 'snow',
                },

                categories: '',

                // postCategories: [
                //     {
                //         id:1,
                //         label:'AI',
                //         img: 'https://pluralsight.imgix.net/paths/path-icons/nodejs-601628d09d.png?w=200',
                //     }
                // ],

                delta: undefined,
                //postcategories json

                select: null,
                items: ['Item 1', 'Item 2', 'Item 3', 'Item 4'],
                checkbox: false,
            },
        };
    },
    methods: {
        validate() {
            this.$refs.form.validate();
        },
        reset() {
            this.$refs.form.reset();
        },
        resetValidation() {
            this.$refs.form.resetValidation();
        },
        //FORM FIELDS DATA SETUP
        async handleSubmit() {
            // Get the selected files from the file input
            const files = this.$refs.fileInput.files;

            // Prepare FormData object to hold the files
            const formData = new FormData();
            for (let i = 0; i < files.length; i++) {
                formData.append(`file${i + 1}`, files[i]);
            }
            const uid = uuidv4(); // generate uids for all the files

            // Add other fields to FormData object
            formData.append('title', this.title);
            formData.append('content', this.content + uid);

            // Example of additional data
            formData.append('user', '1');
            formData.append('category_ids', JSON.stringify(['1', '2']));
            formData.append('is_draft', true);
            formData.append(
                'keywords',
                JSON.stringify(['keyword1', 'keyword2'])
            );
            formData.append(
                'file_placeholders',
                JSON.stringify([
                    { file1: uid }, // only using ONE FILE! a logic has to be implemented for when man files are used
                ])
            );

            // Make the POST request
            try {
                const url = 'http://54.82.93.84:8000/api/create-blog/';
                console.log(Object.fromEntries(formData));
                const response = await axios.post(url, formData);
                console.log(response.data);
            } catch (error) {
                console.error('Error:', error);
            }
        },
    },
    watch: {
        content() {
            this.delta = this.$refs.myQuillEditor.quill.getContents(); //helps reduce load to database
        },
    },
};
</script>

<template>
    <!-- <div class="hello">
    <h1>{{ msg }}</h1>
    <form @submit.prevent="handleSubmit">
      <input type="file" ref="fileInput" multiple accept="image/*, video/*" />
      <input type="text" v-model="title" placeholder="Title" required />
      <textarea v-model="content" placeholder="Content" required></textarea>
      <button type="submit">Upload Files</button>
    </form>
  </div> -->
    <main class="editing">
        <v-container>
            <h2>Add a New Article</h2>
            <v-form ref="form" v-model="valid" lazy-validation>
                <v-text-field
                    label="User ID"
                    v-model="blog.user_id"
                ></v-text-field>
                <v-text-field
                    label="Article ID"
                    v-model="blog.id"
                ></v-text-field>
                <v-text-field
                    label="Magazine ID"
                    v-model="blog.mag_id"
                ></v-text-field>
                <v-select
                    :categories="categories"
                    label="Categories"
                    v-model="blog.categories"
                >
                    <!-- <Option
                        v-for="(cat, index) in postCategories"
                        :key="index"
                        :value="cat.id"
                        >{{}}</Option
                    > -->
                </v-select>
                <v-text-field
                    label="Article Title"
                    v-model="blog.title"
                ></v-text-field>
                <quillEditor
                    placeholder="Content"
                    v-model.lazy="blog.content"
                    ref="myQuillEditor"
                    :options="editorOption"
                />
                <v-file-input
                    show-size
                    v-model="blog.file1"
                    label="File input"
                ></v-file-input>
                <v-file-input
                    show-size
                    v-model="blog.file2"
                    label="File input (Optional)"
                ></v-file-input>
                <v-text-field
                    label="Keywords"
                    v-model="blog.keywords"
                ></v-text-field>
                <v-checkbox label="Keep as draft">Keep as draft</v-checkbox>
                <v-btn>submit</v-btn>
            </v-form>
        </v-container>
    </main>
</template>
<style>
.ql-editor {
    height: 72vh;
}
</style>
