#!/usr/bin/node

// class Rectangle
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // prints the rectangle using the character X
  print () {
    let shape = '';
    for (let i = 0; i < this.width; i++) {
      shape += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(shape);
    }
  }
};
