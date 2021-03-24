#!/usr/bin/node
// print if arguments
const ments = process.argv.length;
if (ments === 2) {
  console.log('No argument');
} else if (ments === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
