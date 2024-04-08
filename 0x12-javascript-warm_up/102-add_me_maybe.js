#!/usr/bin/node

function addMeMaybe (x, theFunction) {
  x++;
  return theFunction(x);
}

module.exports.addMeMaybe = addMeMaybe;
