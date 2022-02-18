<?php
/**
 * Model
 */
require '../model/model.php';

/**
 * Controller
 */
$title = "View post 4";
$post4 = get_post(4);

/**
 * View
 */
require '../view/view-post.php';