<template>
    <main>
        <v-container>
            <v-form ref="form" v-model="valid" lazy-validation>
                <v-textarea
                    width="350px"
                    label="Feedback comment"
                    v-model="feedback_comment"
                ></v-textarea>
                <v-row align="center" justify="space-between">
                    <v-btn class="success" depressed>accept</v-btn>
                    <v-btn class="error" depressed>reject</v-btn>
                </v-row>
            </v-form>
        </v-container>
    </main>
</template>

<script>
export default {};
</script>

<style></style>
