#!/usr/bin/node
/* a class Rectangle that defines a rectangle */

class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
    if ((w <= 0) || (h <= 0)) {
      this.width = undefined;
      this.height = undefined;
    }
  }
}

module.exports = Rectangle;
