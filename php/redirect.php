<?php
/**
 * Redirect to any URL
 */

header('Location: /'); // Defaults to 302 temporary redirect

// Alternatively, specify the exact response code you want
//header('Location: /', TRUE, 301); // 301 Moved Permanently
//header('Location: /', TRUE, 302); // 302 Found

exit; // Ensure nothing else gets output
