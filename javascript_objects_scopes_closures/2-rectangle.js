#!/usr/bin/node
// This script defines a Rectangle class and exports it;
// The constructor checks if the provided width (w) and height (h) are greater than zero before setting the properties;
// If the dimensions are not positive, no properties are set

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
