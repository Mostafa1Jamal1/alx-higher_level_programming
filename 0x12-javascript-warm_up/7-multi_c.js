#!/usr/bin/node
const myint = parseInt(process.argv[2]);
if (!myint) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < myint; i++) {
    console.log('C is fun');
  }
}
