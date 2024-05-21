#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

if (!url) {
  console.error('Usage: node 2-statuscode.js <URL>');
  process.exit(1);
}

request(url, (err, responce) => {
  if (err) {
    console.error('Error:', err);
    return;
  }
  console.log('code:', responce.statusCode);
});
