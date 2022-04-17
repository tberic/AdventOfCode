const delay = ms => new Promise(resolve => setTimeout(resolve, ms));

async function draw() {
    function convert(c) {
        if (c == 0) return '.';
        if (c == 1) return 'X';
        if (c == 2) return '#';
        if (c == 3) return '=';
        if (c == 4) return 'o';
    }
    
    console.clear();

    let s = "";
    for (let y = 0; y < 22; ++y) {
        s = "";
        for (let x = 0; x < SIZE; ++x) 
            s += convert(grid[x][y]);
        console.log(s);
    }
    
    await delay(10);
}

function sign(x) {
    if (x == 0) return 0;
    return x/Math.abs(x);
}


let relativeBase = 0;

let ballx, bally;
let paddlex, paddley;
const SIZE = 40; //Math.max(...inst)+1;
let grid = new Array(SIZE).fill(0).map(() => new Array(SIZE).fill(0));

async function runCode(data=dataMap) {
    let i = 0;
    let outputs = [];

    while (data.get(i) != 99) {
        let a = Math.floor(data.get(i) / 10000);
        let b = Math.floor(data.get(i) / 1000) % 10;
        let c = Math.floor(data.get(i) / 100) % 10;
        let op = data.get(i) % 100;

        //console.log(i + ": " + op + "(" + a+b+c + ") "  + relativeBase);        

        if (op == 1) {
            data.set( pos2(data, i+3, a), data.get( pos(data, i+1, c) ) + data.get( pos(data, i+2, b) ) );
            i += 4;
        }
        else if (op == 2) {
            data.set( pos2(data, i+3, a), data.get( pos(data, i+1, c) ) * data.get( pos(data, i+2, b) ) );
            i += 4;
        }
        else if (op == 3) {
            //console.log('INPUT DETECTED@' + i);
            data.set( pos2(data, i+1, c), sign(ballx - paddlex) );            
            //await draw();
            i += 2;
        }
        else if (op == 4) {
            //console.log(data.get( pos(data, i+1, c) ));
            let out = data.get( pos(data, i+1, c) );
            outputs.push(out);
            if (outputs.length == 3) {
                //console.log(outputs);
                if (outputs[0] == -1 && outputs[1] == 0)
                    console.log(outputs[2]);
                else
                    grid[outputs[0]][outputs[1]] = outputs[2];

                if (outputs[2] == 4) {
                    ballx = outputs[0];
                    bally = outputs[1];
                }
                if (outputs[2] == 3) {
                    paddlex = outputs[0];
                    paddley = outputs[1];
                }

                outputs = [];
            }
            i += 2;

            //draw();
        }
        else if (op == 5) {
            if (data.get( pos(data, i+1, c) ))
                i = data.get( pos(data, i+2, b) );
            else
                i += 3;
        }
        else if (op == 6) {
            if (!data.get( pos(data, i+1, c) ))
                i = data.get( pos(data, i+2, b) );
            else
                i += 3;
        }
        else if (op == 7) {
            data.set( pos2(data, i+3, a), +(data.get( pos(data, i+1, c) ) < data.get( pos(data, i+2, b) )) );
            i += 4;
        }
        else if (op == 8) {
            data.set( pos2(data, i+3, a), +(data.get( pos(data, i+1, c) ) == data.get( pos(data, i+2, b) )) );
            i += 4;
        }
        else if (op == 9) {
            relativeBase += data.get( pos(data, i+1, c) );            
            i += 2;
        }
        else {
            console.log("ERROR");
            break;
        }
    }

    return outputs;
}


function pos(data, i, code) {
    if (code == 0)
        return (data.has(data.get(i))) ? data.get(i) : -1;
    if (code == 1)
        return i;
    if (code == 2)
        return (data.has( data.get(i) + relativeBase )) ? data.get(i) + relativeBase : -1;
}

function pos2(data, i, code) {
    if (code == 0)
        return data.get(i);
    if (code == 1)
        return i;
    if (code == 2)
        return data.get(i) + relativeBase;
}

let fin = require("fs");
const { finished } = require("stream");
const origData = fin.readFileSync('input.txt', 'utf8').toString().split(',').filter(x => x).map(x => parseInt(x));

let dataMap = new Map();
for (let i = 0; i < origData.length; ++i)
    dataMap.set(i, origData[i]);
dataMap.set(-1, 0);

dataMap.set(0, 2);
runCode();