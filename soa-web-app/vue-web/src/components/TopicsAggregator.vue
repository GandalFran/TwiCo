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
			<v-row>
				<v-col
					cols="10"
					md="4"
				>
					<v-row>
						<v-col
							cols="10"
							md="10"
						>
							<v-card
								class="mx-auto"
								tile
							>
								<v-list>
									<v-subheader class="title" color="#1DA1F2" >Topics</v-subheader>
									<v-list-item-group v-model="selectedTopic" color="primary">
										<v-list-item
											v-for="(item, i) in topicsData"
											:key="i"
										>
											<v-list-item-content>
												<v-list-item-title v-text="item.name" class="text" ></v-list-item-title>
											</v-list-item-content>
										</v-list-item>
									</v-list-item-group>
								</v-list>
							</v-card>
						</v-col>
					</v-row>
					<v-row>
						<v-col
							cols="10"
							md="10"
						>

							<v-card
								class="mx-auto"
								tile
							>
								<sentiment-chart
									v-show="dataAvailable === true"
									:chartData="sentimentData"
								/>
							</v-card>
						</v-col>
					</v-row>
				</v-col>
				<v-col
					cols="10"
					md="8"
				>
					<tweets-table
						v-show="dataAvailable === true"
						:data="tweetsData"
					/>

				</v-col>
			</v-row>
		</v-container>
	</div>
</template>

<script>
import TweetsTable from "@/components/TweetsTable.vue";
import SentimentChart from "@/components/SentimentChart.vue";

export default {
	name: 'TopicAggregator',
	props: ['data'],
	components: {
		TweetsTable,
		SentimentChart
	},
	data: function () {
		return {
			selectedTopic: 1,
		};
	},
	methods: {

		prepareTopics: function (data){
			var topics = Object.keys(data).map(function(e){
				return {
					name: e,
					tweets: data[e]
				};
			})

			topics.sort(function(e1, e2){
				return e1.name.localeCompare(e2.name);
			});

			return topics;
		},
	},
	computed: {
		dataAvailable: function() {
			return (this.data !== null && this.data !== undefined);
		},
		sentimentData: function () {
			const topics = this.prepareTopics(this.data.topics);
			return topics[this.selectedTopic].tweets;
		},
		tweetsData: function () {
			const topics = this.prepareTopics(this.data.topics);
			return topics[this.selectedTopic].tweets;
		},
		topicsData: function () {
			const topics = this.prepareTopics(this.data.topics);
			return topics;
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
		color: #657786;	
		font-family: "Helvetica Neue", Roboto, "Segoe UI", Calibri, sans-serif;
	}

	.title {
		color: #1DA1F2;	
		font-family: "Helvetica Neue", Roboto, "Segoe UI", Calibri, sans-serif;
		font-weight: bold;
	}

	.v-subheader {
		font-weight: bold;
		color: #1DA1F2 !important;
	}
</style>