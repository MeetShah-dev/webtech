<template>
    <main class="editing">
        <!-- Top Navigation Bar -->
        <v-app-bar color="primary" dark>
            <v-toolbar-title>Create Profile</v-toolbar-title>
        </v-app-bar>

        <!-- Main Content -->
        <v-container>
            <v-card class="profile-form">
                <v-card-title>Create Your Profile</v-card-title>

                <!-- Form for User Registration -->
                <v-form ref="form" v-model="valid" @submit.prevent="submitForm">
                    <!-- Name Input Field -->
                    <v-text-field
                        v-model="formData.name"
                        label="Name"
                        :rules="nameRules"
                        required
                    ></v-text-field>

                    <!-- Email Input Field -->
                    <v-text-field
                        v-model="formData.email"
                        label="Email"
                        :rules="emailRules"
                        required
                    ></v-text-field>

                    <!-- Password Input Field -->
                    <v-text-field
                        v-model="formData.password"
                        label="Password"
                        type="password"
                        :rules="passwordRules"
                        required
                    ></v-text-field>

                    <!-- Confirm Password Input Field -->
                    <v-text-field
                        v-model="formData.confirmPassword"
                        label="Confirm Password"
                        type="password"
                        :rules="confirmPasswordRules"
                        required
                    ></v-text-field>

                    <!-- Submit Button -->
                    <v-btn type="submit" color="primary" :disabled="!valid">
                        Create Profile
                    </v-btn>
                </v-form>
            </v-card>
        </v-container>
    </main>
</template>

<script>
export default {
    data() {
        return {
            valid: false,
            formData: {
                name: '',
                email: '',
                password: '',
                confirmPassword: '',
            },
            nameRules: [
                (v) => !!v || 'Name is required',
                (v) =>
                    (v && v.length <= 50) ||
                    'Name must be less than 50 characters',
            ],
            emailRules: [
                (v) => !!v || 'Email is required',
                (v) => /.+@.+\..+/.test(v) || 'Email must be valid',
            ],
            passwordRules: [
                (v) => !!v || 'Password is required',
                (v) =>
                    (v && v.length >= 8) ||
                    'Password must be at least 8 characters',
            ],
            confirmPasswordRules: [
                (v) => !!v || 'Confirm Password is required',
                (v) => v === this.formData.password || 'Passwords do not match',
            ],
        };
    },
    methods: {
        submitForm() {
            if (this.$refs.form.validate()) {
                // Form is valid, submit the data (replace with actual API call)
                console.log('Form submitted:', this.formData);

                // Reset form after successful submission
                this.resetForm();
            }
        },
        resetForm() {
            this.$refs.form.reset();
            this.formData = {
                name: '',
                email: '',
                password: '',
                confirmPassword: '',
            };
        },
    },
};
</script>

<style scoped>
.editing {
    display: flex;
    flex-direction: column;
    height: 100vh;
}

.profile-form {
    max-width: 400px;
    margin: auto;
    padding: 20px;
}
</style>
