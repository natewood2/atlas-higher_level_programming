#!/usr/bin/node
const request = require('request');
const movieTitlee = process.argv[2];
const api = `https://swapi-api.hbtn.io/api/films/${movieTitlee}`;

if (!movieTitlee) {
  console.log("Please enter movie ID.");
  process.exit(1);
}

request(api, { json: true }, (err, response, body) => {
  if (err) throw err;
  console.log(body.title);
});
