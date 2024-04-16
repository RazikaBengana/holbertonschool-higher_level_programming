#!/usr/bin/node
// This script defines a function 'callMeMoby' that repeatedly executes a given function 'theFunction' for 'x' times

exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
