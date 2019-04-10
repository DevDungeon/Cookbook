#!/usr/bin/perl
use Glib::Object::Introspection;
Glib::Object::Introspection->setup (
	basename => 'Notify',
	version => '0.7',
	package => 'Notify');
Notify->init;
my $hello = Notify::Notification->new("Hello world!", "This is an example notification.", "dialog-information");
$hello->show;
