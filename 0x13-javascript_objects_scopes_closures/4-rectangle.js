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
    let row = '';
    for (let i = 0; i < this.width; i++) {
      row += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
  // exchanges the width and the height of the rectangle
  rotate() {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }
  // multiples the width and the height of the rectangle by 2
  double() {
    this.width *= 2;
    this.height *= 2;
  }
};
