<?php
require '../framework.php';

delete_post((int)$_GET['id']);

header('Location: /');