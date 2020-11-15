<template>
  <div class="theBackground">
    <v-toolbar
      dense
      floating
    >

      <v-btn 
        :loading="loadingDashboard"
        :disabled="loadingDashboard"
        @click="reloadButton"
      >
        Reload dashboard
      </v-btn>

      <v-btn
        @click="logout"
      >
        Logout
      </v-btn>

    </v-toolbar>
     <grid-layout
        :layout.sync="layout"
        :col-num="10"
        :row-height="10"
        :is-draggable="false"
        :is-resizable="false"
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
            <covid-chart v-if="item.chartType == 'covid'" :covidData="covidData" > </covid-chart>
            <chart v-if="item.chartType == 'twitter'" :chartData="twitterData" > </chart>
        </grid-item>
    </grid-layout>
  </div>
</template>

<script>
import axios from "axios";
import Chart from "@/components/Chart.vue";
import CovidChart from "@/components/CovidChart.vue";
import VueGridLayout from 'vue-grid-layout';

export default {
  name: 'Dashboard',
  components: {
     'chart':Chart,
     CovidChart,
     GridLayout: VueGridLayout.GridLayout,
     GridItem: VueGridLayout.GridItem
  },
  data () {
    return{
      loadingDashboard: false,
      baseUrl: "https://soa.servehttp.com",
      covidData: null,
      twitterData: null,
      layout: [
            {"x":0,"y":0,"w":5,"h":20,"i":"0", "chartType": "covid"},
            {"x":5,"y":0,"w":5,"h":20,"i":"1", "chartType": "twitter"},
      ],
    }
  },
  methods: {
    logout: function () {
      window.location = this.baseUrl + "/auth/google/logout";
    },
    checkAuth: function (){
      const uri = this.baseUrl + "/auth/check";
      axios.post(uri, {}).then(response => {
          const isLoggedIn = response.data.auth;
          if(isLoggedIn === false){
            this.$router.push('forbidden');
          }
        }).catch(e => { console.log(e); });
    },
    reloadCovidData: function (){
      const uri = this.baseUrl + "/data/covid";
      axios.post(uri, {}).then(response => {
          const data = response.data;
          this.covidData = data;
      }).catch(e => { console.log(e); });
    },
    reloadTwitterData: function (){
      const uri = this.baseUrl + "/data/twitter";
      axios.post(uri, {}).then(response => {
          const data = response.data;
          this.twitterData = data;
      }).catch(e => { console.log(e); });
    },
    reloadDashBoard: function () {
      this.reloadCovidData();
      this.reloadTwitterData();
    },
    reloadButton: function (){
      this.loadingDashboard=true;
      this.reloadDashBoard();
      this.loadingDashboard=false;
    }
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