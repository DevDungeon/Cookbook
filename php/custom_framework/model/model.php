<?php

// sudo apt install php php-mbstring php8.1-common php8.1-sqlite3

// Connect
$db = new PDO('sqlite:../model/db.sqlite3'); // or 'sqlite::memory:'

// Ensure table exists
$db->exec("CREATE TABLE IF NOT EXISTS posts (title TEXT, content TEXT)");


/**
 *
 *  Define functions for application. E.g. Get user profiles, Create new entry.
 *
 * 
 */
function get_posts() {
    global $db;
    $result = $db->query('SELECT rowid, title, content FROM posts');
    $array_of_posts = $result->fetchAll();
    return $array_of_posts; // Array of arrays
}

function get_post($id) {
    global $db;
    $statement = $db->prepare('SELECT rowid, title, content FROM posts WHERE rowid=?');
    $statement->execute([$id]);
    return $statement->fetch(); // or fetchObject() for an object
}

function add_post($title, $content) {
    global $db;
    $insert = "INSERT INTO posts (title, content) VALUES (:title, :content)";
    $statement = $db->prepare($insert);
    $statement->execute(['title' => $title, 'content' => $content]);
}

function update_post($id, $title, $content) {
    global $db;
    $update = "UPDATE posts SET title=:title, content=:content WHERE rowid=:id";
    $statement = $db->prepare($update);
    $statement->execute(['id' => $id, 'title' => $title, 'content' => $content]);
}

function delete_post($id) {
    global $db;
    $delete = "DELETE FROM posts WHERE rowid=?";
    $db->prepare($delete)->execute([$id]);
}



/* 
  In the "controller", include this mode.php and start using functions
*/
// require_once('model.php');

// CREATE
add_post("New post", "lorem ipsum...");

// READ
print_r(get_posts());
print_r(get_post(4));

// UPDATE
update_post(4, 'New 4 title', 'new 4 content');

// DELETE
delete_post(4);