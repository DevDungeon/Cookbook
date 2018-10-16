# http_download.pl

use File::Fetch;

my $ff = File::Fetch->new(uri => 'http://www.devdungeon.com/archive');

# Fetch to cwd() if "to" value is not specified
my $where = $ff->fetch( to => './' ) or die $ff->error;

print $ff->uri, "\n";
print $ff->scheme, "\n";
print $ff->host, "\n";
print $ff->path, "\n";
print $ff->file, "\n";
