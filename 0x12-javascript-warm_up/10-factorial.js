#!/usr/bin/node
/* a script that computes and prints a factorial */

function factorial(a) {
	let result = a;
	if (isNaN(a)){
		console.log('NaN');
	}
	else {
		result *= factorial(a - 1);
	}
	return result;
}

factorial(process.argv[2]);
