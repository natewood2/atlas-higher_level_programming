#!/usr/bin/node
const request = require('request');
const movieTitle = process.argv[2];
const api = `https://swapi-api.hbtn.io/api/films/${movieTitle}`;

request(api, { json: true }, (error, response, body) => {
  console.log(body.title);
});
