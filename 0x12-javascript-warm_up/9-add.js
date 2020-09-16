#!/usr/bin/node
// JS Warm up

const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

function add (a, b) {
  return a + b;
}

console.log(add(num1, num2));
