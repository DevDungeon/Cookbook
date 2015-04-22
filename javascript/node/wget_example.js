var wget = require('wget');


var src = 'http://www.google.com';
var output = 'test.txt';

var download = wget.download(src, output);

