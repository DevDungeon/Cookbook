var request = require('request');
var cheerio = require('cheerio');

request('http://cheat-sheets.org/', function(err, resp, body) {
	if (err)
		throw err;
	$ = cheerio.load(body);

	

	console.log(body);
});
