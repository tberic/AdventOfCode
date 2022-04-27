let fs = require("fs");
const lines = fs.readFileSync('input.txt', 'utf8').toString().split('\n').filter( x => x );

/*
    precalculated inverses to speed up the program
*/
let inversesLines = fs.readFileSync('inverses.txt', 'utf8').toString().split('\n').filter( x => x );
let inverse = new Map();
for (let line of inversesLines)
    inverse.set( +line.split(',')[0], +line.split(',')[1] );

const M = 119315717514047;
const NSTEPS = 101741582076661;
//const M = 10007;
let pos = 2020;

let visited = new Map();
visited.set(pos, 0);
let steps = 0;
while (true) {
    steps++;
    for (let line of lines.reverse()) {
        if (line.split(' ')[0] == "deal" && line.split(' ')[1] == "with") {
            pos = dealWithIncrement( pos, +line.split(' ')[3] );
        }
        else if (line.split(' ')[0] == "deal" && line.split(' ')[1] == "into")
            pos = dealIntoNewStack( pos );
        else if (line.split(' ')[0] == "cut")
            pos = cutCards( pos, +line.split(' ')[1] );

        //console.log(line + ": " + pos);
    }
    
    if (visited.has(pos)) {
        console.log("Repeats!");
        break;
    }
    visited.set(pos, steps);

//console.log(pos);
}
console.log("Steps: " + steps);
console.log("Last seen: " + visited.get(pos) );
console.log("Steps left: " + (NSTEPS-steps) % (steps-visited.get(pos)) );
console.log("Pos: " + pos);

//pos = 2020;
for (let i = 0; i < (NSTEPS-steps) % (steps-visited.get(pos)); ++i) {

    for (let line of lines.reverse()) {
        if (line.split(' ')[0] == "deal" && line.split(' ')[1] == "with") {
            pos = dealWithIncrement( pos, +line.split(' ')[3] );
        }
        else if (line.split(' ')[0] == "deal" && line.split(' ')[1] == "into")
            pos = dealIntoNewStack( pos );
        else if (line.split(' ')[0] == "cut")
            pos = cutCards( pos, +line.split(' ')[1] );
    }

}
console.log(pos);




function dealIntoNewStack(x) {
    return (M - x - 1);
}

function cutCards(x, N) {
    return ( x + M + N ) % M;
}

function dealWithIncrement(x, N) {
    return (modInverse(N)*x) % M;
}

/* we will hard code this for the given input */
function modInverse(x) {
    if (inverse.has(x))
        return inverse.get(x);
    return undefined;

/*
    for (let i = 1; i < M; ++i)
        if (i*x % M == 1)
            return i;
*/
}