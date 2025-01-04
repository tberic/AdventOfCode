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
    # x0 += 10000000000000
    # y0 += 10000000000000

    x = LpVariable("x", 0, None, cat='Integer')
    y = LpVariable("y", 0, None, cat='Integer')
    prob = LpProblem('MixedIntegerLinearProgramming', LpMinimize)

    prob += xA * x + xB * y == x0
    prob += yA * x + yB * y == y0
    prob += 3 * x + y
    
    # solver_list = listSolvers(onlyAvailable=True)
    # print(solver_list)
    
    status = prob.solve(PULP_CBC_CMD(msg=0))
    solx = x.value()
    soly = y.value()

    if xA * int(solx) + xB * int(soly) == x0 and yA * int(solx) + yB * int(soly) == y0:
        total += int(solx)*3 + int(soly)
        print(solx, soly)

    # print(solx, soly)
    # if ('.0' in str(solx) and '.0' in str(soly)) and not ('-' in str(solx) or '-' in str(soly)):
    # if not ('-' in str(solx) or '-' in str(soly)):
    #     if abs(solx - int(solx)) < 0.001 and abs(soly - int(soly)) < 0.001:
    #         # if xA * solx + xB * soly == x0 and yA * solx + yB * soly == y0:
    #         total += int(solx)*3 + int(soly)
    #         print(solx, soly)

print(total)