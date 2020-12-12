// Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
// See LICENSE for details.

"use strict";

import * as OS from "os";
import * as Path from "path";
import * as FileSystem from "fs";

import { log } from "./log";

const CONFIG_FILE = "config/config.json";

/** Class to store the express HTTP server configuration. */
export class HttpConfig {

    /** The HTTP listen port. */
    public port: number;
    /** The HTTP listen address. */
    public bind: string;

    /**
    * Create a HttpConfig.
    */
    constructor() {
        this.port = 0;
        this.bind = "";
    }
}

/** Class to store the express HTTPS server configuration. */
export class HttpsConfig extends HttpConfig{

    /** The HTTPS certification authority file. */
    public caFile: string;
    /** The HTTPS certificate's key file. */
    public keyFile: string;
    /** The HTTPS certificate file. */
    public certFile: string;

    /**
    * Create a HttpsConfig.
    */
    constructor() {
        super();
        this.caFile = "";
        this.keyFile = "";
        this.certFile = "";
    }
}

/** Class to store the OAuth2.0 flow info. */
export class AuthConfig {

    /** OAuth2.0 application client id. */
    public clientId: string;
    /**OAuth2.0 application client secret. */
    public clientSecret: string;
    /**OAuth2.0 application client callback endpoint to receive the auth params and tokens. */
    public callback: string;

    /**
    * Create a AuthConfig.
    */
    constructor(){
        this.clientId = "";
        this.clientSecret = "";
        this.callback = "";
    }
}

export class Config {

    private static instance: Config = null;
    public static getInstance(): Config {
        if (! Config.instance) {
            Config.instance = Config.buildConfig();
        }
        return Config.instance;
    }

    public static buildConfig(): Config {
        const config: Config = new Config();
        const configPath = Path.resolve(__dirname, "..", "..", CONFIG_FILE);
        Config.load(config, configPath);
        FileSystem.watchFile(configPath, (curr, prev) => {
            Config.load(config, configPath)
        });
        return config;
    }

    private static load(config: Config, configPath: string){
        log('[CONFIG] configuration file update');
        let rawConfig: any = {};
        try {
            rawConfig = JSON.parse(FileSystem.readFileSync(configPath).toString());
        } catch (e) {
            log("Invalid configuration: " + e.message);
        }

        // load other info
        config.redirect = rawConfig.redirect;
        config.whiteList = rawConfig.whiteList;
        config.apiBaseUrl = rawConfig.apiBaseUrl;

        // load http info
        config.http = new HttpConfig();
        if (typeof rawConfig === "object" && typeof rawConfig.http === "object") {
            config.http.port = rawConfig.http.port;
            config.http.bind = rawConfig.http.bind;
        }

        // load https info
        config.https = new HttpsConfig();
        if (typeof rawConfig === "object" && typeof rawConfig.https === "object") {
            config.https.port = rawConfig.https.port;
            config.https.bind = rawConfig.https.bind;
            config.https.caFile = rawConfig.https.caFile;
            config.https.keyFile = rawConfig.https.keyFile;
            config.https.certFile = rawConfig.https.certFile;
        }

        // load google auth info
        config.auth.google = new AuthConfig();
        if (typeof rawConfig === "object" && typeof rawConfig.auth === "object" && typeof rawConfig.auth.google === "object") {
            config.auth.google.clientId = rawConfig.auth.google.id;
            config.auth.google.callback = rawConfig.auth.google.callback;
            config.auth.google.clientSecret = rawConfig.auth.google.secret;
        }

        // load github auth info
        config.auth.github = new AuthConfig();
        if (typeof rawConfig === "object" && typeof rawConfig.auth === "object" && typeof rawConfig.auth.github === "object") {
            config.auth.github.clientId = rawConfig.auth.github.id;
            config.auth.github.callback = rawConfig.auth.github.callback;
            config.auth.github.clientSecret = rawConfig.auth.github.secret;
        }
    }

    /** SOA data API base URL configuration. */
    public apiBaseUrl: string;
    /** redirect configuration. */
    public redirect: boolean;
    /** Whitelist configuration. */
    public whiteList: string;
    /** HTTP configuration. */
    public http: HttpConfig;
    /** HTTPS configuration. */
    public https: HttpsConfig;
    /** Google OAuth2.0 configuration. */
    public auth: any = {
        google: null,
        github: null,
    };
}
