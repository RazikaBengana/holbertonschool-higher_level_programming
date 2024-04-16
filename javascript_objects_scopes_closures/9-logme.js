#!/usr/bin/node
// This script is designed to log each item with its index;
// The index increments after each log

let index = 0;
exports.logMe = function (item) {
  console.log(`${index}: ${item}`);
  index = index + 1;
};
