<template>
    <div class="main">
        <div class="logo">
            <img
                alt="Surrey Horizon logo"
                class="logo-image"
                src="@/assets/Logo.png"
            />
            <img src="@/assets/Asset 1.png" alt="" />
        </div>
        <v-btn class="login-button">
            <img src="../assets/google-color-icon.svg" alt="" />
            <v-spacer></v-spacer>
            Continue with Google
        </v-btn>
    </div>
</template>

<script>
export default {
    // Component logic here
};
</script>

<style scoped>
.main {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background-color: black;
    color: white;
}

.logo {
    display: flex;
    flex-direction: row;
    align-items: center; /* Align items horizontally */
    margin-bottom: 20px; /* Add margin between logo and button */
}

.logo img {
    height: 120px;
    margin-right: 10px; /* Add right margin to separate logo images */
}

.login-button {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 10px 20px; /* Add padding to button */
    background-color: #007bff; /* Example: Blue background color */
    color: white;
    border: none;
    cursor: pointer;
}
.login-button img {
    height: 20px;
    width: 20px;
}
</style>
