<template>
	<div>
		<v-toolbar
			dense
			color="#F5F8FA"
		>
			<v-spacer />
			<v-spacer />
			<v-spacer />
			
			<v-img src="img/logo.png" contain max-height="50" />
			
			<v-spacer />
			<v-spacer />

			<v-btn 
				raised
				color="#E1E8ED"
				@click="loginGoogle"
			>	
				<v-img 
					contain
					width="20px"
					height="20px"
					src="img/google.png"
				/>
			</v-btn>

			<v-btn 
				raised
				color="#E1E8ED"
				@click="loginGitHub"
			>	
				<v-img 
					contain
					width="20px"
					height="20px"
					src="img/github.png"
				/>
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

		<v-span />

		<div class="theOtherBackgrhound">
			<v-row>
				<v-col
					v-for="member in team" :key="member"
				>
					<v-card
						raised
						class="mx-auto"
						max-width="300"
					>
						<a :href="member.link" target="_blank">
							<v-img
								height="200px"
								:src="member.image"
								class="white--text align-end"
							/>
						</a>
						<v-card-subtitle class="mytitle" v-text="member.name" />
						<v-card-text class="mytext" v-text="member.text" />
					</v-card>
				</v-col>
			</v-row>
		</div>
	</div>
</template>

<script>

export default {
	name: "Home",
	data() {
		return {
			mydialog: false,
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
			},
			team: [
				{
					name: 'Francisco Pinto Santos',
					text: 'Escribo cosas y a veces funcionan',
					link: 'https://github.com/GandalFran',
					image: 'https://avatars2.githubusercontent.com/u/29973536?s=460&u=b45b09f015e310153cd146b8903443c9d0080494&v=4',
				},
				{
					name: 'Luis Blazquez Miñambres',
					text: 'Escribo cosas y a veces funcionan',
					link: 'https://github.com/luisblazquezm',
					image: 'https://avatars0.githubusercontent.com/u/40697133?s=460&u=82f3e7d01e88b27ea481e57791fa62c9d519d2ac&v=4',
				},
				{
					name: 'Miguel Cabezas Puerto',
					text: 'Escribo cosas y a veces funcionan',
					link: 'https://github.com/MiguelCabezasPuerto',
					image: 'https://avatars2.githubusercontent.com/u/47638681?s=460&v=4',
				},
				{
					name: 'Oscar Sánchez Juanes',
					text: 'Escribo cosas y a veces funcionan',
					link: 'https://github.com/oscarsanchezj',
					image: 'https://avatars3.githubusercontent.com/u/48065910?s=460&u=c8287b792cf94981253c644207661e75fbda96c2&v=4',
				},				
			],
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
		loginGoogle() {
			window.location = this.baseUrl + "/auth/google";
		},

		loginGitHub() {
			window.location = this.baseUrl + "/auth/github";
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

.theOtherBackgrhound {
	background: #F5F8FA;
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

.mytitle {
	color: #1DA1F2;	
	font-family: "Helvetica Neue", Roboto, "Segoe UI", Calibri, sans-serif;
	font-weight: bold;
}

.mytext{
	color:#F5F8FA;
	font-weight: bold;
	font-family: "Helvetica Neue", Roboto, "Segoe UI", Calibri, sans-serif;
}

.v-dialog > .v-card > .v-toolbar {
  position: sticky;
  top: 0;
  z-index: 999;
}

</style>
