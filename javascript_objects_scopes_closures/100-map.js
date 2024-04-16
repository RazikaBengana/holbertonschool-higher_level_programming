#!/usr/bin/node
// This script imports a list from a module and prints the list and a new list
// where each element is multiplied by its index

const list = require('./100-data').list;
console.log(list);
console.log(list.map((element, index) => element * index));
