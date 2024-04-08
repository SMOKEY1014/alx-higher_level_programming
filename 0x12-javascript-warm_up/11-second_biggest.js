#!/usr/bin/node

const Arg = process.argv;
const myArr = [];

for (let i = 2; i < Arg.length; i++) {
  myArr.push(parseInt(Arg[i]));
}

if (myArr.length < 2) {
  console.log(0);
  process.exit(0);
}

myArr.sort();
console.log(myArr[myArr.length - 2]);
