#!/usr/bin/node

const args = process.argv.slice(2);

const printArg = args[0];

if (printArg === undefined) {
  console.log('No argument');
} else {
  console.log(printArg);
}
