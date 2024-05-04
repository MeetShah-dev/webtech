<template>
    <main class="editing">
      <v-container>
        <h2>Create a Magazine</h2>
        <div class="article-form">
          <v-form ref="form" v-model="valid" lazy-validation>
            <v-text-field label="Magazine title" v-model="mag_title"></v-text-field>
            <v-select v-model="article_num" :items="[1, 2, 3, 4]" label="Number of articles"></v-select>
            <v-row>
              <v-col cols="12" sm="4">
                <v-text-field label="Month" v-model="mag_month"></v-text-field>
              </v-col>
              <v-col cols="12" sm="4">
                <v-text-field label="Date" v-model="mag_date"></v-text-field>
              </v-col>
              <v-col cols="12" sm="4">
                <v-text-field label="Year" v-model="mag_year"></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" sm="4">
                <v-text-field label="Hour" v-model="mag_hour"></v-text-field>
              </v-col>
              <v-col cols="12" sm="4">
                <v-text-field label="Minute" v-model="mag_minute"></v-text-field>
              </v-col>
              <v-col cols="12" sm="4">
                <v-text-field label="Second" v-model="mag_second"></v-text-field>
              </v-col>
            </v-row>
            <v-btn class="primary" @click="submitForm">Submit</v-btn>
          </v-form>
        </div>
      </v-container>
    </main>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        valid: true,
        mag_title: '',
        article_num: null,
        mag_month: '',
        mag_date: '',
        mag_year: '',
        mag_hour: '',
        mag_minute: '',
        mag_second: ''
      };
    },
  
    methods: {
      async submitForm() {
        const data = {
          title: this.mag_title,
          year: parseInt(this.mag_year),
          month: parseInt(this.mag_month),
          date: parseInt(this.mag_date),
          hour: parseInt(this.mag_hour),
          minute: parseInt(this.mag_minute),
          second: parseInt(this.mag_second)
        };
  
        try {
          const response = await axios.post('http://54.211.86.203:3028/schedule_magazine', data);
          console.log('Response:', response.data);
          // Handle successful response
        } catch (error) {
          console.error('Error:', error);
          // Handle error
        }
      }
    }
  };
  </script>