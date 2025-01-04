import math

def convertToDecimal(s):
    result = 0
    power = 1
    for i in range(len(s)-1, -1, -1):
        if (s[i] >= '0' and s[i] <= '2'):
            result += (ord(s[i]) - ord('0')) * power
        elif (s[i] == '-'):
            result -= power
        elif (s[i] == '='):
            result -= 2 * power
        power *= 5
    return result

def convertToBase5(x):
    result = ""
    while (x > 0):
        result = str(x % 5) + result
        x //= 5
    return result

def convertCharToSNAFU(c):
    if (c == '0'):
        return '='
    if (c == '1'):
        return '-'
    if (c == '2'):
        return '0'
    if (c == '3'):
        return '1'
    if (c == '4'):
        return '2'

def convertToSNAFU(x):
    n = math.ceil( math.log(2 * x + 1, 5) )
    s = list(convertToBase5( x + (5**n - 1) // 2 ))
    
    for i in range(len(s)):
        s[i] = convertCharToSNAFU(s[i])
    
    return ''.join(s)


f = open('input.txt', 'r')

sum = 0
for line in f:	
    x = convertToDecimal(line.strip())
    print(x)
    sum += x
    
print(sum)

print(convertToSNAFU(sum))