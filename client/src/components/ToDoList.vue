<template>
<div class="app">
  <div class="todo-wrapper">
    <button class='delete-button' v-on:click="del_tdl">x</button>
    <input :placeholder="todos.title" class="tdl-name" type="text" v-model="name" />
    <todo-input v-on:todo:add="addTodo"></todo-input>
    <todo-item v-for="todo in todos.tdl" v-bind:todo="todo" v-on:todo:remove="removeTodo" :key="todo.id"></todo-item>
  </div>
  <button class="btn btn-primary" v-on:click="save">Save</button>
</div>
</template>

<script>
import TodoInput from './TodoInput.vue';
import TodoItem from './TodoItem.vue';
import axios from 'axios';

export default {
  name: 'td-list',
    props: ['todos'],
    data() {
      return {
        name: ''
      }
    },
    components: {
      TodoInput,
      TodoItem
    },
    mounted() {
      if (localStorage.username) {
        this.username = localStorage.username;
      }
    },
    methods: {
      addTodo(text) {
        if (text == '') {
          pass
        } else {
          this.todos.tdl.push({
            id: this.todos.tdl.length,
            text: text
          })
        }
      },
      del_tdl() {
        this.$emit('tdl:del', this.todos.id);
      },
      removeTodo(id) {
        let todos = this.todos.tdl;
        this.todos.tdl = todos.filter((todo) => todo.id != id);
      },
      save() {
        console.log(this.username)
        if (this.name == null) {} else {
          delete this.todos.title
          this.todos.title = this.name
        }
        axios.post("http://localhost:5000/to_do", this.todos, {
          headers: {
            'username': this.username
          }
        })
      }

    },
  }
</script>

<style>
.delete-button {
  position: relative;
  top: -15px;
  right: -330px;
  margin-right: 2px;
  font-size: 25px;
  color: rgba(203, 20, 32, 0.4);
  background-image: none;
  background: transparent;
  float: left;
  background-color: transparent;
  border: medium none
}

.tdl-name {
  border: none;
  border-bottom: 2px solid rgba(73, 204, 249, 1.0);
  margin-bottom: 10px;
  text-align: center;
}

.tdl-name:focus {
  outline: none;
  border: none;
  border-bottom: 2px solid rgba(73, 204, 249, 1.0);
}

.app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.todo-wrapper {
  margin: 20px auto 20px auto;
  width: 400px;
  min-height: 600px;
  border: 5px solid rgba(73, 204, 249, 1.0);
  padding: 20px;
}
</style>
