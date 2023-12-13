#!/usr/bin/node

const dict = require('./101-data.js').dict;

const mydict = {};

for (const UserId in dict) {
  const occurrences = dict[UserId];

  if (!(occurrences in mydict)) {
    mydict[occurrences] = [];
  }

  mydict[occurrences].push(UserId);
}
console.log(mydict);
