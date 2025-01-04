class Point {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }

    module() {
        return Math.abs(this.x) + Math.abs(this.y);
    }
}

class Seg {
    // sort the points when they are added
    constructor(A, B, dist) {
        this.start = A;
        this.end = B;
        if (A.y == B.y) {
            this.type = "horiz";
            this.y1 = A.y;
            this.y2 = B.y;
            this.x1 = Math.min( A.x, B.x );
            this.x2 = Math.max( A.x, B.x );
            this.length = this.x2 - this.x1;
        }
        if (A.x == B.x) {
            this.type = "vert";
            this.x1 = A.x;
            this.x2 = B.x;
            this.y1 = Math.min( A.y, B.y );
            this.y2 = Math.max( A.y, B.y );
            this.length = this.y2 - this.y1;
        }
        this.dist = dist;
    }

    pointInside(x, y) {
        if (this.type == "horiz") {
            if (this.y1 != y) return false;
            return between(x, this.x1, this.x2);
        }
        else if (this.type == "vert") {
            if (this.x1 != x) return false;
            return between(y, this.y1, this.y2);
        }
        return false;
    }
}

// true if x is between a and b
function between(x, a, b) {
    if (a <= x && x <= b) return true;
    return false;
}

// fix it
function closestIntersection(s, t, type) {
    if (type == "horiz") {
        if ( s.pointInside( t.x1, t.y1 ) ) {
            let min = 0; let P;
            for (let i = t.x1; i <= s.x2; ++i) {
                let T = new Point( i, t.y1 );
                if ( T.module() < min ) {
                    min = T.module();
                    P = T;
                }
            }
            return P;
        }
        else if ( t.pointInside( s.x1, s.y1 ) ) {
            return closestIntersection(t, s, "horiz");
        }
        else 
            return null;
    }    
    if (type == "vert") {
        if ( s.pointInside( t.x1, t.y1 ) ) {
            let min = 0; let P;
            for (let i = t.y1; i <= s.y2; ++i) {
                let T = new Point( t.x1, i );
                if ( T.module() < min ) {
                    min = T.module();
                    P = T;
                }
            }
            return P;
        }
        else if ( t.pointInside( s.x1, s.y1 ) ) {
            return closestIntersection(t, s, "vert");
        }
        else 
            return null;
    }    
}

function intersection(s, t) {
    if (s.type == "horiz" && t.type == "horiz") {
        if (s.y1 != t.y1) return null;
        return closestIntersection(s, t, "horiz");
    }
    else if (s.type == "vert" && t.type == "vert") {
        if (s.x1 != t.x1) return null;
        return closestIntersection(s, t, "vert");
    }

    let a, b;
    if (t.type == "vert") {
        a = (t.x1 - s.x1) / ( s.x2 - s.x1 );
        if (a < 0 || a > 1) return null;
        b = (s.y1 - t.y1) / ( t.y2 - t.y1 );
        if (b < 0 || b > 1) return null;
        
        return new Point( s.x1 + a*( s.x2-s.x1 ), s.y1 + a*( s.y2-s.y1 ) );
    }
    else if (t.type == "horiz") {
        return intersection(t, s);
    }
    
    return null;
}

let fin = require("fs");
const lines = fin.readFileSync('input.txt', 'utf8').toString().split('\n').filter(x => x);
let data = [];
for (let i = 0; i < 2; ++i)
    data[i] = lines[i].split(',');

let a, b;
let wire = [[], []];

for (let i = 0; i < 2; ++i) {
    let x = 0, y = 0, dist = 0;
    for (let command of data[i]) {
        a = x; b = y;
        let len = parseInt(command.substring(1));
        if (command[0] == 'U') y -= len;
        if (command[0] == 'D') y += len;
        if (command[0] == 'L') x -= len;
        if (command[0] == 'R') x += len;

        let seg = new Seg( new Point(a, b), new Point(x, y), dist );
        wire[i].push( seg );
        dist += seg.length;
    }
}

let min = -1, minT;
for (let s of wire[0])
    for (let t of wire[1]) {
        let T = intersection(s, t);
        if (T) {
            let combined = s.dist + t.dist + 
                        new Seg( s.start, T, 0 ).length + new Seg( t.start, T, 0 ).length;
            if (min == -1 || combined < min) {
                min = combined;
                minT = T;
            }
        }
    }

console.log( "(" + minT.x + "," + minT.y + ") " + min );