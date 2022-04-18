/*
    Algorithm: BFS
*/

function gcd(x, y) {
    return y ? gcd(y, x%y) : x;
}

let fin = require("fs");
const lines = fin.readFileSync('input5.txt', 'utf8').toString().split('\r\n').filter(x => x);

let reactions = new Map();
let items = new Map();
for (line of lines) {
    let [a, z] = line.split(' => ');
    /*
    let qties = a.split(', ').concat([z]).map( x => +x.split(' ')[0] );
    let n = qties.reduce( gcd );
    let b = a.split(', ').map( x => { let a = +x.split(' ')[0]/n; let b = x.split(' ')[1]; return a+' '+b; } );    
    reactions.set( z.split(' ')[1], [ qties[qties.length-1]/n, b ] );   
    */
    reactions.set( z.split(' ')[1], [ +z.split(' ')[0], a.split(', ') ] );
    items.set( z.split(' ')[1], 0 );
}

console.log(reactions);

let Q = [ '1 FUEL' ];
//items.set( 'FUEL', 1 );
items.set( 'ORE', 0 );

while (Q.length > 0) {
    //console.log(Q);
    let [qty, product] = Q.shift().split(' ');
    qty = +qty;

    console.log( qty + " " + product );
    console.log(items);

    if (product == 'ORE') {
        items.set(product, items.get(product) + qty);
        continue;
    }

    let inputs = reactions.get(product);
    let n = Math.ceil( (qty-items.get(product)) / inputs[0]);

    if (n <= 0)
        continue;

    items.set( product, n*inputs[0]-qty+items.get(product) );

    //items.set( product, items.get(product) - n*inputs[0] );

    for (let i = 0; i < inputs[1].length; ++i) {
        let [q, name] = inputs[1][i].split(' ');
        q = +q;
        
        //items.set( name, items.get(name) + q*n );
        Q.push(q*n + ' ' + name);
    }
}

console.log(items);
console.log(items.get('ORE'));