let fin = require("fs");
const lines = fin.readFileSync('input.txt', 'utf8').toString().split('\n').filter(x => x);

let reactions = new Map();
let need = new Map();
for (line of lines) {
    let [a, z] = line.split(' => ');
    reactions.set( z.split(' ')[1], [ +z.split(' ')[0], a.split(', ') ] );
}

//console.log(reactions);

/*
    first topologically sort the nodes using DFS
*/
let visited = new Set();
let order = [];

function DFS(node) {
    visited.add(node);
    if (node == 'ORE') 
        return ;
    
    let inputs = reactions.get(node);
    for (let i = 0; i < inputs[1].length; ++i) {
        let [q, ingredient] = inputs[1][i].split(' ');
        if (!visited.has(ingredient))
            DFS(ingredient);
    }

    order.push(node);
}

DFS('FUEL');
order.reverse();
order.push('ORE');

//console.log(order);

function finished() {
    for (let [key, val] of need) 
        if (key != 'ORE') {
            if (val > 0) return false;
    }
    return true;
}

function findFirst() {
    for (let i = 0; i < order.length-1; ++i) 
        if (need.has(order[i]) && need.get(order[i]) > 0)
            return order[i];
}

let target = 1000000000000;

need.set( 'FUEL', 1572358 );

while (!finished()) {
    product = findFirst();

    if (product == 'ORE')
        continue;
    
    let qty = need.get(product);
    //console.log( qty + " " + product );    

    let inputs = reactions.get(product);
    let n = Math.ceil( qty / inputs[0]);
    need.delete( product );

    for (let i = 0; i < inputs[1].length; ++i) {
        let [q, name] = inputs[1][i].split(' ');
        q = +q;
        
        if (need.has(name))
            need.set( name, need.get(name) + q*n );
        else
            need.set( name, q*n );
    }
}

console.log(target-need.get('ORE'));