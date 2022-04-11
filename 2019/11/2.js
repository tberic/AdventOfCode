const SIZE = 1000;

let relativeBase = 0;
let x = SIZE, y = SIZE;
let dir = 0;

let grid = new Array(2*SIZE+1);
let painted = new Array(2*SIZE+1);
for (let i = 0; i < 2*SIZE+1; ++i) {
    grid[i] = new Array(2*SIZE+1);
    painted[i] = new Array(2*SIZE+1);
    for (let j = 0; j < 2*SIZE+1; ++j) {
        grid[i][j] = 0;
        painted[i][j] = 0;
    }
}
grid[SIZE][SIZE] = 1;

function dirRight() {
    if (dir == 3) dir = 0;
    else dir++;
}

function dirLeft() {
    if (dir == 0) dir = 3;
    else dir--;
}

function getColor() {
    return grid[y][x];
}

function setColor(col) {
    grid[y][x] = col;
    painted[y][x] = 1;
}

function runCode(data=dataMap) {
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
            data.set( pos2(data, i+1, c), getColor() );
            i += 2;
        }
        else if (op == 4) {
            //console.log(data.get( pos(data, i+1, c) ));
            let out = data.get( pos(data, i+1, c) );
            if (outputs.length == 0) {
                setColor(out);
                outputs.push(out);
            }
            else if (outputs.length == 1) {
                if (out == 0) dirLeft();
                else if (out == 1) dirRight();
                else console.log('ERROR: output');

                if (dir == 0) y--;
                else if (dir == 1) x++;
                else if (dir == 2) y++;
                else if (dir == 3) x--;
                else console.log('ERROR: direction');

                outputs = [];
            }
            else
                console.log('ERROR: too many outputs');
            i += 2;
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
const origData = fin.readFileSync('input.txt', 'utf8').toString().split(',').filter(x => x).map(x => parseInt(x));

let dataMap = new Map();
for (let i = 0; i < origData.length; ++i)
    dataMap.set(i, origData[i]);
dataMap.set(-1, 0);

runCode();

let x1 = SIZE, x2 = SIZE, y1 = SIZE, y2 = SIZE;
for (let i = 0; i < 2*SIZE+1; ++i)
    for (let j = 0; j < 2*SIZE+1; ++j)
        if (painted[i][j]) {
            x1 = Math.min(x1, x);
            x2 = Math.max(x2, x);
            y1 = Math.min(y1, y);
            y2 = Math.max(y2, y);
        }
console.log(x1 + " " + x2 + " " + y1 + " "  + y2 );

function convert(x) {
    if (x == 0) return '.';
    return '#';
}

for (let j = y1; j <= y2+1; ++j) {
    for (let i = x1; i <= x2+1; ++i)
        process.stdout.write(convert(grid[j][i]));
    console.log();
}