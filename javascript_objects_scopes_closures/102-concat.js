#!/usr/bin/node
// This script reads two text files specified by command line arguments
// and concatenates their contents into a third file, also specified by a command line argument

// Include the file system module to work with the file system
const fs = require('fs');

// Read the content of the first file (argument at index 2) as a string
const textA = fs.readFileSync(process.argv[2], 'utf-8');

// Read the content of the second file (argument at index 3) as a string
const textB = fs.readFileSync(process.argv[3], 'utf-8');

// Write the concatenated result to the third file (argument at index 4)
fs.writeFileSync(process.argv[4], textA + textB, 'utf-8');
