Managing LetsEncrypt certs
=============================


Getting new certs on Ubuntu
---------------------------

	sudo apt-get update
	sudo apt-get install software-properties-common
	sudo add-apt-repository ppa:certbot/certbot
	sudo apt-get update
	sudo apt-get install certbot
	sudo certbot certonly

Renewing
--------

	sudo certbot renew --dry-run