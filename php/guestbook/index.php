<?php
/**
 * Allow people to submit a form and the text goes to a file
 * Also print out contents of file
 */
define("GUESTBOOK_FILE", 'guestbook.txt');

function sanitize_input($string)
{
    return str_replace(array("\r\n", "\r", "\n"), "<br />", htmlspecialchars($string));
}

function store_entry_in_guestbook($text)
{
    /* File open types
    - r - read only
    - w - write only, force new file
    - a - write only with pointer at end
    - x - write only, create new file or error on existing
    - r+ - read/write, file pointer at beginning
    - w+ - read/write, force new file
    - a+ - read/write, file pointer at end
    - x+ - read/write, create new file or error on existing  */
    $file = fopen(GUESTBOOK_FILE, "a") or die("Unable to open file!");
    // https://www.php.net/manual/en/function.flock.php
    flock($file, LOCK_EX); // Get exclusive lock on file
    fwrite($file, "$_SERVER[REMOTE_ADDR]: $text<br />\n"); // Keep regular newline for human readability
    flock($file, LOCK_UN); // Release file lock
    fclose($file); // Automatically releases lock too
}

if (isset($_POST['entry'])) {
    store_entry_in_guestbook(sanitize_input($_POST['entry']));
}
?>
<html lang="en">
<body>

<div>
    <h2>Leave an entry</h2>
    <form method="POST">
        <textarea name="entry"></textarea><br />
        <input type="submit"/>
    </form>
</div>


<?php if (file_exists(GUESTBOOK_FILE)): ?>
    <div>
        <h2>Guestbook entries</h2>
        <?php readfile(GUESTBOOK_FILE); // Dumps file contents right to output buffer ?>
    </div>
<?php endif; ?>

</body>
</html>
