// load the things we need
var express = require('express');
var app = express();
const bodyParser  = require('body-parser');
app.use(bodyParser.urlencoded());
// required module to make calls to a REST API
const axios = require('axios');

// declare a variable for api endpoint (to format user input)
var api = 'http://localhost:5000/api/';


// set the view engine to ejs
// app.set("views", path.resolve(__dirname, "views"));
app.set('view engine', 'ejs');


// index page
//app.get('/', function(req, res) {
//    res.render('./index');
//});



app.listen(6060);
console.log('6060 is the magic port');