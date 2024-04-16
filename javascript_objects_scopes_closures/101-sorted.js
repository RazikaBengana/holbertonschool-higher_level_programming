#!/usr/bin/node
// This script imports a dictionary from a module and inverts its key-value pairs;
// It maps each value to a list of keys that originally mapped to that value

const dict = require('./101-data').dict;
console.log(Object.entries(dict).reduce(function (accumulator, current) {
  accumulator[current[1]] = (accumulator[current[1]] || []).concat(current[0]);
  return accumulator;
}, {}));
