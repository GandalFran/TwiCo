<template>
	<div class="theBackground">
		<v-toolbar
			dense
		>
			<v-toolbar-title>
				<h1 id="title" > Twico </h1>
			</v-toolbar-title>
			
			<v-spacer />

			<v-btn 
				icon
				color="#66ccff"
				@click="reloadButton"
				:loading="loadingDashboard"
				:disabled="loadingDashboard"
			>
				<v-icon>fas fa-sync-alt</v-icon>
			</v-btn>

			<v-btn 
				icon
				color="#66ccff"
				@click="logout"
			>
				<v-icon>fas fa-sign-out-alt</v-icon>
			</v-btn>

			<v-btn 
				icon
				color="#66ccff"
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
				<chart v-if="item.chartType == 'twitter'" :chartData="twitterData" > </chart>
				<covid-chart v-if="item.chartType == 'covid'" :covidData="covidData" > </covid-chart>
				<covid-chart v-if="item.chartType == 'covidBarcelona'" :covidData="covidDataBarcelona" > </covid-chart>
			</grid-item>
		</grid-layout>
	</div>
</template>

<script>
import axios from "axios";
import Chart from "@/components/Chart.vue";
import CovidChart from "@/components/CovidChart.vue";
import VueGridLayout from 'vue-grid-layout';

export default {
	name: 'Dashboard',
	components: {
		'chart':Chart,
		CovidChart,
		GridLayout: VueGridLayout.GridLayout,
		GridItem: VueGridLayout.GridItem
	},
	data () {
		return{
			loadingDashboard: false,
			baseUrl: "https://soa.servehttp.com",
			covidData: null,
			covidDataBarcelona: null,
			twitterData: null,
			layout: [
				{"x":0,"y":0,"w":5,"h":20,"i":"0", "chartType": "covidWorld"},
				{"x":5,"y":0,"w":5,"h":20,"i":"1", "chartType": "covidBarcelona"},
				{"x":0,"y":20,"w":10,"h":20,"i":"2", "chartType": "twitter"},
			],
			barcelonaMapConfig: {
				initialZoom: 8,
				initialCoordinates: [2.021426, 41.560819],
			},
			worldMapConfig: {
				initialZoom: 2,
				initialCoordinates: [0, 0],
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
			const uri = this.baseUrl + "/data/covid";
			axios.post(uri, {}).then(response => {
				const data = response.data;
				this.covidData = data;
			}).catch(e => { console.log(e); });
		},
		reloadCovidBarcelonaData: function (){
			const uri = this.baseUrl + "/data/covid/barcelona";
			axios.post(uri, {}).then(response => {
				const data = response.data;
				this.covidDataBarcelona = data;
			}).catch(e => { console.log(e); });
		},
		reloadTwitterData: function (){
			const uri = this.baseUrl + "/data/twitter";
			axios.post(uri, {}).then(response => {
				const data = response.data;
				this.twitterData = data;
			}).catch(e => { console.log(e); });
		},
		reloadDashBoard: function () {
			this.reloadCovidData();
			this.reloadTwitterData();
		},
		reloadButton: function (){
			this.loadingDashboard=true;
			this.reloadDashBoard();
			this.loadingDashboard=false;
		}
	},
	created: function() {
	//this.checkAuth();
		this.reloadDashBoard();
	}
}
</script>

<style>
	.theBackground {
		background: #66ccff
	}

	#title {
		color: #66ccff;  
		font-family: "Helvetica Neue", Roboto, "Segoe UI", Calibri, sans-serif;
		font-weight: bold;
	}
</style>