#!/usr/bin/node
// function that returns the number of occurrences in a list

exports.esrever = function (list) {
  const reversed = [];
  for (const i in list) {
    reversed.unshift(list[i]);
  }
  return (reversed);
};
