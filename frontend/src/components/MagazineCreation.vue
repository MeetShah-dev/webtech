<script>
import axios from 'axios';
 
export default {
    data() {
        return {
            valid: true,
            mag_title: '',
            article_num: null,
            mag_month: '',
            mag_day: '',
            mag_year: '',
            mag_hour: '',
            mag_minute: '',
            mag_second: '',
        };
    },
 
    methods: {
        async submitForm() { 
            try {
                const data = {
                    title: this.mag_title,
                    year: parseInt(this.mag_year),
                    month: parseInt(this.mag_month),
                    date: parseInt(this.mag_day),
                    hour: parseInt(this.mag_hour),
                    minute: parseInt(this.mag_minute),
                    second: parseInt(this.mag_second),
                };
                console.log(data)
                const response = await axios.post(
                    'http://3.93.17.199:3028/schedule_magazine',
                    data
                );
                console.log('Response:', response.data);
            } catch (error) {
                console.error('Error:', error);
            }
        },
    },
 
    computed: {
        monthRule() {
            return [
                (v) => !!v || 'Month is required',
                (v) =>
                    (parseInt(v) > 0 && parseInt(v) <= 12) ||
                    'Invalid month (1-12)',
            ];
        },
        dayRule() {
            return [
                (v) => !!v || 'Day is required',
                (v) =>
                    (parseInt(v) > 0 && parseInt(v) <= 31) ||
                    'Invalid day (1-31)',
            ];
        },
        yearRule() {
            const currentYear = new Date().getFullYear();
            return [
                (v) => !!v || 'Year is required',
                (v) =>
                    parseInt(v) >= currentYear ||
                    'Year must be current year or later',
            ];
        },
        hourRule() {
            return [
                (v) => !!v || 'Hour is required',
                (v) =>
                    (parseInt(v) >= 0 && parseInt(v) <= 23) ||
                    'Invalid hour time (0-23)',
            ];
        },
        minuteRule() {
            return [
                (v) => !!v || 'Minutes is required',
                (v) =>
                    (parseInt(v) >= 0 && parseInt(v) <= 59) ||
                    'Invalid minute time (0-59)',
            ];
        },
        secondRule() {
            return [
                (v) => !!v || 'Seconds is required',
                (v) =>
                    (parseInt(v) >= 0 && parseInt(v) <= 59) ||
                    'Invalid seconds time (0-59)',
            ];
        },
    },
};
</script>
 
<template>
    <main class="editing">
        <v-container>
            <h2>Create a Magazine</h2>
            <div class="article-form">
                <v-form ref="form" v-model="valid" lazy-validation>
                    <v-text-field
                        label="Magazine title"
                        v-model="mag_title"
                        required
                    ></v-text-field>
                    <v-row>
                        <v-col cols="12" sm="4">
                            <v-text-field
                                label="Day"
                                v-model="mag_day"
                                required
                                :rules="dayRule"
                            ></v-text-field>
                        </v-col>
                        <v-col cols="12" sm="4">
                            <v-text-field
                                label="Month"
                                v-model="mag_month"
                                required
                                :rules="monthRule"
                            ></v-text-field>
                        </v-col>
                        <v-col cols="12" sm="4">
                            <v-text-field
                                label="Year"
                                v-model="mag_year"
                                required
                                :rules="yearRule"
                            ></v-text-field>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="12" sm="4">
                            <v-text-field
                                label="Hour"
                                v-model="mag_hour"
                                :rules="hourRule"
                            ></v-text-field>
                        </v-col>
                        <v-col cols="12" sm="4">
                            <v-text-field
                                label="Minute"
                                v-model="mag_minute"
                                :rules="minuteRule"
                            ></v-text-field>
                        </v-col>
                        <v-col cols="12" sm="4">
                            <v-text-field
                                label="Second"
                                v-model="mag_second"
                                :rules="secondRule"
                            ></v-text-field>
                        </v-col>
                    </v-row>
                    <v-btn class="primary" @click="submitForm">Submit</v-btn>
                </v-form>
            </div>
        </v-container>
    </main>
</template>
 