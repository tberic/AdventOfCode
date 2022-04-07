function pos(x, i, code) {
    if (code)
        return i;
    return x;
}

function runCode(data, i, inputs) {
    let output;

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
            if (inputs.length > 0) {
                data[data[i+1]] = inputs.shift();
                i += 2;
            }
            else {
                return {seq: output, code: data, pos: i, finished: false};
            }
        }
        else if (op == 4) {
            //console.log(data[pos(data[i+1], i+1, c)]);
            output = data[pos(data[i+1], i+1, c)];
            i += 2;
            //return {seq: outputs, code: data, pos: i, finished: false};
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
        else if (op == 99) {
            //console.log("HALT");
            return {seq: output, code: data, pos: i, finished: true};
            //break;
        }
        else {
            console.log("ERROR");
            break;
        }
    }

    return {seq: output, code: data, pos: i, finished: true};
}


let fin = require("fs");
const origData = fin.readFileSync('input.txt', 'utf8').toString().split(',').filter(x => x).map(x => parseInt(x));

let max = 0;
let out = 0;
let phase = [];
let maxPhase;

for (let iA = 5; iA < 10; ++iA) if (!phase.includes(iA)) {
    phase.push(iA);
    for (let iB = 5; iB < 10; ++iB) if (!phase.includes(iB)) {
        phase.push(iB);
        
        for (let iC = 5; iC < 10; ++iC) if (!phase.includes(iC)) {
            phase.push(iC);
            
            for (let iD = 5; iD < 10; ++iD) if (!phase.includes(iD)) {
                phase.push(iD);
                
                for (let iE = 5; iE < 10; ++iE) if (!phase.includes(iE))  {
                    phase.push(iE);
                    
                    
                    out = {seq: 0, finished: false};
                    dataA = [...origData]; posA = 0;
                    dataB = [...origData]; posB = 0;
                    dataC = [...origData]; posC = 0;
                    dataD = [...origData]; posD = 0;
                    dataE = [...origData]; posE = 0;

                    out = runCode(dataA, posA, [iA, out.seq]); dataA = [...out.code]; posA = out.pos;
                    out = runCode(dataB, posB, [iB, out.seq]); dataB = [...out.code]; posB = out.pos;
                    out = runCode(dataC, posC, [iC, out.seq]); dataC = [...out.code]; posC = out.pos;
                    out = runCode(dataD, posD, [iD, out.seq]); dataD = [...out.code]; posD = out.pos;
                    out = runCode(dataE, posE, [iE, out.seq]); dataE = [...out.code]; posE = out.pos;

                    while (!out.finished) {
                        out = runCode(dataA, posA, [out.seq]); dataA = [...out.code]; posA = out.pos;
                        out = runCode(dataB, posB, [out.seq]); dataB = [...out.code]; posB = out.pos;
                        out = runCode(dataC, posC, [out.seq]); dataC = [...out.code]; posC = out.pos;
                        out = runCode(dataD, posD, [out.seq]); dataD = [...out.code]; posD = out.pos;
                        out = runCode(dataE, posE, [out.seq]); dataE = [...out.code]; posE = out.pos;
                    }                    
                    
                    if (out.seq > max) {
                        max = out.seq;
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

console.log(max);
console.log(maxPhase);