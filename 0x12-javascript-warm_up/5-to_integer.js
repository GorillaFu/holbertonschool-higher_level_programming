#!/usr/bin/node
// print arg as int
const ment = parseInt(process.argv[2], 10);
if (Number.isNaN(ment)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + ment);
}
