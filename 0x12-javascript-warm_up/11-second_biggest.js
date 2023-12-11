#!/usr/bin/node

const argv = process.argv.slice(2);

if (argv.length < 2) {
  console.log(0);
} else {
  let biggest = Number(argv[1]);
  let secBig = Number(argv[0]);
  for (const i of argv) {
    const num = Number(i);
    if (num > biggest) {
      secBig = biggest;
      biggest = num;
    }
  }
  console.log(secBig);
}
