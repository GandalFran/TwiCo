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
            {{item.i}}
        </grid-item>
    </grid-layout>
    <v-btn @click="doUpdate"> PUSH ME </v-btn>
  </div>
</template>

<script>
import Home from "@/views/Home.vue";
import Chart from "@/components/Chart.vue";
import VueGridLayout from 'vue-grid-layout';

export default {
  name: 'Dashboard',
  components: {
     GridLayout: VueGridLayout.GridLayout,
     GridItem: VueGridLayout.GridItem
  },
  data () {
    layout: [
          {"x":0,"y":0,"w":2,"h":2,"i":"0"},
          {"x":2,"y":0,"w":2,"h":4,"i":"1"},
          {"x":4,"y":0,"w":2,"h":5,"i":"2"},
          {"x":6,"y":0,"w":2,"h":3,"i":"3"},
          {"x":8,"y":0,"w":2,"h":3,"i":"4"},
          {"x":10,"y":0,"w":2,"h":3,"i":"5"},
          {"x":0,"y":5,"w":2,"h":5,"i":"6"},
          {"x":2,"y":5,"w":2,"h":5,"i":"7"},
          {"x":4,"y":5,"w":2,"h":5,"i":"8"},
          {"x":6,"y":3,"w":2,"h":4,"i":"9"},
          {"x":8,"y":4,"w":2,"h":4,"i":"10"},
          {"x":10,"y":4,"w":2,"h":4,"i":"11"},
          {"x":0,"y":10,"w":2,"h":5,"i":"12"},
          {"x":2,"y":10,"w":2,"h":5,"i":"13"},
          {"x":4,"y":8,"w":2,"h":4,"i":"14"},
          {"x":6,"y":8,"w":2,"h":4,"i":"15"},
          {"x":8,"y":10,"w":2,"h":5,"i":"16"},
          {"x":10,"y":4,"w":2,"h":2,"i":"17"},
          {"x":0,"y":9,"w":2,"h":3,"i":"18"},
          {"x":2,"y":6,"w":2,"h":2,"i":"19"}
      ],
  },
  methods: {
    doUpdate () {
      return 'asdfafds'   
    }
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