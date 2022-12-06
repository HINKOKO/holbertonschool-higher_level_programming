#!/usr/bin/node
exports.esrever = function (list) {
  return list.map(list.pop, [...list]);
};

// # another method to do it
// return list.map((item, idx) => list[list.length - 1 - idx]);

// # or do it this way ==>
// ---------------------
// use const instead of let ,because let allows datatypes to be changed
// behavior we probably don't want with an array
//   const revList = []; ([] or new Array())
//   for (let i = list.length - 1; i >= 0; i--) {
//     revList.push(list[i]);
//   }
//   return revList;
// };
