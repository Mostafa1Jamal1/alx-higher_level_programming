#!/usr/bin/node
const num = parseInt(process.argv[2]);
function fact (a) {
  if (!a || a === 1) {
    return 1;
  } else {
    return a * fact(a - 1);
  }
}
console.log(fact(num));
