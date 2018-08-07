<template>
  <div>
    <v-layout align-center justify-start column fill-height>
      <v-flex xs4>
        <v-text-field
          placeholder="Type what you need to do"
          v-model="text"
          color='black'
        ></v-text-field>
        <v-btn
          ml-5
          color="blue"
          @click="addTodo">
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
