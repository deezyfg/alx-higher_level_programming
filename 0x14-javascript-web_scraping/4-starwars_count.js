#!/usr/bin/node
// Counts films with the given character ID

const request = require('request');
const url = process.argv[2];
let num = 0;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    content.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(18)) {
          num += 1;
        }
      });
    });
    console.log(num);
  }
});
