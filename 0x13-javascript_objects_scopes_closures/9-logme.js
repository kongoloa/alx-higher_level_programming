#!/usr/bin/node
/**
 * A function that prints the number of arguments already printed and the new argument value
 */

let countArg = 0;
exports.logMe = function (item) {
  console.log(countArg + ': ' + item);
  countArg++;
};
