<?php
require '../framework.php';


if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    add_post(e($_POST['title']), e($_POST['content']));
    header('Location: /');
    
}


ob_start(); ?>
    <h1>Add post</h1>
    <form method="POST">
        <label for="title">Title</label>
        <input type="text" id="title" name="title" />
        <br />
        <label for="content">Content</label>
        <input type="text" id="content" name="content" />
        <br />
        <button type="submit">Submit</button>
    </form>
<?php $content = ob_get_clean();
require '../template.php';