require('dotenv').config();
const express = require('express');
const cors = require('cors');
const app = express();

// use replit database
const Database = require("@replit/database");

// use crypto for md5 hashing urls
const crypto = require('crypto');

// use body parser to get body POST data
let bodyParser = require('body-parser');

// use valid url to check for valid http/https urls
var validUrl = require('valid-url');

// create instance of replit database
const db = new Database();

// Basic Configuration
const port = process.env.PORT || 3000;

app.use(cors());

app.use('/public', express.static(`${process.cwd()}/public`));

// use body parser to be able to get POST data
app.use(bodyParser.urlencoded({ extended: false }));

app.get('/', function(req, res) {
  res.sendFile(process.cwd() + '/views/index.html');
});

// shorturl API endpoint (GET)
app.get('/api/shorturl/:shortUrlKey', function(req, res) {
  let shortUrlKey = req.params.shortUrlKey;
  let longUrl = '';

  // check if short url key is in database
  db.get(shortUrlKey).then(value => {
    // get long url
    longUrl = value;
    console.log(shortUrlKey, longUrl);

    // redirect to long url
    res.redirect(301, longUrl);
  });
});

// shorturl API endpoint (POST)
app.post('/api/shorturl', function(req, res) {
  // get long url from POST body data
  let longUrl = req.body.url;

  console.log(longUrl);

  // check if url is valid (http/https)
  if (validUrl.isHttpUri(longUrl) || validUrl.isHttpsUri(longUrl)) {
    let shortUrlKey = crypto.createHash('md5').update(longUrl).digest('hex');
  
    // save short url key in database
    db.set(shortUrlKey, longUrl).then(() => {});

    // valid url, return original url and short url
    res.json({ original_url: longUrl, short_url: shortUrlKey });
  } else {
    // invalid url, return error
    res.json({ error: 'invalid url' });
  }
});

app.listen(port, function() {
  console.log(`Listening on port ${port}`);
});
