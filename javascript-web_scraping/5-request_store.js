#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const [url, filePath] = process.argv.slice(2);

request(url, (error, response, body) => {
  fs.writeFile(filePath, body, 'utf8', () => {});
});
