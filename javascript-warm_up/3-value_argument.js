#!/usr/bin/node
// This script checks if a command-line argument is provided and prints it;
// If not, it prints 'No argument'

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}

