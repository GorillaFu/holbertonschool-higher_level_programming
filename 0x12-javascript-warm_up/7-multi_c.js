#!/usr/bin/node
// script that prints cisfun

const ment = parseInt(process.argv[2]);
let idx = 0;

if (Number.isNaN(ment)) {
  console.log('Missing number of occurrences');
}
while (idx < ment) {
  console.log('C is fun');
  idx += 1;
}
