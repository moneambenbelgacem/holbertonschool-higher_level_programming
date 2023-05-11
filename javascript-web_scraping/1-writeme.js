#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2];
const strToWrite = process.argv[3];

function writeToFile (filePath, str) {
  try {
    fs.writeFileSync(filePath, str, 'utf8');
  } catch (err) {
    console.log(err);
  }
}

writeToFile(filePath, strToWrite);
