#!/usr/bin/node

const argv = process.argv.slice(2);

if (argv.length < 2) {
  console.log(0);
} else {
  let biggest = parseInt(argv[0]);
  let secBig;
  for (const i of argv) {
    const num = parseInt(i);
    if (num > biggest) {
      secBig = biggest;
      biggest = num;
    }
  }
  console.log(secBig);
}
