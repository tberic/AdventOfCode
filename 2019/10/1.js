let fin = require("fs");
let string = fin.readFileSync('input.txt', 'utf8').toString().replace(/(?:\\[rn]|[\r\n]+)+/g, " ");
let image = string.split(' ').filter(x => x);
const m = image.length;
const n = image[0].length;

console.log(image);

class Point {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
}

let asteroids = [];

for (let x = 0; x < m; ++x)
    for (let y = 0; y < n; ++y) 
        if (image[x][y] == '#') 
            asteroids.push( new Point(x, y) );

//console.log(asteroids.length);
//console.log(asteroids);

function gcd(x, y) {
    return y ? gcd(y, x%y) : x;
}

let max = 0;
let nVisible;
for (let i = 0; i < asteroids.length; ++i) {
    nVisible = 0;    
    for (let j = 0; j < asteroids.length; ++j) 
        if (j != i) {
            //console.log(i  + " "  + j);
            let dx = asteroids[j].x - asteroids[i].x;
            let dy = asteroids[j].y - asteroids[i].y;
            let n = gcd(Math.abs(dx), Math.abs(dy));
            dx /= n; dy /= n;

            let blocking = false;
            let x = asteroids[i].x + dx;
            let y = asteroids[i].y + dy;

            while ( x != asteroids[j].x || y != asteroids[j].y ) {
                if (image[x][y] == '#') {
                    blocking = true;
                    break;
                }
                x += dx; y += dy;
            }

            if (!blocking)
                nVisible++;
        }

    if (nVisible > max)
        max = nVisible;
}

console.log(max);