#!/usr/bin/node
/* a function that increments and calls a function */

exports.addMeMaybe = (number, theFunction) => {
  number++;
  theFunction(number);
};
