#!/usr/bin/node
if (process.argv.length <= 3) { console.log(0); } else {
  const arr = [];
  for (let i = 2; i < process.argv.length; i++) {
    arr.push(Number(process.argv[i]));
  }
  const imax = arr.indexOf(Math.max(...arr));
  arr.splice(imax, 1);
  console.log(Math.max(...arr));
}
