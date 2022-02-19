<?php
namespace App;

use \Symfony\Component\HttpKernel\Kernel;
use \Symfony\Bundle\FrameworkBundle\Kernel\MicroKernelTrait;
use \Symfony\Component\DependencyInjection\Loader\Configurator\ContainerConfigurator;

class MyKernel extends Kernel
{
    use MicroKernelTrait;

    /**
     * Alternatively, the bundles can be defined in `config/bundles.php` like this:
     *
     * ```php
     * <?php
     *   // config/bundles.php
     *   return [\Symfony\Bundle\FrameworkBundle\FrameworkBundle::class => ['all' => true]];
     * ```
     *
     * @return array
     */
    public function registerBundles(): array
    {
        return [
            new \Symfony\Bundle\FrameworkBundle\FrameworkBundle(),
            new \Symfony\Bundle\TwigBundle\TwigBundle(),
            new \Doctrine\Bundle\DoctrineBundle\DoctrineBundle(),
            new \Symfony\Bundle\MakerBundle\MakerBundle(),
            
        ];
    }

    /**
     * Alternatively, can be defined in `config/packages/framework.yaml`.
     */
    protected function configureContainer(ContainerConfigurator $c): void
    {
        // Provide all the app settings
        $c->extension('framework', [
            'secret' => 'S0ME_SECRET',
        ]);

        // register all classes in /src/ as service
        $c
            ->services()
            ->load('App\\', __DIR__ . '/../src/*')
            ->autowire()
            ->autoconfigure();
    }
}