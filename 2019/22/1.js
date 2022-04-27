let fs = require("fs");
const lines = fs.readFileSync('input.txt', 'utf8').toString().split('\n').filter( x => x );

const M = 10007;
let pos = 2019;
let a = 1, b = 0; // for the linear congruence new_pos = a*old_pos + b (mod M)

for (let line of lines) {
    if (line.split(' ')[0] == "deal" && line.split(' ')[1] == "with") {
        let n = +line.split(' ')[3];
        a = a*n % M;
        b = b*n % M;
    }        
    else if (line.split(' ')[0] == "deal" && line.split(' ')[1] == "into") {
        a = (M - a) % M;
        b = (M - b - 1) % M;
    }
    else if (line.split(' ')[0] == "cut") {
        let n = +line.split(' ')[1];
        b = (b + M - n) % M;
    }
}
console.log( a + " " + b );
console.log( (a*pos + b)%M );



function dealIntoNewStack(x) {
    return (M - x - 1);
}

function cutCards(x, N) {
    return ( x + M - N ) % M;
}

function dealWithIncrement(x, N) {
    return x*N % M;
}