#!/usr/bin/node

const args = process.argv.slice(2);

const passedInt = parseInt(args[0]);

function factorial (x) {
  return x === 0 ? 1 : x * factorial(x - 1);
}

console.log(isNaN(passedInt) ? 1 : factorial(passedInt));
