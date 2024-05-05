<template>
    <v-dialog v-model="dialogVisible">
      <v-card>
        <v-card-title>Magazine Not Released</v-card-title>
        <v-card-text>
          This magazine hasn't been released yet. You can create a new article instead.
        </v-card-text>
        <v-card-actions>
          <v-btn color="primary" @click="dialogVisible = false" style="margin-right: 20px;">Close</v-btn>
          <router-link :to="{ name: 'dashboard' }">
            <v-btn color="primary">Post</v-btn>
          </router-link>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </template>
  
  <script>
    export default {
      data() {
        return {
          dialogVisible: false
        };
      }
    };
  </script>
    