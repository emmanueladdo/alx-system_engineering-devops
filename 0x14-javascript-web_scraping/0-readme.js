#!/usr/bin/node
/* The file reads and prints a file
 * The first arg is file path
 * The content of the file in utf-8
 * If an error occurred, print the error object
 */

const fs = require('fs'); // Fixed the 'require' statement and 'fs' variable

const filePath = process.argv[2];

if (!filePath) {
  console.error('Usage: ./0-readme.js <file-path>'); // Fixed the error message
  process.exit(1);
}

fs.readFile(filePath, 'utf-8', (err, data) => { // Fixed the 'err.' typo
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
