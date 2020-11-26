<template>
	<div>
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
				@click="$router.push('/')"
			>	
				<v-icon>fas fa-home</v-icon>
			</v-btn>

		</v-toolbar>

		<div id="forbidenapp">
			<div class="txt">
				403 Forbidden <span class="blink">_</span>
			</div>	
		</div>
	</div>
</template>


<script>
export default {
	name: 'Forbidden'
}
</script>

<style scoped>
	@import url('https://fonts.googleapis.com/css?family=Press+Start+2P');

	html,body{
			width: 100%;
			height: 100%;
			margin: 0;
	}

	.txt{
			font-family: 'Press Start 2P', cursive;
			box-sizing: border-box;
	}
	#forbidenapp{
			padding: 1rem;
			position: absolute;
			background: #66ccff;
			display: flex;
			height: 100%;
			width: 100%;
			justify-content: center; 
			align-items: center;
			color: white;
			text-shadow: 0px 0px 10px;
			font-size: 6rem;
			.txt {
				font-size: 1.8rem;
			}
	}
	@keyframes blink {
			0%  {opacity: 0}
			49%  {opacity: 0}
			50%  {opacity: 1}
			100% {opacity: 1}
	}

	.blink {
			animation-name: blink;
			animation-duration: 1s;
			animation-iteration-count: infinite;
	}


	#title {
		color: #66ccff;  
		font-family: "Helvetica Neue", Roboto, "Segoe UI", Calibri, sans-serif;
		font-weight: bold;
	}
</style>