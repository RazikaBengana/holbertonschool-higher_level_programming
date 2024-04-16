#!/usr/bin/node
// This script defines a Rectangle class that can be used to create rectangle objects with specified width and height;
// It includes a print method to visually represent the rectangle using the 'X' character

class Rectangle {
  constructor (w, h) {
    // Constructor that initializes a rectangle only if both width (w) and height (h) are greater than zero
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    // Method to print the rectangle using the 'X' character
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle; // Export the Rectangle class so it can be imported in other files
