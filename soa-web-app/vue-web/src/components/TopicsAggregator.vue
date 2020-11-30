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
		<v-container>
			<v-row>
				<v-col
					cols="10"
					md="4"
				>
					<v-row>
						<v-card
							class="mx-auto"
							max-width="300"
							tile
						>
							<v-list>
								<v-subheader>Topics</v-subheader>
								<v-list-item-group v-model="selectedTopic" color="primary">
									<v-list-item
										v-for="(item, i) in topicsData"
										:key="i"
									>
										<v-list-item-content>
											<v-list-item-title v-text="item"></v-list-item-title>
										</v-list-item-content>
									</v-list-item>
								</v-list-item-group>
							</v-list>
						</v-card>
					</v-row>
					<v-row>
						<sentiment-chart
							v-show="dataAvailable === true"
							:chartData="sentimentData"
						/>
					</v-row>
				</v-col>
				<v-col
					cols="10"
					md="6"
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

		createChart: function (data){

		},
	},
	computed: {
		dataAvailable: function() {
			return (this.data !== null && this.data !== undefined);
		},
		sentimentData: function () {
			console.log(this.selectedTopic);
			return this.data.topics.t1[this.selectedTopic].tweets;
		},
		tweetsData: function () {
			console.log(this.selectedTopic);
			return this.data.topics.t1[this.selectedTopic].tweets;
		},
		topicsData: function () {
			return this.data.topics.t1.map(function(e){
				return e.name.replace('covidAND ','');
			});
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