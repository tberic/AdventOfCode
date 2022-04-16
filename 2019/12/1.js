function l1(a) {
    let sum = 0;
    for (let x of a)
        sum += Math.abs(x);
    return sum;
}

function mathSign(x) {
    if (x == 0) return 0;
    return x/Math.abs(x);
}

const { sign } = require("crypto");
let fin = require("fs");
let lines = fin.readFileSync('input.txt', 'utf8').toString().split('\n').filter(x => x);

let pos = [];
let vel = [];
for (line of lines) {
    let p = [];
    for (s of line.split(',')) {
        p.push( parseInt(s.split('=')[1]) );
    }
    pos.push(p);
    vel.push( [0, 0, 0] );
}

let energy = 0;
for (let step = 0; step < 1000; ++step) {

    for (let i = 0; i < pos.length; ++i)
        for (let j = 0; j < pos.length; ++j)
            if (j != i) {
                for (let k = 0; k < 3; ++k) {
                    vel[i][k] += -mathSign(pos[i][k] - pos[j][k]);
            }
        }

    for (let i = 0; i < pos.length; ++i) 
        for (let k = 0; k < 3; ++k) {
            pos[i][k] += vel[i][k];
        }

    //console.log(pos);

    energy = 0;
    for (let i = 0; i < pos.length; ++i) {
        energy += l1(pos[i])*l1(vel[i]);
    }
    //console.log( energy );
}

console.log( energy );