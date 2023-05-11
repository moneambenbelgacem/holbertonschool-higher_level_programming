#!/usr/bin/node

const args = process.argv.slice(2);

const passedInt = parseInt(args[0]);

if (!isNaN(passedInt)) {
  let myString = '';

  for (let i = 0; i < passedInt; i++) {
    if (i !== 0) myString += '\n';

    for (let j = 0; j < passedInt; j++) {
      myString += 'X';
    }
  }
  console.log(myString);
} else console.log('Missing size');
