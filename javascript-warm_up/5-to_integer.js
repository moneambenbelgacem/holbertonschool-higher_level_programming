#!/usr/bin/node

const args = process.argv.slice(2);

const passedInt = parseInt(args[0]);

if (!isNaN(passedInt)) console.log('My number:', passedInt);
else console.log('Not a number');
