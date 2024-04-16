#!/usr/bin/node
// This script checks the number of command line arguments passed and prints a message based on that count

if (process.argv.length === 2) {
  // If only one argument (the script file name), print "No argument"
  console.log('No argument');
} else if (process.argv.length === 3) {
  // If one additional argument is passed, print "Argument found"
  console.log('Argument found');
} else {
  // If more than one additional argument is passed, print "Arguments found"
  console.log('Arguments found');
}
