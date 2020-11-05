<template>
  <div>
     <grid-layout
        :layout.sync="layout"
        :col-num="4"
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
            <chart :chartData="chartData" > </chart>
        </grid-item>
    </grid-layout>
  </div>
</template>

<script>
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
      chartData: null,
      layout: [
            {"x":0,"y":0,"w":2,"h":4,"i":"0"},
            {"x":2,"y":0,"w":2,"h":8,"i":"1"},
      ],
    }
  },
  methods: {
    doRequest () {
      return {message: 'holawo'};
    }
  },
  created: function() {
    const response = this.doRequest();
    this.chartData = response;
  }
}
</script>