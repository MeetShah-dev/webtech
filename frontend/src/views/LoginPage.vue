<template>
    <div class="main">
        <div class="top-image">
            <img src="@/assets/UniofSurrey.jpg" alt="University of Surrey" />
        </div>
        <div class="logo">
            <img
                alt="Surrey Horizon logo"
                class="logo-image"
                src="@/assets/Logo.png"
            />
            <img src="@/assets/Asset 1.png" alt="" />
        </div>
        <v-btn
            color="#114C6E"
            class="google-login-btn"
            @click="loginWithGoogle"
            outlined
            large
        >
            <v-icon left dark>mdi-google</v-icon>
            Sign in with Google
        </v-btn>
    </div>
</template>

<script>
export default {
    methods: {
        loginWithGoogle() {
            window.location.href =
                'https://svfg5klna6.execute-api.us-east-1.amazonaws.com/dev/auth/google/login';
        },
    },
};
</script>

<style scoped>
.main {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background-size: cover;
    background-repeat: no-repeat;
    color: white;
}

.top-image {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    overflow: hidden;
    height: 70%;
}
.top-image:after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    background: linear-gradient(
        to bottom,
        rgba(255, 255, 255, 0) 0%,
        rgba(255, 255, 255, 1) 30%
    );
    height: 40%;
}

.top-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    opacity: 0.8; /* Adjust opacity for fading effect */
}

.logo {
    position: relative;
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
    padding: 10px 20px;
    border: none;
    cursor: pointer;
}
.login-button img {
    padding: 3px;
    height: 20px;
    width: 20px;
}
.google-login-btn {
    color: #4285f4; /* Google blue */
    font-weight: 500;
    box-shadow: 0 3px 4px -2px rgba(0, 0, 0, 0.2);
}

.google-login-btn:hover {
    background-color: #e8f0fe; /* Light blue background on hover*/
}
</style>
