#!/usr/bin/node
const args = process.argv.slice(2);

const ArgisInt = parseInt(args[0], 10);

if (isNaN(ArgisInt)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${ArgisInt}`);
}
