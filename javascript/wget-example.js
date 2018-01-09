const wget = require('wget');

let url = 'http://www.google.com';
let outputFilename = 'test.txt';

wget.download(url, outputFilename);
