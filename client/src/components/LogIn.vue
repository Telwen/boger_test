<template>
<div class='login'>
  <input placeholder="Enter your login" class="log-input" type="text" v-model="username" />
  <button type="button" class="login-but btn btn-primary" @click="login">
    Log in
  </button>

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
      login(username) {
        axios.post("http://localhost:5000/login", {
            'username': this.username
          })
          .then(response => {})
        localStorage.username = this.username;
        this.$router.push('todos')
      }
    }
  }
</script>

<style>
.login {
  height: 500px;
}

.log-input {
  position: relative;
  border: 2px solid rgba(73, 204, 249, 1.0);
  bottom: -80%;
  left: 45%;
}

.log-input:focus {
  outline: none;
}

.login-but {
  position: relative;
  bottom: -90%;
  left: 35%;
  color: rgba(73, 204, 249, 1.0);
  border-color: rgba(73, 204, 249, 1.0);
  background-color: transparent;
}
</style>