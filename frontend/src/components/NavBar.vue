<template>

<!-- START NAVIGATION BAR -->
    <div class="nav">
        <!-- This is a static menu used for testing purpose -->
        <!-- <ul>
            <li v-for="nav in navItems" :key="nav">
                {{ nav }}
            </li>
        </ul> -->
        
        
        <!-- This is the dynamic navigation bar that we can later on modify depending on the visibility users are to have -->

        <ul>
            <li v-for="item in items" :key="item">
                {{ item }}
            </li>
        </ul>

    </div>

<!-- END NAVIGATION BAR -->
</template>

<script>
import nav from '../../src/navbar.json'
export default{
    data(){
        return{
            navItems:['Home', 'Category', 'User', 'Notification'],
            items:[],
        }
    },
    created(){
        let arr=Object.entries(nav)
        console.log(arr)
        for(let i = 0; i < arr.length; i++){
            this.items.push(arr[i][1].item)
        }

        console.log(this.items)
    }
}

</script>


<style scoped>

.nav{
    background-color: #114C6E;
    color: white;
    overflow: hidden;
}

li{
    display: inline;
    width: 100px;
    height: fit-content;
    padding: 10px;
    margin: 5px;
    align-content: center;
}

li:hover{
    cursor: pointer;
    background: white;
    color: black;
}
</style>