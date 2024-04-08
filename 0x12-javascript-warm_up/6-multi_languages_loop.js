#!/usr/bin/node

const numArgs = ['JavaScript is amazing', 'Python is cool', 'C is fun'];

while (numArgs.length > 0) {
  console.log(numArgs[numArgs.length - 1]);
  numArgs.length--;
}
