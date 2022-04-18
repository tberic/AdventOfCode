function modifiedFFT() {
    let sum = 0;    
    for (let pos = a.length-1; pos >= 0; pos--) {        
        sum += a[pos];
        sum %= 10;
        a[pos] = sum;
    }    
}

let fin = require("fs");
const input = fin.readFileSync('input.txt', 'utf8').toString().split('')
            .map( x => parseInt(x) ).filter( x => !isNaN(x) );

let offset = +input.slice(0, 7).join('');
let N = input.length*10000;
//console.log(offset);

let a = [];
while (a.length < N-offset)
    a = a.concat(input);

a.splice(0, offset - N+a.length);

for (let i = 0; i < 100; ++i) {
    modifiedFFT();    
}

console.log(a.slice(0, 8).join(''));