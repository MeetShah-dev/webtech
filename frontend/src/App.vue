<script setup>
import NavBar from './components/NavBar.vue'
</script>

<template>
  <div>
    <div class="logo-img">
      <img src="../public/SH-logo.png" alt="">
    </div>
    <nav-bar></nav-bar>
  </div>
</template>

<style scoped>

/* <uniquifier>: Use a unique and descriptive class name
<weight>: Use a value from 100 to 900 */
template{
    background-color: white;
    font-family: "Inter", sans-serif;
    font-style: normal;
    font-variation-settings:
      "slnt" 0;
    font-size: 14px;
}
.logo-img{
   align-content: center;
   margin: auto;
   padding: auto;
}
.logo-img, img{
    width: 250px;
    height: 200px;

}
</style>
