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

            <v-container>
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
import ArticleApprove from './ArticleApprove.vue';
import ArticleReject from './ArticleReject.vue';
import ArticleCreation from './ArticleCreation.vue';
import MagazineCreation from './MagazineCreation.vue';
import ArticleList from './ArticleList.vue';
import ArticleWait from './ArticleWait.vue';
import ScheduleSet from './ScheduleSet.vue';
import RescheduleSet from './RescheduleSet.vue';
import FeedbackApp from './FeedbackApp.vue';

export default {
    components: {
        ArticleApprove,
        ArticleReject,
        ArticleCreation,
        MagazineCreation,
        ArticleList,
        ArticleWait,
        ScheduleSet,
        RescheduleSet,
        FeedbackApp,
    },
    data() {
        return {
            tab: null,
            links: [
                { text: 'Create Article', component: 'ArticleCreation' },
                { text: 'Create Magazine', component: 'MagazineCreation' },
                { text: 'View Article(s)', component: 'ArticleList' },
                { text: 'Add Categories', component: '' },
                { text: 'Create a Feedback', component: 'FeedbackApp' },
                { text: 'New Article to Check', component: 'ArticleWait' },
                { text: 'Approved Article', component: 'ArticleApprove' },
                { text: 'Rejected Articles', component: 'ArticleReject' },
                { text: 'Schedule Magazine', component: 'ScheduleSet' },
                { text: 'Reschedule Magazine', component: 'RescheduleSet' },
            ],
        };
    },
};
</script>

<style scoped></style>
