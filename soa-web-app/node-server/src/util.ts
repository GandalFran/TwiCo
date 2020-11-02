// Copyright 2020 Luis Blazquez Miñambres (@luisblazquezm), Miguel Cabezas Puerto (@MiguelCabezasPuerto), Óscar Sánchez Juanes (@oscarsanchezj) and Francisco Pinto-Santos (@gandalfran)
// See LICENSE for details.

"use strict";

/** Constant with the HTTP cookie secret */
export const HTTP_COOKIE_SECRET: string = "estoEsSoaAmigos";
/** Constant with the HTTP session secret */
export const HTTP_SESSION_SECRET: string = "tengoHambreYMeVoyAlGoiko";

/** Constant with the text response ok status */
export const MESSAGE_STATUS_OK: string = "ok";
/** Constant with the text response error status */
export const MESSAGE_STATUS_ERROR: string = "error";

/** Constant with the HTTP ok status code */
export const STATUS_OK: number = 200;

/** Constant with the HTTP bad request status code */
export const STATUS_BAD_REQUEST: number = 400;
/** Constant with the HTTP forbidden status code */
export const STATUS_FORBIDDEN: number = 403;
/** Constant with the HTTP not found status code */
export const STATUS_NOT_FOUND: number = 404;
/** Constant with the HTTP internal server error status code */
export const STATUS_INTERNAL_SERVER_ERROR: number = 500;

/** Constant with the HTTP content type for HTML */
export const CONTENT_TEXT_HTML: string = "text/html; charset=utf-8";
/** Constant with the HTTP content type for text plain */
export const CONTENT_TEXT_PLAIN: string = "text/plain; charset=utf-8";
/** Constant with the HTTP content type for JSON */
export const CONTENT_APPLICATION_JSON: string = "application/json; charset=utf-8";