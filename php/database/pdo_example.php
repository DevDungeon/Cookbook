<?php

// Create or open a database file
$db = new PDO('sqlite:db.sqlite3'); // or in memory with 'sqlite::memory:'

try {
    # MS SQL Server and Sybase with PDO_DBLIB
    $DBH = new PDO("mssql:host=$host;dbname=$dbname, $user, $pass");
    $DBH = new PDO("sybase:host=$host;dbname=$dbname, $user, $pass");
   
    # MySQL with PDO_MYSQL
    $DBH = new PDO("mysql:host=$host;dbname=$dbname", $user, $pass);
   
    # SQLite Database
    $DBH = new PDO("sqlite:my/database/path/database.db");
  }
  catch(PDOException $e) {
      echo $e->getMessage();
  }






# STH means "Statement Handle"
$STH = $DBH->prepare("INSERT INTO folks ( first_name ) values ( 'Cathy' )");
$STH->execute();


//# no placeholders - ripe for SQL Injection!
//$STH = $DBH->("INSERT INTO folks (name, addr, city) values ($name, $addr, $city)");
//$STH = $DBH->("INSERT INTO folks (name, addr, city) values (?, ?, ?);
//$STH = $DBH->("INSERT INTO folks (name, addr, city) value (:name, :addr, :city)");

// Fetch as assoc array
$STH->setFetchMode(PDO::FETCH_ASSOC);
$STH = $DBH->query('SELECT name, addr, city from folks');
$STH->setFetchMode(PDO::FETCH_ASSOC);
while($row = $STH->fetch()) {
    echo $row['name'] . "\n";
    echo $row['addr'] . "\n";
    echo $row['city'] . "\n";
}


// Set fetch mode globally if you want
//$DBH->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_OBJ);

// Fetch as generic object
$STH = $DBH->query('SELECT name, addr, city from folks');
$STH->setFetchMode(PDO::FETCH_OBJ);
while($row = $STH->fetch()) {
    echo $row->name . "\n";
    echo $row->addr . "\n";
    echo $row->city . "\n";

    

// Fetch as a specific class
class secret_person {
    public $name;
    public $addr;
    public $city;
    public $other_data;
 
    function __construct($other = '') {
        $this->address = preg_replace('/[a-z]/', 'x', $this->address);
        $this->other_data = $other;
    }
}
$STH = $DBH->query('SELECT name, addr, city from folks');
$STH->setFetchMode(PDO::FETCH_CLASS, 'secret_person');
while($obj = $STH->fetch()) {
    echo $obj->addr;
}



$DBH->lastInsertId();

$sql = "SELECT COUNT(*) FROM folks";
if ($STH = $DBH->query($sql)) {
    # check the row count
    if ($STH->fetchColumn() > 0) {
 
    # issue a real select here, because there's data!
    }
    else {
        echo "No rows matched the query.";
    }
}







// `PDOException`s are returned when errors encountered with database
try {
    $db->exec(
        "CREATE TABLE IF NOT EXISTS user (
    username TEXT PRIMARY KEY,
    password_hash TEXT, 
    email TEXT)"
    );

} catch(PDOException $e) {
    echo $e->getMessage();
}



