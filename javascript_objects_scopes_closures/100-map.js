#!/usr/bin/node
const list = require('./100-data').list;

const listMapped = list.map((elm, idx) => elm * idx);
console.log(list);
console.log(listMapped);
