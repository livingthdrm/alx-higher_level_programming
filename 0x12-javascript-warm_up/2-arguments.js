#!/usr/bin/node
/* a script that prints a message depending of the 
 * numbe rod arguments passed */

const { argv } = require('node:process');

if (process.argv.length == 2) {
	console.log('No argument');
}
else if (process.argv.length == 3) {
	console.log('Argument found');
}
else {
	console.log('Arguments found');
}
