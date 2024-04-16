#!/usr/bin/node
// This script reads a file specified by the command line argument and prints its contents to the console;
// It uses Node.js's file system module to asynchronously read file data

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (err, data) {

  if (err) {
    console.log(err);  // Log any errors encountered during file reading to the console

  } else {
    process.stdout.write(data);  // Write the file content to stdout if no errors occur
  }
});
