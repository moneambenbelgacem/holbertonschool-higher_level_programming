#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2];

function printFileContent (filePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf8');
    console.log(content);
  } catch (err) {
    console.log(err);
  }
}

printFileContent(filePath);
