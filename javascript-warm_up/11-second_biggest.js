#!/usr/bin/node

const numsArray = process.argv.slice(2);
let secondMax = 0;
if (numsArray.length > 1) {
// we provide a compare function, to prevent incorrect result
// if numbers sorted as strings, 25 would be greater than 100
  secondMax = numsArray.sort(function (a, b) { return b - a; })[1];
}
console.log(secondMax);
