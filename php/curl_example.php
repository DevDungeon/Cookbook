<?php
    function curl1($url) {
        $ch = curl_init();
        // Set options 1 at a time
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE); // Return the webpage data
        $data = curl_exec($ch);
        curl_close($ch);
        return $data;
    }
    
    function curl2($url) {
        // Set all options in array
        $options = [
            CURLOPT_RETURNTRANSFER => TRUE,  // Return the webpage data
            CURLOPT_FOLLOWLOCATION => TRUE,  // Follow 'location' HTTP headers
            CURLOPT_AUTOREFERER => TRUE, // Automatically set the referer where following 'location' HTTP headers
            CURLOPT_CONNECTTIMEOUT => 120,   // Setting the amount of time (in seconds) before the request times out
            CURLOPT_TIMEOUT => 120,  // maximum amount of time for cURL to execute queries
            CURLOPT_MAXREDIRS => 10, // maximum number of redirections to follow
            CURLOPT_USERAGENT => "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1a2pre) Gecko/2008073000 Shredder/3.0a2pre ThunderBrowse/3.2.1.8",  // Setting the useragent
            CURLOPT_URL => $url,
        ];
         
        $ch = curl_init();
        curl_setopt_array($ch, $options);
        $data = curl_exec($ch);
        curl_close($ch);
        return $data;
    }

    /** Curl options */
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



    echo curl1("http://www.example.com");  // Executing our curl function to scrape the webpage http://www.example.com and return the results into the $scraped_website variable

    // // Defining the basic scraping function
    // function scrape_between($data, $start, $end){
    //     $data = stristr($data, $start); // Stripping all data from before $start
    //     $data = substr($data, strlen($start));  // Stripping $start
    //     $stop = stripos($data, $end);   // Getting the position of the $end of the data to scrape
    //     $data = substr($data, 0, $stop);    // Stripping all data from after and including the $end of the data to scrape
    //     return $data;   // Returning the scraped data from the function
    // }


