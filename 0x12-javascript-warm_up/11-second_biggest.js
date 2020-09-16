#!/usr/bin/node
// JS Warm up

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const arr = process.argv.slice(2).sort((a, b) => a - b);
  console.log(arr[arr.length - 2]);
}
