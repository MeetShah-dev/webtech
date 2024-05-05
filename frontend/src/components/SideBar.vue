<template>
    <div class="side-drawer">
        <v-card>
            <v-navigation-drawer
                app
                permanent
                color="#c1e2f4"
                v-bind:width="325"
            >
                <v-tabs
                    vertical
                    v-model="tab"
                    background-color="#c1e2f4"
                    class="mt-9 mb-9"
                >
                    <v-tab
                        v-for="(link, index) in links"
                        :key="index"
                        class="mt-6 mb-6"
                    >
                        {{ link.text }}
                    </v-tab>
                </v-tabs>
            </v-navigation-drawer>

 
            <v-container class="custom-container">
                <v-tabs-items v-model="tab">
                    <v-tab-item v-for="(link, index) in links" :key="index">
                        <component :is="link.component"></component>
                    </v-tab-item>
                </v-tabs-items>
            </v-container>
        </v-card>
    </div>
</template>

<script>
import AddCategory from './AddCategory.vue';
import ArticleCreation from './ArticleCreation.vue';
import MagazineCreation from './MagazineCreation.vue';
import ArticleList from './ArticleList.vue';
import ArticleWait from './ArticleWait.vue';
import ScheduleSet from './ScheduleSet.vue';
import RescheduleSet from './RescheduleSet.vue';
import AdminConsole from './AdminConsole.vue';

export default {
    components: {
        ArticleCreation,
        MagazineCreation,
        ArticleList,
        ArticleWait,
        ScheduleSet,
        RescheduleSet,
        AddCategory,
        AdminConsole
    },
    name: 'SideBarComponent',
    props: {
        role: Number,
        default: () => {
        const user = JSON.parse(sessionStorage.getItem('user'));
        return user ? user.role_id : null;
    }
},
    data() {
        return {
            tab: null,
            links: this.getLinksBasedOnRole(),
        };
    },
    methods: {
        getLinksBasedOnRole() {
            const links = [
                { text: 'Create Article', component: 'ArticleCreation', roles: [1, 2, 3] },
                { text: 'Create Magazine', component: 'MagazineCreation', roles: [2, 3] },
                { text: 'View Article(s)', component: 'ArticleList', roles: [1, 2 ,3] },
                { text: 'Add Categories', component: 'AddCategory', roles: [2, 3] },
                { text: 'Article Waiting', component: 'ArticleWait', roles: [2, 3] },
                { text: 'Schedule Magazine', component: 'ScheduleSet', roles: [2 ,3] },
                { text: 'Reschedule Magazine', component: 'RescheduleSet', roles: [3] },
            ];
            console.log("this role", this.role)
            // Filter links based on role_id
            return links.filter(link => link.roles.includes(this.role));
        }
    },
    watch: {
        role(newVal) { // corrected from role_id to role
        this.links = this.getLinksBasedOnRole();
         }
    }
};
</script>

<style scoped>
.custom-container {
    width: 900px;
    height: max-content;
}
</style>
