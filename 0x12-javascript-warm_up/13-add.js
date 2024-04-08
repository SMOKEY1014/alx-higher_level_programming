#!/usr/bin/node

const arg1 = process.argv[2];

const a = parseInt(arg1);

const arg2 = process.argv[3];

const b = parseInt(arg2);

const add = (a, b) => {
        if (!isNaN(a) && !isNaN(b)) {
                return (a + b);
        } else {
                console.log(NaN);
        }
}
module.exports.add = add;
