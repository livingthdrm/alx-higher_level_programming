#!/usr/bin/node
/* a script that computes and prints a factorial */

function factorial (a) {
  if ((a === 1) || (a === 0)) {
    return 1;
  } else {
    return (a * factorial(a - 1));
  }
}

if (process.argv.length !== 3) {
  console.log('1');
} else if (parseInt(process.argv[2], 10)) {
  console.log(factorial(process.argv[2]));
} else {
  console.log('1');
}
