import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify';
import { DashboardLayoutPlugin } from "@syncfusion/ej2-vue-layouts";

Vue.config.productionTip = false

Vue.use(DashboardLayoutPlugin);

new Vue({
  router,
  vuetify,
  DashboardLayoutPlugin,
  render: h => h(App)
}).$mount('#app')