// index.js
// where your node app starts

// init project
var express = require('express');
var app = express();

// enable CORS (https://en.wikipedia.org/wiki/Cross-origin_resource_sharing)
// so that your API is remotely testable by FCC 
var cors = require('cors');
app.use(cors({optionsSuccessStatus: 200}));  // some legacy browsers choke on 204

// http://expressjs.com/en/starter/static-files.html
app.use(express.static('public'));

// http://expressjs.com/en/starter/basic-routing.html
app.get("/", function (req, res) {
  res.sendFile(__dirname + '/views/index.html');
});


// your first API endpoint... 
app.get("/api/:time", function (req, res) {
  let apiDate = new Date(req.params.time);
  let apiTimestamp = 0;
  
  // check if the date is valid
  if(isNaN(apiDate.valueOf())) {
    // invalid date format, use unix timestamp in milliseconds as number
    apiTimestamp = parseInt(req.params.time);
    apiDate = new Date(apiTimestamp);
  } else {
    // valid date, set timestamp
    apiTimestamp = apiDate.getTime();
  }

  res.json({unix: apiTimestamp, utc: apiDate.toUTCString() });
});



// listen for requests :)
var listener = app.listen(process.env.PORT, function () {
  console.log('Your app is listening on port ' + listener.address().port);
});
