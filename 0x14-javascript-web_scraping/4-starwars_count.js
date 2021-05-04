#!/usr/bin/node

const URL = process.argv[2]
const request = require('request');
request(URL, function (error, reponse, body) {
  if (!error) {
    const results = JSON.parse(body).results;
    let count = 0;
    for (const i of results) {
      const characters = results[i].characters;
      for (const j in characters) {
        if (characters[j].search('/18/') !== 0) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
