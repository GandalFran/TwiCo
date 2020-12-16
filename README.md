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

<img src="https://github.com/GandalFran/soa-final/blob/master/soa-web-app/vue-web/public/img/twico.PNG" align="center">
<img src="https://github.com/GandalFran/soa-final/blob/master/soa-web-app/vue-web/public/img/dashboard.PNG" align="center">

## Authors
- Luis Blazquez Miñambres (@luisblazquezm)	<table>
- Miguel Cabezas Puerto (@MiguelCabezasPuerto)	  <tr>
- Óscar Sánchez Juanes (@oscarsanchezj)	    <td align="center"><a href="https://github.com/GandalFran"><img src="https://avatars2.githubusercontent.com/u/29973536?s=460&u=b45b09f015e310153cd146b8903443c9d0080494&v=4" width="100px;" alt=""/><br /><sub><b>Francisco Pinto Santos</b></sub></a><br /><a href="https://github.com/GandalFran?tab=repositories" title="Code">💻</a> <a href="https://github.com/all-contributors/all-contributors/commits?author=GandalFran" title="Documentation">📖</a> <a href="https://github.com/all-contributors/all-contributors/commits?author=GandalFran" title="Front-end">🎨</a> <a href="https://github.com/all-contributors/all-contributors/commits?author=GandalFran" title="Back-end">⛏</a> <a href="https://github.com/GandalFran" title="Ideas, Planning, & Feedback">🤔</a></td>
- Francisco Pinto-Santos (@gandalfran)	    <td align="center"><a href="https://github.com/luisblazquezm"><img src="https://avatars0.githubusercontent.com/u/40697133?s=460&u=82f3e7d01e88b27ea481e57791fa62c9d519d2ac&v=4" width="100px;" alt=""/><br /><sub><b>Luis Blázquez Miñambres</b></sub></a><br /><a href="https://github.com/luisblazquezm?tab=repositories" title="Code">💻</a> <a href="https://github.com/all-contributors/all-contributors/commits?author=luisblazquezm" title="Documentation">📖</a> <a href="https://github.com/all-contributors/all-contributors/commits?author=luisblazquezm" title="Back-end">⛏</a> <a href="https://github.com/all-contributors/all-contributors/commits?author=luisblazquezm" title="IA">🧠</a> <a href="https://github.com/luisblazquezm" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/MiguelCabezasPuerto"><img src="https://avatars2.githubusercontent.com/u/47638681?s=460&v=4" width="100px;" alt=""/><br /><sub><b>Miguel Cabezas Puerto</b></sub></a><br /> <a href="https://github.com/MiguelCabezasPuerto?tab=repositories" title="Code">💻</a> <a href="https://github.com/all-contributors/all-contributors/commits?author=MiguelCabezasPuerto" title="Documentation">📖</a> <a href="https://github.com/all-contributors/all-contributors/commits?author=MiguelCabezasPuerto" title="Back-end">⛏</a> <a href="https://github.com/MiguelCabezasPuerto" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/oscarsanchezj"><img src="https://avatars3.githubusercontent.com/u/48065910?s=460&u=c8287b792cf94981253c644207661e75fbda96c2&v=4" width="100px;" alt=""/><br /><sub><b>Oscar Sánchez Juanes</b></sub></a><br /> <a href="https://github.com/oscarsanchezj?tab=repositories" title="Code">💻</a> <a href="https://github.com/all-contributors/all-contributors/commits?author=oscarsanchezj" title="Documentation">📖</a> <a href="https://github.com/all-contributors/all-contributors/commits?author=oscarsanchezj" title="Back-end">⛏</a> <a href="https://github.com/oscarsanchezj" title="Ideas, Planning, & Feedback">🤔</a></td>
  </tr>
