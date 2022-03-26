f = open('input.txt', 'r')
boss = {}
lines = [line for line in f]
a, b = lines[0].split(': ')
bossHPrem = int(b)
a, b = lines[1].split(': ')
bossDMG = int(b)
a, b = lines[2].split(': ')
bossARMR = int(b)
f.close()

weapon = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
armor = [(0, 0, 0), (13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]
ring = [(0, 0, 0), (0, 0, 0), (25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)]

minCost = 10**10
maxCost = 0
for w in weapon:
    for a in armor:
        for i in range(len(ring)):
            for j in range(i+1, len(ring)):
                myDMG = w[1]
                myARMR = a[2]
                myDMG += ring[i][1] + ring[j][1]
                myARMR += ring[i][2] + ring[j][2]
                cost = w[0] + a[0] + ring[i][0] + ring[j][0]

                myHP = 100
                bossHP = bossHPrem
                while myHP > 0 and bossHP > 0:
                    damage = myDMG - bossARMR
                    if damage <= 0:
                        damage = 1
                    bossHP -= damage
                    damage = bossDMG - myARMR
                    if damage <= 0:
                        damage = 1
                    myHP -= damage
                
                if bossHP <= 0 and cost < minCost:
                    minCost = cost
                if bossHP > 0 and cost > maxCost:
                    maxCost = cost

print(minCost)
print(maxCost)