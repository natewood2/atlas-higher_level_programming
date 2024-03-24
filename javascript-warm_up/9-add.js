#!/usr/bin/node
function add(a, b) {
  return a + b;
}

const numbersEntered = process.argv.slice(2);

const number = parseInt(numbersEntered[0], 10);
const number2 = parseInt(numbersEntered[1], 10);

const sum = add(number, number2)

console.log(sum)
