#!/usr/bin/node

const { argv } = require('process');

if (isNaN(parseInt(argv[2]))) {
  console.log('Missing size');
} else {
  const x = parseInt(argv[2]);
  for (let i = 0; i < x; i++) {
    let str = '';
    for (let j = 0; j < x; j++) {
      str += 'X';
    }
    console.log(str);
  }
}
