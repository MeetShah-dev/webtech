<template>
    <v-container>
        <v-row class="mb-2">
            <v-col
                v-for="category in displayedCategories"
                :key="category.id"
                cols="4"
            >
                <v-list-item>
                    <v-list-item-content>{{
                        category.name
                    }}</v-list-item-content>
                </v-list-item>
            </v-col>
        </v-row>

        <v-row v-if="categoriesItems && categoriesItems.length > 0">
            <v-row
                class="mb-2"
                style="justify-content: center; align-items: center"
            >
                <v-btn v-if="currentPage > 1" @click="currentPage--"
                    >Previous</v-btn
                >
                <v-btn v-if="hasNextPage" @click="currentPage++">Next</v-btn>
            </v-row>
        </v-row>

        <v-row v-else>
            <v-col>Loading...</v-col>
        </v-row>

        <!-- Form for adding a new category -->
        <v-row>
            <v-col>
                <h3>Add a New Category</h3>
                <v-form @submit.prevent="addCategory">
                    <v-text-field
                        v-model="newCategoryName"
                        label="Enter category name"
                        required
                        clearable
                        solo
                    ></v-text-field>
                    <v-row>
                        <v-btn color="primary" type="submit" class="mr-4"
                            >Add Category</v-btn
                        >
                    </v-row>
                    <v-row> </v-row>
                </v-form>
            </v-col>
        </v-row>

        <v-row> </v-row>
        <v-row> </v-row>
        <v-row> </v-row>
        <v-row> </v-row>

        <!-- Toast for displaying success message -->
        <v-row>
            <CToast :autohide="true" :visible="toast">
                <CToastHeader closeButton>
                    <svg
                        class="rounded me-2"
                        width="20"
                        height="20"
                        xmlns="http://www.w3.org/2000/svg"
                        preserveAspectRatio="xMidYMid slice"
                        focusable="false"
                        role="img"
                    ></svg>
                    <v-row>
                        <rect width="80%" height="80%" fill="#007aff"></rect>
                    </v-row>
                </CToastHeader>
                <CToastBody>{{ newCategoryMessage }}</CToastBody>
            </CToast>
        </v-row>
    </v-container>
</template>

<script>
import axios from 'axios';

export default {
    name: 'CategoryList',
    data() {
        return {
            itemsPerPage: 9,
            currentPage: 1,
            categoriesItems: [],
            newCategoryName: '',
            toast: false,
            newCategoryMessage: '',
            toastTime: '',
        };
    },
    computed: {
        displayedCategories() {
            const startIndex = (this.currentPage - 1) * this.itemsPerPage;
            const endIndex = startIndex + this.itemsPerPage;
            return this.categoriesItems.slice(startIndex, endIndex);
        },
        hasNextPage() {
            const startIndex = this.currentPage * this.itemsPerPage;
            return startIndex < this.categoriesItems.length;
        },
    },
    async mounted() {
        await this.fetchCategories();
    },
    methods: {
        async fetchCategories() {
            try {
                const response = await axios.get(
                    'http://18.206.186.97:8000/getAllCategories'
                );
                this.categoriesItems = response.data;
            } catch (error) {
                console.error('Error fetching categories:', error);
            }
        },
        async addCategory() {
            try {
                const response = await axios.post(
                    'http://18.206.186.97:8000/addCategory',
                    {
                        name: this.newCategoryName,
                    }
                );
                this.newCategoryName = '';
                this.categoriesItems.push(response.data);

                // Show toast when category is added successfully
                this.newCategoryMessage =
                    'New category "' + response.data.name + '" added';
                this.toastTime = new Date().toLocaleTimeString();
                this.toast = true;
            } catch (error) {
                console.error('Error adding category:', error);
            }
        },
    },
};
</script>

<style scoped>
/* Add scoped styles here if needed */
</style>
