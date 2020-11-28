import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify';
import Mapbox from "mapbox-gl";
import VueMapbox from "vue-mapbox";


Vue.config.productionTip = false

new Vue({
	router,
	vuetify,
	render: h => h(App)
}).$mount('#app')

Vue.use(VueMapbox, { mapboxgl: Mapbox });