const w = 25;
const h = 6;

function pos(layer, i, j) {
    return layer*w*h + i*w + j;
}

let fin = require("fs");
const line = fin.readFileSync('input.txt', 'utf8').toString().trim().split('').map(x => parseInt(x));

const layers = line.length / (w*h);

let image = new Array(h);
for (let i = 0; i < h; ++i)
    image[i] = new Array(w);


for (let layer = 0; layer < layers; ++layer)
    for (let i = 0; i < h; ++i)
        for (let j = 0; j < w; ++j)
            if (image[i][j] == undefined && line[pos(layer, i, j)] != 2)
                image[i][j] = line[pos(layer, i, j)];


//console.log(image);

function convert(c) {
    return c ? '*' : ' ';
}

let s = "";
for (let i = 0; i < h; ++i) {
    for (let j = 0; j < w; ++j) 
        s += convert(image[i][j]);
    s += "\n";
}
console.log(s);