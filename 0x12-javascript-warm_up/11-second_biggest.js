#!/usr/bin/node

const { argv } = require('process');

if (argv.length === 2 || argv.length === 3) {
  console.log(+'0');
} else {
  const arr = [];
  for (let i = 2; i < argv.length; i++) {
    arr.push(+argv[i]);
  }
  arr.sort();
  console.log(arr[arr.length - 2]);
}
