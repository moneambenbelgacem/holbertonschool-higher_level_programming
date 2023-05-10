#!/usr/bin/node

const add = (a, b) => a + b;

const args = process.argv.slice(2);

const a = parseInt(args[0]);
const b = parseInt(args[1]);

console.log(add(a, b));
