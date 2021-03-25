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
};
