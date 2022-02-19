<?php
/**
 * Any other global helper functions could be defined here.
 * This is loaded in the `index.php` and available to controllers, model, and views
 */

 /**
 * Connect to db and load model functions
 */
require '../model/model.php'; // relative to index.php


/**
 * Escape content for template rendering
 *
 * Example usage:
 *   <?=e($_POST['untrusted_content']);?>
 */
function e($content) {
  return htmlspecialchars($content, ENT_QUOTES, 'UTF-8');
}