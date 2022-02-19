<?php
require '../framework.php';




$posts = get_posts();

ob_start(); ?>
    <h2>Posts</h2>
    <ul>
    <?php foreach ($posts as $post): ?>
        <li>
            <a href="/post_view.php?id=<?=$post['id']?>"><?= $post['title'] ?></a>
            (<a href="/post_delete.php?id=<?=$post['id']?>">Delete</a>)
            (<a href="/post_edit.php?id=<?=$post['id']?>">Edit</a>)
        </li>
    <?php endforeach; ?>
    </ul>
<?php
$content = ob_get_clean();



require '../template.php'; ?>


