<?php

// To essentially do a HEREDOC and store raw content as var instead of outputting
// use ob_start(); (output buffer) and ob_get_clean();

// It is also similar to "{% block content %} {% endblock %}
ob_start(); ?>
    <h2>Post title: <?=e($post4['title'])?></h2>
    <p>Content: <?=e($post4['content'])?></p>
<?php
$body = ob_get_clean();

// Now any variables from the controller and any vars/blocks set here
// Can go on to the larger base template
// Similar to {% extends 'layout.php' %}
require 'layout.php';