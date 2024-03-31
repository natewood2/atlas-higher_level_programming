#!/usr/bin/node
const filePath = process.argv[2];
const fs = require('fs');

fs.readFile(filePath, 'utf-8', function (err, data) {
  if (err) {
    throw err;
  }
  console.log(data);
});
