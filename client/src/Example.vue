<template>
<div class='tdl-holder'>
    <ToDoList v-for="todos in response" v-bind:todos='todos' :key="response.id"></ToDoList>
</div>

</template>

<script>
import ToDoList from './ToDoList.vue';
import axios from 'axios';


export default {
    name: 'example',
    data: () => ({
        response: []
    }),
    created() {
        axios.get("http://localhost:5000/to_do").then(response => {this.response = response.data})
        //console.log(this.response, 'here')
        //return {
            //response: response
        //};
    },
    components: {
        ToDoList
    },
    methods: {

    },
}

</script>

<style>
    .tdl-holder{
        display : flex;
        flex-direction: row;
        justify-content: space-around; 
        align-items: center;
        flex-wrap: wrap;
    }

</style>