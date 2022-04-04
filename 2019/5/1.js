function pos(x, i, code) {
    if (code)
        return i;
    return x;
}

let fin = require("fs");
const data = fin.readFileSync('input.txt', 'utf8').toString().split(',').filter(x => x).map(x => parseInt(x));

console.log(data.length);

inputs = [1];
outputs = [];

let i = 0;
while (i < data.length) {
    let a = Math.floor(data[i] / 10000);
    let b = Math.floor(data[i] / 1000) % 10;
    let c = Math.floor(data[i] / 100) % 10;
    let op = data[i] % 100;

    if (op == 1) {
        data[data[i+3]] = data[pos(data[i+1], i+1, c)] + data[pos(data[i+2], i+2, b)];
        i += 4;
    }
    else if (op == 2) {
        data[data[i+3]] = data[pos(data[i+1], i+1, c)] * data[pos(data[i+2], i+2, b)];
        i += 4;
    }
    else if (op == 3) {
        data[data[i+1]] = inputs.pop();
        i += 2;
    }
    else if (op == 4) {
        console.log(data[pos(data[i+1], i+1, c)]);
        outputs.push(data[pos(data[i+1], i+1, c)]);        
        i += 2;
    }
    else if (op == 99)
        break;
    else {
        console.log("ERROR");
        break;
    }
}

//console.log(data[0]);