var express = require('express');
var cors = require('cors');
require('dotenv').config()

var app = express();

app.use(cors());
app.use('/public', express.static(process.cwd() + '/public'));

// use body parser to get body POST data
let bodyParser = require('body-parser');

// use express file upload
const fileUpload = require('express-fileupload');

// use body parser to be able to get POST data
app.use(bodyParser.urlencoded({ extended: false }));

// set file upload middleware
app.use(fileUpload());


app.get('/', function (req, res) {
  res.sendFile(process.cwd() + '/views/index.html');
});

// API file analyse
app.post('/api/fileanalyse', function (req, res) {
  if (!req.files || Object.keys(req.files).length === 0) {
    return res.status(400).send('No files were uploaded.');
  }

  // get file info
  const fileInfo = {
    name: req.files.upfile.name,
    type: req.files.upfile.mimetype,
    size: req.files.upfile.size
  };
  
  console.log(req.files);
  
  res.json(fileInfo);
});


const port = process.env.PORT || 3000;
app.listen(port, function () {
  console.log('Your app is listening on port ' + port)
});
