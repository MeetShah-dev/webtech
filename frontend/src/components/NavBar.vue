<template>
    <nav>
        <div class="logo">
            <img
                alt="Surrey Horizon logo"
                class="logo"
                src="@/assets/Logo.png"
            />
            <h1>SURREY HORIZON</h1>
        </div>
        <v-toolbar flat dark app color="#114C6E">
            <v-tabs>
                <v-tab exact to="/" active>Home</v-tab>
                <v-tab exact to="/dashboard">Dashboard</v-tab>
                <v-tab exact to="/editing">Editing</v-tab>
            </v-tabs>
            <v-spacer></v-spacer>
            <v-menu open-on-hover bottom offset-y>
                <template v-slot:activator="{ on, attrs }">
                    <v-btn icon v-bind="attrs" v-on="on">
                        <v-btn icon>
                            <v-icon>mdi-bell</v-icon>
                        </v-btn>
                    </v-btn>
                </template>

                <v-list v-bind:width="370">
                    <v-list-item v-for="(notif, index) in notifs" :key="index">
                        <v-list-item-title>{{ notif.title }}</v-list-item-title>
                    </v-list-item>
                </v-list>
            </v-menu>
            <v-menu bottom>
                <template v-slot:activator="{ on, attrs }">
                    <v-btn icon v-bind="attrs" v-on="on">
                        <v-icon>mdi-menu</v-icon>
                    </v-btn>
                </template>

                <v-list>
                    <v-list-item v-for="(menu, index) in menus" :key="index">
                        <v-list-item-title>{{ menu.title }}</v-list-item-title>
                    </v-list-item>
                </v-list>
            </v-menu>

            <v-btn>
                <span>Sign Out</span>
                <v-icon right>mdi-exit-to-app</v-icon>
            </v-btn>
        </v-toolbar>
    </nav>
</template>

<script>
// import UserRegistration from '../components/UserRegistration.vue';
export default {
    name: 'nav-bar',
    data() {
        return {
            links: [
                { tab: 'home', text: 'Home', route: '/' },
                { tab: 'dashboard', text: 'Dashboard', route: '/dashboard' },
                { tab: 'editing', text: 'Editing', route: '/editing' },
                { tab: 'author', text: 'Authors', route: '/author-page' },
            ],
            menus: [
                { title: 'Author page' },
                { title: 'Blog list' },
                { title: 'Update profile', components: 'UserRegistration' },
            ],
            notifs: [{ title: 'Notification 1' }, { title: 'Notification 2' }],
        };
    },
    components: {
        // UserRegistration,
    },
};
</script>

<style scoped>
.logo {
    display: flex;
    flex-direction: row;
}
.logo h1 {
    height: 120px;
    font-size: 30pt;
    font-stretch: ultra-expanded;
    padding-top: 23px;
}

.logo img {
    height: 120px;
}
</style>
