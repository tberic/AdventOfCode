def denseHash(a):
    h = []
    for i in range(16):
        s = 0
        for j in range(16):
            s ^= a[ 16*i+j ]
        h.append(s)
    return h            

def knot(a, pos, n):
    if pos + n < len(a):
        return a[:pos] + a[pos:pos+n][::-1] + a[pos+n:]
    
    b = (a[pos:] + a[:(pos+n)%len(a)])[::-1]
    return b[len(a)-pos:] + a[ (pos+n)%len(a):pos ] + b[ :len(a)-pos ]

def knotHash(a, l, pos=0, skip=0):
    for n in l:
        a = list(knot(a, pos, n))
        pos = (pos + n + skip) % len(a)
        skip += 1
    return (a, pos, skip)

f = open('input.txt', 'r')
lengths = [ ord(c) for c in f.readline().strip() ]
lengths = lengths + [17, 31, 73, 47, 23]
f.close()

a = list(range(256))
pos = 0
skip = 0
for _ in range(64):
    a, pos, skip = knotHash( a, lengths, pos, skip )

for x in denseHash(a):
    print((str(hex(x))[2:]).zfill(2), end='')