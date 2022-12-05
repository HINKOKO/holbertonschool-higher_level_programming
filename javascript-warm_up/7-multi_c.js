#!/usr/bin/node
const x = process.argv[2];
if (x && isNaN(x) === false) {
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
