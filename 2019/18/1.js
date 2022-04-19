/*
    Didn't feel like implementing a priority queue from scratch 
    so I coded the solution in Python
*/

class QElement {
    constructor(element, priority)
    {
        this.element = element;
        this.priority = priority;
    }
}
 
// PriorityQueue class
class PriorityQueue {
    constructor()
    {
        this.items = [];
    }
 
    enqueue(element, priority)
    {
        // creating object from queue element
        var qElement = new QElement(element, priority);
        var contain = false;
     
        // iterating through the entire
        // item array to add element at the
        // correct location of the Queue
        for (var i = 0; i < this.items.length; i++) {
            if (this.items[i].priority > qElement.priority) {
                // Once the correct location is found it is
                // enqueued
                this.items.splice(i, 0, qElement);
                contain = true;
                break;
            }
        }
     
        // if the element have the highest priority
        // it is added at the end of the queue
        if (!contain) {
            this.items.push(qElement);
        }
    }

    dequeue()
    {
        // return the dequeued element
        // and remove it.
        // if the queue is empty
        // returns Underflow
        if (this.isEmpty())
            return "Underflow";
        return this.items.shift();
    }    

    front()
    {
        // returns the highest priority element
        // in the Priority queue without removing it.
        if (this.isEmpty())
            return "No elements in Queue";
        return this.items[0];
    }

    isEmpty()
    {
        // return true if the queue is empty.
        return this.items.length == 0;
    }
}

let fin = require("fs");
const grid = fin.readFileSync('input2.txt', 'utf8').toString().split('\r\n').filter( x => x );

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
/*
let visited = new Array(m).fill(0);
for (let i = 0; i < m; ++i)
    visited[i] = new Array(n).fill(0);
*/
let dirs = [ [-1, 0], [+1, 0], [0, -1], [0, +1] ];

let PQ = new PriorityQueue();
PQ.enqueue([y0, x0, 1], 0);
//let Q = [ [0, y0, x0, 1] ];
//visited[y0][x0] = 1;

let nKeys = countKeys();
let x, y, steps, keysCollected;
while (!PQ.isEmpty()) {
    [y, x, keysCollected] = PQ.front().element;
    steps = PQ.front().priority;
    PQ.dequeue();

    //console.log( y + " " + x + " " + steps + " " + keysCollected.toString(2));

    // if all the keys have been collected, we are finished
    if (nOnes(keysCollected) == nKeys+1) {
        console.log(steps);
        break;
    }
/*
    if (y == 1 && x == 6) {
        console.log(keysCollected);
        console.log(visited[1]);
        console.log(grid);
    }
*/
    for (let [dy, dx] of dirs)
        if ( possible(y+dy, x+dx, keysCollected) ) {
            //visited[y+dy][x+dx] |= keysCollected | convert(grid[y+dy][x+dx]);

            PQ.enqueue( [y+dy, x+dx, keysCollected | convert(grid[y+dy][x+dx])], steps+1 );
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
/*
function visitedKeys(y, x, keys) {
    return nOnes(visited[y][x] & keys) == nOnes(keys);
}
*/
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
    //if (visitedKeys(y, x, keys)) return false;
    if (grid[y][x] == '.' || grid[y][x] == '@') return true;    
    if (grid[y][x] >= 'a' && grid[y][x] <= 'z')
        return true;
    if (grid[y][x] >= 'A' && grid[y][x] <= 'Z' && (keys & convert(grid[y][x].toLowerCase())) )
        return true;
    return false;
}