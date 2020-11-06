import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify';
import VueParticles from 'vue-particles'


Vue.config.productionTip = false


new Vue({
  router,
  vuetify,
  VueParticles,
  render: h => h(App)
}).$mount('#app')