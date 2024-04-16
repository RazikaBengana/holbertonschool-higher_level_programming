#!/usr/bin/node
// This script counts the number of times a specified element appears in a given array

exports.nbOccurences = function (list, searchElement) {
  return list.filter(x => x === searchElement).length;
};
