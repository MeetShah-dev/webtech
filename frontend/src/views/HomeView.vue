<!-- eslint-disable no-undef -->
<script>
import axios from 'axios';
import 'quill/dist/quill.snow.css';
import { quillEditor } from 'vue-quill-editor';
import Dialog from '@/components/Dialog.vue';


export default {
    name: 'Home-view',
    data() {
        return {
            userData: null,
            magazines: [],
            LatestMagazineBlogs: [],
            archivedMagazineData: [],
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
        NavBar: () => import('@/components/NavBar.vue'),
        FooterBar: () => import('@/components/FooterBar.vue'),
        quillEditor,
        Dialog,
    },
    async mounted() {
        await this.fetchLatestMagazine(); 
        await this.fetchAllMagazines();
    },
    methods: {
        async showDialog() {
            this.$refs.Dialog.dialogVisible = true;
        },


        async fetchLatestMagazine() {
            /*************************************************
            Getting latest magazine's associated blogs
            **************************************************/
            try {
                const url = import.meta.env.VITE_BLOGGING_SERVER + '/api/magazine-feed/';
                const response = await axios.get(url);
                this.LatestMagazineBlogs = response.data;

                const latestBlog = response.data.results[0];
                const files = latestBlog.files;
                let htmlContent = `<h1>${latestBlog.title}</h1><br>` + latestBlog.content; 
                if (files.length > 0) {
                    for (var i = 0; i < files.length; i++) {
                        const uidRegExp = new RegExp(files[i].uid.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'g');
                        const imgTag = `<img src="${files[i].url}" alt="Image">`;
                        htmlContent = htmlContent.replace(uidRegExp, imgTag + ' ');
                    }
                }
                this.blog.content = htmlContent;
                /////////////////////////////////////////////////////////////////////
            } catch (error) {
                console.error('Error:', error);
            }
        },

        async fetchAllMagazines() {
            /*************************************************
            Getting latest magazine's associated blogs
            **************************************************/
            try {
                const url = import.meta.env.VITE_ADMIN_SERVER + '/getAllMagazines'; // change for auth api
                const response = await axios.get(url);
                this.magazines = response.data;
                this.magazines.reverse(); // ordering by the latest
            } catch (error) {
                console.error('Error:', error);
            }
        },

        async getArchivedMagazine(magazineId) {
            try {
                const url = import.meta.env.VITE_BLOGGING_SERVER + '/api/archived-magazine/'; // change for auth api
                const response = await axios.get(url, {
                    params: {'magazine': magazineId}
                });
                return response.data;
            } catch (error) {
                console.error('Error:', error);
            }
        },

        async handleMagazineClick(magazineId) { // need to work on that...
            console.log('Clicked on magazine with ID:', magazineId);
            const magazinedata = await this.getArchivedMagazine(magazineId);
            this.$router.push({ name: 'magazine view', query: { data: JSON.stringify(magazinedata) } });
        },

        async readLatestMagazine() {
            this.$router.push({ name: 'magazine view', query: { data: JSON.stringify(this.LatestMagazineBlogs) } });
        }
    },
};
</script>

<template>
    <main class="home">
        <nav-bar></nav-bar>
        <h1>Homepage</h1>
        <div class="main">
            <div class="side-container">
                <h2>Magazine Archives</h2>
                <br />
                <ul id="sidebar-ul" v-for="magazine in magazines" :key="magazine.id">
                    <li v-if="magazine.flag !== 'upcoming'" @click="handleMagazineClick(magazine.id)">
                        <b class="archived-magazine">{{ magazine.title }}</b>
                        <b><span v-if="magazine.flag === 'upcoming'"><small id="upcoming">  - upcoming</small></span></b>
                    </li>
                    <li v-else @click="showDialog">
                        <b class="archived-magazine">{{ magazine.title }}</b>
                        <b><span v-if="magazine.flag === 'upcoming'"><small id="upcoming">  - upcoming</small></span></b>
                    </li>
                </ul>
            </div>
            <div class="main-container">
                <h2>
                    <div class="center">Latest Magazine's Article</div>
                </h2>

                <div class="cover-image">
                    <quillEditor id="ql-editor" placeholder="Content" v-model.lazy="blog.content" ref="myQuillEditor"
                    :options="blog.editorOption" />
                </div>
                <div class="center">
                    <div class="main-container-btn">
                        <v-row>
                            <router-link :to="{ name: 'dashboard' }">
                                <v-btn flat dark color="#114C6E" style="margin-right: 20px;">Post to our upcoming Magazine</v-btn>
                            </router-link>
                            <v-btn @click="readLatestMagazine" flat dark color="#114C6E" tag="button">Read Latest released Magazine</v-btn>
                        </v-row>
                    </div>
                </div>
            </div>
            <div class="side-container">
                <h2>Your Digital Guide to University Living</h2>
                <br />
                <p>
                    Surrey Horizon is designed to be your go-to source for all
                    things related to university life, catering specifically to
                    students and staff. Whether you're looking for campus news,
                    academic resources, or engaging content to stay informed and
                    entertained, our app has you covered.
                </p>
            </div>
            <Dialog ref="Dialog"></Dialog>
        </div>
        <footer-bar></footer-bar>
    </main>
</template>

<style scoped>
.home h1 {
    margin: 7px;
    padding: 10px;
}
.main {
    margin: 7px;
    padding: 10px;
    width: 100%;
    height: 1000px;
    display: flex;
    justify-content: space-around;
}

.main-container {
    margin: 7px;
    padding: 10px;
    width: 50%;
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

.center {
    margin: 5px;
    padding: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.main-container,
.cover-image {
    margin: 5px;
    padding: 10px;
    height: 80%;
}

.main-container-btn {
    margin: 5px;
    padding: 10px;
    display: flex;
    justify-content: space-between;
}
.side-container {
    margin: 7px;
    padding: 10px;
    width: 20%;
    height: 70%;
    background-color: #c1e2f4;
}

#sidebar-ul {
    margin: 5px;
    list-style-type: none;
    margin: 0;
    padding: 0px;
}
#sidebar-ul li {
    margin: 5px;
    margin-bottom: 10px;
    padding: 5px;
}
#ql-editor {
    height: 76vh;
}
.archived-magazine {
    color: rgb(102, 101, 101);
}
.archived-magazine:hover {
    color: rgb(79, 146, 204);
    cursor: pointer;
    transition: color 0.3s;
}
#upcoming {
    color: rgb(17, 148, 43);
}
</style>
