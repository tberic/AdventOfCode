let fin = require("fs");
const data = fin.readFileSync('input.txt', 'utf8').toString().split(',').filter(x => x).map(x => parseInt(x));
data[1] = 12;
data[2] = 2;

for (let i = 0; i < data.length; i += 4) {
    if (data[i] == 1)
        data[data[i+3]] = data[data[i+1]] + data[data[i+2]];
    else if (data[i] == 2)
        data[data[i+3]] = data[data[i+1]] * data[data[i+2]];
    else if (data[i] == 99)
        break;    
}

console.log(data[0]);