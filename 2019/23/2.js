"use strict";

class IntcodeComputer {

    constructor(dataMap) {
        this.relativeBase = 0;
        this.data = new Map(dataMap);
        this.inputs = [];
        this.outputs = [];
        this.i = 0;
        //this.inputs = [...startingInput];
    }

    runCode(input) {

        this.inputs = this.inputs.concat(input.slice());

        while (this.data.get(this.i) != 99) {
            let a = Math.floor(this.data.get(this.i) / 10000);
            let b = Math.floor(this.data.get(this.i) / 1000) % 10;
            let c = Math.floor(this.data.get(this.i) / 100) % 10;
            let op = this.data.get(this.i) % 100;

            //console.log(i + ": " + op + "(" + a+b+c + ") "  + relativeBase);        

            if (op == 1) {
                this.data.set( this.pos2(this.i+3, a), this.data.get( this.pos(this.i+1, c) ) + this.data.get( this.pos(this.i+2, b) ) );
                this.i += 4;
            }
            else if (op == 2) {
                this.data.set( this.pos2(this.i+3, a), this.data.get( this.pos(this.i+1, c) ) * this.data.get( this.pos(this.i+2, b) ) );
                this.i += 4;
            }
            else if (op == 3) {
                //console.log( this.inputs );
                if (this.inputs.length > 0)
                    this.data.set( this.pos2(this.i+1, c), this.inputs.shift() );
                else {
					//input = this.inputs.slice();
                    return ;
                }
                this.i += 2;
            }
            else if (op == 4) {
                //console.log(data.get( pos(data, i+1, c) ));
                let x = this.data.get( this.pos(this.i+1, c) );
                out.push(x);
                this.i += 2;            
            }
            else if (op == 5) {
                if (this.data.get( this.pos(this.i+1, c) ))
                    this.i = this.data.get( this.pos(this.i+2, b) );
                else
                    this.i += 3;
            }
            else if (op == 6) {
                if (!this.data.get( this.pos(this.i+1, c) ))
                    this.i = this.data.get( this.pos(this.i+2, b) );
                else
                    this.i += 3;
            }
            else if (op == 7) {
                this.data.set( this.pos2(this.i+3, a), +(this.data.get( this.pos(this.i+1, c) ) < this.data.get( this.pos(this.i+2, b) )) );
                this.i += 4;
            }
            else if (op == 8) {
                this.data.set( this.pos2(this.i+3, a), +(this.data.get( this.pos(this.i+1, c) ) == this.data.get( this.pos(this.i+2, b) )) );
                this.i += 4;
            }
            else if (op == 9) {
                this.relativeBase += this.data.get( this.pos(this.i+1, c) );
                this.i += 2;
            }
            else {
                console.log("ERROR");
                break;
            }
        }

//        return this.outputs;
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

let inp = new Array(50);
for (let i = 0; i < 50; ++i)
    inp[i] = [];

let out = [];

let NAT = [];
let lastSeen = -1;
let anyOutputs, anyInputs;

/*
	initialize the computers
*/
for (let i = 0; i < 50; ++i)
		comp[i].runCode([i]);

while (true) {

	anyOutputs = (out.length > 0);
    while (out.length > 0) {
        let address = out.shift();
        let X = out.shift(), Y = out.shift();

        if (address == 255) {
        	console.log("------------");
        	console.log("SENDING TO NAT " + Y);
        	console.log("------------");
        	NAT = [X, Y];
        }
        else {
	        inp[address].push(X);
	        inp[address].push(Y);

	        console.log(`Sending packet (${X}, ${Y}) to address ${address}`);
        }
    }


	anyInputs = false;
    for (let i = 0; i < 50; ++i)
    	if (inp[i].length > 0)
    	{    	
    		anyInputs = true;
			comp[i].runCode(inp[i]);
		    inp[i] = [];
	    }
	    else
		    comp[i].runCode([-1]);
		    
    
    if (!anyInputs && !anyOutputs) {
    	console.log("Waiting...");
    	out.push(0);
    	out.push(NAT[0]);    	
    	out.push(NAT[1]);

        if (lastSeen == NAT[1])
            process.exit(1);
        lastSeen = NAT[1];   	
    }
}
