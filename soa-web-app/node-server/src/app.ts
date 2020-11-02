// Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
// See LICENSE for details.

"use strict";

import Cors from 'cors';
import * as Fs from "fs";
import * as HTTP from "http";
import * as Path from "path";
import Express from "express";
import * as HTTPS from "https";
import Passport from 'passport';
import Compression from "compression";
import CookieParser from 'cookie-parser';
import CookieSession from 'cookie-session';
import Session from 'express-session';
import * as BodyParser from 'body-parser';
import GoogleStrategy from 'passport-google-oauth';

import { log } from "./log";
import { Config } from "./config";
import { AuthController } from "./controller/authController";
import { ApiSOADataController } from "./controller/apiSOADataController";
import { HTTP_COOKIE_SECRET, HTTP_SESSION_SECRET, STATUS_FORBIDDEN } from "./util";

/** Class to handle the express APIs. */
export class Application {

    /** Express application. */
    private application: Express.Express;

    /** Create an express application and configures it */
    constructor() {
        this.application = Express();
        this.application.use(Cors());
        this.application.use(Compression());
        this.registerParsers();
        this.configurePassportAuth();
        this.configureRoutes();
        this.registerControllers();
        this.application.use(Express.static(Path.join( __dirname, "..", "..", "static" )));
    }

    /** Initializes the express HTTP and HTTPS servers. */
    public start() {
        if(Config.getInstance().redirect === true){
            // redirect to https
            HTTP.createServer(function(request, response){
                response.writeHead(301, { Location: 'https://' + request.headers.host + request.url });
                response.end();
            }).on("error", (e: any) => {
                log(`[HTTP] ${e}`);
            }).listen(Config.getInstance().http.port, Config.getInstance().http.bind, () => {
                log(`[HTTP] Application listening on http://${Config.getInstance().http.bind}:${Config.getInstance().http.port}`);
            });
        }else{
            // register http server
            HTTP.createServer(this.application).on("error", (e: any) => {                
                log(`[HTTP] ${e}`);
            }).listen(Config.getInstance().http.port, Config.getInstance().http.bind, () => {
                log(`[HTTP] Application listening on http://${Config.getInstance().http.bind}:${Config.getInstance().http.port}`);
            });
        }

        if(Config.getInstance().https.caFile){
            // https server
            HTTPS.createServer({
                ca: Fs.readFileSync(Config.getInstance().https.caFile),
                key: Fs.readFileSync(Config.getInstance().https.keyFile),
                cert: Fs.readFileSync(Config.getInstance().https.certFile)
            }, this.application).on("error", (e: any) => {                
                log(`[HTTPS] ${e}`);
            }).listen(Config.getInstance().https.port, Config.getInstance().https.bind, () => {
                log(`[HTTPS] Application listening on https://${Config.getInstance().https.bind}:${Config.getInstance().https.port}`);
            });
        }

    }

    /** Initialize express request parsers. */
    private registerParsers() {
        this.application.use(BodyParser.raw());
        this.application.use(BodyParser.text());
        this.application.use(CookieParser(HTTP_COOKIE_SECRET));
        this.application.use(BodyParser.json({ limit: "16mb" }));
        this.application.use(BodyParser.urlencoded({ limit: "16mb", extended: true }));
        this.application.use(Session({
            secret: HTTP_SESSION_SECRET,
            resave: true,
            saveUninitialized: true,
            cookie: { secure: true }
        }));
    }

    /** Configure Oauth2.0 login and session with passport. */
    public configurePassportAuth(){
        this.application.use(Passport.initialize());
        this.application.use(Passport.session());
        Passport.use(new GoogleStrategy.OAuth2Strategy({
            clientID: Config.getInstance().auth.clientId,
            callbackURL: Config.getInstance().auth.callback,
            clientSecret: Config.getInstance().auth.clientSecret
        }, function(token, refreshToken, profile, done){
            return done(null, {
                profile: profile,
                token: token,
                refreshToken: refreshToken
            });
        }));
        Passport.serializeUser((user, done) => {
            done(null, user);
        });
        Passport.deserializeUser((user, done) => {
            done(null, user);
        });
    }

    /** Ensure user is logged in when accessing critical endpoints. */
    private configureRoutes(){
        this.application.use((request, response, next) => {
            if (!request.session.user && request.path.match(/\/data\/.*/)) {
                response.status(STATUS_FORBIDDEN);
                response.send();
            }else{
                next();
            }
        });
    }

    /** Register controllers. */
    private registerControllers() {
        new AuthController().registerController(this.application);
        new ApiSOADataController().registerController(this.application);
    }
}