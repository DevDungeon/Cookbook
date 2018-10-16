# Google Hacking Like a True Script Kiddie

Do you wanna go from 0 to script kiddie in 30 seconds? Do you wanna get superuser access on a Linux box with no effort at all? Do you wanna find MySQL root passwords with your eyes closed? Look no further! You will be the dorkiest skid on the block!


## Disclaimer

Don't try this at home. In fact, don't even try this.


## The Dorkiest Dorks

    ?filetype:inc mysql_connect -database.mysql.inc

    ?filetype:ini WS_FTP  

    ?site:github.com master/wp_config.php password blob DB_PASSWORD
    ?inurl:wp-config -intext:wp-config "'DB_PASSWORD'"

    ?site:github.com master/id_rsa

    ?".php?id="

    ?intitle: index of / mp3
    ?intitle: index of / private
    ?intitle: index of / photos


## Prevention

* Serving .inc files? Configure your web server!
* Serving .php files as plain-text? Configure your web server!
* Directory listings? Configure your web server!
* SQL injection? Escape parameters!
* WordPress config files? Don't commit them!
* Private SSH Keys? Don't commit them!

##  Challenge

Find an interesting Google Dork and share it with me


## References and Resources

* https://www.exploit-db.com/google-hacking-database/
* http://www.effecthacking.com/2015/05/google-dorks-ultimate-connection-for-hackers.html
* http://www.tekgyd.com/2015/07/fresh-google-dorks-list-of-2015.html
* http://waziristanihaxor.blogspot.com/2015/03/5000-fresh-google-dorks-sql-injection.html
* http://lab.artlung.com/ws-ftp-password-decoder/
