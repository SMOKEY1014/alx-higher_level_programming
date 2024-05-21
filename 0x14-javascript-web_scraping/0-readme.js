#!/usr/bin/node

const fs = require('fs');
const path = process.argv[2];

if (!path) {
  console.error('Usage: node 0-readme.js <file-path>');
  process.exit(1);
}

fs.readFile(path, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