//
//// Drop a table
//$drop = "DROP TABLE uselessTable";
//$file_db->exec($drop);
//// Querying
//$result = $file_db->query('SELECT * FROM myTable');
//foreach ($result as $result) {
//    print $result['id'];
//}
//// Updating
//$update = "UPDATE myTable SET value = 'Hakuna matata!' WHERE id = 5";
//$database->exec($update);
//// Inserting multiple records at once
//$items = array(
//    array(
//        'title' => 'Hello!',
//        'value' => 'Just testing...',
//    ),
//    array(
//        'title' => 'Hello Twice!',
//        'value' => 'Who is there?',
//    ),
//);
//
//// Prepare INSERT statement to SQLite3 file db
//$insert = "INSERT INTO myTable (title, value) VALUES (:title, :value)";
//$statement = $db->prepare($insert);
//
//// Bind parameters to statement variables
//$stmt->bindParam(':title', $title);
//$stmt->bindParam(':value', $value);
//
//// Insert all of the items in the array
//foreach ($data as $item) {
//    $title = $item['title'];
//    $message = $item['value'];
//
//    $stmt->execute();
//}
//
//
//
/////////////////////////////////
///// ///////////////////////////////
/////
/////
//
//
//// Set default timezone
//date_default_timezone_set('UTC');
//
//try {
//    /**************************************
//     * Create databases and                *
//     * open connections                    *
//     **************************************/
//
//    // Create (connect to) SQLite database in file
//    $file_db = new PDO('sqlite:messaging.sqlite3');
//    // Set errormode to exceptions
//    $file_db->setAttribute(PDO::ATTR_ERRMODE,
//        PDO::ERRMODE_EXCEPTION);
//
//    // Create new database in memory
//    $memory_db = new PDO('sqlite::memory:');
//    // Set errormode to exceptions
//    $memory_db->setAttribute(PDO::ATTR_ERRMODE,
//        PDO::ERRMODE_EXCEPTION);
//
//
//    /**************************************
//     * Create tables                       *
//     **************************************/
//
//    // Create table messages
//    $file_db->exec("CREATE TABLE IF NOT EXISTS messages (
//                    id INTEGER PRIMARY KEY,
//                    title TEXT,
//                    message TEXT,
//                    time INTEGER)");
//
//    // Create table messages with different time format
//    $memory_db->exec("CREATE TABLE messages (
//                      id INTEGER PRIMARY KEY,
//                      title TEXT,
//                      message TEXT,
//                      time TEXT)");
//
//
//    /**************************************
//     * Set initial data                    *
//     **************************************/
//
//    // Array with some test data to insert to database
//    $messages = array(
//        array('title' => 'Hello!',
//            'message' => 'Just testing...',
//            'time' => 1327301464),
//        array('title' => 'Hello again!',
//            'message' => 'More testing...',
//            'time' => 1339428612),
//        array('title' => 'Hi!',
//            'message' => 'SQLite3 is cool...',
//            'time' => 1327214268)
//    );
//
//
//    /**************************************
//     * Play with databases and tables      *
//     **************************************/
//
//    // Prepare INSERT statement to SQLite3 file db
//    $insert = "INSERT INTO messages (title, message, time)
//                VALUES (:title, :message, :time)";
//    $stmt = $file_db->prepare($insert);
//
//    // Bind parameters to statement variables
//    $stmt->bindParam(':title', $title);
//    $stmt->bindParam(':message', $message);
//    $stmt->bindParam(':time', $time);
//
//    // Loop thru all messages and execute prepared insert statement
//    foreach ($messages as $m) {
//        // Set values to bound variables
//        $title = $m['title'];
//        $message = $m['message'];
//        $time = $m['time'];
//
//        // Execute statement
//        $stmt->execute();
//    }
//
//    // Prepare INSERT statement to SQLite3 memory db
//    $insert = "INSERT INTO messages (id, title, message, time)
//                VALUES (:id, :title, :message, :time)";
//    $stmt = $memory_db->prepare($insert);
//
//    // Select all data from file db messages table
//    $result = $file_db->query('SELECT * FROM messages');
//
//    // Loop thru all data from messages table
//    // and insert it to file db
//    foreach ($result as $m) {
//        // Bind values directly to statement variables
//        $stmt->bindValue(':id', $m['id'], SQLITE3_INTEGER);
//        $stmt->bindValue(':title', $m['title'], SQLITE3_TEXT);
//        $stmt->bindValue(':message', $m['message'], SQLITE3_TEXT);
//
//        // Format unix time to timestamp
//        $formatted_time = date('Y-m-d H:i:s', $m['time']);
//        $stmt->bindValue(':time', $formatted_time, SQLITE3_TEXT);
//
//        // Execute statement
//        $stmt->execute();
//    }
//
//    // Quote new title
//    $new_title = $memory_db->quote("Hi''\'''\\\"\"!'\"");
//    // Update old title to new title
//    $update = "UPDATE messages SET title = {$new_title}
//                WHERE datetime(time) >
//                datetime('2012-06-01 15:48:07')";
//    // Execute update
//    $memory_db->exec($update);
//
//    // Select all data from memory db messages table
//    $result = $memory_db->query('SELECT * FROM messages');
//
//    foreach ($result as $row) {
//        echo "Id: " . $row['id'] . "\n";
//        echo "Title: " . $row['title'] . "\n";
//        echo "Message: " . $row['message'] . "\n";
//        echo "Time: " . $row['time'] . "\n";
//        echo "\n";
//    }
//
//
//    /**************************************
//     * Drop tables                         *
//     **************************************/
//
//    // Drop table messages from file db
//    $file_db->exec("DROP TABLE messages");
//    // Drop table messages from memory db
//    $memory_db->exec("DROP TABLE messages");
//
//
//    /**************************************
//     * Close db connections                *
//     **************************************/
//
//    // Close file db connection
//    $file_db = null;
//    // Close memory db connection
//    $memory_db = null;
//} catch (PDOException $e) {
//    // Print PDOException message
//    echo $e->getMessage();
//}
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//

$db = null; // Closes a database connection