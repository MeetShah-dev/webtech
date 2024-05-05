<template>
    <v-dialog v-model="dialogVisible">
      <v-card>
        <v-card-title>Blog Submitted Successfully</v-card-title>
        <v-card-text>
          Your blog has been submitted successfully. It will undergo moderation checks, and you will be notified of the status.
        </v-card-text>
        <v-card-actions>
          <v-btn color="primary" @click="dialogVisible = false" style="margin-right: 20px;">Close</v-btn>
          <router-link :to="{ name: 'home' }">
            <v-btn color="primary">Go Back to Home</v-btn>
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