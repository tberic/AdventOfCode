class Point {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
}

function print(arr) {
    for (let i = 0; i < arr.length; ++i)
        console.log(arr[i]);
}

function quadrant(T, O=origin) {
    let x = T.x-O.x, y = T.y-O.y;
    if (x >= 0 && y > 0) return 1;
    if (x > 0 && y <= 0) return 2;
    if (x <= 0 && y < 0) return 3;
    if (x < 0 && y >= 0) return 4;
    return 5;
}

function compare(A, B) {
    if ( quadrant(A) != quadrant(B) )
        return quadrant(A) - quadrant(B);
    return (A.x - origin.x)*(B.y - origin.y) - (A.y - origin.y)*(B.x - origin.x);
}

function dist2(T, O) {
    return (T.x-O.x)*(T.x-O.x) + (T.y-O.y)*(T.y-O.y);
}

function blocks(A, B, O) {
    let crossProduct = (A.x - O.x)*(B.y - O.y) - (A.y - O.y)*(B.x - O.x);
    let dotProduct = (A.x - O.x)*(B.x - O.x) + (A.y - O.y)*(B.y - O.y);    
    return !crossProduct && dotProduct > 0 && dist2(A, O) < dist2(B, O);
}

function blocked(T, O) {
    for (let i = 0; i < asteroids.length; ++i)
        if ( (asteroids[i].x != T.x || asteroids[i].y != T.y) && blocks(asteroids[i], T, O) )
            return true;

    return false;
}

let fin = require("fs");
let string = fin.readFileSync('input.txt', 'utf8').toString().replace(/(?:\\[rn]|[\r\n]+)+/g, " ");
let image = string.split(' ').filter(x => x);
const m = image.length;
const n = image[0].length;

let asteroids = [];
for (let y = 0; y < m; ++y)
    for (let x = 0; x < n; ++x) 
        if (image[y][x] == '#') 
            asteroids.push( new Point(x, -y) );

let origin;
let max = 0;
let nVisible;
let X, Y;
for (let i = 0; i < asteroids.length; ++i) {
    nVisible = 0;
    for (let j = 0; j < asteroids.length; ++j) 
        if (j != i && !blocked(asteroids[j], asteroids[i]))
            nVisible++;
            
    if (nVisible > max) {
        max = nVisible;
        X = asteroids[i].x;
        Y = asteroids[i].y;
    }
}

origin = new Point(X, Y);

console.log("Best point: " + X + "," + Y);
console.log("Max visible: " + max);

image[-Y] = image[-Y].substring(0,X) + 'X' + image[-Y].substring(X+1); //image[X][Y] = 'X';
asteroids = asteroids.filter( T => T.x != X || T.y != Y );

let visibleAsteroids = [];
let deletedAsteroids = [];

while (asteroids.length) {
    visibleAsteroids = [];
    for (let i = 0; i < asteroids.length; ++i) 
        if (!blocked(asteroids[i], origin)) {
            visibleAsteroids.push( asteroids[i] );
            let x = asteroids[i].x, y = asteroids[i].y;
            image[-y] = image[-y].substring(0,x) + 'O' + image[-y].substring(x+1); //image[X][Y] = 'X';
        }

    asteroids = asteroids.filter( T => !visibleAsteroids.includes(T) );
    visibleAsteroids.sort( compare );
    deletedAsteroids = deletedAsteroids.concat(visibleAsteroids);
    print(image);
    console.log();

    for (let i = 0; i < visibleAsteroids.length; ++i) {
        let x = visibleAsteroids[i].x, y = -visibleAsteroids[i].y;
        image[y] = image[y].substring(0,x) + '.' + image[y].substring(x+1); //image[X][Y] = 'X';
    }
}

console.log(deletedAsteroids.length);
console.log( deletedAsteroids[199] );