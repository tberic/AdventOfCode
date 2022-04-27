let fs = require("fs");
const lines = fs.readFileSync('input.txt', 'utf8').toString().split('\n').filter( x => x );

const M = 10007;
let pos = 2019;

for (let line of lines) {
    if (line.split(' ')[0] == "deal" && line.split(' ')[1] == "with")
        pos = dealWithIncrement( pos, +line.split(' ')[3] );
    else if (line.split(' ')[0] == "deal" && line.split(' ')[1] == "into")
        pos = dealIntoNewStack( pos );
    else if (line.split(' ')[0] == "cut")
        pos = cutCards( pos, +line.split(' ')[1] );
}

console.log(pos);



function dealIntoNewStack(x) {
    return (M - x - 1);
}

function cutCards(x, N) {
    return ( x + M - N ) % M;
}

function dealWithIncrement(x, N) {
    return x*N % M;
}