#!/usr/bin/node
/* a script that searches the
 * second biggest integer in the list of arguments. */
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const argument = [];
  for (let i = 2; i <= process.argv.length; i++) {
    argument.push(process.argv[i]);
  }

  argument.sort((a, b) => b - a);
  console.log(argument[1]);
}
