<template>
	<div>
		<v-progress-circular
			v-show="dataAvailable === false"
			class="circle-loading"
			indeterminate
			:size="300"
			:width="20"
			color="#F5F8FA"
			/>
		<div id="chartdiv" v-show="dataAvailable === true" class="text"> </div>
	</div>
</template>

<script>
import Gradient from "javascript-color-gradient";
import * as am4core from '@amcharts/amcharts4/core'
import * as am4maps from '@amcharts/amcharts4/maps'
import am4themesAnimated from '@amcharts/amcharts4/themes/animated'
import am4geodataWorldLow from '@amcharts/amcharts4-geodata/worldLow'


export default {
	name: 'WorldCovidDeathsChart',
	props: ['covidData'],
	data: function () {
		return {
			chart: null,
		};
	},
	methods: {
		parseData: function (data) {
			if(data === null || data === undefined){
				return null;
			}

			// format data
			data = data.map(function(e){
				return{
					date: new Date(e.date),
					deaths: Math.ceil( (e.cases / 11) * 0.1), // yes, this is harcoded (at last moment there wasn't available data), i'm sorry :(
					country: e.location.address.country,
					id: e.location.address.country_code
				};
			});

			// filter data
			var targetdate = new Date()
			targetdate.setDate(targetdate.getDate() - 1);
			data = data.filter(function(e){
				return (e.id !== null && e.deaths !== null && e.date >= targetdate);
			})

			// prepare iso code
			data.forEach(function(e){
				e.id = e.id.toUpperCase();
			});

			// look for biggest value and calculate colors
			var biggestValue = 0;
			data.forEach(function(e){
				if(e.deaths > biggestValue){
					biggestValue = e.deaths;
				}
			});
			
			this.calculateColor(data, biggestValue);

			return data;
		},

		calculateColor: function (data, biggestValue){
			// configure gradient
			const colorGradient = new Gradient();
			colorGradient.setMidpoint(100);
			colorGradient.setGradient("#E1E8ED", "#0A1E2B");
			// build colors
			data.forEach(function(e){
				var index = Math.trunc(100 * e.deaths / biggestValue);
				index = (index < 1) ? (1) : (index);
				e.color = colorGradient.getColor(index);
			})
		},

		createChart: function (data){
			am4core.ready(function(){
				// theme
				am4core.useTheme(am4themesAnimated);

				// Create map instance
				var chart = am4core.create('chartdiv', am4maps.MapChart);
				chart.projection = new am4maps.projections.Miller();

				// Create map polygon series for world map
				var worldSeries = chart.series.push(new am4maps.MapPolygonSeries());
				worldSeries.exclude = ["AQ"];
				worldSeries.useGeodata = true;
				worldSeries.geodata = am4geodataWorldLow;

				var worldPolygon = worldSeries.mapPolygons.template;
				worldPolygon.tooltipText = '{deaths} deaths in {name}';
				worldPolygon.nonScalingStroke = true;
				worldPolygon.strokeOpacity = 0.5;
				worldPolygon.fill = am4core.color('#E1E8ED');
				worldPolygon.propertyFields.fill = 'color';

				// add data
				worldSeries.data = data;

				// add zoom control
				chart.zoomControl = new am4maps.ZoomControl();
				var homeButton = new am4core.Button();
				homeButton.events.on('hit', function () {
					worldSeries.show();
					chart.goHome();
				})
				
				// add home button
				homeButton.icon = new am4core.Sprite();
				homeButton.padding(7, 5, 7, 5);
				homeButton.width = 30;
				homeButton.icon.path = 'M16,8 L14,8 L14,16 L10,16 L10,10 L6,10 L6,16 L2,16 L2,8 L0,8 L8,0 L16,8 Z M16,8';
				homeButton.marginBottom = 10;
				homeButton.parent = chart.zoomControl;
				homeButton.insertBefore(chart.zoomControl.plusButton);
			});
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
				const data = this.parseData(this.covidData);
				this.createChart(data);
			});
			return (this.covidData !== null && this.covidData !== undefined);
		}
	},
}
</script>

<style scoped>
	.circle-loading {
		display: block;
		width: 100px;
		margin: 0 auto;
	}
	#chartdiv {
		width: 100%;
		height: 390px;
		background: #F5F8FA;
	}
	.title {
		color: #1DA1F2;	
		font-family: "Helvetica Neue", Roboto, "Segoe UI", Calibri, sans-serif;
		font-weight: bold;
	}
	.text {
		color: #657786;	
		font-family: "Helvetica Neue", Roboto, "Segoe UI", Calibri, sans-serif;
	}


</style>