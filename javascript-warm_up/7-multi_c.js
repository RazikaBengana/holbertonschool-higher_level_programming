#!/usr/bin/node
// This script checks if the second command-line argument is a number;
// If not, it outputs an error message;
// Otherwise, it prints "C is fun" the specified number of times

const line = 'C is fun';

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log(line);
  }
}

