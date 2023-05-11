#!/usr/bin/node

const args = process.argv.slice(2);

const passedInt = parseInt(args[0]);

if (!isNaN(passedInt)) {
  for (let i = 0; i < passedInt; i++) {
    console.log('C is fun');
  }
} else console.log('Missing number of occurrences');
