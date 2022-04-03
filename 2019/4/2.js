

function valid(x) {
    let s = x.toString();   

    if (s[0] != s[1] && s[1] != s[2] && s[2] != s[3] && s[3] != s[4] && s[4] != s[5])
        return false;

    if ( !( (s[0] == s[1] && s[1] < s[2]) || (s[0] < s[1] && s[1] == s[2] && s[2] < s[3]) ||
    (s[1] < s[2] && s[2] == s[3] && s[3] < s[4]) || (s[2] < s[3] && s[3] == s[4] && s[4] < s[5]) ||
    (s[3] < s[4] && s[4] == s[5]) ) )
        return false;

    return (s[0] <= s[1] && s[1] <= s[2] && s[2] <= s[3] && s[3] <= s[4] && s[4] <= s[5]);
}

const start = 246540;
const end = 787419;

let count = 0;
for (let x = start; x <= end; ++x) {
    if ( valid(x) )
        count++;
}

console.log(count);