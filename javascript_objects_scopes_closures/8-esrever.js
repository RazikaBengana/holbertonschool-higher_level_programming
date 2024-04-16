#!/usr/bin/node
// This script defines a function to reverse the elements of an array

exports.esrever = function (list) {
  const reversedArray = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversedArray.push(list[i]);
  }
  return reversedArray;
};
