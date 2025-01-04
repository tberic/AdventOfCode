f = open('input.txt', 'r')

sumM = 0
sumN = 0
for line in f:
    s = line.strip()[1:-1]
    #print(s)
    m = len(s)+2
    i = 0
    n = 0
    while i < len(s):
        if s[i] != '\\':
            n += 1
        else:
            if i+1 < len(s) and s[i+1] in '\"\\':
                n += 1
                i += 1
            elif i+1 < len(s) and s[i+1] == 'x':
                n += 1
                i += 3
            else:
                n += 1
        i += 1
    sumM += m
    sumN += n
    #print(m, n)

print(sumM, sumN)
print(sumM - sumN)

f.close()