<script>
import ArticleCreation from '../components/ArticleCreation.vue';
export default {
    components: {
        ArticleCreation,
        SideBar: () => import('@/components/SideBar.vue'),
        NavBar: () => import('@/components/NavBar.vue'),
    },
    //     name: '',
    //     nameRules: [
    //         (v) => !!v || 'Name is required',
    //         (v) =>
    //             (v && v.length <= 10) || 'Name must be less than 10 characters',
    //     ],
    //     email: '',
    //     emailRules: [
    //         (v) => !!v || 'E-mail is required',
    //         (v) => /.+@.+\..+/.test(v) || 'E-mail must be valid',
    //     ],
    //     select: null,
    //     items: ['Item 1', 'Item 2', 'Item 3', 'Item 4'],
    //     checkbox: false,
    // }),
    // methods: {
    //     validate() {
    //         this.$refs.form.validate();
    //     },
    //     reset() {
    //         this.$refs.form.reset();
    //     },
    //     resetValidation() {
    //         this.$refs.form.resetValidation();
    //     },
    // },
    data() {
        return {
            links: [
                { icon: 'mdi-home', text: 'Go Home', route: '/' },
                {
                    icon: 'mdi-file-eye-outline',
                    text: 'View Article(s)',
                    route: '',
                },
                {
                    icon: 'mdi-file-document-plus-outline',
                    text: 'Add Article',
                    route: '',
                },
                {
                    icon: 'mdi-file-document-edit-outline',
                    text: 'Edit Article(s)',
                    route: '',
                },
                {
                    icon: 'mdi-file-document-check-outline',
                    text: 'Approved Article',
                    route: '',
                },
                {
                    icon: 'mdi-file-document-remove-outline',
                    text: 'Rejected Articles',
                    route: '',
                },
            ],
            //FORM FIELDS DATA SETUP
        };
    },
};
</script>

<template>
    <main class="editing">
        <side-bar></side-bar>
        <nav-bar></nav-bar>
        <div class="main-container">
            <article-creation></article-creation>
        </div>
    </main>
</template>

<style scoped>
.editing {
    margin-left: 200px;
    padding: 10px; /*
    display: flex;
    height: 800px;
    width: 100%;
    align-items: center;
    justify-content: space-between; */
}

.main-container {
    /* margin: 10px;
    padding: 10px; */
    width: 60%;
    /* height: max-content; */
}

.main-container-btn {
    display: flex;
    justify-content: space-between;
}
.side-container {
    padding: 0;
    width: 20%;
    height: 550px;
    background-color: #c1e2f4;
}
</style>
