#!/usr/bin/node
// rectangle class w constructor
// includes width and height params
// if no arguments or neg args dont define obj
const SquareR = require('./5-square');

class Square extends SquareR {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
