<?php
// sourceforge.net/projects/phpcrawl/
// http://phpcrawl.cuab.de/

// It may take a whils to crawl a site ...
set_time_limit(10000);

// Inculde the phpcrawl-mainclass
include("libs/PHPCrawler.class.php");


// Extend the class and override the handleDocumentInfo()-method 
class NanoCrawler extends PHPCrawler 
{


  function handleDocumentInfo($DocInfo) 
  {
    // Just detect linebreak for output ("\n" in CLI-mode, otherwise "<br>").
    if (PHP_SAPI == "cli") $lb = "\n";
    else $lb = "<br />";

    // Print the URL and the HTTP-status-Code
    echo "Page requested: ".$DocInfo->url." (".$DocInfo->http_status_code.")".$lb;
    
    // Print the refering URL
    echo "Referer-page: ".$DocInfo->referer_url.$lb;
    
    // Print if the content of the document was be recieved or not
    if ($DocInfo->received == true)
      echo "Content received: ".$DocInfo->bytes_received." bytes".$lb;
    else
      echo "Content not received".$lb; 

    // Print the number of found links in this document
    echo "Links found: ".count($DocInfo->links_found_url_descriptors).$lb;
    
    

    // Now you should do something with the content of the actual
    // received page or file ($DocInfo->source), we skip it in this example 
    
    echo $lb;
    
    flush();
  } 


  function handleHeaderInfo($header) {
      // print_r($header);
      // http_status_code
      // content_type
      // content_length (empty)
      // content_encoding (empty)
      // transfer_encoding (chunked)
      // cookies -> array
      // source_url
    // store headers
    // if bad mime type
    //return (-1); // Negative number means do not download body

    }
}



// Create new custom crawler class
$crawler = new NanoCrawler();

// Set rules and params
$crawler->setURL("example.com");
$crawler->addContentTypeReceiveRule("#text/html#");
$crawler->addURLFilterRule("#\.(jpg|jpeg|gif|png)$# i"); // Ignore links to pictures, dont even request pictures
$crawler->enableCookieHandling(true); // Store and send cookie-data like a browser does
$crawler->setTrafficLimit(1000 * 1024 * 10); // Set the traffic-limit to 10 MB  (in bytes)
$crawler->setUserAgentString("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36");
//setPageLimit(0, true) // limit, count only requested pages
//obeyRobotsTxt(false)
//setFollowMode(0)
$crawler->setRequestDelay(0); // delay between requests in seconds

// Start crawling
$crawler->go();

// Get post-crawl report
$report = $crawler->getProcessReport();

if (PHP_SAPI == "cli") $lb = "\n";
else $lb = "<br />";
    
echo "Summary:".$lb;
echo "Links followed: ".$report->links_followed.$lb;
echo "Documents received: ".$report->files_received.$lb;
echo "Bytes received: ".$report->bytes_received." bytes".$lb;
echo "Process runtime: ".$report->process_runtime." sec".$lb; 
echo "Memory peak usage: ".(($report->memory_peak_usage/1024)/1024)." MB".$lb; 
// file_limit_reached
// traffic_limit_reached
//print_r($report);