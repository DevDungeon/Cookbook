const cheerio = require('cheerio');

let $ = cheerio.load('<html><head></head><body><div id="content"><div id="sidebar"></div><div id="main"><div id="breadcrumbs"></div><table id="data"><tr><th>Name</th><th>Address</th></tr><tr><td class="name">John</td><td class="address">Address of John</td></tr><tr><td class="name">Susan</td><td class="address">Address of Susan</td></tr></table></div></div></body></html>');

$('#data .name').each(function() {
    console.log($(this).text());
});


// var request = require('request');
// request('http://devdungeon.com/archive', function(err, resp, body) {
//     if (err) throw err;
//     // Load string containing the HTML document
//     // $ can be used just like jQuery
//     $ = cheerio.load(body);
// });



// For each link
// $('.view-blog-archive a').each(function() {
//     console.log($(this).text());
// });



// Find all links that end with a specific file extension (.xml)
// $('a').each(function() {
//     url = ($(this).attr('href'));
//     if (typeof url == 'string') {
//         extension = url.split('.').pop();
//         if (extension == 'xml') {
//             console.log('Found a XML link ' + url)
//         }
//     }
// });
