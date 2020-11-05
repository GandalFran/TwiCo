<template>
  <div class="control-section">
     <grid-layout
        :layout.sync="layout"
        :col-num="12"
        :row-height="30"
        :is-draggable="true"
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
            <chart :ref="item.chartRef" :chartData="chartData" > </chart>
        </grid-item>
    </grid-layout>
    <v-btn @click="doUpdate"> PUSH ME </v-btn>
  </div>
</template>

<script>
import Chart from "@/components/Chart.vue";
import VueGridLayout from 'vue-grid-layout';

export default {
  name: 'Dashboard',
  components: {
     Chart,
     GridLayout: VueGridLayout.GridLayout,
     GridItem: VueGridLayout.GridItem
  },
  data () {
    return{
      layout: [
            {"x":0,"y":0,"w":2,"h":2,"i":"0", "chartRef": "chartRef1"},
            {"x":2,"y":0,"w":2,"h":4,"i":"1", "chartRef": "chartRef2"},
      ],
      chartData: {}
    }
  },
  methods: {
    doRequest () {
      return {message: 'holitas'};
    }
  },
  created: function() {
    const data = this.doRequest();
    this.chartData = data;
  }
}
</script>

<style>
@import "../../node_modules/@syncfusion/ej2-base/styles/material.css";
@import "../../node_modules/@syncfusion/ej2-vue-layouts/styles/material.css";

#dashboard_default .e-panel .e-panel-container .content {
  vertical-align: middle;
  font-weight: 600;
  font-size: 20px;
  text-align: center;
  line-height: 80px;
}
</style>