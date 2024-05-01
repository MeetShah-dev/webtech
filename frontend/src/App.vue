<!-- <script>
import NavBar from '@/components/NavBar.vue';
import FooterBar from './components/FooterBar.vue';
export default {
    name: 'App',
    components: { NavBar, FooterBar },
    watch: {
        $route: {
            immediate: true,
            handler(to) {
                document.title = to.meta.title || 'Surrey Horizon';
            },
        },
    },
};
</script> -->

<script>
export default {
    name: 'App',
    components: {},
    watch: {
        $route: {
            immediate: true,
            handler(to) {
                document.title = to.meta.title || 'Surrey Horizon';
            },
        },
    },
};
</script>

<!-- <template>
    <v-app class="grey lightn-4">
        <img alt="Surrey Horizon logo" class="logo" src="@/assets/s-h.png" />
        <nav-bar></nav-bar>
        <v-main>
            <router-view></router-view>
        </v-main>

        <v-footer>
            <footer-bar></footer-bar>
        </v-footer>
    </v-app>
</template> -->

<template>
    <v-app class="grey lightn-4">
        <!-- <img alt="Surrey Horizon logo" class="logo" src="@/assets/s-h.png" /> -->
        <router-view></router-view>
    </v-app>
</template>

<!-- <template>
    <div id="app">
        <header>
            <nav>
                <router-link to="/">Home</router-link>
                <router-link to="/catalogue">Catalogue</router-link>
            </nav>
        </header>

        <router-view />
    </div>
</template> -->

<style scoped>
.logo {
    display: block;
    margin: auto;
    justify-content: center;
    height: 120px;
    width: auto;
}
</style>
