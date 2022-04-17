function mathSign(x) {
    if (x == 0) return 0;
    return x/Math.abs(x);
}

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

/*
    IDEA:   for each coordinate separately find the period?
            after that chinese remainder theorem
*/

function pack(x, y, z, w, a, b, c, d) {
    return x+","+y+","+z+","+w+","+a+","+b+","+c+","+d;
}

let repeats = [];

for (let coord = 0; coord < 3; ++coord) {
    let seen = new Array();
    let step = 0;
    while (true) {

        for (let i = 0; i < pos.length; ++i)
            for (let j = 0; j < pos.length; ++j)
                if (j != i)                     
                    vel[i][coord] += -mathSign(pos[i][coord] - pos[j][coord]);

        for (let i = 0; i < pos.length; ++i) 
                pos[i][coord] += vel[i][coord];

        let A = pack(pos[0][coord], pos[1][coord], pos[2][coord], pos[3][coord], 
                    vel[0][coord], vel[1][coord], vel[2][coord], vel[3][coord]);

        if ( seen.includes(A) ) {
            repeats[coord] = step;
            seen.push( A );
            break;
        }
        seen.push( A );

        step++;
    }
    
    console.log( repeats[coord] + " " + seen.indexOf(seen[repeats[coord]]) );
}
/*
console.log( seen );
console.log( repeatsX + " " + repeatsY + " " + repeatsZ );

console.log( seen[0].indexOf(seen[0][repeatsX]) );
console.log( seen[1].indexOf(seen[1][repeatsY]) );
console.log( seen[2].indexOf(seen[2][repeatsZ]) );
*/