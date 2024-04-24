#!/usr/bin/node
/* a script that prints the addition of 2 integers */

function add (a, b) {
  a = parseInt(a);
  b = parseInt(b);

  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    console.log(a + b);
  }
}

if (process.argv.length !== 4) {
  console.log('NaN');
} else {
  add(process.argv[2], process.argv[3]);
}
