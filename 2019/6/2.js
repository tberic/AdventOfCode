let fin = require("fs");
const lines = fin.readFileSync('input.txt', 'utf8').toString().split('\n').filter(x => x);

let orbits = new Map();
let nOrbits = new Map();
let planets = new Set();

for (const line of lines) {
    orbits.set(line.split(')')[1], line.split(')')[0]);
    nOrbits.set(line.split(')')[0], 0);
    nOrbits.set(line.split(')')[1], 0);
    planets.add(line.split(')')[0]);
    planets.add(line.split(')')[1]);
}

function findOrbits(planet) {
    if (nOrbits.get(planet))
        return nOrbits.get(planet);

    if (!orbits.has(planet))
        return 0;   

    nOrbits.set(planet, findOrbits( orbits.get(planet) ) + 1);
    return nOrbits.get(planet);
}

for (let planet of planets) {
    findOrbits(planet);
}

let you = ['YOU'];
let san = ['SAN'];

let planet = 'YOU';
while ( orbits.has(planet) ) {
    planet = orbits.get(planet);
    you.push( planet );
}

planet = 'SAN';
while ( orbits.has(planet) ) {
    planet = orbits.get(planet);
    san.push( planet );
}

console.log( 'YOU ' + nOrbits.get('YOU') );
console.log( 'SAN ' + nOrbits.get('SAN') );

let i = 0;
while (!san.includes(you[i]))
    i++;
let j = 0;
while (san[j] != you[i])
    j++;

console.log(i+j-2);