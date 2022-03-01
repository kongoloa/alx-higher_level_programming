#!/usr/bin/node
/**
 * A script that imports an array and computes a new array
 */

let list = require('./100-data.js').list;
console.log(list);
let newList = list.map((x, index) => x * index);
console.log(newList);
