/*
    this doesn't work because all the distances between keys are precalculated
    the distances should change as we collect keys
*/


const top = 0;
const parent = i => ((i + 1) >>> 1) - 1;
const left = i => (i << 1) + 1;
const right = i => (i + 1) << 1;

class PriorityQueue {
  constructor(comparator = (a, b) => a[0] < b[0]) {
    this._heap = [];
    this._comparator = comparator;
  }
  size() {
    return this._heap.length;
  }
  isEmpty() {
    return this.size() == 0;
  }
  peek() {
    return this._heap[top];
  }
  push(...values) {
    values.forEach(value => {
      this._heap.push(value);
      this._siftUp();
    });
    return this.size();
  }
  pop() {
    const poppedValue = this.peek();
    const bottom = this.size() - 1;
    if (bottom > top) {
      this._swap(top, bottom);
    }
    this._heap.pop();
    this._siftDown();
    return poppedValue;
  }
  replace(value) {
    const replacedValue = this.peek();
    this._heap[top] = value;
    this._siftDown();
    return replacedValue;
  }
  _greater(i, j) {
    return this._comparator(this._heap[i], this._heap[j]);
  }
  _swap(i, j) {
    [this._heap[i], this._heap[j]] = [this._heap[j], this._heap[i]];
  }
  _siftUp() {
    let node = this.size() - 1;
    while (node > top && this._greater(node, parent(node))) {
      this._swap(node, parent(node));
      node = parent(node);
    }
  }
  _siftDown() {
    let node = top;
    while (
      (left(node) < this.size() && this._greater(left(node), node)) ||
      (right(node) < this.size() && this._greater(right(node), node))
    ) {
      let maxChild = (right(node) < this.size() && this._greater(right(node), left(node))) ? right(node) : left(node);
      this._swap(node, maxChild);
      node = maxChild;
    }
  }
}




let fin = require("fs");
const grid = fin.readFileSync('input2.txt', 'utf8').toString().split('\n').filter( x => x );

let pos = new Map();

let m = grid.length, n = grid[0].length;
let origin = new Map();
let allKeys = 1;
for (let y = 0; y < m; ++y)
    for (let x = 0; x < n; ++x)
        if (grid[y][x] >= '0' && grid[y][x] <= '9') {
            origin.set( +grid[y][x] , [y, x]);
            pos.set(grid[y][x], [y, x]);
        }
        else if (grid[y][x] >= 'a' && grid[y][x] <= 'z') {
            pos.set(grid[y][x], [y, x]);
            allKeys |= convert(grid[y][x]);
        }
            
//console.log(grid);
//console.log(origin);

let dirs = [ [-1, 0], [+1, 0], [0, -1], [0, +1] ];

let paths = new Map();
for (let [key, value] of pos)
    paths.set(key, []);
for (let i = 0; i < origin.size; ++i)
    paths.set(String(i), []);

function BFS([y0, x0]) {
    let Q = [ [0, y0, x0, [], [] ] ]; //steps, y, x, doors on the path, keys on the path
    let visited = new Set();
    visited.add([y0, x0].toString());
    let steps, y, x, doorsVisited = [], keysVisited = [];

    while (Q.length > 0) {
        [steps, y, x, doorsVisited, keysVisited] = Q.shift();

        //console.log(steps + " " + y + " " + x + " " + doors);

        if (grid[y][x] >= 'a' && grid[y][x] <= 'z' || grid[y][x] >= '0' && grid[y][x] <= '9') {
            if (grid[y][x] != grid[y0][x0])
                paths.get(grid[y0][x0]).push([ grid[y][x], steps, [...doorsVisited], [...keysVisited] ]);
        }
        
        for (let [dy, dx] of dirs) 
            if ( possible(y+dy, x+dx) && !visited.has( [y+dy, x+dx].toString() ) ) {
                visited.add( [y+dy, x+dx].toString() );
                if (grid[y][x] >= 'A' && grid[y][x] <= 'Z')
                    doorsVisited.push(grid[y][x]);
                if (grid[y][x] >= 'a' && grid[y][x] <= 'z' && grid[y][x] != grid[y0][x0])
                    keysVisited.push(grid[y][x]);

                Q.push( [steps+1, y+dy, x+dx, [...doorsVisited], [...keysVisited] ] );
            }
    }
}

for (let [key, value] of pos)
    BFS( value );
/*
for (let i = 0; i < origin.size; ++i)
    BFS( origin.get(i) );
*/

console.log( paths.get('z') );
//console.log( paths.get('0') );



let visited = new Set();
let keysNeeded = [ 
    countKeys(0, 0, Math.floor(m/2), Math.floor(n/2)), 
    countKeys(Math.floor(m/2)+1, 0, m, Math.floor(n/2)), 
    countKeys(0, Math.floor(n/2)+1, Math.floor(m/2), n), 
    countKeys(Math.floor(m/2)+1, Math.floor(n/2)+1, m, n) 
    ];
let nKeys = keysNeeded.reduce( (a,b)=>a+b, 0 );

let steps, keysCollected;
let keysC = [], place = [];

let stepsStarting = 0;
let keys0 = [1, 1, 1, 1];

let Q = new PriorityQueue();
Q.push( [ stepsStarting, '0', '1', '2', '3', ...keys0 ] );
visited.add( ['0', '1', '2', '3', keys0[0]|keys0[1]|keys0[2]|keys0[3]].join(',') );

//console.log(visited);
//console.log(Q);

//console.log(paths.get('3'));

while (!Q.isEmpty()) {
    [steps, place[0], place[1], place[2], place[3], keysC[0], keysC[1], keysC[2], keysC[3]] = Q.pop();
    keysCollected = keysC[0]|keysC[1]|keysC[2]|keysC[3];
    //console.log( steps + " " + place + " " + keysCollected.toString(2));
    
    // if all the keys have been collected, we are finished
    if (nOnes(keysCollected) == nKeys+1) { 
        console.log(steps);
        break;
    }

    for (let i = 0; i < origin.size; ++i)
        // we only move those bots that have uncollected keys    
        if (nOnes(keysC[i]) <= keysNeeded[i]) 
        for (let [target, moves, doorsNeeded, keysOnTheWay] of paths.get(place[i])) {

            let p = [...place];
            p[i] = target;

            let k = [...keysC];
            k[i] |= convert(target);

            for (let key of keysOnTheWay) {
                k[i] |= convert(key);
            }

            if ( couldUnlock(doorsNeeded, keysCollected) && 
                !visited.has( [ ...p, keysCollected | k[i]].join(',')) ) {
                    visited.add( [...p, keysCollected | k[i]].join(',') );
                    Q.push( [steps+moves, ...p, ...k] );
            }
        }
}


function couldUnlock(doors, keys) {
    for (let d of doors) 
        if ( !( convert(d.toLowerCase()) & keys) )
            return false;
    return true;
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

function possible(y, x, keys=allKeys) {
    if (y < 0 || y >= m) return false;
    if (x < 0 || x >= n) return false;
    if (grid[y][x] == '#' || grid[y][x] == '*') return false;
    if (grid[y][x] == '.' || grid[y][x] == '@') return true;
    if (grid[y][x] >= '0' && grid[y][x] <= '9') return true;
    if (grid[y][x] >= 'a' && grid[y][x] <= 'z')
        return true;
    if (grid[y][x] >= 'A' && grid[y][x] <= 'Z' && (keys & convert(grid[y][x].toLowerCase())) )
        return true;
    return false;
}