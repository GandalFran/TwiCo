<template>
	<div>
		<div v-show="dataAvailable === true" id="chartdiv_sentiment" class="text"> </div>
	</div>
</template>

<script>
import * as am4core from "@amcharts/amcharts4/core";
import * as am4charts from "@amcharts/amcharts4/charts";
import am4themes_animated from "@amcharts/amcharts4/themes/animated";

export default {
	name: 'SentimentChart',
	props: ['chartData'],
	data: function () {
		return {
			chart: null,
			data: null,
		};
	},
	methods: {

		parseData: function (data) {
			if(data === null || data === undefined){
				return null;
			}

			const elementsBySentiment = {
				positive: 0,
				negative: 0,
				neutral: 0,
			};

			data.forEach(function(e){
				switch(e.sentiment){
				case 'positive':
					elementsBySentiment.positive++;
					break;
				case 'negative':
					elementsBySentiment.negative++;
					break;
				case 'neutral':
					elementsBySentiment.neutral++;
					break;
				}
			});

			const colors = {
				positive: '#6bff77',
				neutral: '#6ba4ff',
				negative: '#ff726b',
			};

			const parsed = Object.keys(elementsBySentiment).map(function(e){
				return {
					name: e,
					color: colors[e],
					value: elementsBySentiment[e],
				}
			});

			return parsed;
		},

		createChart: function (data){

			am4core.ready(function(){
				am4core.useTheme(am4themes_animated);

				let chart = am4core.create("chartdiv_sentiment", am4charts.PieChart);

				chart.innerRadius = am4core.percent(50);
				chart.data = data;

				// Add and configure Series
				let pieSeries = chart.series.push(new am4charts.PieSeries());
				pieSeries.dataFields.value = "value";
				pieSeries.dataFields.category = "name";
				pieSeries.slices.template.strokeWidth = 2;
				pieSeries.slices.template.strokeOpacity = 1;
				pieSeries.slices.template.propertyFields.fill = 'color'
				
				// This creates initial animation
				pieSeries.hiddenState.properties.opacity = 1;
				pieSeries.hiddenState.properties.endAngle = -90;
				pieSeries.hiddenState.properties.startAngle = -90;

			});
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

	#chartdiv_sentiment {
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