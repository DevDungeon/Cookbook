<?php
/**
 * ## References
 *
 * - Bootstrap website: https://getbootstrap.com/
 * - Bootstrap CDN: https://www.bootstrapcdn.com/
 * - jQuery CDN: https://code.jquery.com/
 * - Bootstrap Icons (Find CSV copy to copy directly to file): https://icons.getbootstrap.com/
 * - Add Free Icons to a Web App (FontAwesome): https://www.devdungeon.com/content/add-free-icons-web-app
 * - Get Started with Google Fonts API: https://developers.google.com/fonts/docs/getting_started
 */
//

//
// ?>
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!--<meta name="description" content="">-->
    <!--<meta name="author" content="">-->
    <!--<meta name="generator" content="">-->
    <!-- Preferred URL for search engines to use, query params, with or w/o www, https or not, slash at end or not -->
    <!--<link rel="canonical" href="https://www.example.com/this/path/">-->

    <title>Home</title>

    <!-- Bootstrap CSS -->
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
    <!-- jQuery -->
    <script
            src="https://code.jquery.com/jquery-3.5.1.min.js"
            integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0="
            crossorigin="anonymous"></script>
    <!-- Bootstrap JS -->
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js"
            integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI"
            crossorigin="anonymous"></script>

    <!-- Favicons -->
    <link rel="icon" href="/favicon.php" sizes="32x32" type="image/png">
    <meta name="theme-color" content="#444444">

    <script>
        $(document).ready(function () {
            // alert("Ready!");
        });
    </script>

    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Ubuntu">
    <style>
        body {
            font-family: Ubuntu, sans-serif;
            padding-top: 5rem;
            background-color: #222222;
            color: #DDDDDD;
        }

        a {
        }

        a:hover {
        }

        a:visited {
        }

        .table {
            color: #DDDDDD
        }

        nav {

        }


        /* Extra small devices (phones, 600px and down) */
        @media only screen and (max-width: 600px) {
        }

        /* Small devices (portrait tablets and large phones, 600px and up) */
        @media only screen and (min-width: 600px) {
        }

        @media only screen and (min-width: 768px) {
        }

        /* Large devices (laptops/desktops, 992px and up) */
        @media only screen and (min-width: 992px) {
        }

        /* Extra large devices (large laptops and desktops, 1200px and up) */
        @media only screen and (min-width: 1200px) {
        }
    </style>
</head>

<body>

<nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
    <a class="navbar-brand" href="/">Home</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault"
            aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarsExampleDefault">
        <ul class="navbar-nav mr-auto">

            <li class="nav-item active">
                <a class="nav-link" href="#">Home</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#">Link</a>
            </li>
            <li class="nav-item">
                <a class="nav-link disabled" href="#">Disabled</a>
            </li>
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="http://example.com" id="dropdown01" data-toggle="dropdown"
                   aria-haspopup="true" aria-expanded="false">Dropdown</a>
                <div class="dropdown-menu" aria-labelledby="dropdown01">
                    <a class="dropdown-item" href="#">Action</a>
                    <a class="dropdown-item" href="#">Another action</a>
                    <a class="dropdown-item" href="#">Something else here</a>
                </div>
            </li>

        </ul>
        <form class="form-inline my-2 my-lg-0">
            <input class="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        </form>
    </div>
</nav>

<main role="main" class="container">

    <h1>Welcome</h1>
    <p class="lead">Welcome to the site</p>

    <div class="row">
        <div class="col-md-4">
            <p>Something</p>
            <a href="#" class="btn btn-primary">Click</a>
        </div>
        <div class="col-md-4">
            <p>Something</p>
            <a href="#" class="btn btn-primary">Click</a>
        </div>
        <div class="col-md-4">
            <p>Something</p>
            <a href="#" class="btn btn-primary">Click</a>
        </div>
    </div>

</main><!-- /.container -->

</body>

</html>
