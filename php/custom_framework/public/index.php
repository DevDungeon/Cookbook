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
 * Load global functions that are used in both controller and views
 */
require '../functions.php';

/**
 * Handle routing. Passes control to a "controller"
 */
require '../router.php';
