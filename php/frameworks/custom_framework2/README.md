# Example PHP framework

This is a very simple starting place for small apps. Start separating out files as needed when you expand.

- `framework.php` - Bootstraps things. Loads model and helper functions. Also contains the "model" aspect. Contains database connection and CRUD functions.
- `base.tpl.php` - Base HTML layout template for pages
- `public/` - Root for web server.
- `public/index.php` - Example page listing posts.

## How it works:

The web server itself acts as the router, directing requests to the right file in `public/` directory.

The PHP files in the `public/` directory act as either the controller, the view, or both. The web server itself acts as the router serving the individual PHP files. So each file is it's own controller.

At the top of each controller, if you need to do any database interaction or use any framework functions, require `framework.php`. Do whatever logic is needed after loading the framework and setting variables for the view to follow.

At the end of the controller file, be sure to define a `$content` variable and then require the `template.php` file. You could also create a separate template file and load that if you don't want to combine the controller and view. For simple pages though, you can keep the view in the controller.

Some pages may omit the "view" aspect. For example, a page that deletes an item may end with a `header('Location: /')` redirect and not need to render anything. If you have an API endpoint that returns JSON, set the MIME info with `header('Content-Type: application/json')` and then `echo json_encode($the_data);`. To return a downloadable file, set the content disposition to attachment. `header('Content-Disposition: attachment; filename=file.zip')`.

If you're page is flat static content, you can forego even loading `framework.php` and just do the "view" part by providing content for the base template.

A sample starter page/snippet might look like:

```php
<?php // public/some_page.php
require '../framework.php';

ob_start(); ?>
    <p>Hello</p>
<?php $content = ob_get_clean();

require '../template.php';
```