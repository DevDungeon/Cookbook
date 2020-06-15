<?php
/**
 * Rename all tables with a prefix if it does not already have one.
 */
// if (php_sapi_name() !== 'cli') { die("Can only be executed from CLI"); }

$host = 'localhost';
$dbname = 'my_db_name';
$user = 'root';
$pass = '$ecret!';
$prefix = 'drupal_';

if (file_exists('settings.local.php')) {
    require_once('settings.local.php');
}

try {
    $db = new PDO("mysql:host=$host;dbname=$dbname", $user, $pass);
} catch (PDOException $e) {
    echo $e->getMessage();
}

// Select all table names from a database
$query = 'SHOW TABLES';
if ($response = $db->query($query)) {
    while ($table_name = $response->fetchColumn(0)) {
        if (substr($table_name, 0, 7) != $prefix) {
            echo "Renaming $table_name to $prefix$table_name<br />";
            $statement = "RENAME TABLE $table_name TO $prefix$table_name";
            $db->exec($statement);
        } else {
            echo "Not renaming table: $table_name<br />";
        }
    }
}
?>
<html>
<body>
<?= print_r($db) ?>
</body>
</html>
