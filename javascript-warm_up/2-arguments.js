#!/usr/bin/node
const arguments = process.argv.slice(2);

if (process.argv.length === 2) {
    console.log('No argument')
} else if (process.argv.length === 3) {
    console.log('Argument found');
};

if (process.argv.length === 4) {
    console.log('Argument found');
};

if (process.argv.length === 5) {
    console.log('Arguments found');
};
