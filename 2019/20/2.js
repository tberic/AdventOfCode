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

function isLetter(c) {
    return (c>= 'A' && c <= 'Z');
}

function isOuterPortal([y, x]) {
    return (y == 3 || y == m-2 || x == 3 || x == n-2);
}



let fs = require("fs");
const gridIn = fs.readFileSync('input.txt', 'utf8').toString().replace(/(\r\n|\n|\r)/gm, "\n").split('\n').filter( x => x );
const m = gridIn.length;
const n = gridIn[0].length;
let grid = new Array(m+2);
grid[0] = new Array(n+2).fill(' ').join('');
for (let i = 1; i <= m; ++i)
    grid[i] = ' ' + gridIn[i-1] + ' ';
grid[m+1] = new Array(n+2).fill(' ').join('');

let portal = new Map();

// find the portal names
for (let y = 1;  y <= m-1; ++y)
    for (let x = 1;  x <= n-1; ++x) 
        if ( isLetter(grid[y][x]) ) {
            if ( isLetter(grid[y][x+1]) )
                portal.set(grid[y][x]+grid[y][x+1], []);
            if ( isLetter(grid[y+1][x]) )
                portal.set(grid[y][x]+grid[y+1][x], []);
        }

// find the portal entrances/exits
for (let y = 1;  y <= m-1; ++y)
    for (let x = 1;  x <= n-1; ++x) 
        if ( isLetter(grid[y][x]) ) {
            if ( isLetter(grid[y][x+1]) ) {
                if (grid[y][x+2] == '.')
                    portal.get( grid[y][x]+grid[y][x+1] ).push( [y,x+2] );
                if (grid[y][x-1] == '.')
                    portal.get( grid[y][x]+grid[y][x+1] ).push( [y,x-1] );
            }
            
            if ( isLetter(grid[y+1][x]) ) {
                if (grid[y+2][x] == '.')
                    portal.get( grid[y][x]+grid[y+1][x] ).push( [y+2,x] );
                if (grid[y-1][x] == '.')
                    portal.get( grid[y][x]+grid[y+1][x] ).push( [y-1,x] );
            }
        }

let start = portal.get("AA")[0];
let end = portal.get("ZZ")[0];
portal.delete("AA");
portal.delete("ZZ");

let teleportInner = new Map();
let teleportOuter = new Map();

for (let [k, v] of portal) {
    if ( isOuterPortal( v[0] ) )
        teleportOuter.set( v[0].join(','), v[1] );
    else
        teleportInner.set( v[0].join(','), v[1] );
    
    if ( isOuterPortal( v[1] ) )
        teleportOuter.set( v[1].join(','), v[0] );
    else
        teleportInner.set( v[1].join(','), v[0] );
}

let dirs = [[-1, 0], [+1, 0], [0, -1], [0, +1]];

let PQ = new PriorityQueue();
PQ.push( [0, 0, ...start] );

let dist = new Map();
dist.set( [0, ...start].join(','), 0 );

while (true) {
    let [steps, level, y, x] = PQ.pop();

    //console.log( [steps, level, y, x] );

    if (level == 0 && y == end[0] && x == end[1]) {
        console.log(steps);
        break;
    }

    for (let [dy, dx] of dirs) 
        if (grid[y+dy][x+dx] == '.') {
            let alt = dist.get( [level, y, x].join(',') ) + 1;

            if (!dist.has( [level, y+dy, x+dx].join(',') ) || alt < dist.get( [level, y+dy, x+dx].join(',') ) ) {
                dist.set( [level, y+dy, x+dx].join(','), alt );

                PQ.push( [alt, level, y+dy, x+dx] );
            }
        }

    if ( teleportInner.has( [y, x].join(',') ) ) {
        let alt = dist.get( [level, y, x].join(',') ) + 1;

        let [y0, x0] = teleportInner.get( [y, x].join(',') );

        if (!dist.has( [level+1, y0, x0].join(',') ) || alt < dist.get( [level+1, y0, x0].join(',') ) ) {
            dist.set( [level+1, y0, x0].join(','), alt );
            PQ.push( [alt, level+1, y0, x0] );
        }
    }

    if (level == 0)
        continue;

    if ( teleportOuter.has( [y, x].join(',') ) ) {
        let alt = dist.get( [level, y, x].join(',') ) + 1;

        let [y0, x0] = teleportOuter.get( [y, x].join(',') );

        if (!dist.has( [level-1, y0, x0].join(',') ) || alt < dist.get( [level-1, y0, x0].join(',') ) ) {
            dist.set( [level-1, y0, x0].join(','), alt );
            PQ.push( [alt, level-1, y0, x0] );
        }
    }

}