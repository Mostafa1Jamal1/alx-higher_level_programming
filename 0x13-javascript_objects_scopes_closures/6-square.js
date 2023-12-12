#!/usr/bin/node
const Square1 = require('./5-square');

module.exports = class Square extends Square1 {
  constructor(size) {
    super(size);
  }
  // prints the rectangle using the character c
  // If c is undefined, use the character X
  charPrint(c) {
    // check the character c
    let chr = c;
    if (!c) {
      chr = 'X';
    }
    // create a row
    let row = '';
    for (let i = 0; i < this.width; i++) {
      row = row + chr;
    }
    // print the Square
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
};
