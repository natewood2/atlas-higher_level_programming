#!/usr/bin/env node
const request = require('request');
const movieTitle = process.argv[2];
const api = `https://swapi-api.hbtn.io/api/films/${movieTitle}`;

if (!movieTitle) {
  console.log("Please enter movie ID.");
  process.exit(1);
}

request(api, { json: true }, (error, response, body) => {
  console.log(body.title);
});
