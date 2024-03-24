#!/usr/bin/node
const numofArgs = process.argv.slice(2);
const numberEnter = parseInt(numofArgs[0], 10);

if (!numberEnter) {
  console.log('Missing number of occurrences');
} else {
    for (let i = 0; i < numberEnter; i++) {
      console.log('C is fun');
    }
}
