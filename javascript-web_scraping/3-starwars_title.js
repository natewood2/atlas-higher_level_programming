#!/usr/bin/node
const request = require('request');
const movieTitle = process.argv[2];
const api = `https://swapi-api.hbtn.io/api/films/${movieTitle}`;

if (!movieTitle) {
  console.log("Please enter movie ID.");
  process.exit(1);
}

request(api, { json: true }, (err, response, body) => {
  if (err) throw err;
  console.log(body.title);
});
