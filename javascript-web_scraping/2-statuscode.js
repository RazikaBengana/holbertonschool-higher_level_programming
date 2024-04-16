#!/usr/bin/node
// This script sends a GET request to the URL provided as a command-line argument
// and prints the HTTP status code of the response

const request = require('request');

request(process.argv[2], function (_err, res) {
  console.log('code:', res.statusCode);
});

