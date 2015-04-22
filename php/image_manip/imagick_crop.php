<?php

$inFile = "300x200.png";
$outFile = "200x200_imagick.png";
$image = new Imagick($inFile);
$image->cropImage(200,200, 50,0);
$image->writeImage($outFile);