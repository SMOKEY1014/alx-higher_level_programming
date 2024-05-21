#!/usr/bin/node

const fs = require('fs');
const path = process.argv[2];
const content = process.argv[3];

if (!path || !content) {
  console.error('Usage: node 1-writeme.js <file-path> <string_to_write>');
  process.exit(1);
}
fs.writeFile(path, content, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
