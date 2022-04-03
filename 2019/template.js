var fin = require("fs");
const data = fin.readFileSync('input.txt', 'utf8');
var fout = require("fs");
fout.writeFileSync('output.txt', data);