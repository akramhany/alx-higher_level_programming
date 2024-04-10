#!/usr/bin/node

const fs = require('fs');
const { argv } = require('process');

const fileOneContent = fs.readFileSync(argv[2], 'utf8');
const fileTwoContent = fs.readFileSync(argv[3], 'utf8');

fs.writeFileSync(argv[4], fileOneContent + fileTwoContent);
