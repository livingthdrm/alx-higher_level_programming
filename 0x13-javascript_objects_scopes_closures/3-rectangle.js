#!/usr/bin/node
/* a class Rectangle that defines a rectangle */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { this.width = w; }
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      process.stdout.write('X');
      for (let j = 1; j < this.width; j++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }
}

module.exports = Rectangle;
