<?php
// Do controller things. Set vars.
$post4 = get_post(4);
$title = $post4['title'];

// Render template
require '../view/view-post.php';