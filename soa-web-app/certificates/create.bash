#!/bin/bash
# src: https://medium.com/@saurabh6790/generate-wildcard-ssl-certificate-using-lets-encrypt-certbot-273e432794d7

# prepare letsencrypt certificates
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"

# install letsencript
sudo apt install letsencrypt -y

# create certificate
letsencrypt certonly \
	--manual \
	--email franpintosantos@usal.es \
	--server https://acme-v02.api.letsencrypt.org/directory \
	--agree-tos -d soa.servehttp.com