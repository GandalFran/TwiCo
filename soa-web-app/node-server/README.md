# bisicaidos

## How to deploy

### install
To install depencies run `npm install`

### configure
To configure, modify a file called `config.json` in the root directory.

### run
To run the server first compile the project with `npm run build` and then start the server with `npm run start`.

### deploy
To deploy use PM2 (configuration in pm2.json) with `pm2 start pm2.json`.

### maintenance and posterior developement
 - Application developed with Node.js + Typescript with EJS view engine.
 - The team members data is stored in the config/data.json file, and the images and pages in static/members/img and static/members/page respectively.
 - The team information is updated once a day, and when the file data.json is updated (because of banned members).
 - To log important information, please use the src/log function.
 - If web changes, update the service/ScraperService.ts file (the scraper is developed with Cheerio.js).
 - To add old members not registered or honour members, please add manually to data.json file and and the files to static/members/img static/members/page.