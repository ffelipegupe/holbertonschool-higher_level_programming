#!/usr/bin/node

const fpath = require('fs');

fpath.writeFile(`${process.argv[2]}`, `${process.argv[3]}`, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
