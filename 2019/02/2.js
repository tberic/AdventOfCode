let fin = require("fs");
const originalData = fin.readFileSync('input.txt', 'utf8').toString().split(',').filter(x => x).map(x => parseInt(x));

outerloop:
for (let a = 0; a < 100; ++a)
    for (let b = 0; b < 100; ++b) {
        data = originalData.slice();
        data[1] = a;
        data[2] = b;

        for (let i = 0; i < data.length; i += 4) {
            if (data[i] == 1)
                data[data[i+3]] = data[data[i+1]] + data[data[i+2]];
            else if (data[i] == 2)
                data[data[i+3]] = data[data[i+1]] * data[data[i+2]];
            else if (data[i] == 99)
                break;    

        if (data[0] == 19690720) {
            console.log(100*a+b);
            break outerloop;
        }        
    }
}