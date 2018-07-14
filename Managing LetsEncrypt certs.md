Managing LetsEncrypt certs
=============================


Installing on Ubuntu
----------

	sudo apt-get update
	sudo apt-get install software-properties-common
	sudo add-apt-repository ppa:certbot/certbot
	sudo apt-get update
	sudo apt-get install certbot
	
Getting new certs on Ubuntu
---------------------------

	sudo certbot certonly
	# It will ask you for what domains
	# and the public location to placea verification file
	


Renewing
--------

	sudo certbot renew --dry-run