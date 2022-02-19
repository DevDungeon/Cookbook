<?php
namespace App\Controller;

use \Symfony\Component\HttpFoundation\Response;
use \Symfony\Bundle\FrameworkBundle\Controller\AbstractController;


class MainController extends AbstractController
{

    public function hi()
    {
        return $this->render('main/hi.html.twig');
    }

}
