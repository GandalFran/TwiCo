<template>
	<div>
		<v-toolbar
			dense
			color="#F5F8FA"
		>
			<v-toolbar-title>
				<h1 id="title" > Twico </h1>
			</v-toolbar-title>
			
			<v-spacer />
			
			<v-btn 
				raised
				color="#1DA1F2"
				@click="login"
			>	
				<p class="myText" >Dashboard</p>
			</v-btn>

		</v-toolbar>

		<div :id="particles.id" class="particles-js theBackground text-center">
			<v-img
				lazy-src="img/architectureLow.png"
				src="img/architecture.png"
				class="architecture"
				contain
			/>
		</div>
	</div>
</template>

<script>

export default {
	name: "Home",
	data() {
		return {
			baseUrl: "https://soa.servehttp.com",
			particles: {
				id: "particles-instance-" + Math.floor(Math.random() * 5000),
				color: "#F5F8FA",
				linesColor: "#474747",
				shapeType: "image",
				lineOpacity: 0.4,
				particleOpacity: 0.7,
				particleSize: 5,
				particlesNumber: 100,
				linesWidth: 1,
				lineLinked: false,
				linesDistance: 100,
				moveSpeed: 14,
				hoverEffect: true,
				clickEffect: true,
				hoverMode: "bubble",
				clickMode: "repulse"
			}
		};
	},

	mounted: function() {
		// import particle.js only on client-side
		require("particles.js");
		this.$nextTick(() => {
			this.initParticleJS(
				this.particles.color,
				this.particles.particleOpacity,
				this.particles.particlesNumber,
				this.particles.shapeType,
				this.particles.particleSize,
				this.particles.linesColor,
				this.particles.linesWidth,
				this.particles.lineLinked,
				this.particles.lineOpacity,
				this.particles.linesDistance,
				this.particles.moveSpeed,
				this.particles.hoverEffect,
				this.particles.hoverMode,
				this.particles.clickEffect,
				this.particles.clickMode
			);
		});
	},
	methods: {
		login() {
			window.location = this.baseUrl + "/auth/google";
		},

		initParticleJS(
			color,
			particleOpacity,
			particlesNumber,
			shapeType,
			particleSize,
			linesColor,
			linesWidth,
			lineLinked,
			lineOpacity,
			linesDistance,
			moveSpeed,
			hoverEffect,
			hoverMode,
			clickEffect,
			clickMode
		) {
			/* eslint-disable */
			particlesJS(this.particles.id, {
				particles: {
					number: {
						value: particlesNumber,
						density: {
							enable: true,
							value_area: 800
						}
					},
					color: {
						value: color
					},
					shape: {
						// circle, edge, triangle, polygon, star, image
						type: shapeType,
						stroke: {
							width: 0,
							color: "#192231"
						},
						polygon: {
							nb_sides: 5
						},
						image: {
							src: "img/covid.png",
							width: 150,
							height: 150
						}
					},
					opacity: {
						value: particleOpacity,
						random: false,
						anim: {
							enable: true,
							speed: 1,
							opacity_min: 0.1,
							sync: false
						}
					},
					size: {
						value: particleSize,
						random: true,
						anim: {
							enable: false,
							speed: 40,
							size_min: 0.1,
							sync: false
						}
					},
					line_linked: {
						enable: lineLinked,
						distance: linesDistance,
						color: linesColor,
						opacity: lineOpacity,
						width: linesWidth
					},
					move: {
						enable: true,
						speed: moveSpeed,
						direction: "none",
						random: false,
						straight: false,
						out_mode: "out",
						bounce: false,
						attract: {
							enable: false,
							rotateX: 600,
							rotateY: 1200
						}
					}
				},
				interactivity: {
					detect_on: "canvas",
					events: {
						onhover: {
							enable: hoverEffect,
							mode: hoverMode
						},
						onclick: {
							enable: clickEffect,
							mode: clickMode
						},
						onresize: {
							enable: true,
							density_auto: true,
							density_area: 400
						}
					},
					modes: {
						grab: {
							distance: 140,
							line_linked: {
								opacity: 1
							}
						},
						bubble: {
							distance: 300,
							size: 20,
							duration: 4,
							opacity: 8,
							speed: 3
						},
						repulse: {
							distance: 300,
							duration: 0.4
						},
						push: {
							particles_nb: 4
						},
						remove: {
							particles_nb: 2
						}
					}
				},
				retina_detect: false
			});
		}
	}
};
</script>

<style>
.theBackground {
	background: #1DA1F2;
}
.architecture {
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
	width: 50%;
	height: 30%;
	margin: auto;
}

#title {
	color: #1DA1F2;  
	font-family: "Helvetica Neue", Roboto, "Segoe UI", Calibri, sans-serif;
	font-weight: bold;
}

.myText{
	color:#F5F8FA;
	font-weight: bold;
	font-family: "Helvetica Neue", Roboto, "Segoe UI", Calibri, sans-serif;
}

</style>
