<template>
  <v-container id="upgrade" fluid tag="section">
    <div :id="particles.id" class="particles-js theBackground text-center">
      <v-row align="center" justify="center">
        <v-col cols="12" md="8">
          <h1>Twico analysis service</h1>
        </v-col>
      </v-row>
      <v-row align="center" justify="center">
        <v-col cols="12" md="8">
          <v-img
            lazy-src="img/architecture.png"
            src="img/architecture.png"
            class="architecture"
            contain
          />
        </v-col>
      </v-row>
      <v-row align="center" justify="center">
        <v-col cols="12" md="8">
          <v-btn x-large rounded class="theButton" @click="login">
            Go to dashboard
          </v-btn>
        </v-col>
      </v-row>
    </div>
  </v-container>
</template>

<script>

export default {
  name: "Home",
  data() {
    return {
      baseUrl: "https://soa.servehttp.com",
      particles: {
        id: "particles-instance-" + Math.floor(Math.random() * 5000),
        color: "#ffffff",
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
  background: #66ccff;
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
.theButton2 {
  position: absolute;
  top: 1;
  bottom: 0;
  left: 0;
  right: 0;
  width: 50%;
  height: 30%;
  margin: auto;
}
.title2 {
  position: absolute;
  top: 1;
  bottom: 0;
  left: 0;
  right: 0;
  width: 50%;
  height: 30%;
  margin: auto;
}

h1 {
  color: white;
  font-family: Futura, "Trebuchet MS", Arial, sans-serif;
  font-size: 100px;
  font-style: normal;
  font-variant: normal;
  font-weight: 700;
  line-height: 26.4px;
}
</style>
