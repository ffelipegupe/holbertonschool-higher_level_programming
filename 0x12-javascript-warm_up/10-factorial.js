#!/usr/bin/node
// JS Warm up

const arg = parseInt(process.argv[2]);
function factorial (n) {
  if (isNaN(n)) {
    return 1;
  } else {
    return (n !== 1) ? n * factorial(n - 1) : 1;
  }
}
console.log(factorial(arg));
