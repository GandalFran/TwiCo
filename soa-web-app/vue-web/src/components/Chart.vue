<template>
	<div>
		<p v-text="chartData"> </p>
		<p v-text="chartDataProperty"> </p>
	</div>
</template>

<script>
	export default {
		name: 'Chart',
		props: ['chartDataProperty'],
		data () {
			return {
				chartData : 'hola',
			}
		},
		methods: {
			updateData: function(data) {
				console.log('xddd');
				this.chartData = data
			}
		}
	}
</script>