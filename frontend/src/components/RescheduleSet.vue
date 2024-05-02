<template>
    <main class="editing">
        <v-container>
            <h2>Reschedule a Magazine</h2>
            <div class="scheduling-form">
                <v-form ref="form" v-model="valid" lazy-validation>
                    <v-select
                        v-model="selectedMagazine"
                        :items="magazines"
                        label="Scheduled Magazine(s)"
                    ></v-select>
                    <v-text-field
                        v-model="mag_id"
                        label="Magazine ID"
                    ></v-text-field>
                    <v-text-field
                        v-model="mag_title"
                        label="Magazine Title"
                    ></v-text-field>
                    <v-row>
                        <v-col cols="12" sm="6">
                            <v-menu
                                v-model="datePicker"
                                :close-on-content-click="false"
                                :nudge-right="40"
                                transition="scale-transition"
                                offset-y
                            >
                                <template v-slot:activator="{ on }">
                                    <v-text-field
                                        v-model="selectedDate"
                                        label="Date"
                                        readonly
                                        v-on="on"
                                    ></v-text-field>
                                </template>
                                <v-date-picker
                                    v-model="selectedDate"
                                    no-title
                                    scrollable
                                ></v-date-picker>
                            </v-menu>
                        </v-col>
                        <v-col cols="12" sm="6">
                            <v-select
                                v-model="selectedTime"
                                :items="timeOptions"
                                label="Time"
                            ></v-select>
                        </v-col>
                    </v-row>
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
            selectedMagazine: null,
            selectedDate: null,
            selectedTime: null,
            magazines: ['Magazine A', 'Magazine B', 'Magazine C', 'Magazine D'],
            timeOptions: [
                '08:00 AM',
                '09:00 AM',
                '10:00 AM',
                '11:00 AM',
                '12:00 PM',
                '01:00 PM',
                '02:00 PM',
                '03:00 PM',
            ],
            datePicker: false,
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

<style scoped>
.scheduling-form {
    max-width: 600px; /* Adjust as needed */
    margin: auto;
}
</style>
