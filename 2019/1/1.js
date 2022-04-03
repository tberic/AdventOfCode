function fuel(x) {
    return Math.floor(x/3) - 2;
}

var fin = require("fs");
const data = fin.readFileSync('input.txt', 'utf8').toString().split('\n').filter(x => x);

var sum = 0;
for (x of data) 
    sum += fuel(x);

console.log(sum);