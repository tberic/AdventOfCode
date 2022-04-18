let relativeBase = 0;

function runCode(i, input, data=dataMap) {    
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
            data.set( pos2(data, i+1, c), input );
            i += 2;
        }
        else if (op == 4) {
            //console.log(data.get( pos(data, i+1, c) ));
            let out = data.get( pos(data, i+1, c) );
            //outputs.push(out);
            i += 2;
            return {output: out, index: i};
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
const { deflateRaw } = require("zlib");
const origData = fin.readFileSync('input.txt', 'utf8').toString().split(',').filter(x => x).map(x => parseInt(x));

let dataMap = new Map();
for (let i = 0; i < origData.length; ++i)
    dataMap.set(i, origData[i]);
dataMap.set(-1, 0);

//let inst = runCode(0, 1);

const SIZE = 100;
const OFFSET = SIZE / 2;
let grid = new Array(SIZE).fill(' ').map(() => new Array(SIZE).fill(' '));
let visited = new Array(SIZE).fill(0).map(() => new Array(SIZE).fill(0));


/*
ret = runCode(i, 3);
i = ret.index;
ret = runCode(i, 3);
i = ret.index;
ret = runCode(i, 3);
i = ret.index;
ret = runCode(i, 3);
*/
let dir = [ [], [-1, 0], [1, 0], [0, -1], [0, 1] ];
let inverseDir = [ 0, 2, 1, 4, 3 ];

let minX = 0, maxX = 0, minY = 0, maxY = 0;

let i = 0, ret;
let x = 0, y = 0;
grid[OFFSET][OFFSET] = 'D';

function draw() {
    for (let y = minY-1; y <= maxY+1; ++y) {
        s = "";
        for (let x = minX-1; x <= maxX+1; ++x)
            s += grid[OFFSET + y][OFFSET + x];
        console.log(s);
    }
    console.log();
    console.log();
}

function DFS(y, x, i) {

    visited[OFFSET + y][OFFSET + x] = 1;

    minX = Math.min(minX, x);
    maxX = Math.max(maxX, x);
    minY = Math.min(minY, y);
    maxY = Math.max(maxY, y);

    for (let d = 1; d <= 4; ++d) 
        if ( grid[ OFFSET + y + dir[d][0] ][ OFFSET + x + dir[d][1] ] == ' ' )
        {
            ret = runCode(i, d); i = ret.index;
            if (ret.output == 2) {
                grid[OFFSET + y + dir[d][0]][OFFSET + x + dir[d][1]] = 'O';
                ret = runCode(i, inverseDir[d]); i = ret.index;
                //return ;
            }
            else if (ret.output == 0) {
                grid[ OFFSET + y + dir[d][0] ][ OFFSET + x + dir[d][1] ] = '#';
            }
            else if (ret.output == 1) {
                grid[ OFFSET + y + dir[d][0] ][ OFFSET + x + dir[d][1] ] = '.';
                //go back
                ret = runCode(i, inverseDir[d]); i = ret.index;

                //y += dir[d][0];
                //x += dir[d][1];
            }

        }
   
    if (!visited[OFFSET+y-1][OFFSET+x] && grid[OFFSET+y-1][OFFSET+x] == '.') {
        ret = runCode(i, 1); i = ret.index;
        DFS(y-1, x, i);
        ret = runCode(i, 2); i = ret.index;
    }
    if (!visited[OFFSET+y+1][OFFSET+x] && grid[OFFSET+y+1][OFFSET+x] == '.') {
        ret = runCode(i, 2); i = ret.index;
        DFS(y+1, x, i);
        ret = runCode(i, 1); i = ret.index;
    }
    if (!visited[OFFSET+y][OFFSET+x-1] && grid[OFFSET+y][OFFSET+x-1] == '.') {
        ret = runCode(i, 3); i = ret.index;
        DFS(y, x-1, i);
        ret = runCode(i, 4); i = ret.index;
    }
    if (!visited[OFFSET+y][OFFSET+x+1] && grid[OFFSET+y][OFFSET+x+1] == '.') {
        ret = runCode(i, 4); i = ret.index;
        DFS(y, x+1, i);
        ret = runCode(i, 3); i = ret.index;
    }
}

DFS(0, 0, 0);
draw();

visited = new Array(SIZE).fill(0).map(() => new Array(SIZE).fill(0));
let Q = [ [0, 0, 0] ];
visited[OFFSET][OFFSET] = 1;
//let x, y;
while (Q.length > 0) {
    [y, x, dist] = Q.shift();

    if (grid[OFFSET+y][OFFSET+x] == 'O') {
        console.log(`(${y}, ${x}), dist: ${dist}`);
        break;
    }

    for (let d = 1; d <= 4; ++d) 
        if ( grid[ OFFSET + y + dir[d][0] ][ OFFSET + x + dir[d][1] ] != '#' &&
            !visited[ OFFSET + y + dir[d][0] ][ OFFSET + x + dir[d][1] ]  ) {
            visited[OFFSET + y + dir[d][0]][OFFSET + x + dir[d][1]] = 1;
            Q.push( [y + dir[d][0], x + dir[d][1], dist+1] );
            }
}

// PART TWO: flood fill
visited = new Array(SIZE).fill(0).map(() => new Array(SIZE).fill(0));
visited[OFFSET + y][OFFSET + x] = 1;
Q = [ [0, y, x] ];

let time, maxTime = 0;
while (Q.length > 0) {
    [time, y, x] = Q.shift();
    grid[OFFSET + y][OFFSET + x] = 'O';

    if (time > maxTime)
        maxTime = time;

    for (let d = 1; d <= 4; ++d) 
        if ( grid[ OFFSET + y + dir[d][0] ][ OFFSET + x + dir[d][1] ] != '#' &&
            !visited[ OFFSET + y + dir[d][0] ][ OFFSET + x + dir[d][1] ]  ) {
            visited[OFFSET + y + dir[d][0]][OFFSET + x + dir[d][1]] = 1;
            Q.push( [time+1, y + dir[d][0], x + dir[d][1]] );
            }
}

draw();
console.log(maxTime);