#!/usr/bin/node
// script that prints sum of two numbers

const first = parseInt(process.argv[2]);
const second = parseInt(process.argv[3]);

function add (a, b) {
  return a + b;
}
console.log(add(first, second));
