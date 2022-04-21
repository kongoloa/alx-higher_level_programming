#!/usr/bin/node

/**
 * prints a message depending of the number of arguments passed
 */

let x = process.argv.length;
if (x === 2) {
  console.log('No argument');
} else if (x === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
