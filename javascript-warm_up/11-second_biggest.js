#!/usr/bin/node
// This script calculates the 2nd highest number from the command line arguments provided

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.map(Number) // Convert command line arguments to numbers
    .slice(2, process.argv.length) // Ignore the first two arguments (node path and script path)
    .sort((a, b) => a - b); // Sort the numbers in ascending order
  console.log(args[args.length - 2]); // Output the 2nd highest number
}
