#!/usr/bin/node
// This script demonstrates creating and modifying an object in JavaScript;
// It defines an object `myObject` with properties `type` and `value`,
// and dynamically adds a method `incr` to increment its `value`

const myObject = {
  type: 'object',
  value: 12
};

console.log(myObject);

// Adds the 'incr' method to 'myObject' which increases the 'value' by 1
myObject.incr = function () {
  this.value += 1;
};

myObject.incr();  // Increments the value to 13
console.log(myObject);

myObject.incr();  // Increments the value to 14
console.log(myObject);

myObject.incr();  // Increments the value to 15
console.log(myObject);
