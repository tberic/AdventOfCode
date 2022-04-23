let fs = require("fs");
const data = fs.readFileSync('input.txt', 'utf8').toString().split('\n').filter( x => x );
let grid = [ ".......".split('') ];
for (let i = 0; i < data.length; ++i)
    grid.push( ("."+data[i]+".").split('') );
grid.push( ".......".split('') );

print(grid);

let visited = new Set();

while (true) {
    let b = biodiversity(grid);
    if (visited.has(b))
        break;
    else
        visited.add(b);

    let grid2 = [];
    for (let i = 0; i < grid.length; ++i)
        grid2[i] = grid[i].slice();
   
    for (let i = 1; i <= 5; ++i)
        for (let j = 1; j <= 5; ++j) {
            let cnt = neighboursCount(grid, i, j);            
            if (grid[i][j] == '#' && cnt != 1)
                grid2[i][j] = '.';
            else if (grid[i][j] == '.' && (cnt == 1 || cnt == 2))
                grid2[i][j] = '#';
        }

    print(grid2);

    for (let i = 0; i < grid2.length; ++i)
        grid[i] = grid2[i].slice();
}

console.log(biodiversity(grid));

function neighboursCount(arr, i, j) {
    return (arr[i-1][j]=='#')+(arr[i+1][j]=='#')+(arr[i][j-1]=='#')+(arr[i][j+1]=='#');
}

function biodiversity(arr) {
    let pos = 1;
    let sum = 0;
    for (let i = 1; i <= 5; ++i)
        for (let j = 1; j <= 5; ++j) {
            if (arr[i][j] == '#')
                sum += pos;
            pos = pos << 1;
        }
    
    return sum;
}

function print(arr) {
    for (let i = 0; i < arr.length; ++i) {
        let s = "";
        for (let j = 0; j < arr[0].length; ++j)
            s += arr[i][j];
        console.log(s);
    }
    console.log();
}