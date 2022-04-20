let fin = require("fs");
const grid = fin.readFileSync('input2-pruned.txt', 'utf8').toString().split('\n').filter( x => x );

let m = grid.length, n = grid[0].length;
let x0, y0;
let origin = [];
for (let y = 0; y < m; ++y)
    for (let x = 0; x < n; ++x)
        if (grid[y][x] == '@')
            origin.push( y, x );

console.log(grid);
//console.log(origin);

let visited = new Set();

let dirs = [ [-1, 0], [+1, 0], [0, -1], [0, +1] ];

let Q = [ [ 0, 1, ...origin ] ];
visited.add( [ ...origin, 1 ].join(',') );

let nKeys = countKeys();
let steps, keysCollected;
let points = [], x = [], y = [];
while (Q.length > 0) {    
    [steps, keysCollected, ...points] = Q.shift();
    y = [points[0], points[2], points[4], points[6]];
    x = [points[1], points[3], points[5], points[7]];

    //console.log( points + " " + steps + " " + keysCollected.toString(2));

    // if all the keys have been collected, we are finished
    if (nOnes(keysCollected) == nKeys+1) {
        console.log(steps);
        break;
    }

    for (let i = 0; i < 4; ++i)
        for (let [dy, dx] of dirs) {

            let p = [...points];
            p[2*i] = y[i]+dy;
            p[2*i+1] = x[i]+dx;

            if ( possible(y[i]+dy, x[i]+dx, keysCollected) && !visited.has( [...p, keysCollected | convert(grid[y[i]+dy][x[i]+dx])].join(',')) ) {

                visited.add( [...p, keysCollected | convert(grid[y[i]+dy][x[i]+dx])].join(',') );
                Q.push( [steps+1, keysCollected | convert(grid[y[i]+dy][x[i]+dx]), ...p] );
            }
        }
}

function pack(steps, y, x, keys) {
    return [ steps, y[0], x[0], y[1], x[1], y[2], x[2], y[3], x[3], keys ];
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
    if (grid[y][x] == '.' || grid[y][x] == '@') return true;    
    if (grid[y][x] >= 'a' && grid[y][x] <= 'z')
        return true;
    if (grid[y][x] >= 'A' && grid[y][x] <= 'Z' && (keys & convert(grid[y][x].toLowerCase())) )
        return true;
    return false;
}