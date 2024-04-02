#!/usr/bin/env node
const fs = require('fs');
const request = require('request');

const [url, filePath] = process.argv.slice(2);

request(url, (err, response, body) => {
  fs.writeFile(filePath, body, 'utf8', () => {});
  if (err) {
    console.log(err);
  }
});
