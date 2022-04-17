#!/usr/bin/nodejs

// -------------- load packages -------------- //
// INITIALIZATION STUFF

var express = require('express')
var app = express();

var hbs = require('hbs')
app.set('view engine','hbs')

app.use(express.static('static_files'))
app.use(express.json())
app.use(express.urlencoded({extended:true}))



app.get('/', function(req,res){
    res.render('index');
});



// -------------- listener -------------- //
// // The listener is what keeps node 'alive.' 

var listener = app.listen(process.env.PORT || 8080, process.env.HOST || "0.0.0.0", function() {
    console.log("Express server started");
});