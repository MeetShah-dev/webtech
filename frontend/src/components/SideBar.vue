<template>
    <div class="side-drawer">
        <v-card>
            <v-navigation-drawer
                app
                permanent
                color="#c1e2f4"
                v-bind:width="325"
            >
                <v-tabs vertical v-model="tab" background-color="#c1e2f4">
                    <v-tab v-for="(link, index) in links" :key="index">
                        {{ link.text }}
                    </v-tab>
                    <v-spacer></v-spacer>
                    <v-tab>Home</v-tab>
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
    data() {
        return {
            tab: null,
            links: [
                { text: 'Create Article', component: 'ArticleCreation' },
                { text: 'Schedule Magazine', component: 'MagazineCreation' },
                { text: 'Add Categories', component: 'AddCategory' },
                { text: 'Article Waiting', component: 'ArticleWait' },
                { text: 'ADMIN', component: 'AdminConsole' },
            ],
        };
    },
};
</script>

<style scoped>
.custom-container {
    width: 900px;
    height: 900px;
}
</style>
