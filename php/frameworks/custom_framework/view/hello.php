<?php

$title = "Hello!";

ob_start(); ?>
Hello, world!
<?php
$body = ob_get_clean();

require 'layout.php';