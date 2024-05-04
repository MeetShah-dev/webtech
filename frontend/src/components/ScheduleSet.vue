<template>
    <main class="editing">
        <v-container>
            <h2>Create a Schedule</h2>
            <div class="scheduling-form">
                <v-form ref="form" v-model="valid" lazy-validation>
                    <v-text-field
                        label="Magazine ID"
                        v-model="mag_id"
                    ></v-text-field>
                    <v-text-field
                        label="Magazine Title"
                        v-model="mag_title"
                    ></v-text-field>

                    <!-- Date Picker for Day, Month, Year -->
                    <v-row>
                        <v-col cols="4">
                            <v-menu
                                v-model="dayPicker"
                                :close-on-content-click="false"
                                transition="scale-transition"
                                offset-y
                            >
                                <template v-slot:activator="{ on }">
                                    <v-text-field
                                        v-model="selectedDay"
                                        label="Day"
                                        readonly
                                        v-on="on"
                                    ></v-text-field>
                                </template>
                                <v-date-picker
                                    v-model="selectedDay"
                                ></v-date-picker>
                            </v-menu>
                        </v-col>
                        <v-col cols="4">
                            <v-select
                                v-model="selectedMonth"
                                :items="items_m"
                                label="Month"
                            ></v-select>
                        </v-col>
                        <v-col cols="4">
                            <v-select
                                v-model="selectedYear"
                                :items="items_y"
                                label="Year"
                            ></v-select>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="4">
                            <v-select
                                v-model="selectedHour"
                                :items="items_h"
                                label="Hour"
                            ></v-select>
                        </v-col>
                        <v-col cols="4">
                            <v-select
                                v-model="selectedMinutes"
                                :items="items_ms"
                                label="Minutes"
                            ></v-select>
                        </v-col>
                        <v-col cols="4">
                            <v-select
                                v-model="selectedSeconds"
                                :items="items_s"
                                label="Seconds"
                            ></v-select>
                        </v-col>
                    </v-row>
                    <v-row
                        ><v-btn class="primary">schedule magazine</v-btn></v-row
                    >
                </v-form>
            </div>
        </v-container>
    </main>
</template>

<script>
export default {
    data() {
        return {
            valid: true,
            mag_id: '',
            mag_title: '',
            selectedDay: null,
            selectedMonth: null,
            selectedYear: null,
            selectedHour: null,
            selectedMinutes: null,
            selectedSeconds: null,
            items_d: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
            items_m: [
                'January',
                'February',
                'March',
                'April',
                'May',
                'June',
                'July',
                'August',
                'September',
                'October',
                'November',
                'December',
            ],
            items_y: ['2022', '2023', '2024'],
            items_h: Array.from({ length: 24 }, (_, i) => `${i}`),
            items_ms: Array.from({ length: 60 }, (_, i) => `${i}`),
            items_s: Array.from({ length: 60 }, (_, i) => `${i}`),
            dayPicker: false,
        };
    },
    methods: {
        validate() {
            this.$refs.form.validate();
        },
        reset() {
            this.$refs.form.reset();
        },
        resetValidation() {
            this.$refs.form.resetValidation();
        },
    },
};
</script>

<style scoped></style>
