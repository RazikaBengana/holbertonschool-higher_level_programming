#!/usr/bin/node
// This script defines a module that exports a 'converter' function;
// This function takes a numerical 'base' and returns a new function;
// This returned function converts a given number to a string in the specified base

exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
