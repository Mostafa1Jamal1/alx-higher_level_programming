#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (!err) {
    const obj = JSON.parse(body);
    const films = obj.results;

    let num = 0;
    for (const film in obj.results) {
      const chrs = films[film].characters
        .map(chr => chr.split('/')[5]);

      if (chrs.includes('18')) {
        num++;
      }
    }
    console.log(num);
  }
});
