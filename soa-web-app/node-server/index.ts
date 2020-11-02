// Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
// See LICENSE for details.

import { log } from "./src/log";
import { Application } from "./src/app";

// start crash guard
process.on("uncaughtException", function(e: Error){
	log(`[NOT CONTROLLED EXCEPTION] ${e.message}`);
});

// start application
const app: Application = new Application();
app.start();
