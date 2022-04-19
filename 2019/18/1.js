let fin = require("fs");
const grid = fin.readFileSync('input.txt', 'utf8').toString().split('\n').filter( x => x );

let m = grid.length, n = grid[0].length;
let x0, y0;
for (let y = 0; y < m; ++y)
    if (grid[y].includes('@')) {
        y0 = y;
        x0 = grid[y].indexOf('@');
        break;
    }
//grid[y0][x0] = '.';

console.log(grid);

let visited = new Map();

let dirs = [ [-1, 0], [+1, 0], [0, -1], [0, +1] ];

let Q = [ [0, y0, x0, 1] ];
visited.set( [y0,x0,1].join(','), 1 );

let nKeys = countKeys();
let x, y, steps, keysCollected;
while (Q.length > 0) {
    [steps, y, x, keysCollected] = Q.shift();

    //console.log( y + " " + x + " " + steps + " " + keysCollected.toString(2));

    // if all the keys have been collected, we are finished
    if (nOnes(keysCollected) == nKeys+1) {
        console.log(steps);
        break;
    }

    for (let [dy, dx] of dirs)
        if ( possible(y+dy, x+dx, keysCollected) ) {
            //visited[y+dy][x+dx] |= keysCollected | convert(grid[y+dy][x+dx]);
            visited.set( [y+dy, x+dx, keysCollected | convert(grid[y+dy][x+dx])].join(','), 1 );
            Q.push( [steps+1, y+dy, x+dx, keysCollected | convert(grid[y+dy][x+dx])] );
        }
}


function convert(c) {
    if (c >= 'a' && c <= 'z')
        return 1 << (c.charCodeAt(0)-'a'.charCodeAt(0)+1);
    return 0;
}

function nOnes(x) {
    let n = 0;
    while (x > 0) {
        n += x%2;
        x = (x-x%2)/2;
    }
    return n;
}

function visitedKeys(y, x, keys) {
    return visited.has([y,x,keys].join(','));
}

/*
function intKeys(keys) {
    let res = 1;
    for (let k of keys) {
        let n = k.charCodeAt(0)-'a'.charCodeAt(0)+1;
        res |= 1<<n;
    }
    return res;
}
*/

function countKeys() {
    let keys = 0;
    for (let y = 0; y < m; ++y)
        for (let x = 0; x < n; ++x)
            if (grid[y][x] >= 'a' && grid[y][x] <= 'z')
                keys++;
    return keys;
}

function possible(y, x, keys) {
    if (y < 0 || y >= m) return false;
    if (x < 0 || x >= n) return false;
    if (grid[y][x] == '#') return false;
    if (visitedKeys(y, x, keys)) return false;
    if (grid[y][x] == '.' || grid[y][x] == '@') return true;    
    if (grid[y][x] >= 'a' && grid[y][x] <= 'z')
        return true;
    if (grid[y][x] >= 'A' && grid[y][x] <= 'Z' && (keys & convert(grid[y][x].toLowerCase())) )
        return true;
    return false;
}