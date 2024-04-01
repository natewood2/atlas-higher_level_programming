#!/usr/bin/node
const request = require('request');
const movie_title = process.argv[2];
const api = `https://swapi-api.hbtn.io/api/films/${movie_title}`;

request(api, { json: true }, (error, response, body) => {
    console.log(body.title);
});
