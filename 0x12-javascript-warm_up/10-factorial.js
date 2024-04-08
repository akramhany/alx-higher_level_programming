#!/usr/bin/node

const { argv } = require('process');

function factorial (a) {
  if (a === 1 || a === 0) {
    return 1;
  }
  return a * factorial(a - 1);
}

if (isNaN(parseInt(argv[2]))) {
  console.log(+'1');
} else {
  console.log(factorial(parseInt(argv[2])));
}
