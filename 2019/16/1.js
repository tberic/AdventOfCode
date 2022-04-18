function f(n, pos) {
    return (n & 1) * ( ((n+2) & 2) - 1 );
}

function multiplier(n, pos) {
    return f( Math.floor((n+1)/pos) ) ;
}

function FFT(a) {
    let sum;
    let b = [];
    for (let pos = 1; pos <= a.length; ++pos) {
        sum = 0;
        for (let i = 0; i < a.length; ++i)
            sum += a[i]*multiplier(i, pos);
        b.push( Math.abs(sum)%10 );
    }
    return b;
}

let fin = require("fs");
const input = fin.readFileSync('input.txt', 'utf8').toString().split('')
            .map( x => parseInt(x) ).filter( x => !isNaN(x) );

let b = input;
for (let phase = 0; phase < 100; ++phase) 
    b = FFT(b);

console.log(b.join('').slice(0, 8));