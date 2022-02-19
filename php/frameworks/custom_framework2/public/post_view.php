<?php
require '../framework.php';

$post = get_post($_GET['id']);

ob_start(); ?>
<h1><?=$post['title']?></h1>
<p>(<a href="/post_edit.php?id=<?=$post['id']?>">Edit</a>)</p>
<p><?=$post['content']?></p>
<?php $content = ob_get_clean();

require '../template.php';