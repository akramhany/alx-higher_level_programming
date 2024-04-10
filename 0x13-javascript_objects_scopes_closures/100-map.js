#!/usr/bin/node

const list = require('./100-data').list;

const newList = list.map((x, indx) => x * indx);

console.log(list);
console.log(newList);
