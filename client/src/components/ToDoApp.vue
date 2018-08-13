<template>
<div class='tdl-holder'>
  <v-layout 
    align-end 
    justify-end 
    row
  >
    <v-btn
      outline right 
      color='blue'
      @click='logout'>Log out
    </v-btn>
  </v-layout
  <v-container 
    grid-list-md 
    text-xs-center 
  >
    <v-layout 
      align-center  
      justify-space-around 
      row 
      wrap 
      fill-height 
      grid-list-{xl}
    >
      <to-do-list
        v-for="todos in response" 
        :key="response.id" 
        :todos='todos' 
        @tdl:del="del_tdl"
        mt-5 
      />
      <v-btn
        @click='add_new_tdl'
        color='blue'
        large fab 
      >
        +
      </v-btn>
    </v-layout>
  </v-container>
</div>
</template>

<script>
import ToDoList from './ToDoList.vue';
import axios from 'axios';


export default {
  name: 'App',
    data() {
      return {
        username: localStorage.username,
        response: [],
      }
    },
    mounted() {
      if (localStorage.username) {
        this.username = localStorage.username;
      }
    },
    created() {
      axios.get(
        "http://localhost:5000/todos",
        {
          headers:
           {'username': this.username}
        }).then(response => 
        {
          this.response = response.data
        })
    },
    components: {
      ToDoList,
    },
    methods: {
      /**
        * add to current todo list new one 
        */
      add_new_tdl() {
        this.response.push(
          {
            'id': this.response.length,
            'title': 'New todo list',
            'tdl': []
          })
      },
      /**
        * delete current username from local storage and redirect to login page  
        */
      logout() {
        this.username = null
        localStorage.username = null
        this.$router.push('/')
      },
      /**
        * take from children element todo if and remove if from local var and server
        *
        *@id {number} removable todo id
        */
      del_tdl(id) {
        let todos = this.response;
        this.response = todos.filter((todo) => todo.id != id);
        axios.delete(
          "http://localhost:5000/todos/", {
          params: 
            {'id': id},
          headers: 
            {'username': this.username}
        })
      }
    }
  }
</script>
