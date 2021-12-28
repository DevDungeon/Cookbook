// Run with `node app.js`
const path = require('path')
const express = require('express')

/*********************************
 * SETUP                         *
 *********************************/

const app = express()
const port = 3000

// Serve static files from public/
app.use('/static', express.static(path.join(__dirname, 'public')))
// Set template engine
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'html');
app.set('views', path.join(__dirname, 'templates'))  // EJS HTML Templates dir


/********************************
 * PAGES                        *
 ********************************/

app.get('/', (req, res) => {
    // app.get('/', (req, res) => {
    //     console.log(req.query.somequerykey); //?somequerykey=abcdefg
    // })
    res.render('index', { title: 'hello' });
})


/********************************
 * RUN                         *
 *******************************/

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
})