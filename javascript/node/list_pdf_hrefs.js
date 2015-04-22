var request = require('request');
var cheerio = require('cheerio');

request('http://www.cheat-sheets.org/', function(err, resp, body) {
	if (err)
		throw err;
	$ = cheerio.load(body);

	//console.log(body);

	$('a').each(function() {

		url = ($(this).attr('href'));
		if (typeof url == 'string') {
			ext = url.split('.').pop();
			if (ext == 'pdf') {
				if (url[0] == '/') {
					url = 'http://cheat-sheets.org' + url;
				}
				console.log(url);
			}
		}
	});
	

});
