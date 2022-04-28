class IntcodeComputer {

    constructor(dataMap) {
        this.relativeBase = 0;
        this.data = new Map(dataMap);
        this.inputs = [];
        this.outputs = [];
        //this.inputs = [...startingInput];
    }

    runCode(input=[], i=0) {

        this.inputs = [...input];

        while (this.data.get(i) != 99) {
            let a = Math.floor(this.data.get(i) / 10000);
            let b = Math.floor(this.data.get(i) / 1000) % 10;
            let c = Math.floor(this.data.get(i) / 100) % 10;
            let op = this.data.get(i) % 100;

            //console.log(i + ": " + op + "(" + a+b+c + ") "  + relativeBase);        

            if (op == 1) {
                this.data.set( this.pos2(i+3, a), this.data.get( this.pos(i+1, c) ) + this.data.get( this.pos(i+2, b) ) );
                i += 4;
            }
            else if (op == 2) {
                this.data.set( this.pos2(i+3, a), this.data.get( this.pos(i+1, c) ) * this.data.get( this.pos(i+2, b) ) );
                i += 4;
            }
            else if (op == 3) {
                //console.log( this.inputs );
                if (this.inputs.length > 0)
                    this.data.set( this.pos2(i+1, c), this.inputs.shift() );
                else
                    return [i, this.outputs];                
                i += 2;
            }
            else if (op == 4) {
                //console.log(data.get( pos(data, i+1, c) ));
                let out = this.data.get( this.pos(i+1, c) );
                this.outputs.push(out);
                i += 2;            
            }
            else if (op == 5) {
                if (this.data.get( this.pos(i+1, c) ))
                    i = this.data.get( this.pos(i+2, b) );
                else
                    i += 3;
            }
            else if (op == 6) {
                if (!this.data.get( this.pos(i+1, c) ))
                    i = this.data.get( this.pos(i+2, b) );
                else
                    i += 3;
            }
            else if (op == 7) {
                this.data.set( this.pos2(i+3, a), +(this.data.get( this.pos(i+1, c) ) < this.data.get( this.pos(i+2, b) )) );
                i += 4;
            }
            else if (op == 8) {
                this.data.set( this.pos2(i+3, a), +(this.data.get( this.pos(i+1, c) ) == this.data.get( this.pos(i+2, b) )) );
                i += 4;
            }
            else if (op == 9) {
                this.relativeBase += this.data.get( this.pos(i+1, c) );
                i += 2;
            }
            else {
                console.log("ERROR");
                break;
            }
        }

        return [i, this.outputs];
    }


    pos(i, code) {
        if (code == 0)
            return (this.data.has(this.data.get(i))) ? this.data.get(i) : -1;
        if (code == 1)
            return i;
        if (code == 2)
            return (this.data.has( this.data.get(i) + this.relativeBase )) ? this.data.get(i) + this.relativeBase : -1;
    }
    
    pos2(i, code) {
        if (code == 0)
            return this.data.get(i);
        if (code == 1)
            return i;
        if (code == 2)
            return this.data.get(i) + this.relativeBase;
    }
    
};





let fs = require("fs");
const origData = fs.readFileSync('input.txt', 'utf8').toString().split(',').filter(x => x).map(x => parseInt(x));

let dataMap = new Map();
for (let i = 0; i < origData.length; ++i)
    dataMap.set(i, origData[i]);
dataMap.set(-1, 0);

let comp = new Array(50);
for (let i = 0; i < 50; ++i)
    comp[i] = new IntcodeComputer(dataMap);
let line = new Array(50).fill(0);
let inp = new Array(50);
for (let i = 0; i < 50; ++i)
    inp[i] = [i];
let out = new Array(50);

while (true) {

    for (let i = 0; i < 50; ++i) {
        [line[i], out[i]] = comp[i].runCode(inp[i], line[i]);
        inp[i] = [];
        //console.log(i + " waiting... output length " + out[i].length);
    }

    /*
        analyze the packets
        if any of the packets gets sent to address 255, break
    */
    for (let i = 0; i < 50; ++i)
        while (out[i].length > 0) {
            let address = out[i].shift();
            let X = out[i].shift(), Y = out[i].shift();

            if (address == 255) {
                console.log(Y);
                process.exit(1);
            }

            inp[address].push(X);
            inp[address].push(Y);

            console.log(`Sending packet (${X}, ${Y}) to address ${address}`);
        }

    for (let i = 0; i < 50; ++i) {
        out[i] = [];
        if (inp[i].length == 0)
            inp[i] = [-1];
    }

}