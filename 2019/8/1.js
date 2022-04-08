const w = 25;
const h = 6;

function pos(layer, i, j) {
    return layer*w*h + i*w + j;
}

let fin = require("fs");
const line = fin.readFileSync('input.txt', 'utf8').toString().trim().split('').map(x => parseInt(x));

const layers = line.length / (w*h);

let minLayer;
let leastZeros = w*h;

for (let layer = 0; layer < layers; ++layer) {
    let zeros = 0;    
    for (let i = 0; i < h; ++i)
        for (let j = 0; j < w; ++j)    
            if (!line[pos(layer, i, j)])
                zeros++;
    
    if (zeros < leastZeros) {
        leastZeros = zeros;
        minLayer = layer;
    }
}

let ones = 0, twos = 0;
for (let i = 0; i < h; ++i)
    for (let j = 0; j < w; ++j)    
        if (line[pos(minLayer, i, j)] == 1)
            ones++;
        else if (line[pos(minLayer, i, j)] == 2)
            twos++;

console.log(ones*twos);