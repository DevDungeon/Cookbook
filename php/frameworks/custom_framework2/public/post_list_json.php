<?php
require '../framework.php';

$posts = get_posts();

header('Content-Type: application/json');

echo json_encode($posts);