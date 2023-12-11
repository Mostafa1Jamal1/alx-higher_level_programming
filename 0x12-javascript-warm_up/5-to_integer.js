#!/usr/bin/node
const myint = parseInt(process.argv[2]);
if (!myint) {
  console.log('Not a number');
} else {
  console.log('My number:', myint);
}
