#!/usr/bin/node
// This script checks if the first command line argument is a number and prints a message accordingly

if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(process.argv[2]));
}
