#!/usr/bin/node
// rectangle class w constructor
// includes width and height params
// if no arguments or neg args dont define obj
module.exports = class Rectangle {
  constructor (w, h) {
    if (w !== undefined && w > 0 && h !== undefined && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // print method
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  //swaps vals of heght and width
  rotate () {
    const store = this.width;
    this.width = this.height;
    this.height = store;
  }

  //doubles height and wdth of rect
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
