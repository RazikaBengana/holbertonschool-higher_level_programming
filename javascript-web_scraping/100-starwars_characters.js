#!/usr/bin/node
// This script retrieves film data from the Star Wars API (SWAPI)
// and prints character names based on a film ID passed via command line arguments

const request = require('request');
const FILM_URL = `http://swapi.co/api/films/${process.argv[2]}`;

request(FILM_URL, function (error, response, body) {

  if (error) {
    throw new Error(error);
  }

  for (const url of JSON.parse(body).characters) {
    request(url, (error, response, body) =>
      !error && console.log(JSON.parse(body).name));
  }
});
