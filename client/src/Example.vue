<template>
<div class='tdl-holder'>
    <ToDoList v-for="todos in response" v-bind:todos='todos' :key="response.id" v-on:tdl:del="del_tdl"></ToDoList>
    <button class="add-new-tdl" v-on:click="add_new_tdl">+</button>
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
        add_new_tdl() {
            this.response.push(
                {
                    'id': this.response.length,
                    'title': 'New todo list',
                    'tdl': []
                }
                )
        },
        del_tdl(id){
            let todos = this.response;
            this.response = todos.filter((todo) => todo.id != id);
            axios.post("http://localhost:5000/delete", this.response)
                }
                }
            }

</script>

<style>
    .add-new-tdl {
        font-size: 100px;
        color: rgba(73, 204, 249, 1.0);
        background-image: none; 
        background: transparent;
        float: left;
        background-color: transparent;
        border: medium none
    }
    
    .tdl-holder{
        display : flex;
        flex-direction: row;
        justify-content: space-around; 
        align-items: center;
        flex-wrap: wrap;
    }

</style>