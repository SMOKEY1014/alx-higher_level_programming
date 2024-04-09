#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let rectChar;
    for (let i = 0; i < this.height; i++) {
      rectChar = '';
      for (let j = 0; j < this.width; j++) {
        rectChar += 'X';
      }
      console.log(rectChar);
    }
  }

  rotate () {
    const tempSwap = this.width;
    this.width = this.height;
    this.height = tempSwap;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
