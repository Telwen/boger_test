<template>
  <div class="todo-input">
    <input placeholder='Type what you need to do' class="td-input" type="text" v-model="text"/>
    <button class="btn btn-primary" v-on:click="addTodo">Submit</button>
  </div>
</template>

<script>
export default {
  name: 'todo-input',
  data() {
    return {
      text: ""
    };
  },
  methods: {
    addTodo() {
      this.$emit('todo:add', this.text);
      this.text = '';
    }
  }
}
</script>


<style>
.todo-input-wrapper {
  margin-bottom: 20px;
}
.btn {
  outline: none;
  box-shadow: none;
  border-width: 2px;
  border-radius: 3px;
  border-style: solid;
  padding: 8px;
}

.btn-primary {
  color: rgba(73, 204, 249, 1.0);
  border-color: rgba(73, 204, 249, 1.0);
  background-color: transparent;
}

.td-input {
  width: 80%;
  border: none;
  border-top: 2px solid rgba(73, 204, 249, 1.0);
  border-bottom: 2px solid rgba(73, 204, 249, 1.0);
  margin-right: 10px;
  margin-bottom: 10px;
  padding: 5px;
  line-height: 17px;
  text-align:center;
}

.td-input:focus {
  outline: none;
  border: none;
  border-top: 2px solid rgba(73, 204, 249, 1.0);
  border-bottom: 2px solid rgba(73, 204, 249, 1.0);
}
</style>