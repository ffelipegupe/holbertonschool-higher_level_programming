#!/usr/bin/node

const request = require('request');
const fpath = require('fs');

request(`${process.argv[2]}`, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const bod = body;
    fpath.writeFile(`./${process.argv[3]}`, bod, 'utf8', (err) => {
	    if (err) {
        console.log(err);
	    }
    });
  }
});
