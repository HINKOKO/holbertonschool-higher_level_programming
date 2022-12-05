#!/usr/bin/node
let current;
let max = -1;
let secondMax = -1;
if (process.argv.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    current = parseInt(process.argv[i], 10);
    if (current > max) {
      secondMax = max;
      max = current;
    } else {
      secondMax = current;
    }
  }
  console.log(secondMax);
}
