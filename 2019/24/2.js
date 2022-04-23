let fs = require("fs");
const data = fs.readFileSync('input.txt', 'utf8').toString().split('\n').filter( x => x );
let grid = [];
for (let i = 0; i < data.length; ++i)
    grid.push( data[i].split('') );

//let emptyGrid = new Array(5).fill(".....".split(''));

const MINUTES = 200;
let level = new Array(2*MINUTES+1+2);
for (let l = 0; l < level.length; ++l) {
    level[l] = [];
    for (let i = 0; i < 5; ++i)
        level[l].push(".....".split(''));
    level[l][2][2] = '?';
}

const OFFSET = MINUTES+1;
for (let i = 0; i < 5; ++i)
    for (let j = 0; j < 5; ++j)
        level[OFFSET+0][i][j] = grid[i][j];
level[OFFSET+0][2][2] = '?';


for (let min = 1; min <= MINUTES; ++min) {

    let level2 = new Array(2*MINUTES+1+2);
    for (let l = 0; l < level2.length; ++l) {
        level2[l] = [];
        for (let i = 0; i < 5; ++i) {
            level2[l][i] = [];
            for (let j = 0; j < 5; ++j)
                level2[l][i][j] = level[l][i][j];
        }
    }
    
    for (let l = -min; l <= min; ++l)
        for (let i = 0; i < 5; ++i)
            for (let j = 0; j < 5; ++j) 
                if (i != 2 || j != 2) {
                    let cnt = neighboursCount(i, j, OFFSET+l);
                    if (level[OFFSET+l][i][j] == '#' && cnt != 1)
                        level2[OFFSET+l][i][j] = '.';
                    else if (level[OFFSET+l][i][j] == '.' && (cnt == 1 || cnt == 2))
                        level2[OFFSET+l][i][j] = '#';
                }

    for (let l = 0; l < level.length; ++l) {
        level[l] = [];
        for (let i = 0; i < 5; ++i) {
            level[l][i] = [];
            for (let j = 0; j < 5; ++j)
                level[l][i][j] = level2[l][i][j];
        }
    }
}

/*
print(level[OFFSET-1]);
print(level[OFFSET+0]);
print(level[OFFSET+1]);
*/

let cnt = 0;
for (let l = -MINUTES; l <= MINUTES; ++l)
    for (let i = 0; i < 5; ++i)
        for (let j = 0; j < 5; ++j)
            cnt += (level[OFFSET+l][i][j] == '#');
console.log(cnt);



function neighboursCount(i, j, l) {
    if ( (i == 1 && j == 1) || (i == 1 && j == 3) || (i == 3 && j == 1) || (i == 3 && j == 3) )
        return (level[l][i-1][j]=='#')+(level[l][i+1][j]=='#')+(level[l][i][j-1]=='#')+(level[l][i][j+1]=='#');

    if (j == 0 && i > 0 && i < 4)
        return (level[l][i+1][j]=='#')+(level[l][i-1][j]=='#')+(level[l][i][j+1]=='#')+(level[l+1][2][1]=='#');
    if (j == 4 && i > 0 && i < 4)
        return (level[l][i+1][j]=='#')+(level[l][i-1][j]=='#')+(level[l][i][j-1]=='#')+(level[l+1][2][3]=='#');
    if (i == 0 && j > 0 && j < 4)
        return (level[l][i][j-1]=='#')+(level[l][i][j+1]=='#')+(level[l][i+1][j]=='#')+(level[l+1][1][2]=='#');
    if (i == 4 && j > 0 && j < 4)
        return (level[l][i][j-1]=='#')+(level[l][i][j+1]=='#')+(level[l][i-1][j]=='#')+(level[l+1][3][2]=='#');
    if (i == 0 && j == 0)
        return (level[l][i+1][j]=='#')+(level[l][i][j+1]=='#')+(level[l+1][2][1]=='#')+(level[l+1][1][2]=='#');
    if (i == 0 && j == 4)
        return (level[l][i][j-1]=='#')+(level[l][i+1][j]=='#')+(level[l+1][1][2]=='#')+(level[l+1][2][3]=='#');
    if (i == 4 && j == 0)
        return (level[l][i][j+1]=='#')+(level[l][i-1][j]=='#')+(level[l+1][2][1]=='#')+(level[l+1][3][2]=='#');
    if (i == 4 && j == 4)
        return (level[l][i][j-1]=='#')+(level[l][i-1][j]=='#')+(level[l+1][3][2]=='#')+(level[l+1][2][3]=='#');

    if (i == 2 && j == 1)
        return (level[l][i][j-1]=='#')+(level[l][i-1][j]=='#')+(level[l][i+1][j]=='#')+
        (level[l-1][0][0]=='#')+(level[l-1][1][0]=='#')+(level[l-1][2][0]=='#')+(level[l-1][3][0]=='#')+(level[l-1][4][0]=='#');

    if (i == 1 && j == 2)
        return (level[l][i][j-1]=='#')+(level[l][i][j+1]=='#')+(level[l][i-1][j]=='#')+
        (level[l-1][0][0]=='#')+(level[l-1][0][1]=='#')+(level[l-1][0][2]=='#')+(level[l-1][0][3]=='#')+(level[l-1][0][4]=='#');

    if (i == 2 && j == 3)
        return (level[l][i-1][j]=='#')+(level[l][i+1][j]=='#')+(level[l][i][j+1]=='#')+
        (level[l-1][0][4]=='#')+(level[l-1][1][4]=='#')+(level[l-1][2][4]=='#')+(level[l-1][3][4]=='#')+(level[l-1][4][4]=='#');

    if (i == 3 && j == 2)
        return (level[l][i][j-1]=='#')+(level[l][i][j+1]=='#')+(level[l][i+1][j]=='#')+
        (level[l-1][4][0]=='#')+(level[l-1][4][1]=='#')+(level[l-1][4][2]=='#')+(level[l-1][4][3]=='#')+(level[l-1][4][4]=='#');
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