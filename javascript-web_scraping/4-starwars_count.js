#!/usr/bin/env node
const request = require('request');

const apiUrl = 'https://swapi-api.hbtn.io/api/films/';

request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;

    films.forEach(film => {
      film.characters.forEach(url => {
        if (url.includes('/18/')) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
