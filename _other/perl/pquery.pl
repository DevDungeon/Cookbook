# pQuery.pl - Sample jQuery like DOM searching

use pQuery;

pQuery("http://www.devdungeon.com/archive")
	->find("a")
	->each(sub {
	    my $i = shift;
	    my $pObj = pQuery($_);
	    print $i, ") ", $pObj->text, "\n";
	});