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
		<v-container v-if="dataAvailable === true">

			<v-data-iterator
				:page="page"
				:items="newsitems"
				:items-per-page.sync="itemsPerPage"
				hide-default-footer
			>
		
				<template v-slot:default="props">
					<v-row>
						<v-col
							v-for="(item, i) in props.items"
							:key="i"
							cols="12"
							sm="6"
							md="4"
							lg="3"
						>
							<v-card
								class="mx-auto"
								max-width="344"
								height="600"
							>
								<v-img 
									height="200px"
									:src="item.img"
								/>
								<v-card-title class="text"
									v-text="item.title"
								/>
								<v-card-subtitle class="text"> 
									published on {{item.date}} by {{item.source}}
								</v-card-subtitle>

								<v-card-text v-text="item.description" class="text" />

								<v-divider />

								<v-card-actions >
									<v-btn 
										text
										color="#1DA1F2"
										target="_blank"
										:href="item.url" 
									>
										<p class="text" >Visit the original</p>
									</v-btn>
								</v-card-actions>
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
	name: 'NewsItemsTable',
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
			if(data === null || data === undefined || data.news === null || data.news === undefined){
				return null;
			}

			const defaultImage = 'https://c.files.bbci.co.uk/74E8/production/_112482992__111703877_gettyimages-1128870980.jpg';
			
			const newsitems = data.news.map(function(e){
				return { 
					url: e.url, 
					title: e.title,
					author: e.author, 
					source: e.source.name,
					description: e.description,
					date: new Date(e.publishedAt).toISOString(),
					img: (e.urlToImage !== null && e.urlToImage !== undefined) ? e.urlToImage : defaultImage
				};
			})

			return newsitems;
		},

		previousPage: function() {
			this.page = (this.page-1 >= 1) ? (this.page-1) : (this.page);
		},

		nextPage: function() {
			this.page = (this.page+1 <= this.numberOfPages) ? (this.page+1) : (this.page);
		},

	},
	computed: {
		newsitems: function(){
			const parsed = this.parseData(this.data);
			return parsed;
		},

		dataAvailable: function() {
			return (this.data !== null && this.data !== undefined);
		},

		numberOfPages: function () {
			return Math.ceil(this.data.news.length/this.itemsPerPage);
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

	.text {
		color: #1DA1F2;	
		font-family: "Helvetica Neue", Roboto, "Segoe UI", Calibri, sans-serif;
		font-weight: bold;
	}
</style>