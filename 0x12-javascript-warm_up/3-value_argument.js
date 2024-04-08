#!/usr/bin/node

const Arg = process.argv;

if (Arg[2] === undefined) {
  console.log('No argument');
} else {
  console.log(Arg[2]);
}
