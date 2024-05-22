#!/usr/bin/node
/*
 * script that reads a file's content
 */
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
