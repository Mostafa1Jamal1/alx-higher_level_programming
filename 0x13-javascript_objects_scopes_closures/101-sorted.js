#!/usr/bin/node

const dict = require('./101-data.js').dict;

const mydict = {};
// create pairs of occurrences and empty list
for (const UserId in dict) {
  const occurrences = dict[UserId];
  mydict[occurrences] = [];
}
// add to the empty list the user id
for (const UserId in dict) {
  const occurrences = dict[UserId];
  mydict[occurrences].push(UserId);
}

console.log(mydict);
