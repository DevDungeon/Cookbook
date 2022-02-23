<?php
$files = glob('*.*');

// Order $files with oldest(lowest) time at the beginning,
// and highest (newest) times at the end
usort($files, function($a, $b) {
    // If first and second arg are equal, return 0
    // if first arg is greater than second, return positive int (move it to a higher index)
    // If first arg is less than second, return negative int (move it to lower index)    
    return filemtime($a) - filemtime($b); // or use filesize(), filectime()
});

// To reverse an array, either flip the return values in your `usort()` function, or use array_reverse()
$files = array_reverse($files);

// Return only a portion (the newest 10)
$limited_files = array_slice($files, 0, 10);