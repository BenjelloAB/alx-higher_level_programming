#!/usr/bin/node
if (process.argv.length > 3)
	console.log("Too many arguments");
else{
	let regex = /^\d+$/;
	if(regex.test(process.argv[2]))
			console.log("My number: ", process.argv[2]);
	else
			console.log("Not a number");
    }
