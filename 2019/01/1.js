function fuel(x) {
    return Math.floor(x/3) - 2;
}

let fin = require("fs");
const data = fin.readFileSync('input.txt', 'utf8').toString().split('\n').filter(x => x);

let sum = 0;
for (x of data) 
    sum += fuel(x);

console.log(sum);