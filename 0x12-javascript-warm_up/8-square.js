#!/usr/bin/node
const myint = parseInt(process.argv[2]);
if (!myint) {
  console.log('Missing size');
} else {
  let row = 'X';
  for (let i = 1; i < myint; i++) {
    row += 'X';
  } for (let i = 0; i < myint; i++) {
    console.log(row);
  }
}
