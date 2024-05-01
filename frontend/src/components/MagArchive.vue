<template>
    <v-container align-items: center>
        <div class="archive-container">
            <div class="archive-display">
                <v-row align-content="center">
                    <v-col
                        v-for="n in 9"
                        :key="n"
                        class="d-flex child-flex"
                        cols="4"
                    >
                        <v-img
                            :src="`https://picsum.photos/500/300?image=${
                                n * 5 + 10
                            }`"
                            :lazy-src="`https://picsum.photos/10/6?image=${
                                n * 5 + 10
                            }`"
                            aspect-ratio="1"
                            class="grey lighten-2"
                        >
                            <template v-slot:placeholder>
                                <v-row
                                    class="fill-height ma-0"
                                    align="center"
                                    justify="center"
                                >
                                    <v-progress-circular
                                        indeterminate
                                        color="grey lighten-5"
                                    ></v-progress-circular>
                                </v-row>
                            </template>
                        </v-img>
                    </v-col>
                </v-row>
            </div>
        </div>
    </v-container>
</template>

<script>
export default {
    name: 'mag-archives',
    data() {},
};
</script>

<style scoped>
.archive-container {
    width: 70%;
    height: 70%;
    background-color: #ffffff;
    justify-content: center;
    align-items: center;
}
.archive-display {
    padding: 60px 0;
}
</style>
