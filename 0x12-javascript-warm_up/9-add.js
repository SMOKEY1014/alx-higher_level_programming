#!/usr/bin/env node

const arg1 = process.argv[2];

const num1 = parseInt(arg1);

const arg2 = process.argv[3];

const num2 = parseInt(arg2);

if (!isNaN(num1) && !isNaN(num2)) {
	console.log(num1 + num2);
} else {
	console.log(NaN);
}
