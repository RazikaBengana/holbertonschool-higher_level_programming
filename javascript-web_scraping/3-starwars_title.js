#!/usr/bin/node
// This script retrieves the title of a movie from the Star Wars API using a movie ID passed as a command line argument

const args = process.argv;
const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + args[2], function (err, request) {

  if (err) throw err;

  const json = JSON.parse(request.body);
  console.log(json.title);
});

