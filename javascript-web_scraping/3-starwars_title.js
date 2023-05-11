#!/usr/bin/node
const request = require('request');
const endpoint = 'https://swapi-api.hbtn.io/api/films/';

const movieID = process.argv[2];

request(endpoint + movieID, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
