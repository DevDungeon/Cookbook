<?php

// Write a file
$file = fopen('hello.txt', "w") or die("Unable to open file!");
fwrite($file, "Hello, world!\n");
fclose($file);

// Write whole file at once
file_put_contents('hello.txt', "Hello, world, again!\n");

// Get file all at once
$contents = file_get_contents('test.txt');

// Read lines
$lines = file('test.txt'); // Each line will still have it's line ending character
print_r($lines);


// Read file
$filename = 'test.txt';
$number_of_bytes_to_read = filesize($filename);
$file = fopen($filename, 'r');
$contents = fread($file, $number_of_bytes_to_read);
echo $contents;
// You can check for EOF with `feof()`
echo feof($file);



// Common actions
echo filesize('hello.txt');
echo file_exists('hello.txt');
echo is_dir('/path/to/check');
chdir('/path/to/change/to/');
echo getcwd();
echo __DIR__;
echo __FILE__;
mkdir('/path/to/make');
rmdir('/path/to/delete');






/* Get a lock on a file */
$file = fopen('safe.txt', 'a');
// https://www.php.net/manual/en/function.flock.php
flock($file, LOCK_EX); // Get exclusive lock on file
// Perform read/write actions while holding the lock
fwrite($file, "Test\n");
flock($file, LOCK_UN); // Release file lock
fclose($file);





// Use STDIN/STDOUT/STDERR
fwrite(STDOUT, "Hello, world!\n");
fwrite(STDERR, "Hello, error! Enter some text:\n");
$input = fread(STDIN, 1024);
fwrite(STDOUT, "Input received: " . $input . "\n");



/* Scandir or glob will list files in a dir */
$contents = scandir('.');
print_r($contents);


/** example globs
    *
    ./*
    /path/to/search/*
    *.*
    *.jpg
    log*
 */
$all_contents = glob("*");
print_r($all_contents);
$log_entries = glob("*log*");
print_r($log_entries);






/** Serve gzip */
header('Content-Type: video/x-msvideo');
header('Content-Disposition: attachment; filename=my_video.avi');
$file = fopen("compress.zlib://my_video.avi.gz", 'r');
while (!feof($file)) {
    echo fread($file, 8192);
};