let fin = require("fs");
const lines = fin.readFileSync('input2.txt', 'utf8').toString().split('\n').filter( x => x );

let m = lines.length, n = lines[0].length;
let grid = [];
for (let i = 0; i < m; ++i)
    grid[i] = lines[i].split('');

let x0, y0;
let origin = [];
for (let y = 0; y < m; ++y)
    for (let x = 0; x < n; ++x)
        if (grid[y][x] == '@')
            origin.push( [y, x] );

let visited = new Set();

let dirs = [ [-1, 0], [+1, 0], [0, -1], [0, +1] ];

function possible(y, x) {
    if (y < 0 || y >= m) return false;
    if (x < 0 || x >= n) return false;
    if (grid[y][x] == '#') return false;
    if (visited.has([y,x].join(','))) return false;
    if (grid[y][x] == '.' || grid[y][x] == '@') return true;
    if (grid[y][x] >= 'a' && grid[y][x] <= 'z')
        return true;
    if (grid[y][x] >= 'A' && grid[y][x] <= 'Z')
        return true;
    return false;
}

function DFS(y, x) {
    if (!possible(y,x)) 
        return false;

    visited.add( [y,x].join(',') );

    let flag = false, ret;
    for (let [dy, dx] of dirs) {
        if ( possible(y+dy, x+dx) ) {
            ret = DFS(y+dy, x+dx);
            if (ret) flag = true;
        }
    }
    if (grid[y][x] == '.' && !flag) grid[y][x] = '*';
    if (grid[y][x] >= 'a' && grid[y][x] <= 'z') return true;
    //if (grid[y][x] >= 'A' && grid[y][x] <= 'Z') return true;
    return flag;
}

for (let [y,x] of origin)
    DFS(y,x);

for (let y = 0; y < m; ++y) {
    s = "";
    for (let x = 0; x < n; ++x)
        s += grid[y][x];
    console.log(s);
}
