#!/usr/bin/node

const list = require('./100-data.js').list;

mylist = list.map((num, index) => num * index);

console.log(list);
console.log(mylist);
