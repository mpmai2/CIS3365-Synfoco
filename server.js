// load the things we need
const express = require('express');
const bodyParser  = require('body-parser');

const app = express();
app.use(bodyParser.json());
// required module to make calls to a REST API
const axios = require('axios');

// declare a variable for api endpoint (to format user input)
var api = 'http://localhost:5000/api/';


// set the view engine to ejs
// app.set("views", path.resolve(__dirname, "views"));
app.set('view engine', 'ejs');


// index page
//app.get('/', function(req, res) {
//    res.render('frontend/pages/index');
//});



app.listen(6060);
console.log('6060 is the magic port');