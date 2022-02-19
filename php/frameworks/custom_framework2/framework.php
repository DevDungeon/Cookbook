<?php
/**
 * Bootstrap all the frameworkey stuff.
 * Load the model functions. Load helper functions.
 * 
 * Add anything else you want to load here.
 * 
 * Do any pre-processing like loading user from session.
 */



/**
 * Escape content for template rendering
 *
 * Example usage:
 *   <?=e($_POST['untrusted_content']);?>
 */
function e($content) {
  return htmlspecialchars($content, ENT_QUOTES, 'UTF-8');
}


/**
 * 
 * Handle any user auth?
 * 
 */
// Inspect the cookie sent
// Tie it to a session (on disk, in db?)
// Load and store a `$user` object so it will be available moving forward
// e.g.:
//
// function load_user_from_session() {}
// $user = load_user_from_session();


/**
 * 
 * 
 * Database and "model" stuff
 * 
 * 
 */

// sudo apt install php php-mbstring php8.1-common php8.1-sqlite3
// Connect
$db = new PDO('sqlite:' . __DIR__ . '/db.sqlite3'); // or 'sqlite::memory:'
// Fetch associate arrays by default. Or: PDO::FETCH_OBJ, PDO::FETCH_BOTH
$db->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
// Ensure table exists
$db->exec("CREATE TABLE IF NOT EXISTS posts (title TEXT, content TEXT)");


/**
 *
 *  Define functions for application. E.g. Get post, delete post
 * 
 */
function get_posts() {
  global $db;
  $result = $db->query('SELECT rowid as id, title, content FROM posts');
  $array_of_posts = $result->fetchAll();
  return $array_of_posts; // Array of arrays
}

function get_post($id) {
  global $db;
  $statement = $db->prepare('SELECT rowid as id, title, content FROM posts WHERE rowid=?');
  $statement->execute([$id]);
  return $statement->fetch(PDO::FETCH_ASSOC); // or fetchObject() for an object
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

