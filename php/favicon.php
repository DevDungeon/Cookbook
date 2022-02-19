<?php
/**
 * Dynamically generate a favicon image with background color and text overlay
 *
 * Use in an HTML template like:
 *
 * ```
 * <link rel="icon" href="/favicon.php" sizes="32x32" type="image/png">
 * ```
 */

// PHP Image Processing and Generation https://www.php.net/manual/en/refs.utilspec.image.php

// Generate a black image
$generated_image = imagecreate(32, 32);
// Set background color
imagecolorallocate($generated_image, 0, 255, 0);  // #00FF00 Green

// Add text overlay to image
// https://www.php.net/manual/en/function.imagestring.php
// To use other fonts, call `imageloadfont()` https://www.php.net/manual/en/function.imageloadfont.php
$text_color = imagecolorallocate($generated_image, 0, 0, 255); // #0000FF Blue
imagestring($generated_image, 5, 12, 8,  '!', $text_color);

// Begin HTTP response output
header('Content-Type: image/png');
imagepng($generated_image); // Write binary data to output
imagedestroy($generated_image); // Free up memory