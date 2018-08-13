<template>
  <div>
    <v-layout 
      align-center 
      justify-start 
      column 
      fill-height
    >
      <v-flex xs4>
        <v-text-field
          v-model="text"
          placeholder="Type what you need to do"
          color='black'
        ></v-text-field>
        <v-btn
          @click="addTodo"
          ml-5
          color="blue"
        >
          Submit
        </v-btn>
      </v-flex>
    </v-layout>
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
    /**
    * add entered value to users todo strings
    */
    addTodo() {
      this.$emit('todo:add', this.text);
      this.text = '';
    }
  }
}
</script>
