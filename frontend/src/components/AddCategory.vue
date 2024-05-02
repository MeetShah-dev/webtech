<template>
    <v-container>
        <v-row>
            <v-col>
                <!-- Display categories with pagination -->
                <v-list
                    dense
                    v-if="categoriesItems && categoriesItems.length > 0"
                    class="d-flex flex-wrap"
                >
                    <!-- Iterate over categories to display -->
                    <v-list-item
                        v-for="category in displayedCategories"
                        :key="category.id"
                        class="mb-2"
                    >
                        <v-list-item-content>{{
                            category.name
                        }}</v-list-item-content>
                    </v-list-item>
                </v-list>
                <v-row
                    v-if="categoriesItems && categoriesItems.length > 0"
                    style="justify-content: space-between; padding-bottom: 5px"
                >
                    <v-btn v-if="currentPage > 1" @click="currentPage--"
                        >Previous</v-btn
                    >
                    <v-btn v-if="hasNextPage" @click="currentPage++"
                        >Next</v-btn
                    >
                </v-row>
                <v-row v-else>
                    <v-col>Loading...</v-col>
                </v-row>
            </v-col>
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
                    <v-btn color="primary" type="submit" class="mr-4"
                        >Add Category</v-btn
                    >
                </v-form>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import axios from 'axios';

export default {
    name: 'axios-category',
    data() {
        return {
            // categoriesItems: [], // Assuming this is your list of categories
            itemsPerPage: 10,
            currentPage: 1,
            categoriesItems: null,
            newCategoryName: '', // Data binding for the new category input
        };
    },
    computed: {
        // Compute the categories to display based on pagination
        displayedCategories() {
            const startIndex = (this.currentPage - 1) * this.itemsPerPage;
            const endIndex = startIndex + this.itemsPerPage;
            return this.categoriesItems.slice(startIndex, endIndex);
        },
        // Determine if there is a next page
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
                this.newCategoryName = ''; // Clear the input after a successful post
                this.categoriesItems.push(response.data); // Add the new category to the list
            } catch (error) {
                console.error('Error adding category:', error);
            }
        },
    },
};
</script>

<style scoped></style>
