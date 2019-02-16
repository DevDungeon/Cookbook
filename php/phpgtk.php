<?php
    function doshutdown() {
        gtk::main_quit();
    }

    function btnClick($button) {
        print "Hello, console!\n";
    }

    $window =& new GtkWindow();
    $window->connect("destroy", "doshutdown");
    $button =& new GtkButton("Hello, GTK!");
    $button->connect("clicked", "btnClick");
    $window->add($button);
    $window->show_all();

    gtk::main();
?>