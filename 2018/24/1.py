import re

def finished():
    global army
    
    dead = True
    for unit in army[0]:
        if convert(unit)['alive']:
            dead = False
            break
    if dead:
        return True

    dead = True
    for unit in army[1]:
        if convert(unit)['alive']:
            dead = False
            break
    if dead:
        return True

    return False


def damage(a, b):
    if convert(a)['type'] in convert(b)['immune']:
        return 0
    if convert(a)['type'] in convert(b)['weak']:
        return convert(a)['dmg']*convert(a)['n']*2
    return convert(a)['dmg']*convert(a)['n']


def findWeakest(i, k):
    global army, target
    maxDmg = 0
    maxj = -1
    for j in range(len(army[k])):
        if convert(army[k][j])['alive'] and j not in target[1-k]:
            dmg = damage(army[1-k][i], army[k][j])
            if dmg > maxDmg:
                maxDmg = dmg
                maxj = j
    return maxj


def attack(k, i, l, j):
    global army
    unitsLost = damage(army[k][i], army[l][j]) // convert(army[l][j])['hp']
    army[l][j][2] -= unitsLost
    army[l][j][0] = army[l][j][2] * army[l][j][4]

    if army[l][j][2] <= 0:
        army[l][j][8] = False

    return unitsLost


def convert(a):
    return { 'power': a[0], 'init': a[1], 'n': a[2], 'hp': a[3], 'dmg': a[4], 'type': a[5], 'weak': a[6], 'immune': a[7], 'alive': a[8] }


def findInit(init):
    for i in range(len(army[0])):
        if convert(army[0][i])['init'] == init:
            return 0, i
    for j in range(len(army[1])):
        if convert(army[1][j])['init'] == init:
            return 1, j


f = open('input.txt', 'r')
lines = [line.strip() for line in f]
f.close()

army = [[], []]
inits = []
i = 1
while lines[i] != "":
    m = re.match(r'(\d+) units each with (\d+) hit points (.*)with an attack that does (\d+) (.+) damage at initiative (\d+)', lines[i])
    n, hp, special, attck, type, initiative = m.groups()
    inits.append(int(initiative))
    l = special[1:-2].split('; ') 
    weak = []
    immune = []
    for s in l:
        if s.split(' ')[0] == 'immune':
            immune = s[10:].split(', ')
        if s.split(' ')[0] == 'weak':
            weak = s[8:].split(', ')
    army[0].append( [int(n)*int(attck), int(initiative), int(n), int(hp), int(attck), type, weak, immune, True] )
    i += 1

i += 2
while i < len(lines):
    m = re.match(r'(\d+) units each with (\d+) hit points (.*)with an attack that does (\d+) (.+) damage at initiative (\d+)', lines[i])
    n, hp, special, attck, type, initiative = m.groups()
    inits.append(int(initiative))
    l = special[1:-2].split('; ') 
    weak = []
    immune = []
    for s in l:
        if s.split(' ')[0] == 'immune':
            immune = s[10:].split(', ')
        if s.split(' ')[0] == 'weak':
            weak = s[8:].split(', ')
    army[1].append( [int(n)*int(attck), int(initiative), int(n), int(hp), int(attck), type, weak, immune, True] )    
    i += 1

inits.sort(reverse=True)

which = ["Immune System", "Infection"]


while not finished():

    army[0].sort(reverse=True)
    army[1].sort(reverse=True)

    # choose target
    target = [[-1 for j in range(len(army[i]))] for i in range(2)]

    i, j = 0, 0
    while i < len(army[0]) and j < len(army[1]):
        if not convert(army[0][i])['alive']:
            i += 1
            continue
        if not convert(army[1][j])['alive']:
            j += 1
            continue
        
        if army[0][i] > army[1][j]:
            target[0][i] = findWeakest(i, 1)            
            i += 1
        else:
            target[1][j] = findWeakest(j, 0)
            j += 1

    while i < len(army[0]):    
        if not convert(army[0][i])['alive']:
            i += 1
            continue
        target[0][i] = findWeakest(i, 1)
        i += 1

    while j < len(army[1]):    
        if not convert(army[1][j])['alive']:
            j += 1
            continue
        target[1][j] = findWeakest(j, 0)
        j += 1

    
    # attack!
    for init in inits:
        k, l = findInit(init)
        if not convert(army[k][l])['alive'] or target[k][l] == -1:
            continue
        dead = attack(k, l, 1-k, target[k][l])


print('Immune: ')
for i, unit in enumerate(army[0]):
    print(convert(unit))

print()
print('Infection: ')
for j, unit in enumerate(army[1]):
    print(convert(unit))
print()
print()

if not convert(army[0][0])['alive']:
    k = 1
else:
    k = 0

s = 0
for unit in army[k]:
    if convert(unit)['alive']:
        s += convert(unit)['n']
print(s)