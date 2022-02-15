<?php
/**
 * TIPS:
 *  - Make sure the web server user (www-data usually) has write access to both the database file AND the directory it resides in.
 *  - Might need to install `apt install php-pdo-sqlite`.
 */

$db = new PDO('sqlite:myDatabase.sqlite3'); // or 'sqlite::memory:'
// $db = null; // Close when done by setting to null

// Error handling
try {    
    // Attempt something
} catch(PDOException $e) {
    echo $e->getMessage();
}

// Querying
$result = $file_db->query('SELECT * FROM myTable');
foreach ($result as $result) {
    print $result['id'];
}

// Executing
$statement = "DROP TABLE uselessTable";
$db->exec($statement);

// Execute many
$items = [
    [
        'title' => 'Hello!',
        'value' => 'Just testing...',
    ],
    [
        'title' => 'Hello Twice!',
        'value' => 'Who is there?',
    ],
];
$insert = "INSERT INTO myTable (title, value) VALUES (:title, :value)";
$statement = $db->prepare($insert);
$stmt->bindParam(':title', $title);
$stmt->bindParam(':value', $value);
foreach ($data as $item) {
    $title = $item['title'];
    $message = $item['value'];
    $stmt->execute();
}