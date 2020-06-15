<?php
/**
 * List enabled modules and highlight any important modules that may be missing.
 */
$important_modules = [ // Modules I think are important to have on for most situations
    'hash',
    'json',
    'session',
    'PDO',
    'pdo_sqlite',
    'pdo_mysql',
    'curl',
    'openssl',
    'gd',
    'Phar',
];
$loaded_modules = get_loaded_extensions();
?>
<html>
<body>

<h1>Loaded Modules</h1>

<?php foreach ($important_modules as $important_module): ?>
    <?php if (!in_array($important_module, $loaded_modules)): ?>
        <span style="color: red;">Missing module: <?=$important_module?></span><br />
    <?php endif; ?>
<?php endforeach; ?>

<ul>
    <?php foreach ($loaded_modules as $module): ?>
        <li><?= $module ?></li>
    <?php endforeach; ?>
</ul>

</body>
</html>