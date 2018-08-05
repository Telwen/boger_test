<template>
<div class='tdl-holder'>
  <button class='logout btn btn-primary' @click='logout'>logout</button>
  <ToDoList v-for="todos in response" v-bind:todos='todos' :key="response.id" v-on:tdl:del="del_tdl"></ToDoList>
  <button class="add-new-tdl" v-on:click="add_new_tdl">+</button>
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
      axios.get("http://localhost:5000/todos", {
          headers: {
            'username': this.username
          }
        })
        .then(response => {
          this.response = response.data
        })
    },
    components: {
      ToDoList,
    },
    methods: {
      add_new_tdl() {
        this.response.push({
          'id': this.response.length,
          'title': 'New todo list',
          'tdl': []
        })
      },
      logout() {
        this.username = null
        localStorage.username = null
        this.$router.push('/')
      },
      del_tdl(id) {
        let todos = this.response;
        this.response = todos.filter((todo) => todo.id != id);
        console.log(id)
        axios.delete("http://localhost:5000/delete", {
          params: {
            'id': id
          },
          headers: {
            'username': this.username
          }
        })
      }
    }
  }
</script>

<style>
.logout {
  position: fixed;
  bottom: 90%;
  left: 85%;
}

.add-new-tdl {
  font-size: 100px;
  color: rgba(73, 204, 249, 1.0);
  background-image: none;
  background: transparent;
  float: left;
  background-color: transparent;
  border: medium none
}

.tdl-holder {
  height: 800px;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
  flex-wrap: wrap;
}
</style>