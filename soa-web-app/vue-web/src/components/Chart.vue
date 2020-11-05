<template>
	<div>
		<p v-text="chartData"> </p>
		<p :v-show="isUpdated === true" v-text="'updated'"> </p>
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
			update: function () {
				console.log('update')
			},
		},
		watch: {
			chartData: function (oldData, newData) {
				var x = oldData;
				x = newData;
				x = true;
				this.isUpdated = x;
			}
		},
	}
</script>