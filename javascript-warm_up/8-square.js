#!/usr/bin/node
const numberEnter = parseInt(process.argv[2]);

const square = 'X';
if (!numberEnter) {
  console.log('Missing size');
} else {
  for (let i = 0; i < numberEnter; i++) {
    console.log(square.repeat(numberEnter));
  }
}
