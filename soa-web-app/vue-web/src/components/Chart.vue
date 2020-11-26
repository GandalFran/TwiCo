<template>
	<div>
		<v-progress-circular
			v-show="dataAvailable === false"
			class="circle-loading"
			indeterminate
			:size="300"
			:width="20"
			color="#4DCCBD"
			/>
		<div v-show="dataAvailable === true" ref="chartdiv"> </div>
		<div v-show="dataAvailable === true" v-text="chartData"> </div>
	</div>
</template>

<script>
import * as am4core from "@amcharts/amcharts4/core";
import * as am4charts from "@amcharts/amcharts4/charts";
import am4themes_animated from "@amcharts/amcharts4/themes/animated";

am4core.useTheme(am4themes_animated);

export default {
	name: 'Chart',
	props: ['chartData'],
	data: function () {
		return {
			chart: null,
			isUpdated: false,
		};
	},
	methods: {
		parseData: function (data) {
			if(data === null || data === undefined){
				return null;
			}
			return data;
		},

		createChart: function (data){
			console.log('create chart')
			let chart = am4core.create(this.$refs.chartdiv, am4charts.XYChart);

			chart.paddingRight = 20;

			chart.data = data;

			let dateAxis = chart.xAxes.push(new am4charts.DateAxis());
			dateAxis.renderer.grid.template.location = 0;

			let valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
			valueAxis.tooltip.disabled = true;
			valueAxis.renderer.minWidth = 35;

			let series = chart.series.push(new am4charts.LineSeries());
			series.dataFields.dateX = "date";
			series.dataFields.valueY = "value";

			series.tooltipText = "{valueY.value}";
			chart.cursor = new am4charts.XYCursor();

			let scrollbarX = new am4charts.XYChartScrollbar();
			scrollbarX.series.push(series);
			chart.scrollbarX = scrollbarX;

			this.replaceChart(chart);
		},

		destroyChart: function() {
			if(this.chart !== null){
				this.chart.dispose();
			}
		},

		replaceChart: function(chart) {
			this.destroyChart();
			this.chart = chart;
		},
	},
	computed: {
		dataAvailable: function() {
			this.$nextTick(() => {
				const data = this.parseData(this.chartData);
				this.createChart(data);
			});
			return (this.chartData !== null && this.chartData !== undefined);
		}
	},
}
</script>

<style>
	.circle-loading {
		display: block;
		width: 100px;
		margin: 0 auto;
	}
</style>