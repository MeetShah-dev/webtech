<template>  
  <div>  
     <h2>{{msg}}</h2>  
     <smart-list-box :data-source.prop="items">  
     </smart-list-box>  
  </div>  
</template>  
<script>  
import 'smart-webcomponents/source/modules/smart.listbox.js';
import 'smart-webcomponents/source/styles/smart.default.css';
export default {  
name: 'HelloWorld',  
props: {  
 msg: String,  
 items: Array  
}  
}  
</script>  


<!-- Add "scoped" attribute to limit CSS to this component only -->  
<style scoped>  
h3 {  
margin: 40px 0 0;  
}  
ul {  
list-style-type: none;  
padding: 0;  
}  
li {  
display: inline-block;  
margin: 0 10px;  
}  
a {  
color: #42b983;  
}  
</style>  