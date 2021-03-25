#!/usr/bin/node
// returns number of matches in list

exports.nbOccurences = function (list, searchElement) {
  let match = 0;
  for (const x in list) {
    if (list[x] === searchElement) {
      match++;
    }
  }
  return (match);
};
