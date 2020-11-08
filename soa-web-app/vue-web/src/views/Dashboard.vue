<template>
  <div class="theBackground">
     <grid-layout
        :layout.sync="layout"
        :col-num="4"
        :row-height="30"
        :is-draggable="false"
        :is-resizable="true"
        :is-mirrored="false"
        :vertical-compact="true"
        :margin="[10, 10]"
        :use-css-transforms="true"
    >

        <grid-item v-for="item in layout"
                   :x="item.x"
                   :y="item.y"
                   :w="item.w"
                   :h="item.h"
                   :i="item.i"
                   :key="item.i">
            <chart :chartData="chartData" > </chart>
        </grid-item>
    </grid-layout>
  </div>
</template>

<script>
import axios from "axios";
import Chart from "@/components/Chart.vue";
import VueGridLayout from 'vue-grid-layout';

export default {
  name: 'Dashboard',
  components: {
     'chart':Chart,
     GridLayout: VueGridLayout.GridLayout,
     GridItem: VueGridLayout.GridItem
  },
  data () {
    return{
      baseUrl: "https://soa.servehttp.com",
      chartData: null,
      layout: [
            {"x":0,"y":0,"w":2,"h":4,"i":"0"},
            {"x":2,"y":0,"w":2,"h":8,"i":"1"},
      ],
    }
  },
  methods: {
    logout() {
      window.location = this.baseUrl + "/auth/google/logout";
    },
    checkAuth(){
      const uri = this.baseUrl + "/auth/check";
      axios.post(uri, {}).then(response => {
          const isLoggedIn = response.data.auth;
          if(isLoggedIn === false){
            this.$router.push('forbidden');
          }
        }).catch(e => { console.log(e); });
    },
    reloadDashBoard () {
      const uri = this.baseUrl + "/data/covid";
      axios.post(uri, {}).then(response => {
          const data = response.data;
          this.chartData = data;
      }).catch(e => { console.log(e); });
    },
  },
  created: function() {
    this.checkAuth();
    this.reloadDashBoard();
  }
}
</script>

<style>

.theBackground {
  background: #66ccff
}
</style>