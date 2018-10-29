<?php
$src_img = imagecreatefrompng('300x200.png');
if(!$src_img) {
    die('Error when reading the source image.');
}
$thumbnail = imagecreatetruecolor(200, 200);
if(!$thumbnail) {
    die('Error when creating the destination image.');
}
// Take 200x200 from 200x200 starting at 50,0
$result = imagecopyresampled($thumbnail, $src_img, 0, 0, 50, 0, 200, 200, 200, 200);
if(!$result) {
    die('Error when generating the thumbnail.');
}
$result = imagejpeg($thumbnail, '200x200gd.png');
if(!$result) {
    die('Error when saving the thumbnail.');
}
$result = imagedestroy($thumbnail);
if(!$result) {
    die('Error when destroying the image.');
}

/* bool imagecopyresampled ( resource $dst_image , resource $src_image , 
int $dst_x , int $dst_y ,
 int $src_x , int $src_y ,
  int $dst_w , int $dst_h ,
   int $src_w , int $src_h )
*/