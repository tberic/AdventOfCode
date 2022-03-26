from operator import add
import re

def plus(a, b):
    return list(map(add, a, b))

def scalar(t, a):
    return [ t*x for x in a ]

def norm(T):
    return sum( [abs(x) for x in T] )

f = open('input.txt', 'r')

p = []
v = []
a = []

for line in f:
    w = line.strip().split(', ')
    p.append(list(map(int, w[0][3:-1].split(','))))
    v.append(list(map(int, w[1][3:-1].split(','))))
    a.append(list(map(int, w[2][3:-1].split(','))))
f.close()

farTime = 10**10

minDist = norm( plus( p[0],  plus( scalar( farTime, v[0] ) , scalar( farTime**2, a[0] ) )  ) )
minPos = 0
for i in range(1, len(p)):
    T = plus( p[i],  plus( scalar( farTime, v[i] ) , scalar( farTime**2, a[i] ) )  )
    d = norm(T)
    if d < minDist:
        minDist = d
        minPos = i

print(minPos)