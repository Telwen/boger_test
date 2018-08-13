<template>
  <div>
    <v-app>
      <v-layout align-center>
        <v-flex
          xs4 class='text-xs-center'
          offset-xs4 >
          <v-text-field
            placeholder="Enter your login"
            v-model.trim="username"
          ></v-text-field>
          <v-btn
            outline
            color='blue'
            @click="login"
          >
            Log in
          </v-btn>
        </v-flex>
      </v-layout>
    </v-app>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'loginApp',
    data() {
      return {
        username: ''
      }
    },
    methods: {
      /**
        * take username from input and uisng axios send it to server to check if user exist, add current username
        * to local storage, redirects to users todos page
        *  
        * @username {string} entered username
        */
      login(username) {
        axios.post(
          "http://localhost:5000/login",
          {
            'username': this.username
          }
          ).then(response => {})
        localStorage.username = this.username;
        this.$router.push('todos')
      }
    }
  }
</script>