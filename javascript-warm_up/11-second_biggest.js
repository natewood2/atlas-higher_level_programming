#!/usr/bin/node
const numberEnter = process.argv.slice(2).map(Number);
if (numberEnter.length === 1) {
  console.log('0');
} else if (numberEnter.length > 1) {
  numberEnter.sort((a, b) => a - b);
  const secondLargest = numberEnter[numberEnter.length - 2];
  console.log(secondLargest);
}
