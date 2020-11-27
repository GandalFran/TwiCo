# Twico
Twico, is the final project for the SOA subject of the Computer Science Master's degree at USAL. It consists in a set of subsystems to aggregate information from newsitems,Twitter and opendata covid sources, for the creation of a dashboard served as a service, to serve a summary of the covid situation based in social media (Twitter).

## Subsystems
- soa-api: API to retrieve data from different sources and combine it in most of cases (locationIq, opendata europe, opendata barcelona and newsapi).
- soa-web-app: MEVN web application.
	- vue-web: web develoved in Vue.js, Vuetify mainly. It also uses Mapbox, Amcharts and Grid.js for visuaization purposes.
	- node-server: application server, coded in node.js and TypeScript, that integrates the soa-api with the web application. Also it verifies the user's identity with the Google OAuth2.0 login.

<img src="https://github.com/GandalFran/soa-final/blob/master/soa-web-app/vue-web/public/img/architecture.png" align="center">

## Current deployments
- web: https://soa.servehttp.com
- api: http://soa.servehttp.com:5000/soa/v1/

<img src="https://github.com/GandalFran/soa-final/blob/master/soa-web-app/vue-web/public/img/twico.png" align="center">

## Authors
- Luis Blazquez Miñambres (@luisblazquezm)
- Miguel Cabezas Puerto (@MiguelCabezasPuerto)
- Óscar Sánchez Juanes (@oscarsanchezj)
- Francisco Pinto-Santos (@gandalfran)
