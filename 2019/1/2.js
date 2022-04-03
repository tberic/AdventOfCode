function fuel(x) {
    var y = Math.floor(x/3) - 2;
    if (y <= 0) 
        return 0;
    return y+fuel(y);
}

var fin = require("fs");
const data = fin.readFileSync('input.txt', 'utf8').toString().split('\n').filter(x => x);

var sum = 0;
for (x of data) 
    sum += fuel(x);

console.log(sum);