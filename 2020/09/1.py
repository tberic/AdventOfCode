f = open('input.txt', 'r')
a = [int(line) for line in f]
b = a[:25]

for k in range(25, len(a)):
    t = 0
    for i in range(25):
        for j in range(i+1, 25):
            if a[k] == b[i] + b[j]:
                t = 1
    if not t:
        print(a[k])
        break
    
    for i in range(24):
        b[i] = b[i+1]
    b[24] = a[k]

f.close()