#!/usr/bin/node
// print first arg
let ment = 0;
process.argv.forEach(() => {
  ment += 1;
});
if (ment === 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
