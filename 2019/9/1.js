let relativeBase = 0;

function runCode(inputs, data=dataMap) {
    let i = 0;
    let outputs = [];

    while (data.get(i) != 99) {
        let a = Math.floor(data.get(i) / 10000);
        let b = Math.floor(data.get(i) / 1000) % 10;
        let c = Math.floor(data.get(i) / 100) % 10;
        let op = data.get(i) % 100;

        //console.log(i + ": " + op + "(" + a+b+c + ") "  + relativeBase);        

        if (op == 1) {
            data.set( pos2(data, i+3, a), data.get( pos(data, i+1, c) ) + data.get( pos(data, i+2, b) ) );            
            i += 4;
        }
        else if (op == 2) {
            data.set( pos2(data, i+3, a), data.get( pos(data, i+1, c) ) * data.get( pos(data, i+2, b) ) );
            i += 4;
        }
        else if (op == 3) {
            data.set( pos2(data, i+1, c), inputs.shift() );
            i += 2;
        }
        else if (op == 4) {
            //console.log(data.get( pos(data, i+1, c) ));
            outputs.push(data.get( pos(data, i+1, c) ));
            i += 2;
        }
        else if (op == 5) {
            if (data.get( pos(data, i+1, c) ))
                i = data.get( pos(data, i+2, b) );
            else
                i += 3;
        }
        else if (op == 6) {
            if (!data.get( pos(data, i+1, c) ))
                i = data.get( pos(data, i+2, b) );
            else
                i += 3;
        }
        else if (op == 7) {
            data.set( pos2(data, i+3, a), +(data.get( pos(data, i+1, c) ) < data.get( pos(data, i+2, b) )) );
            i += 4;
        }
        else if (op == 8) {
            data.set( pos2(data, i+3, a), +(data.get( pos(data, i+1, c) ) == data.get( pos(data, i+2, b) )) );
            i += 4;
        }
        else if (op == 9) {
            relativeBase += data.get( pos(data, i+1, c) );            
            i += 2;
        }
        else {
            console.log("ERROR");
            break;
        }
    }

    return outputs;
}


function pos(data, i, code) {
    if (code == 0)
        return (data.has(data.get(i))) ? data.get(i) : -1;
    if (code == 1)
        return i;
    if (code == 2)
        return (data.has( data.get(i) + relativeBase )) ? data.get(i) + relativeBase : -1;
}

function pos2(data, i, code) {
    if (code == 0)
        return data.get(i);
    if (code == 1)
        return i;
    if (code == 2)
        return data.get(i) + relativeBase;
}

let fin = require("fs");
const origData = fin.readFileSync('input.txt', 'utf8').toString().split(',').filter(x => x).map(x => parseInt(x));

let dataMap = new Map();
for (let i = 0; i < origData.length; ++i)
    dataMap.set(i, origData[i]);
dataMap.set(-1, 0);

console.log(runCode([1]));