#!/usr/bin/env node

const arg1 = process.argv[2];

const a = parseInt(arg1);

const arg2 = process.argv[3];

const b = parseInt(arg2);
function add (a, b) {
  if (!isNaN(a) && !isNaN(b)) {
    console.log(a + b);
  } else {
    console.log(NaN);
  }
}
add(a, b);
