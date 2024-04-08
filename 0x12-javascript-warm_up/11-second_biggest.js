#!/usr/bin/node

const { argv } = require('process');

if (argv.length === 2 || argv.length === 3) {
  console.log(+'0');
} else {
  const arr = [];
  for (let i = 2; i < argv.length; i++) {
    arr.push(+argv[i]);
  }
  arr.sort(function (a, b) { return a - b; });
  let i = arr.length - 1;
  while (i >= 0 && arr[i] === arr[arr.length - 1]) {
    i--;
  }
  if (i >= 0) {
    console.log(arr[i]);
  } else {
    console.log(+'0');
  }
}
