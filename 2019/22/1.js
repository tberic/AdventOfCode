let fs = require("fs");
const lines = fs.readFileSync('input.txt', 'utf8').toString().split('\n').filter( x => x );

const SIZE = 10007;
let cards = new Array(SIZE);
for (let i = 0; i < SIZE; ++i)
    cards[i] = i;

for (let line of lines) {
    if (line.split(' ')[0] == "deal" && line.split(' ')[1] == "with")
        dealWithIncrement( +line.split(' ')[3] );
    else if (line.split(' ')[0] == "deal" && line.split(' ')[1] == "into")
        dealIntoNewStack( );
    else if (line.split(' ')[0] == "cut")
        cutCards( +line.split(' ')[1] );
}

console.log(cards.indexOf(2019));



function dealIntoNewStack() {
    cards.reverse();
}

function cutCards(N) {
    if (N < 0)
        cutCards(SIZE+N);
    else {
        cards = cards.slice( N, SIZE ).concat( cards.slice( 0, N ) );
    }
}

function dealWithIncrement(N) {
    let cards2 = new Array(SIZE);
    let pos = 0;
    for (let i = 0; i < SIZE; ++i) {
        cards2[ pos ] = cards[i];
        pos = (pos + N) % SIZE;
    }
    cards = [...cards2];
}