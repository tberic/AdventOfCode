let fin = require("fs");
const data = fin.readFileSync('input.txt', 'utf8').toString().split(',').filter(x => x).map(x => parseInt(x));
data[1] = 12;
data[2] = 2;

for (let i = 0; i < data.length; i += 4) {
    
}