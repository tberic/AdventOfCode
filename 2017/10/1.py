def knot(a, pos, n):
    if pos + n < len(a):
        return a[:pos] + a[pos:pos+n][::-1] + a[pos+n:]
    
    b = (a[pos:] + a[:(pos+n)%len(a)])[::-1]
    return b[len(a)-pos:] + a[ (pos+n)%len(a):pos ] + b[ :len(a)-pos ]

def knotHash(a, l):
    skip = 0
    pos = 0
    for n in l:
        a = list(knot(a, pos, n))
        pos = (pos + n + skip) % len(a)
        skip += 1
    return (a, pos, skip)

f = open('input.txt', 'r')
lengths = list(map(int, f.readline().split(',')))
f.close()

#a = knot([4, 3, 0, 1, 2], 1, 5)
#print(knotHash( list(range(5)), [3, 4, 1, 5] ))

print(knotHash( list(range(256)), lengths ))