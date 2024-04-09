#!/usr/bin/node

const mySquare = require("./5-square");

module.exports = class Square extends mySquare {
  charPrint(c) {
    if (!c) {
      c = "X";
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
