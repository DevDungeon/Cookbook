<?php /*
# index.php

A single-file Symfony app

https://symfony.com/doc/current/configuration/micro_kernel_trait.html#a-single-file-symfony-application

```bash
composer.phar require symfony/config symfony/http-kernel \
  symfony/http-foundation symfony/routing \
  symfony/dependency-injection symfony/framework-bundle

  # These might be needed too for routing
  symfony/yaml doctrine/annotations
```

To run locally:

```bash
cd public/
php -S localhost:9000 index.php
```

To run with Apache's .htaccess:

```
# .htaccess
RewriteEngine On
RewriteBase /
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule ^(.+)$ index.php [QSA,L]
```

*/
use Symfony\Bundle\FrameworkBundle\Kernel\MicroKernelTrait;
use Symfony\Component\DependencyInjection\Loader\Configurator\ContainerConfigurator;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpKernel\Kernel;
use Symfony\Component\Routing\Loader\Configurator\RoutingConfigurator;

require __DIR__ . '/vendor/autoload.php';

class MyKernel extends Kernel
{
    use MicroKernelTrait;

    /**
     * # Register the bundles (required)
     *
     * You must specify what bundles to load. This is required and at minimum
     * includes the Symfony Framework Bundle itself.
     *
     * https://symfony.com/doc/current/bundles.html
     *
     * Alternatively, the bundles can be defined in `config/bundles.php` like this:
     *
     * ```php
     * <?php
     *   // config/bundles.php
     *   return [Symfony\Bundle\FrameworkBundle\FrameworkBundle::class => ['all' => true]];
     * ```
     *
     * @return array
     */
    public function registerBundles(): array
    {
        return [new \Symfony\Bundle\FrameworkBundle\FrameworkBundle()];
    }

    /**
     * # Define configuration (required)
     *
     * You must provide the configuration/settings for Symfony. At minimum, should provide `framework.secret`.
     *
     * Alternatively, this data can be configured in `config/packages/framework.yaml`
     *
     * For example:
     *
     * ```yaml
     * # config/packages/framework.yaml
     * # https://symfony.com/doc/current/reference/configuration/framework.html
     * framework:
     *     secret: '%env(APP_SECRET)%'
     *     #csrf_protection: true
     *     http_method_override: false
     * # Enables session support. Note that the session will ONLY be started if you read or write from it.
     * # Remove or comment this section to explicitly disable session support.
     * session:
     *     handler_id: null
     *     cookie_secure: auto
     *     cookie_samesite: lax
     *     storage_factory_id: session.storage.factory.native
     * #esi: true
     * #fragments: true
     * php_errors:
     *     log: true
     * when@test:
     *    framework:
     *         test: true
     *         session:
     *             storage_factory_id: session.storage.factory.mock_file
     * ```
     */
    protected function configureContainer(ContainerConfigurator $c): void
    {
        // Provide all the app settings
        $c->extension('framework', [
            'secret' => 'S0ME_SECRET',
        ]);

        // If using controllers, register all classes in /src/ as service
        // $c
        //     ->services()
        //     ->load('App\\', __DIR__ . '/../src/*')
        //     ->autowire()
        //     ->autoconfigure();
        
    }

    /**
     * # Define the routes (required)
     *
     * https://symfony.com/doc/current/routing.html
     *
     * Alternatively, routes can be defined in `config/routes.yaml`, `config/routes.xml`,
     * or defined as annotations or attributes on the controller methods.
     *
     * ## Define routes with annotations
     *
     * ```bash
     * composer require doctrine/annotations
     * ```
     * And then add this config:
     *
     * ```yaml
     * # config/routes/annotations.yaml
     * # Tells Symfony to look for routes defined
     * # in annotations inside the controller file
     * # and inside the Kernel file
     * controllers:
     *     resource: ../../src/Controller/
     *     type: annotation
     *
     * kernel:
     *     resource: ../../src/Kernel.php
     *     type: annotation
     * ```
     *
     * ## Define routes with YAML
     *
     * Instead of using annotations, routes can be defined in YAML or XML.
     * For example: `config/routes.yaml`.
     *
     * ```yaml
     * # config/routes.yaml
     * blog_list:
     *     path: /blog
     *     # the controller value has the format 'controller_class::method_name'
     *     controller: App\Controller\BlogController::list
     *
     *     # if the action is implemented as the __invoke() method of the
     *     # controller class, you can skip the '::method_name' part:
     *     # controller: App\Controller\BlogController
     * ```
     *
     * @param RoutingConfigurator $routes
     * @return void
     */
    protected function configureRoutes(RoutingConfigurator $routes): void
    {
        $routes
            ->add('random_number', '/random/{limit}')
            ->controller([$this, 'randomNumber']);
    }

    /**
    
        */

    /**
     * Example controller action
     *
     * @param integer $limit
     * @return JsonResponse
     */
    public function randomNumber(int $limit): JsonResponse
    {
        return new JsonResponse([
            'number' => random_int(0, $limit),
        ]);
    }
}


$kernel = new MyKernel('dev', true); // vs 'prod'
$request = Request::createFromGlobals();
$response = $kernel->handle($request);
$response->send();
$kernel->terminate($request, $response);
