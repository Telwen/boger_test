import Vue from 'vue'
import LoginApp from './components/Login.vue'
import App from './App.vue'
import ToDoApp from './components/ToDoApp.vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter);

const routes = [
   { path:'/todos', component: ToDoApp},
   { path:'/', component: LoginApp}
];

const router = new VueRouter({
  routes: routes
})
new Vue({
  el: '#app',
  router: router,
  render: h => h(App)
})
