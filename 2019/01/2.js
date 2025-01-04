function fuel(x) {
    let y = Math.floor(x/3) - 2;
    if (y <= 0) 
        return 0;
    return y+fuel(y);
}

let fin = require("fs");
const data = fin.readFileSync('input.txt', 'utf8').toString().split('\n').filter(x => x);

let sum = 0;
for (x of data) 
    sum += fuel(x);

console.log(sum);