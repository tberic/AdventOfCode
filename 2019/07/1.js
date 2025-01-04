function runCode(inputs) {
    let i = 0;
    let outputs = [];

    let data = [...origData];

    while (i < data.length) {
        let a = Math.floor(data[i] / 10000);
        let b = Math.floor(data[i] / 1000) % 10;
        let c = Math.floor(data[i] / 100) % 10;
        let op = data[i] % 100;

        //console.log(op + ": " + data);

        if (op == 1) {
            data[data[i+3]] = data[pos(data[i+1], i+1, c)] + data[pos(data[i+2], i+2, b)];
            i += 4;
        }
        else if (op == 2) {
            data[data[i+3]] = data[pos(data[i+1], i+1, c)] * data[pos(data[i+2], i+2, b)];
            i += 4;
        }
        else if (op == 3) {
            data[data[i+1]] = inputs.shift();
            i += 2;
        }
        else if (op == 4) {
            //console.log(data[pos(data[i+1], i+1, c)]);
            outputs.push(data[pos(data[i+1], i+1, c)]);
            i += 2;
        }
        else if (op == 5) {
            if (data[pos(data[i+1], i+1, c)])
                i = data[pos(data[i+2], i+2, b)];
            else
                i += 3;
        }
        else if (op == 6) {
            if (!data[pos(data[i+1], i+1, c)])
                i = data[pos(data[i+2], i+2, b)];
            else
                i += 3;
        }
        else if (op == 7) {
            data[data[i+3]] = +(data[pos(data[i+1], i+1, c)] < data[pos(data[i+2], i+2, b)]);
            i += 4;
        }
        else if (op == 8) {
            data[data[i+3]] = +(data[pos(data[i+1], i+1, c)] == data[pos(data[i+2], i+2, b)]);
            i += 4;
        }
        else if (op == 99)
            break;
        else {
            console.log("ERROR");
            break;
        }
    }

    return outputs;
}


function pos(x, i, code) {
    if (code)
        return i;
    return x;
}

let fin = require("fs");
const origData = fin.readFileSync('input.txt', 'utf8').toString().split(',').filter(x => x).map(x => parseInt(x));

let max = 0;
let out = [];
let phase = [];
let maxPhase;

for (let iA = 0; iA < 5; ++iA) if (!phase.includes(iA)) {
    phase.push(iA);
    out[0] = +runCode([iA, 0]);    
    for (let iB = 0; iB < 5; ++iB) if (!phase.includes(iB)) {
        phase.push(iB);
        out[1] = +runCode([iB, out[0]]);
        for (let iC = 0; iC < 5; ++iC) if (!phase.includes(iC)) {
            phase.push(iC);
            out[2] = +runCode([iC, out[1]]);
            for (let iD = 0; iD < 5; ++iD) if (!phase.includes(iD)) {
                phase.push(iD);
                out[3] = +runCode([iD, out[2]]);
                for (let iE = 0; iE < 5; ++iE) if (!phase.includes(iE))  {
                    phase.push(iE);                    
                    out[4] = +runCode([iE, out[3]]);
                    if (out[4] > max) {
                        max = out[4];
                        maxPhase = [...phase];                    
                    }
                    phase.pop();
                }
                phase.pop();
            }
            phase.pop();
        }
        phase.pop();
    }
    phase.pop();
}


//runCode([5, 1234]);

console.log(max);
console.log(maxPhase);