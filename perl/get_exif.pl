#!/usr/bin/perl

use Image::ExifTool qw(:Public);
my $info = ImageInfo('0550942555.jpg');
foreach (keys %$info) {
	print "$_ => $$info{$_}\n"
}


=alt comment
Or with

se Image::ExifTool;
my $exifTool = new Image::ExifTool;
my $info = $exifTool->ImageInfo('image.jpg');

=cut

