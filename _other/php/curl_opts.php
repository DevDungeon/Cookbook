<?php

$ch = curl_init("http://www.example.com/");
$fp = fopen("example.txt", "w");

curl_setopt($ch, CURLOPT_FILE, $fp); // output to file instead of STDOUT
curl_setopt($ch, CURLOPT_HEADER, 1); // include headers
curl_setopt($ch, CURLOPT_VERBOSE, 1); // include headers

curl_exec($ch);
curl_close($ch);
fclose($fp);


/*

CURLOPT_VERBOSE // 1 if you want Curl to give detailed reports about everything that is happening.

CURLOPT_URL // String containing the URL you want Curl to fetch.

CURLOPT_USERAGENT // A string containing the "user-agent" header to be used in a HTTP request.

CURLOPT_TIMEOUT // A number equal to the maximum time in seconds that Curl functions can take.

CURLOPT_NOBODY // 1 to tell Curl not to include the body part in the output. For HTTP(S) servers, this is equivalent to a HEAD request - only the headers will be returned.

CURLOPT_POST // 1 if you want Curl to do a regular HTTP POST.

CURLOPT_POSTFIELDS // A string containing the data to post in the HTTP "POST" operation.

CURLOPT_COOKIE

CURLOPT_COOKIEFILE

CURLOPT_USERPWD // A string formatted in the username:password manner, for Curl to give to the remote server if requested.

CURLOPT_RESUME_FROM // A number equal to the offset, in bytes, that you want your transfer to start from.

CURLOPT_FOLLOWLOCATION // 1 to follow Location: headers

CURLOPT_MAXREDIRS // limits FollowLocations

CURLOPT_REFERER // A string containing the "referer" header to be used in an HTTP request. This is only necessary if the remote server relies on this value.


CURLOPT_FAILONERROR // 1 for silent fail

CURLOPT_FTPAPPEND // append not overwrite

CURLOPT_FTPLISTONLY // 1 to list just the names of an FTP directory as opposed to more detailed information.

CURLOPT_HTTPHEADER //An array of HTTP header fields to be set.

CURLOPT_INFILE // String containing the filename where the input of your transfer comes from.

CURLOPT_INFILESIZE //The size of the file being uploaded to a remote site.

CURLOPT_CRLF // convert unix to CRLF new lines

CURLOPT_RETURNTRANSFER // 1 if you want Curl to return the transfer data instead of printing it out directly.

CURLOPT_STDERR // A string containing the filename to write errors to instead of normal output.

CURLOPT_UPLOAD // 1 if you want PHP to prepare for a file upload.

CURLOPT_WRITEHEADER // containing the filename to write the header part of the output into.

*/