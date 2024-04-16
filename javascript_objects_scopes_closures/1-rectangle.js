#!/usr/bin/node
// This script defines a Rectangle class with a constructor that initializes the width and height properties;
// It then makes the Rectangle class available for use in other modules by exporting it

class Rectangle {
  constructor (w, h) {
    this.width = w;    // Set the width of the rectangle
    this.height = h;   // Set the height of the rectangle
  }
}
module.exports = Rectangle; // Export the Rectangle class

