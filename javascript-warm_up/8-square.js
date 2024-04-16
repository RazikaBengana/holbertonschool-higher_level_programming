#!/usr/bin/node
// This script checks if the first command line argument is not a number;
// If it's not a number, it logs 'Missing size';
// If it is a number, it prints a square of 'X' characters,
// where each side of the square has a length equal to the provided number

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log('X'.repeat(parseInt(process.argv[2])));
  }
}
