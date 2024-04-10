#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};

for (const val of Object.values(dict)) {
  newDict[val] = [];
}

for (const [key, val] of Object.entries(dict)) {
  newDict[val].push(key);
}

console.log(newDict);
