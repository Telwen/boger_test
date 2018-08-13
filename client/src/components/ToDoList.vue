<template>
<div class="list-wraper">
    <v-card >
      <v-container>
          <v-flex
            xs
            class='text-xs-center'
          >
            <v-btn
              @click='del_tdl'
              small round fab flat block 
              color='red'
            >
              x
            </v-btn>
            <v-text-field
              v-model="name"
              :placeholder="todos.title"
              color='black'
            />
            <todo-input 
              @todo:add="addTodo"
            />
            <todo-item 
              v-for="todo in todos.tdl" 
              :key="todo.id"
              :todo="todo" 
              @todo:remove="removeTodo" 
            />
            <v-btn
              @click='save'
              outline
              color='blue'
            >
              Save
            </v-btn>
          </v-flex>
      </v-container>
    </v-card>
</div>
</template>

<script>
import TodoInput from './TodoInput.vue';
import TodoItem from './TodoItem.vue';
import axios from 'axios';

export default {
  name: 'to-do-list',
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
      /**
      * add entered text to users todo 
      *@text {string} text which user entered in input form
      */
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
      /**
      * send to parant deleted todo id 
      */
      del_tdl() {
        this.$emit('tdl:del', this.todos.id);
      },
      /**
      * take from the cheldren deleted todo string and remove it in variable containing local copy of users todo 
      *@id {number} id of string which need to delete
      */
      removeTodo(id) {
        let todos = this.todos.tdl;
        this.todos.tdl = todos.filter((todo) => todo.id != id);
      },
      /**
      * check if user change the todo title, if change replace it in user todo list, and send 
      * all changes to server to apply it
      */
      save() {
        if (this.name == null) {} 
        else {
          delete this.todos.title
          this.todos.title = this.name
        }
        axios.post(
          "http://localhost:5000/todos",
          this.todos,
          {
            headers:
              {'username': this.username}
          })
      }

    },
  }
</script>

<style>

.list-wraper {
  width: 400px;
  margin-bottom: 30px;
  border: 2px solid rgba(73, 204, 249, 1.0);
}

</style>

