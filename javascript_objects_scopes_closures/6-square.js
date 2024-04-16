#!/usr/bin/node
// This script defines a class Square that extends the Rectangle class;
// It includes a constructor for square dimensions and a method to print the square using a specified character

const Rectangle = require('./5-square');

class Square extends Rectangle {
  constructor (size) {  // Constructor takes a size parameter to set both width and height of the square
    super(size, size);  // Call the parent class (Rectangle) constructor
  }

  charPrint (c) {  // Method to print the square using a character
    if (c === undefined) {  // If no character is provided, use 'X' as the default
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {  // Loop through each line
      console.log(c.repeat(this.width));  // Print the character repeated to the width of the square
    }
  }
}
module.exports = Square;  // Export the Square class so it can be used in other files
