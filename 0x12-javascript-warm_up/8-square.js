#!/usr/bin/node
/* a script that prints a square */

if (parseInt(process.argv[2])) {
  for (let i = 0; i < process.argv[2]; i++) {
    process.stdout.write('X');
    for (let j = 1; j < process.argv[2]; j++) {
      process.stdout.write('X');
    }
    console.log();
  }
} else {
  console.log('Missing size');
}
