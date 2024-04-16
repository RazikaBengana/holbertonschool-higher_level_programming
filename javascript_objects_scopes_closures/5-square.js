#!/usr/bin/node
// This script defines a Square class that extends a Rectangle class;
// It requires the Rectangle definition from another file and redefines the constructor to support square properties,
// making both sides of the rectangle equal to the given size;
// It then makes the Square class available for import

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size); // Call the parent class constructor with both height and width set to 'size', specific to squares
  }
}
module.exports = Square; // Export the Square class so it can be required in other files

