from itertools import combinations
from math import sqrt

precision = 0.001

def collide(i, j, t):
    global p, v, a
    r1 = [ p[i][k] + v[i][k]*t + a[i][k]*t*(t+1)//2 for k in range(3) ]
    r2 = [ p[j][k] + v[j][k]*t + a[j][k]*t*(t+1)//2 for k in range(3) ]
    return r1 == r2

def integer(x):
    return abs( x - round(x) ) < precision

def collision(i, j):
    global p, v, a
    
    for k in range(3):
        if a[i][k] != a[j][k]:
            b = v[i][k]-v[j][k] + (a[i][k]-a[j][k])/2
            d = b**2 - 2*(a[i][k]-a[j][k])*(p[i][k]-p[j][k])
            if d < 0:
                return False
            t1 = ( -b - sqrt( d ) ) / (a[i][k]-a[j][k])
            t2 = ( -b + sqrt( d ) ) / (a[i][k]-a[j][k])
            t1, t2 = sorted([t1, t2])
            
            if integer(t1) and t1 > 0:
                if collide(i, j, round(t1)):
                    return round(t1)
            if integer(t2) and t2 > 0:
                if collide(i, j, round(t2)):
                    return round(t2)
            return False
        elif v[i][k] != v[j][k]:
            t1 = (p[j][k] - p[i][k]) / (v[i][k]-v[j][k])
            if integer(t1) and t1 > 0:
                if collide(i, j, round(t1)):
                    return round(t1)
            return False
        else:
            if p[i][k] != p[j][k]:
                return False

    # if we reached this point, we are dealing with two identical particles
    return False


p = []
v = []
a = []

f = open('input.txt', 'r')
for line in f:
    w = line.strip().split(', ')
    p.append(list(map(int, w[0][3:-1].split(','))))
    v.append(list(map(int, w[1][3:-1].split(','))))
    a.append(list(map(int, w[2][3:-1].split(','))))
f.close()

n = len(p)
farTime = 10**6

col = {}

# calculate all the times for collisions
for x, y in combinations(range(n), 2):
    t = collision(x, y)
    if t:
        if t not in col:
            col[t] = [(x, y)]
        else:
            col[t].append( (x, y) )
        #col.append( (t, x, y) )

alive = [1 for i in range(n)]

# remember that more than two particles can collide at the same time, we will have to deal with that
# sort the collisions: first by time, then by indices
for t in sorted(col):
    #print(t, col[t])
    destroy = set()
    for i, j in col[t]:
        if alive[i] and alive[j]:
            destroy.add(i)
            destroy.add(j)    
    for x in destroy:
        alive[x] = 0

print(sum(alive))