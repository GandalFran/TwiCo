<template>
  <div class="control-section">
    <ejs-dashboardlayout id='dashboard_default' ref="dashboard" :cellSpacing="[10, 10]" :allowResizing='true' :resizableHandles="['e-south-east','e-east','e-west','e-north','e-south']" :columns="6">
      <e-panels>
        <e-panel :sizeX="1" :sizeY="1" :row="0" :col="0" content='<chart ref="chart1" :chartDataProperty="myData" > </chart>'> </e-panel>
        <e-panel :sizeX="3" :sizeY="2" :row="0" :col="1" content='<home ref="home1"> </home>'></e-panel>
        <e-panel :sizeX="1" :sizeY="3" :row="0" :col="4" :content="homeComponent"></e-panel>
        <e-panel :sizeX="1" :sizeY="1" :row="1" :col="0" :content="homeComponent"></e-panel>
        <e-panel :sizeX="2" :sizeY="1" :row="2" :col="0" :content="homeComponent"></e-panel>
        <e-panel :sizeX="1" :sizeY="1" :row="2" :col="2" :content="homeComponent"></e-panel>  
        <e-panel :sizeX="1" :sizeY="1" :row="2" :col="3" :content="homeComponent"></e-panel>  
      </e-panels>
    </ejs-dashboardlayout>
  </div>
</template>

<script>
import Home from "@/views/Home.vue";
import Chart from "@/components/Chart.vue";

export default {
  name: 'Dashboard',
  mounted () {
    this.$refs.chart1.updateData('hello');
    this.$refs.panel2.content.updateData('hello');
    this.$refs.panel3.content.updateData('hello');
    this.$refs.panel4.content.updateData('hello');
    this.$refs.panel5.content.updateData('hello');
    this.$refs.panel6.content.updateData('hello');
    this.$refs.panel7.content.updateData('hello');
  },
  methods: {
    homeComponent () {
      return { template: Chart};
    },
    homeComponent2 () {
      return { template: Home};
    },
    myData () {
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