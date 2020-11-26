<template>
	<v-container class="map_box_container" >
		<v-progress-circular
			v-if="dataAvailable === false"
			class="circle-loading"
			indeterminate
			:size="300"
			:width="20"
			color="#ffffff"
			/>
		<MglMap id="map" ref="map" v-if="dataAvailable === true"
			:accessToken="accessToken"
			:mapStyle.sync="mapStyle"
			:sourceId="sourceId"
			:source="geoJsonMapData"
			:zoom="initialZoom"
			:maxzoom="initialZoom"
			:center="initialCoordinates"
			>
			<MglGeojsonLayer
				:layerId="layerId"
				:layer="layerProps"
				:sourceId="sourceId"
				:source="geoJsonMapData"
			/>
		</MglMap>
	</v-container>
</template>

<script>
import Mapbox from "mapbox-gl";
import { MglMap, MglGeojsonLayer } from "vue-mapbox";

export default {
	name: 'CovidChart',
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
							cases: e.cases
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
						cases: e.cases,
						lat: e.location.lat,
						lon: e.location.lon,
					}
				});

				mappedData.sort(function(a, b){ 
					return a.date - b.date; 
				});

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
			return {
				'type': 'heatmap',
				'source': this.sourceId,
				'minzoom': 1,
				'maxzoom': this.initialZoom,
				'paint':{
					'heatmap-weight': {
						property: 'cases',
						type: 'identity'
					},
					'heatmap-color': [
						'interpolate',
						['linear'],
						['heatmap-density'],
						0, 'rgba(43,131,186,0)',
						0.2, 'rgb(171,221,164)',
						0.4, 'rgb(255,255,191)',
						0.6, 'rgb(253,174,97)',
						0.8, 'rgb(215,25,28)'
					],
					'heatmap-radius': {
						stops: [
							[3, 15],
							[15, 20]
						]
					},
				},
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