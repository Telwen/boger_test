<template>
<div class="app">
    <div class="todo-wrapper">
      <app-header></app-header>
      <todo-input v-on:todo:add="addTodo"></todo-input>
      <todo-item  v-for="todo in todos" v-bind:todo="todo" v-on:todo:remove="removeTodo" :key="todo.id"></todo-item>
    </div>
    <button class="btn btn-primary" v-on:click="save">Save</button>
  </div>
</template>

<script>
import AppHeader from './components/AppHeader.vue';
import TodoInput from './components/TodoInput.vue';
import TodoItem from './components/TodoItem.vue';
import axios from 'axios';

export default {
  name: 'app',
  data() {
    return {
      todos: [],
      nextId: 0
    };
  },
  components: {
    AppHeader,
    TodoInput,
    TodoItem
  },
  methods: {
    addTodo(text) {
      if (text == ''){
        pass}
      else{
      this.todos.push({id: this.nextId, text: text});
      this.nextId++;}
    },
    removeTodo(id) {
      let todos = this.todos;
      this.todos= todos.filter((todo) => todo.id != id);
    },
    save() {
      axios.post("http://localhost:5000/to_do",
       this.todos
       )
      .then(response => console.log(response.data)
    )}

  },
}
</script>

<style>
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
  width: 500px;
  min-height: 600px;
  border: 5px solid rgba(73, 204, 249, 1.0);
  padding: 20px;
}
</style>
