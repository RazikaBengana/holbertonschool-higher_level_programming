#!/usr/bin/node
// This script makes an HTTP request to the URL provided as a command line argument,
// parses the JSON response, and counts the number of completed tasks for each user

const request = require('request');
const args = process.argv;

request(args[2], function (err, response, body) {

  if (err) throw err;

  const json = JSON.parse(body);
  const dict = {};

  json.forEach(element => {
    if (element.completed) {
      if (dict[element.userId]) {
        dict[element.userId] += 1;
      } else {
        dict[element.userId] = 1;
      }
    }
  });

  console.log(dict);
});
