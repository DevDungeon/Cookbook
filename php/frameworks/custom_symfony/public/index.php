<?php
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
namespace App;

require_once __DIR__.'/../vendor/autoload.php';

use Symfony\Component\HttpFoundation\Request;

$kernel = new MyKernel('prod', false);
$kernel->handle(Request::createFromGlobals())->send();
