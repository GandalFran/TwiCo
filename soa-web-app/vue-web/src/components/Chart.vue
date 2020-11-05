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
		<p v-show="dataAvailable === true" v-text="processedData"> </p>
	</div>
</template>

<script>
	export default {
		name: 'Chart',
		props: ['chartData'],
		data: function () {
			return {
				isUpdated: false,
			};
		},
		methods: {
			parseData: function (data) {
				if(data === null || data === undefined){
					return null;
				}
				return data.message;
			},
		},
		computed: {
			dataAvailable: function() {
				return (this.chartData !== null && this.chartData !== undefined);
			},
			processedData: function () {
				return this.parseData(this.chartData);
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