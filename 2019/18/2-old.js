let fin = require("fs");
const grid = fin.readFileSync('input2-pruned-premoved.txt', 'utf8').toString().split('\n').filter( x => x );

let m = grid.length, n = grid[0].length;
let x0, y0;
let origin = [];
for (let y = 0; y < m; ++y)
    for (let x = 0; x < n; ++x)
        if (grid[y][x] == '@')
            origin.push( y, x );

console.log(grid);
//console.log(origin);

//let visited = [new Set(), new Set(), new Set(), new Set() ];
let visited = new Set();

let dirs = [ [-1, 0], [+1, 0], [0, -1], [0, +1] ];

let keysNeeded = [ 
    countKeys(0, 0, Math.floor(m/2), Math.floor(n/2)), 
    countKeys(Math.floor(m/2)+1, 0, m, Math.floor(n/2)), 
    countKeys(0, Math.floor(n/2)+1, Math.floor(m/2), n), 
    countKeys(Math.floor(m/2)+1, Math.floor(n/2)+1, m, n) 
    ];
let nKeys = keysNeeded.reduce( (a,b)=>a+b, 0 );

//console.log(keysNeeded);

let steps, keysCollected;
let points = [], x = [], y = [], keysC = [];

/* 
    we could premove untile there are no unique choices for moves
    (and close the path we took)
*/

let stepsStarting = 166+36+208+16;
//let stepsStarting = 164+274+228+472;
//let stepsStarting = 0;

let keys0 = [ 
    convert('m') | convert('l') | convert('r'),
    1,
    1,
    1
    ];

//let keys0 = [1, 1, 1, 1], path = [];

let Q = [ [ stepsStarting, ...keys0, ...origin, ] ];
//let Q = [ [ stepsStarting, [], ...keys0, ...origin, ] ];

visited.add( [...origin, keys0[0]|keys0[1]|keys0[2]|keys0[3]].join(',') );

//console.log(visited);
//console.log(Q);

while (Q.length > 0) {
    [steps, keysC[0], keysC[1], keysC[2], keysC[3], ...points] = Q.shift();
    //[steps, path, keysC[0], keysC[1], keysC[2], keysC[3], ...points] = Q.shift();
    y = [points[0], points[2], points[4], points[6]];
    x = [points[1], points[3], points[5], points[7]];
    keysCollected = keysC[0]|keysC[1]|keysC[2]|keysC[3];
    console.log( points + " " + steps + " " + keysCollected.toString(2));
    //console.log( [steps, keysCollected.toString(2), ...points] );

    // if all the keys have been collected, we are finished
    if (nOnes(keysCollected) == nKeys+1) { 
        console.log(steps);
        //console.log(path);
        break;
    }

    for (let i = 0; i < 4; ++i)
        if (nOnes(keysC[i]) <= keysNeeded[i]) // we only move those bots that have uncollected keys
        for (let [dy, dx] of dirs) {

            let p = [...points];
            p[2*i] = y[i]+dy;
            p[2*i+1] = x[i]+dx;

            let k = [...keysC];
            k[i] |= convert(grid[y[i]+dy][x[i]+dx]);

            if ( possible(y[i]+dy, x[i]+dx, keysCollected) && 
                !visited.has( [ ...p, keysCollected | k[i]].join(',')) ) {

                visited.add( [...p, keysCollected | k[i]].join(',') );
                Q.push( [steps+1, ...k, ...p] );
                //Q.push( [steps+1, path.concat([ [i, y[i]+dy, x[i]+dx] ]), ...k, ...p] );
            }
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

function countKeys(y1, x1, y2, x2) {
    let keys = 0;
    for (let y = y1; y < y2; ++y)
        for (let x = x1; x < x2; ++x)
            if (grid[y][x] >= 'a' && grid[y][x] <= 'z')
                keys++;
    return keys;
}

function possible(y, x, keys) {
    if (y < 0 || y >= m) return false;
    if (x < 0 || x >= n) return false;
    if (grid[y][x] == '#' || grid[y][x] == '*') return false;    
    if (grid[y][x] == '.' || grid[y][x] == '@') return true;    
    if (grid[y][x] >= 'a' && grid[y][x] <= 'z')
        return true;
    if (grid[y][x] >= 'A' && grid[y][x] <= 'Z' && (keys & convert(grid[y][x].toLowerCase())) )
        return true;
    return false;
}