#!/usr/bin/node
class Rectangle {
  w;
  h;

  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
  double () {
    const doubleHeight = this.height * 2;
    const doubleWidth = this.width * 2;
  }
}
const rec1 = new Rectangle(4, 3);
