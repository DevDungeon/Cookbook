#!/usr/bin/perl

use Minecraft::RCON;

my $rcon = Minecraft::RCON->new({
	address		=> 'blockalicious.com',
	port		=> 25565,
	password	=> "",
});

if ($rcon->connect) {
	print $rcon->command('help');
} else {
	print "Error connecting";
}
$rcon->disconnect;
