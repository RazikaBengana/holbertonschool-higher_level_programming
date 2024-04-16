#!/usr/bin/node
// This script makes an HTTP request to a URL provided as the first command line argument
// and writes the response body to a file specified as the second command line argument

const request = require('request');
const fs = require('fs');

request(process.argv[2], function (_err, _res, body) {

  fs.writeFile(process.argv[3], body, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
