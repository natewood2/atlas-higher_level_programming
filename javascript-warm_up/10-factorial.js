#!/usr/bin/node
const numberEnter = parseInt(process.argv[2], 10);

function factorial (f) {
  if (isNaN(f) || f <= 1) {
    return 1;
  } else {
    return f * factorial(f - 1);
  }
}
const result = factorial(numberEnter)

console.log(result)
