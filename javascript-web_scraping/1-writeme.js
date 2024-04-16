#!/usr/bin/node
// This script creates or overwrites a file with specified content provided via command line arguments

const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
