<?php
/**
 * Router
 */

// To run locally:
//    cd public/
//    php -S localhost:9000 index.php

// To run with .htaccess:
/*
# .htaccess
RewriteEngine On
RewriteBase /
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule ^(.+)$ index.php [QSA,L]
*/


/**
 * Setup and load global functions to be available everywhere
 */
require '../bootstrap.php';

/**
 * Handle routing. Passes control to a "controller"
 */
require '../router.php';
