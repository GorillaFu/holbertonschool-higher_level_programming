#!/usr/bin/node

const ID = process.argv[2];
const URL = 'https://swapi-api.hbtn.io/api/films/' + ID;
const request = require('request');
request(URL, function (error, reponse, body) {
  if (!error) {
    const info = JSON.parse(body);
    console.log(info.title);
  }
});
