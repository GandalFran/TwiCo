<template>
	<div>
		<v-container v-if="dataAvailable === true">

			<v-data-iterator
				:page="page"
				:items="tweets"
				:items-per-page.sync="itemsPerPage"
				hide-default-footer
			>
		
				<template v-slot:default="props">
					<v-row>
						<v-col
							v-for="(item, i) in props.items"
							:key="i"
							cols="12"
							md="3"
						>
							<v-card
								outlined
								class="mx-auto"
								max-width="344"
								height="300"
								:color="item.color"
								target="_blank"
								:href="item.url" 
							>
								<v-card-text class="text text-center"
									v-text="item.text"
								/>

							</v-card>
						</v-col>
					</v-row>
				</template>

				<template v-slot:footer>
					<v-row class="mt-2" align="center" justify="center">
						<v-btn
							fab
							dark
							color="#AAB8C2"
							class="mr-1"
							@click="previousPage"
						>
							<v-icon>mdi-chevron-left</v-icon>
						</v-btn>
						<v-spacer />
						<v-btn
							fab
							dark
							color="#AAB8C2"
							class="ml-1"
							@click="nextPage"
						>
							<v-icon>mdi-chevron-right</v-icon>
						</v-btn>
					</v-row>
				</template>
			</v-data-iterator>

		</v-container>
	</div>
</template>

<script>

export default {
	name: 'TweetsTable',
	props: ['data'],
	data: function () {
		return {
			sortDesc: false,
			page: 1,
			itemsPerPage: 4,
		};
	},
	methods: {
		parseData: function (data) {
			if(data === null || data === undefined){
				return null;
			}

			const colors = {
				positive: '#6bff77',
				neutral: '#6ba4ff',
				negative: '#ff726b',
			};

			const tweets = data.map(function(e){
				return { 
					url: e.url, 
					text: e.text,
					sentiment: e.sentiment,
					color: colors[e.sentiment],
				};
			});

			// set page to one when data is served
			this.page = 1;
			
			return tweets;
		},

		previousPage: function() {
			this.page = (this.page-1 >= 1) ? (this.page-1) : (this.page);
		},

		nextPage: function() {
			this.page = (this.page+1 <= this.numberOfPages) ? (this.page+1) : (this.page);
		},

	},
	computed: {
		tweets: function(){
			const parsed = this.parseData(this.data);
			return parsed;
		},

		dataAvailable: function() {
			return (this.data !== null && this.data !== undefined);
		},

		numberOfPages: function () {
			return Math.ceil(this.data.length/this.itemsPerPage);
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