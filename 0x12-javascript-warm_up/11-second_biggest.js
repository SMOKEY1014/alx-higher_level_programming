#!/usr/bin/node

const Arg = process.argv;
let myArr = [];

for(i = 2; i < Arg.length; i++){
	if(isNaN(Arg[i])){
		return;
	}
	myArr.push(parseInt(Arg[i]));
}
if(myArr.length < 2){
	return console.log(0);
}
myArr.sort();

return console.log(myArr[myArr.length - 2]);
