import re
from z3 import Int, If, Optimize

def dist(A, B):
    return abs(A[0]-B[0]) + abs(A[1]-B[1]) + abs(A[2]-B[2])

def z3_abs(x):
    return If(x >= 0, x, -x)

def z3_dist(A, B):
    return z3_abs(A[0] - B[0]) + z3_abs(A[1] - B[1]) + z3_abs(A[2] - B[2])

f = open('input.txt', 'r')
lines = [line.strip() for line in f]
f.close()

cube = []
for line in lines:
    m = re.match(r'pos=<(\-?\d+),(\-?\d+),(\-?\d+)>, r=(\d+)', line)
    x, y, z, r = list(map(int, m.groups()))
    cube.append( (r, (x, y, z)) )

x = Int('x')
y = Int('y')
z = Int('z')
orig = (x, y, z)
cost = Int('cost')

cost_expr = x * 0

for r, pos in cube:
    cost_expr += If(z3_dist(orig, pos) <= r, 1, 0)

opt = Optimize()
opt.add(cost == cost_expr)
opt.maximize(cost)
opt.minimize(z3_dist((0, 0, 0), (x, y, z)))

opt.check()

model = opt.model()
pos = (model[x].as_long(), model[y].as_long(), model[z].as_long())
print("position: ", pos)
print("num in range: ", model[cost].as_long())
print("distance: ", dist((0, 0, 0), pos))