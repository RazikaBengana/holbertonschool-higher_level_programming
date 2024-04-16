#!/usr/bin/node
// This script demonstrates the use of objects in JavaScript;
// It creates an object, logs it, updates its value, and logs it again

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject); // Output: { type: 'object', value: 12 }
myObject.value = 89;   // Update the 'value' property of 'myObject'
console.log(myObject); // Output: { type: 'object', value: 89 }

