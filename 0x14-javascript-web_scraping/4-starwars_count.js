#!/usr/bin/node

const request = require('request');

request(`${process.argv[2]}`, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const film = JSON.parse(body).results;
    console.log(film.reduce((count, el) => {
	    el.characters.forEach(e => {
        if (e.includes('18')) {
		    count++;
        }
	    });
	    return count;
    }, 0));
  }
});
