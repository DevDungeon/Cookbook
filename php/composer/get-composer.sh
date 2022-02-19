#!/usr/bin/bash
# https://getcomposer.org/download/

# Download setup script
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"

# Verify v2.2.6
php -r "if (hash_file('sha384', 'composer-setup.php') === '906a84df04cea2aa72f40b5f787e49f22d4c2f19492ac310e8cba5b96ac8b64115ac402c8cd292b8a03482574915d1a8') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"

# Ensure a `composer.phar` is in the current dir and cleanup
php composer-setup.php
php -r "unlink('composer-setup.php');"

php composer.phar --version