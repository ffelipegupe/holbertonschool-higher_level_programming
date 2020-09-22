#!/usr/bin/node

const fpath = require('fs');

fpath.readFile(`${process.argv[2]}`, (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data.toString('utf8'));
  }
});
