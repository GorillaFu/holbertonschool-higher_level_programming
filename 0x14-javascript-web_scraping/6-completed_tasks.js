#!/usr/bin/node

const URL = process.argv[2];
const request = require('request');
request(URL, function (err, response, body) {
  if (!err) {
    const json = JSON.parse(body);
    const task = {};
    for (const x in json) {
      const data = json[x];
      if (data.completed === true) {
        const id = data.userId;
        if (id in task) {
          task[id]++;
        } else {
          task[id] = 1;
        }
      }
    }
    console.log(task);
  }
});
