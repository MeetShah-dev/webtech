<template>
    <v-container>
      <!-- Display categories if they exist -->
      <v-list dense v-if="categoriesItems && categoriesItems.length > 0">
        <v-list-item 
          v-for="category in categoriesItems" 
          :key="category.id"
          class="mb-2"
        >
          <v-list-item-content>{{ category.name }}</v-list-item-content>
        </v-list-item>
      </v-list>
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
            <v-btn color="primary" type="submit" class="mr-4">Add Category</v-btn>
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
              categoriesItems: null,
              newCategoryName: '', // Data binding for the new category input
          };
      },
      async mounted() {
          await this.fetchCategories(); // Call the method to fetch categories
      },
      methods: {
          async fetchCategories() {
              try {
                  const response = await axios.get("http://18.206.186.97:8000/getAllCategories");
                  this.categoriesItems = response.data; // Populate categories array
              } catch (error) {
                  console.error('Error fetching categories:', error);
              }
          },
          async addCategory() {
              try {
                  const response = await axios.post("http://18.206.186.97:8000/addCategory", {
                      name: this.newCategoryName
                  });
                  this.newCategoryName = ''; // Clear the input after a successful post
                  this.categoriesItems.push(response.data); // Add the new category to the list
              } catch (error) {
                  console.error('Error adding category:', error);
              }
          }
      }
  };
  </script>
  


<style scoped>
main {
    width: 900px;
}
</style>
