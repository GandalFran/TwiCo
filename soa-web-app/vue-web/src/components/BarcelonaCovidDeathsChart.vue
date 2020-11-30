<template>
	<v-container class="map_box_container" >
		<v-progress-circular
			v-if="dataAvailable === false"
			class="circle-loading"
			indeterminate
			:size="300"
			:width="20"
			color="#F5F8FA"
			/>
		<mgl-map id="map" ref="map" v-if="dataAvailable === true"
			:accessToken="accessToken"
			:mapStyle.sync="mapStyle"
			:sourceId="sourceId"
			:source="geoJsonMapData"
			:zoom="initialZoom"
			:maxzoom="initialZoom"
			:center="initialCoordinates"
			>
			<mgl-geojson-layer
				:layerId="layerId"
				:layer="layerProps"
				:sourceId="sourceId"
				:source="geoJsonMapData"
			/>
		</mgl-map>
	</v-container>
</template>

<script>
import Mapbox from "mapbox-gl";
import Gradient from "javascript-color-gradient";
import { MglMap, MglGeojsonLayer } from "vue-mapbox";

export default {
	name: 'BarcelonaCovidDeathsChart',
	props: ['covidData', 'initialZoom', 'initialCoordinates'],
	components: {
		MglMap,
		MglGeojsonLayer,
	},
	data: function () {
		return {
			mapbox: Mapbox,
			isUpdated: false,
			geojsonSeries: [],
			layerId: "myLayerId",
			sourceId: "mySourceId",
			mapStyle: 'mapbox://styles/mapbox/streets-v10',
			accessToken: "pk.eyJ1IjoiZ2FuZGFsZnJhbiIsImEiOiJja2hmOGcwaXUwbmc2Mnludjg1ejl6MHFxIn0.kBKAiWYbkEFFnJupLTooNQ",
		};
	},
	created: function (){
		this.mapbox = Mapbox;
	},
	methods: {

		seriesToGeoJson(data){
			return{
				type: "FeatureCollection",
				features: data.map(function(e){
					return {
						type: 'Feature',
						properties: {
							date: e.date,
							deaths: e.deaths
						},
						geometry: {
							type: 'Point',
							coordinates: [
								e.lon,
								e.lat
							]
						}
					}
				})
			}
		},

		parseData: function (data) {
			if(data === null || data === undefined){
				return this.seriesToGeoJson([]);
			}else{

				var mappedData = data.map(function(e){
					return {
						date: new Date(e.date),
						deaths: e.deaths,
						lat: e.location.lat,
						lon: e.location.lon,
					}
				});

				// filter data
				var targetdate = new Date()
				targetdate.setDate(targetdate.getDate() - 1);
				mappedData = mappedData.filter(function(e){
					return (e.date >= targetdate);
				})

				var geojsonSeries = this.seriesToGeoJson(mappedData);

				return geojsonSeries;
			}
		},

		createChart: function (data){
			this.geojsonSeries = data;
		},
	},
	computed: {
		dataAvailable: function() {
			this.$nextTick(() => {
				const data = this.parseData(this.covidData);
				this.createChart(data);
			});
			return (this.covidData !== null && this.covidData !== undefined);
		},
		geoJsonMapData: function () {
			return {
				type: 'geojson',
				data: this.geojsonSeries
			};
		},
		layerProps: function () {
			const colorGradient = new Gradient();
			colorGradient.setMidpoint(5);
			colorGradient.setGradient("#E1E8ED", "#0A1E2B");

			return {
				type: 'heatmap',
				'source': this.sourceId,
				maxzoom: 15,
				paint: {
					// increase weight as diameter breast height increases
					'heatmap-weight': {
						property: 'deaths',
						type: 'exponential',
						stops: [
							[1, 0],
							[62, 1]
						]
					},
					// increase intensity as zoom level increases
					'heatmap-intensity': {
						stops: [
							[11, 1],
							[15, 3]
						]
					},
					// assign color values be applied to points depending on their density
					'heatmap-color': [
						'interpolate',
						['linear'],
						['heatmap-density'],
						0, 'rgba(0,0,0,0)',
						0.1, colorGradient.getColor(1),
						0.2, colorGradient.getColor(2),
						0.4, colorGradient.getColor(3),
						0.6, colorGradient.getColor(4),
						0.8, colorGradient.getColor(5)
					],
					// increase radius as zoom increases
					'heatmap-radius': {
						stops: [
							[11, 15],
							[15, 20]
						]
					},
					// decrease opacity to transition into the circle layer
					'heatmap-opacity': {
						default: 1,
						stops: [
							[14, 1],
							[15, 0]
						]
					}
				}
			};
		},
	},
}
</script>

<style>
	.circle-loading {
		display: block;
		width: 100px;
		margin: 0 auto;
	}

	.map_box_container{
		position: relative;
		height: 100% !important;
		width: 100% !important;
	}

	#map {
		position: absolute;
		top: 0;
		bottom: 0;
		width: 100%;
		height: 100%;
	}
</style>