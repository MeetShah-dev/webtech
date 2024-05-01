<script>
export default {
    data: () => ({
        valid: true,
        name: '',
        nameRules: [
            (v) => !!v || 'Name is required',
            (v) =>
                (v && v.length <= 10) || 'Name must be less than 10 characters',
        ],
        email: '',
        emailRules: [
            (v) => !!v || 'E-mail is required',
            (v) => /.+@.+\..+/.test(v) || 'E-mail must be valid',
        ],
        select: null,
        items: ['Item 1', 'Item 2', 'Item 3', 'Item 4'],
        checkbox: false,
    }),

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
    },
};
</script>

<template>
    <main class="editing">
        <v-container>
            <h2>Create a Magazine</h2>
            <div class="article-form">
                <v-form ref="form" v-model="valid" lazy-validation>
                    <v-text-field
                        label="Magazine ID"
                        v-model="mag_id"
                    ></v-text-field>
                    <v-text-field
                        label="Magazine title"
                        v-model="mag_title"
                    ></v-text-field>
                    <v-select
                        :article_num="article_num"
                        label="Number of articles"
                    ></v-select>
                    <v-file-input
                        show-size
                        label="Article cover image"
                    ></v-file-input>
                    <v-btn class="primary">submit</v-btn>
                </v-form>
            </div>
        </v-container>
    </main>
</template>
