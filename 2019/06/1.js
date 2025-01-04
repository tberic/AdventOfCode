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

let sum = 0;
for (planet of planets) {
    let n = findOrbits(planet);
    sum += n;
}

console.log(sum);