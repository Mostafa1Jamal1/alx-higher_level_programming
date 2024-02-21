#!/usr/bin/node
const fs = require('fs');
const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (!err) {
    fs.writeFile(process.argv[3], body, function (err, data) {
      if (err) {
        console.log(err);
      }
    });
  }
});
