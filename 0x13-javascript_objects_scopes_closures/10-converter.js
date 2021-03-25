#!/usr/bin/node
// converts base 10 to specfied base
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
