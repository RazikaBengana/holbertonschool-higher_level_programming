#!/usr/bin/node
// This script takes two command line arguments, converts them to integers, and adds them together

function add (a, b) {
  return parseInt(a) + parseInt(b);
}
console.log(add(process.argv[2], process.argv[3]));
