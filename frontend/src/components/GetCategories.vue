<template>
    <div>
        <div v-if="responseData">
            {{ responseData }}
        </div>
        <div v-else>Loading...</div>
    </div>
</template>
3()

<script>
import axios from 'axios';
export default {
    name: 'axios-category',
    data() {
        return {
            responseData: null,
        };
    },
    mounted() {
        // Example headers
        const headers = {
            Accept: 'application/json',
            // Add any other headers you need here
        };

        // Example GET request with headers
        axios
            .get('http://localhost:8083/getAllCategories', { headers })
            .then((response) => {
                this.responseData = response.data;
                console.log(this.responseData); // Print the response data to the console
                console.log('CCCCC'); // Print the response data to the console
            })
            .catch((error) => {
                console.error('Error fetching data:', error);
            });
    },
};
</script>
