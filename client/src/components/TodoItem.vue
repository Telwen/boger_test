<template>
<div style='border-bottom: 1px solid black'>
  <v-layout>
    <v-btn
      @click="removeTodo"
      color="red lighten-1"
    >
      Remove
    </v-btn>
    <p style='font-size: 20px; margin-top: 11px'
    >
      {{todo.text}}
    </p>
  </v-layout>
</div>

</template>

<script>
export default {
  name: 'todo-item',
    props: ['todo'],
    methods: {
      /**
      * send to parent todo string id which need to delete  
      */
      removeTodo() {
        this.$emit('todo:remove', this.todo.id);
      }
    }
  }
</script>
