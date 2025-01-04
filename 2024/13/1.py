from pulp import *

def parseInput(text, op):
    _, buttonA = text.split(': ')
    x, y = buttonA.split(', ')
    _, x = x.split(op)
    _, y = y.split(op)
    return int(x), int(y)

def con1(t):
    return xA*t[0] + xB*t[0] - x0
def con2(t):
    return yA*t[1] + yB*t[1] - y0

def target(t):
    return 3*t[0] + t[1]

f = open('input.txt')

lines = [line.strip() for line in f]
total = 0

for i in range(0, len(lines), 4):
    buttonA = lines[i]
    buttonB = lines[i+1]
    cons = lines[i+2]

    xA, yA = parseInput(buttonA, '+')
    xB, yB = parseInput(buttonB, '+')
    x0, y0 = parseInput(cons, '=')

    x = LpVariable("x", cat=LpInteger)
    y = LpVariable("y", cat=LpInteger)
    prob = LpProblem('MixedIntegerLinearProgramming', LpMinimize)

    prob += xA * x + xB * y == x0
    prob += yA * x + yB * y == y0
    prob += 3 * x + y

    prob.solve(PULP_CBC_CMD(msg=0))
    solx = x.value()
    soly = y.value()

    if '.0' in str(solx) and '.0' in str(soly):
        total += int(solx)*3 + int(soly)
        # print(solx, soly)

print(total)