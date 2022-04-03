let fin = require("fs");
const data = fin.readFileSync('input.txt', 'utf8');
let fout = require("fs");
fout.writeFileSync('output.txt', data);