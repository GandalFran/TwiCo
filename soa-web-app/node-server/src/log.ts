// Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
// See LICENSE for details.

"use strict";

export function log(message: string){
	console.log(`[${new Date().toISOString().replace(/T/, ' ').replace(/\..+/, '')}] ${message}`)
}