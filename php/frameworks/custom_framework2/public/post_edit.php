<?php
require '../framework.php';

$post_id = (int)$_GET['id'];

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    update_post($post_id, e($_POST['title']), e($_POST['content']));
    header('Location: /');
}


$post = get_post($post_id);


ob_start(); ?>
    <h1>Edit post</h1>
    <form method="POST">
        <label for="title">Title</label>
        <input type="text" id="title" name="title" value="<?=$post['title']?>" />
        <br />
        <label for="content">Content</label>
        <input type="text" id="content" name="content" value="<?=$post['content']?>" />
        <br />
        <button type="submit">Submit</button>
    </form>
<?php $content = ob_get_clean();

require '../template.php';