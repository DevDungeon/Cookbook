#!/usr/bin/perl
use Device::SerialPort;
my $port = Device::SerialPort->new("/dev/ttyUSB3");

$port->baudrate(9600);
$port->databits(8);
$port->parity("none");
$port->stopbits(1);

$port->write("\nBegin perl serial listener\n");

    while (1) {
        my $char = $port->lookfor();
        if ($char) {
            print "Received character: $char \n";
        }
        $port->lookclear; # needed to prevent blocking
        sleep (1);
    }

