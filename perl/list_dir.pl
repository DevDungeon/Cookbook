#!/usr/bin/perl

my $directory = '/tmp';

opendir (DIR, $directory) or die $!;

while (my $filename = readdir(DIR)) {
	
	#only files
	next unless (-f "$directory/$filename");

	#regex only .jpg
	next unless($filename =~ m/\.jpg$/);

	print "$filename\n";
	
}


closedir(DIR);
exit 0;
