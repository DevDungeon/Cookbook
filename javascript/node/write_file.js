var request = require('request');
var cheerio = require('cheerio');
var fs = require('fs');

request('http://www.cheat-sheets.org/', function(err, resp, body) {
	if (err)
		throw err;
	$ = cheerio.load(body);

	var list_file = fs.createWriteStream('pdflist.txt');

	$('a').each(function() {

		url = ($(this).attr('href'));
		if (typeof url == 'string') {
			ext = url.split('.').pop();
			if (ext == 'pdf') {
				if (url[0] == '/') {
					url = 'http://cheat-sheets.org' + url;
				}

				list_file.write(url + "\n");


			}
		}
	});
	

});
