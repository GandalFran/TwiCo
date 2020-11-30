<template>
	<div class="theBackground">
		<v-toolbar
			dense
			color="#F5F8FA"
		>
			<v-spacer />
			<v-spacer />
			<v-spacer />
			
			<v-img src="img/logo.png" contain max-height="50" />
			
			<v-spacer />
			<v-spacer />
			
			<v-btn 
				icon
				color="#1DA1F2"
				@click="reloadButton"
				:loading="loadingDashboard"
				:disabled="loadingDashboard"
			>
				<v-icon>fas fa-sync-alt</v-icon>
			</v-btn>

			<v-btn 
				icon
				color="#1DA1F2"
				@click="logout"
			>
				<v-icon>fas fa-sign-out-alt</v-icon>
			</v-btn>

			<v-btn 
				icon
				color="#1DA1F2"
				target="_blank"
				href="http://soa.servehttp.com:5000/soa/v1/" 
			>	
				<v-icon>fas fa-code</v-icon>

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
				:key="item.i"
			>
				<world-covid-cases-chart 
					v-if="item.chartType == 'world-covid-cases-chart'" 
					:covidData="covidDataWorld"
				/>

				<world-covid-deaths-chart 
					v-if="item.chartType == 'world-covid-deaths-chart'" 
					:covidData="covidDataWorld"
				/>

				<bareclona-covid-cases-chart 
					v-if="item.chartType == 'barcelona-covid-cases-chart'" 
					:covidData="covidDataBarcelona" 
					:initialZoom="barcelonaMapConfig.initialZoom" 
					:initialCoordinates="barcelonaMapConfig.initialCoordinates"
				/>

				<bareclona-covid-deaths-chart 
					v-if="item.chartType == 'barcelona-covid-deaths-chart'" 
					:covidData="covidDataBarcelona" 
					:initialZoom="barcelonaMapConfig.initialZoom" 
					:initialCoordinates="barcelonaMapConfig.initialCoordinates"
				/>

				<newsitems-table
					v-if="item.chartType == 'newsitems-table'" 
					:data="topicsData"
				/>

				<topics-aggregator
					v-if="item.chartType == 'topics-aggregator'" 
					:data="topicsData"
				/>
				<chart 
					v-if="false && item.chartType == 'twitter'" :chartData="topicsData"
				/>
			</grid-item>
		</grid-layout>
	</div>
</template>

<script>
import axios from "axios";
import VueGridLayout from 'vue-grid-layout';

import Chart from "@/components/Chart.vue";
import NewsItemsTable from "@/components/NewsItemsTable.vue";
import TopicsAggregator from "@/components/TopicsAggregator.vue";
import WorldCovidCasesChart from "@/components/WorldCovidCasesChart.vue";
import WorldCovidDeathsChart from "@/components/WorldCovidDeathsChart.vue";
import BarcelonaCovidCasesChart from "@/components/BarcelonaCovidCasesChart.vue";
import BarcelonaCovidDeathsChart from "@/components/BarcelonaCovidDeathsChart.vue";


export default {
	name: 'Dashboard',
	components: {
		'chart':Chart,
		'topics-aggregator': TopicsAggregator,
		'newsitems-table': NewsItemsTable,
		'world-covid-cases-chart': WorldCovidCasesChart,
		'world-covid-deaths-chart': WorldCovidDeathsChart,
		'bareclona-covid-cases-chart': BarcelonaCovidCasesChart,
		'bareclona-covid-deaths-chart': BarcelonaCovidDeathsChart,
		GridLayout: VueGridLayout.GridLayout,
		GridItem: VueGridLayout.GridItem
	},
	data () {
		return{
			loadingDashboard: false,
			baseUrl: "https://soa.servehttp.com",
			covidDataWorld: null,
			covidDataBarcelona: null,
			topicsData: null,
			layout: [
				{"x":0,"y":0,"w":5,"h":20,"i":"0", "chartType": "world-covid-cases-chart"}, 
				{"x":5,"y":0,"w":5,"h":20,"i":"1", "chartType": "barcelona-covid-cases-chart"},
				{"x":0,"y":20,"w":5,"h":20,"i":"2", "chartType": "world-covid-deaths-chart"}, 
				{"x":5,"y":20,"w":5,"h":20,"i":"3", "chartType": "barcelona-covid-deaths-chart"},
				{"x":0,"y":40,"w":10,"h":28,"i":"5", "chartType": "topics-aggregator"},
				{"x":0,"y":80,"w":10,"h":40,"i":"4", "chartType": "newsitems-table"},
			],
			barcelonaMapConfig: {
				initialZoom: 7,
				initialCoordinates: [2.021426, 41.560819],
			},
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
			const uri = this.baseUrl + "/data/covid/world";
			axios.post(uri, {}).then(response => {
				const data = response.data;
				this.covidDataWorld = data;
			}).catch(e => { console.log(e); });
		},
		reloadCovidBarcelonaData: function (){
			const uri = this.baseUrl + "/data/covid/barcelona";
			axios.post(uri, {}).then(response => {
				const data = response.data;
				this.covidDataBarcelona = data;
			}).catch(e => { console.log(e); });
		},
		reloadTopicsData: function (){
			const uri = this.baseUrl + "/data/topics";
			axios.post(uri, {}).then(response => {
				const data = response.data;
				this.topicsData = data;
			}).catch(e => { console.log(e); });
		},
		reloadDashBoard: function () {
			this.reloadCovidData();
			this.reloadTopicsData();
			this.reloadCovidBarcelonaData();
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
		background: #1DA1F2
	}

	#title {
		color: #1DA1F2;	
		font-family: "Helvetica Neue", Roboto, "Segoe UI", Calibri, sans-serif;
		font-weight: bold;
	}
</style>