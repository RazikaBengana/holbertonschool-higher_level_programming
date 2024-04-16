#!/usr/bin/node
// This script calculates the factorial of a number passed as a command-line argument;
// Factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n

function factorial (n) {
  if ((isNaN(n)) || (n === 1)) {
    return 1; // Return 1 because the factorial of 1 is 1
  } else {
    return n * factorial(n - 1); // Recursive call to compute the factorial
  }
}
// Parse the second command line argument as an integer and prints its factorial
console.log(factorial(parseInt(process.argv[2])));
