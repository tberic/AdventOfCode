/*
  Dijkstra on a 3D graph (y,x,keysCollected)
  end nodes are (*,*,allKeys)
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



let fs = require("fs");
const grid = fs.readFileSync('input2.txt', 'utf8').toString().split('\n').filter( x => x );

let pos = new Map();

let m = grid.length, n = grid[0].length;
let origin = new Map();
let allKeys = 1;
for (let y = 0; y < m; ++y)
    for (let x = 0; x < n; ++x)
        if (grid[y][x] >= '0' && grid[y][x] <= '9') {
            origin.set( grid[y][x] , [y, x]);
            pos.set(grid[y][x], [y, x]);
        }
        else if (grid[y][x] >= 'a' && grid[y][x] <= 'z') {
            pos.set(grid[y][x], [y, x]);
            allKeys |= convert(grid[y][x]);
        }
            
let dirs = [ [-1, 0], [+1, 0], [0, -1], [0, +1] ];

let keysNeeded = [ 
    countKeys(0, 0, Math.floor(m/2), Math.floor(n/2)),     
    countKeys(0, Math.floor(n/2)+1, Math.floor(m/2), n), 
    countKeys(Math.floor(m/2)+1, 0, m, Math.floor(n/2)), 
    countKeys(Math.floor(m/2)+1, Math.floor(n/2)+1, m, n) 
    ];
//let nKeys = keysNeeded.reduce( (a,b)=>a+b, 0 );

console.log(keysNeeded);
console.log(origin);

let steps, keysCollected;
let keysC = [], place = [];

let keys0 = [1, 1, 1, 1];

let PQ = new PriorityQueue();
PQ.push( [ 0, ...origin.keys(), ...keys0 ] );

let dist = new Map();
dist.set( [ ...origin.keys(), 1 ].join(','), 0 );

while (!PQ.isEmpty()) {
    
    [steps, place[0], place[1], place[2], place[3], ...keysC] = PQ.pop();
    keysCollected = keysC[0]|keysC[1]|keysC[2]|keysC[3];
    //console.log( steps + " " + place + " " + keysCollected.toString(2));    

    // if all the keys have been collected, we are finished
    if (keysCollected == allKeys) {
        console.log(steps);
        break;
    }

    for (let i = 0; i < origin.size; ++i)
        // we only move those bots that have uncollected keys    
        if (nOnes(keysC[i]) <= keysNeeded[i])  {
          let path = BFS( pos.get(place[i]), keysCollected );

          for (p of path) {
            
            let alt = dist.get( [...place, keysCollected].join(',') ) + p[1];
            let place2 = [...place];
            place2[i] = p[0];
            let k = [...keysC];
            k[i] |= convert( p[0] ); 

            if ( !dist.has( [...place2, keysCollected | convert(p[0]) ].join(',') ) ||
              alt < dist.get( [...place2, keysCollected | convert(p[0]) ].join(',') ) ) {
              
              dist.set( [...place2, keysCollected | convert(p[0]) ].join(','), alt );
              PQ.push( [alt, ...place2, ...k] );
              
            }
            


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

function possible([y, x], keys=allKeys) {
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


function BFS([y0, x0], keys) {
  let Q = [ [0, y0, x0] ]; //steps, y, x, doors on the path, keys on the path
  let visited = new Set();
  visited.add([y0, x0].join(','));
  let steps, y, x;

  let path = [];
  //path.set( grid[y0][x0], [] );

  while (Q.length > 0) {
      [steps, y, x] = Q.shift();

      //console.log(steps + " " + y + " " + x + " " + doors);
/*
      if (grid[y][x] >= 'A' && grid[y][x] <= 'Z' && !( convert(grid[y][x].toLowerCase()) & keys ) )
        continue;
*/
      if (grid[y][x] >= 'a' && grid[y][x] <= 'z' || grid[y][x] >= '0' && grid[y][x] <= '9') {
          if (grid[y][x] != grid[y0][x0])
              path.push([ grid[y][x], steps ]);
      }
      
      for (let [dy, dx] of dirs) 
          if ( possible([y+dy, x+dx], keys) && !visited.has( [y+dy, x+dx].join(',') ) ) {
              visited.add( [y+dy, x+dx].join(',') );
              Q.push( [steps+1, y+dy, x+dx ] );
          }
  }

  return path;
}