#!/usr/bin/node
/**
 * A function that returns the reversed version of a list
 */

exports.esrever = function (list) {
  let rev = [];
  let i = list.length - 1;
  while (i >= 0) {
    rev.push(list[i]);
    i--;
  }
  return rev;
};

