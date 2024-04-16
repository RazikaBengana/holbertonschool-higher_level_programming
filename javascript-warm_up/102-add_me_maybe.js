#!/usr/bin/node
// This script demonstrates the use of callback functions in JavaScript;
// It exports a function called 'addMeMaybe' which takes two parameters:
// 'number', an integer, and 'theFunction', a callback function;
// When invoked, 'addMeMaybe' increments the number by 1 and passes it to the callback function

exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
