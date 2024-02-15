#!/usr/bin/node
function addMeMaybe(x, theFunction)
{
	theFunction(++x);
}
module.exports.addMeMaybe = addMeMaybe;
