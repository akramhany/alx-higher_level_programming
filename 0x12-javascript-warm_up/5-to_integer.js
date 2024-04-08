#!/usr/bin/node

const { argv } = require('process');

if (isNaN(parseInt(argv[2]))) {
  console.log('Not a number');
} else {
  console.log(parseInt(argv[2]));
}
