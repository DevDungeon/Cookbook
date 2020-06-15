<?php
/**
 * Simple HTML list of files in a directory with links
 */

/**
 * Recursively print directory contents with links
 *
 * @param $dir_path string Current directory being looked at
 * @param $parent_dir string Path of parent dir used in recursive calls
 */
function print_dir_contents($dir_path, $parent_dir)
{
    if (is_null($parent_dir)) {
        $dir_contents = glob("*");
    } else {
        $dir_contents = glob("$dir_path/*");
    }

    foreach ($dir_contents as $item) {
        if (is_dir($item)): ?>
            <li><a href="<?=$item?>"><?=$item?>/</a></li>
            <ul>
                <?php print_dir_contents($item, $dir_path); ?>
            </ul>
        <?php else: ?>
            <li><a href="<?=$item?>"><?=str_replace($dir_path . '/', '', $item)?></a></li>
        <?php endif;
    }
}

?>

<div>
    <h2>Contents: <?php echo $_SERVER['DOCUMENT_ROOT']; ?></h2>
    <ul>
        <?php print_dir_contents($_SERVER['DOCUMENT_ROOT'], null); ?>
    </ul>
</div>