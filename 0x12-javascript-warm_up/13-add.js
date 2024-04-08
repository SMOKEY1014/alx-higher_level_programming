#!/usr/bin/node

const add = (a, b) => {
  if (!isNaN(a) && !isNaN(b)) {
    return (a + b);
  } else {
    console.log(NaN);
  }
};
module.exports.add = add;
