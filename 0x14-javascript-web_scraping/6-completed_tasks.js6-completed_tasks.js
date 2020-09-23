#!/usr/bin/node

const request = require('request');

request(`${process.argv[2]}`, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const arr = JSON.parse(body);
    console.log(arr.reduce((obj, el) => {
	    if (el.completed) {
        obj[el.userId]
          ? obj[el.userId]++
          : obj[el.userId] = 1;
	    }
	    return obj;
    }, {}));
  }
});
