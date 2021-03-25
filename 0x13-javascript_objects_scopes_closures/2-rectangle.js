#!/usr/bin/node
// rectangle class w constructor
// includes width and height params
module.exports = class Rectangle {
    constructor (width, height) {
	if (width !== undefined && width > 0 && height !== undefined && height > 0) {
	    this.width = width;
	    this.height = height;
	}
    }
};
