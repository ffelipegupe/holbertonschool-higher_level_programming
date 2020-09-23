#!/usr/bin/node

const request = require('request');

request(`http://swapi.co/api/films/${process.argv[2]}`, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const chars = JSON.parse(body).characters;
    chars.forEach(char => {
      request(char, (err, response, body) => {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
