// Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
// See LICENSE for details.

"use strict";

import * as OS from "os";
import * as Path from "path";
import * as FileSystem from "fs";

import { Config } from "../config";

/** Serves information about the whitelisted users. */
export class WhiteList {

    /** Whitelist information. */
    private static whiteList: string [] = null;
    /** Whitelitsted users emails array. */
    public static dataPath: string = Path.resolve(__dirname, "..", "..", "..", Config.getInstance().whiteList);

    /** Loads whitelist infomation from whitelist file. */
    constructor(){
    	WhiteList.whiteList = WhiteList.load();
    }

    /** 
    * Load the email whitelist from file.
    * @return list of whitelisted emails.
    */
    private static load(): Array<string>{
        let rawData: any = {};
        try {
            rawData = FileSystem.readFileSync(WhiteList.dataPath).toString();
        } catch (e) {
            console.error("Whitelist not found" + e.message);
        }
        return JSON.parse(rawData);
    }

    /** 
    * Checks if the given email is in the whitelist.
    * @param email - email to check if is in whitelist
    * @return true if the email is in whitelist and false in other case.
    */
    public static isInWhitelist(email: string): boolean{
        for(const e of WhiteList.whiteList){
            if(e === email){
                return true;
            }
        }
        return false;
    }
}