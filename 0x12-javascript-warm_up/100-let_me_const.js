#!/usr/bin/node
/* a file that modifies the value of myVar to 333 */

exports.myVar = () => {
	global.myVar = 333;
}

exports.myVar();
