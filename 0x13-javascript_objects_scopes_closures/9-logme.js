#!/usr/bin/node
// prints item and number of times its printed
exports.logMe = (function (item) {
  let num = 0;
  return function (item) { return console.log('%d: %s', num++, item); };
}
)();
