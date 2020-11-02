// Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
// See LICENSE for details.

"use strict";

import * as OS from "os";
import * as Path from "path";
import * as FileSystem from "fs";
import * as Request from "request";

import { Config } from "../config";

/** Serves information retrieved from the data API. */
export class ApiSOADataModel {

    /** 
    * Retrieves COVID information.
    * @return COVID information.
    */
    public async covid(): Promise<Array<any>>{
    	const uri = `${Config.getInstance().apiBaseUrl}/covid`;
    	const rawData = await this.doRequest(uri, {});
        return Promise.resolve(rawData);
    }

    /** 
    * Performs a HTTP POST.
    * @param uri - the request's URI
    * @param requestBody - the request's body
    * @return the body of the response if success and the error in other case.
    */
    private async doRequest(uri: string, requestBody: any): Promise<any>{
        return new Promise<string>(function(resolve, reject) {
            Request.post(uri, requestBody, function(error:any,response:any,body:any){
            	if(error){
            		reject(error);
            	}else{
                	resolve(body);
            	}
            });
        });
    }
}