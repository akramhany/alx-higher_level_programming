#!/usr/bin/node

const { argv } = require('process');

if (isNaN(+argv[2])) {
  console.log('Not a number');
} else {
  console.log(+argv[2]);
}
