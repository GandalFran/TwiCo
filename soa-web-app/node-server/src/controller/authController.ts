// Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
// See LICENSE for details.

"use strict";

import Passport from 'passport';
import * as Express from "express";

import { Config } from "../config";
import { WhiteList } from "../model/whiteList";
import { CONTENT_APPLICATION_JSON } from "../util";

/** Controller for retrieving results from backend */
export class AuthController{

    /** 
    * Register the controller's endpoints.
    * @param application - the express aplication.
    */
    public registerController(application: Express.Express): any {
        application.get("/auth/google",
            Passport.authenticate('google', {
                scope: ['https://www.googleapis.com/auth/plus.login',
                'https://www.googleapis.com/auth/userinfo.email']
            })
        );
        application.get("/auth/google/callback", 
            Passport.authenticate('google', {failureRedirect: '/#/forbidden' }), 
            this.authCallback.bind(this)
        );
        application.get("/auth/google/logout", this.logout.bind(this));
        
        application.post("/auth/check", this.checkAuth.bind(this));
    }

    /** 
    * Callback endpoint for Google OAuth2.0. Here the user login session is generated.
    * @param request - the express request.
    * @param response - the express response.
    */
    public async authCallback(request: Express.Request, response: Express.Response) {
        const user: any = request.user;
        const email: string = user.profile.emails[0].value;
        
        if(WhiteList.isInWhitelist(email)){
            request.session.user = {
                id: user.profile.id,
                email: user.profile.emails[0].value
            }
            request.session.token = user.token;
            response.redirect('/#/dashboard');
        }else{
            response.redirect('/#/forbidden');
        }
    }

    /** 
    * Endpoint to logout and destroy the session.
    * @param request - the express request.
    * @param response - the express response.
    */
    public async logout(request: Express.Request, response: Express.Response){
        await request.session.destroy(function(e){
            request.logout();
            response.redirect('/#/');
        });
    }

    /** 
    * Endpoint to check if user is loged in.
    * @param request - the express request.
    * @param response - the express response.
    */
    public async checkAuth(request: Express.Request, response: Express.Response) {
        var isAutenticated = false;
        if(request.session.user){
            isAutenticated = true;
        }

        response.contentType(CONTENT_APPLICATION_JSON);
        response.json({
            "auth": isAutenticated
        })
    }

}