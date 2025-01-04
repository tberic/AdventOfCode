def sumData(i):
    global a, sum
    m = a[i]
    n = a[i+1]
    pos = i+2
    for i in range(m):
        pos = sumData(pos)
    for j in range(n):
        sum += a[pos+j]
    return pos+n

f = open('input.txt', 'r')
a = list(map(int, f.readline().split()))
f.close()

sum = 0
sumData(0)
print(sum)