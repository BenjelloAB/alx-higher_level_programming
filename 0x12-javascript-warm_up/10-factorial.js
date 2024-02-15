#!/usr/bin/node
function factorial(number)
{
	if(n < 0)
	{
		return (-1);
	}
	if(isNaN(number) || number === 0)
		return (1);
	return (number * factorial(number - 1));
}
console.log(factorial(Number(process.argv[2])));
