<template>
    <main>
        <v-container>
            <v-form ref="form" v-model="valid" lazy-validation>
                <v-text-field
                    width="300px"
                    label="Add New Category"
                    v-model="addCategory"
                ></v-text-field>
                <v-row align="center" justify="space-between">
                    <v-btn class="primary" depressed>add category</v-btn>
                </v-row>
            </v-form>
        </v-container>
        <v-container>
            <h2>Categories</h2>
            <div>
                <div v-if="responseData">
                    {{ responseData }}
                </div>
                <div v-else>Loading...</div>
            </div>
        </v-container>
    </main>
</template>

<script>
export default {
    data() {
        return {
            addCategory: '',
        };
    },
};
</script>

<style scoped>
main {
    width: 900px;
}
</style>
