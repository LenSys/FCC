const express = require('express')
const app = express()
const cors = require('cors')
require('dotenv').config()

require('dotenv').config();

let mongoose = require('mongoose');

const mongoURI = process.env['MONGO_URI'];

// connect to mongoose database
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true });

const Schema = mongoose.Schema;

// create exercises schema
const exercisesSchema = new Schema({
  userId: { type: String, required: true },
  description: { type: String, required: true },
  duration: { type: Number, required: true },
  date: {type: Date }
});

// create users schema
const usersSchema = new Schema({
  username: { type: String, required: true }
});

// create models from schemas
const ExerciseModel = mongoose.model("Exercise", exercisesSchema);
const UserModel = mongoose.model("User", usersSchema);
// const LogModel = mongoose.model("Log", logsSchema);

app.use(cors())
app.use(express.static('public'))

// use body parser to get body POST data
let bodyParser = require('body-parser');

// use body parser to be able to get POST data
app.use(bodyParser.urlencoded({ extended: false }));

/*
fs = require('fs');

app.use(({ method, url, query, params, body }, res, next) => {
  
  if(url.endsWith('logs')) {
    console.log('>>> ', method, url);
    console.log(' QUERY:', query);
    console.log(' PRAMS:', params);
    console.log('  BODY:', body);
    const _json = res.json;
    res.json = function (data) {
      console.log(' RESLT:', JSON.stringify(data, null, 2));
      return _json.call(this, data);
    };
    console.log(' ----------------------------');

    let data = {
      method,
      url,
      query,
      params,
      body
    };
    
    fs.appendFile('logs.txt', JSON.stringify(data, null, 2), function (err) {
      if (err) return console.log(err);
      console.log('Hello World > helloworld.txt');
    });
  }
  next();
});
*/

// get index html view
app.get('/', function (req, res) {
  res.sendFile(process.cwd() + '/views/index.html');
});


// get all users from mongoose database as json response
app.get('/api/users', function (req, res) {

  UserModel.find({ }, function(err, users) {
    if(err) {
        console.log(err);
        return
    }

    res.status(200).json(users);
  });
});


// post new user to mongoose database
app.post('/api/users', function (req, res) {
  userData = {
    username: req.body.username
  };
  // use a Model to create new documents using `new`:
  const userDoc = new UserModel(userData);
  userDoc.save();
//  console.log(userDoc);
  
  res.status(200).json(userDoc);
});


// get all log entries for current user id from mongoose database as json response
app.get('/api/users/:_id/logs', function (req, res) {

  let userId = req.params._id;

  let exerciseLimit = req.query.limit || 0;

  if(userId.length < 12) {
    res.status(500).json({
        error: 'Invalid user id'
    });
  }
  
  // find user data from user id
  UserModel.findById(userId, function(err, user) {
    if(err) {
        console.log(err);
        return res.status(500).json({
            error: 'Invalid user id'
        });
    }

    if(!user) {
      return res.status(500).json({
          error: 'Invalid user id'
      });
    }

    // check for valid from date
    if(typeof req.query.from !== 'undefined') {
      if (new Date(req.query.from).toDateString() == 'Invalid Date') {
        return res.status(400).json({
            error: "from query value is not a valid date. Suggested format is yyyy-mm-dd"
        });
      }
    }

    // check for valid to date
    if(typeof req.query.to !== 'undefined') {
      if (new Date(req.query.to).toDateString() == 'Invalid Date') {
        return res.status(400).json({
            error: "to query value is not a valid date. Suggested format is yyyy-mm-dd"
        });
      }
    }
    
    let exerciseSearchQuery = { 
      userId: userId 
    };
    
    if(req.query.from && req.query.to) {
      exerciseSearchQuery.date = { $gte: req.query.from, $lte: req.query.to }
    } else if(req.query.from) {
      exerciseSearchQuery.date = { $gte: req.query.from }
    } else if(req.query.to) {
      exerciseSearchQuery.date = { $lte: req.query.to }
    }
    
    // console.log(exerciseSearchQuery);
    
    // find all exercises of current user
    ExerciseModel.find(exerciseSearchQuery, function(err, exerciseData) {
      if(err) {
          console.log(err);
          return
      }

      let changedExerciseData = [];

      // iterate through all exercise data and change date format
      for (let index = 0; index < exerciseData.length; index++) {
        let data = {
          description: exerciseData[index].description,
          duration: exerciseData[index].duration,
          date: new Date(Date.parse(exerciseData[index].date)).toDateString()
        };
        
        changedExerciseData.push(data);
      }

      // create log data
      const logData = {
        "_id": userId,
        "username": user.username,
        "count": changedExerciseData.length,
        "log": changedExerciseData
      };
      
      res.json(logData);
    }).limit(exerciseLimit);
  });
});


// post exercise to mongoose database
app.post('/api/users/:_id/exercises', function (req, res) {

  let userId = req.params._id;
  
  // find username from user id
  UserModel.findById(userId, function(err, user) {
    if(err) {
        console.log(err);
        return
    }
    
    // use current date as default if date is not provided
    let exerciseDate = '';
    if(typeof req.body.date === 'undefined' || req.body.date === '') {
      exerciseDate = new Date();
    } else {
      exerciseDate = new Date(req.body.date);
    }
    
    const exerciseData = {
      userId: userId,
      date: exerciseDate.toDateString(),
      duration: parseInt(req.body.duration),
      description: req.body.description
    };

    const exerciseDoc = new ExerciseModel(exerciseData);
    exerciseDoc.save();

    // set response data
    const responseData = {
      _id: userId,
      username: user.username,
      description: exerciseDoc.description,
      duration: exerciseDoc.duration,
      date: exerciseDate.toDateString()
    };
    
    res.json(responseData);
  });
});


const listener = app.listen(process.env.PORT || 3000, () => {
  console.log('Your app is listening on port ' + listener.address().port)
})
