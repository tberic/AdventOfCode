f = open('input.txt', 'r')

sumN = 0
for line in f:
    s = line.strip()[1:-1]
    #print(s)    
    i = 0
    n = 6
    while i < len(s):
        if s[i] == '\\' or s[i] == '\"':
            n += 2
        else:
            n += 1
        i += 1
    sumN += n
    #print(m, n)

print(sumN)

f.close()