#!/usr/bin/node
if (isNaN(process.argv[2])) { console.log('Missing size'); } else {
  const rows = Number(process.argv[2]);
  const cols = Number(process.argv[2]);

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      process.stdout.write('X');
    }
    console.log();
  }
}
