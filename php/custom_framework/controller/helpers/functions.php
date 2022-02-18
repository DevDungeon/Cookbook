<?php
/**
 * Any other global helper functions could be defined here.
 */

function render($template_name) {
  // Example usage: 
  //   render("view-post"); // view-post.tpl.php
  require "../view/php/$template_name.tpl.php";
}

