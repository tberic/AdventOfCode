def roundPlayer():
    global spell, inPlay
    d, a, hp, m = (0, 0, 0, 0)
    for i in range(len(inPlay)):
        if inPlay[i]:
            inPlay[i] -= 1
            d += spell[i][2]
            a += spell[i][3]
            hp += spell[i][4]
            m += spell[i][5]
    return (d, a, hp, m)

def roundBoss():
    global bossDMG, spell, inPlay
    d, a, hp, m = (0, 0, 0, 0)
    for i in range(len(inPlay)):
        if inPlay[i]:
            inPlay[i] -= 1
            d += spell[i][2]
            a += spell[i][3]
            hp += spell[i][4]
            m += spell[i][5]
    dBoss = bossDMG - a
    if dBoss < 1:
        dBoss = 1
    return dBoss, (d, a, hp, m)

def play(mana, myHP, bossHP, manaSpent, path):
    global spell, minCost, inPlay

    #recharge mana if Recharge spell is in effect so we can spend new mana on spells
    m = 0
    if inPlay[4]:
        m += spell[4][5]

    if myHP <= 1:
        return False

    #if I can't afford to cast mana, I lose
    if mana+m < 53:
        return False

    inPlayBkp = inPlay.copy()
    for i in range(len(spell)):        
        if (inPlay[i] <= 1) and (mana+m >= spell[i][0]):
            if i <= 1:
                inPlay[i] = spell[i][1]

            (x1, a, hp1, m1) = roundPlayer()
            if bossHP-x1 <= 0:
                if manaSpent + spell[i][0] < minCost:
                    minCost = manaSpent + spell[i][0]
                return True

            if i > 1:
                inPlay[i] = spell[i][1]

            y, (x2, a, hp2, m2) = roundBoss()
            if bossHP-x1-x2 <= 0:
                if manaSpent + spell[i][0] < minCost:
                    minCost = manaSpent + spell[i][0]
                return True
            if myHP+hp1+hp2-y-1 <= 0:
                return False

            play(mana + m + m2 - spell[i][0], myHP + hp1 + hp2 - y - 1, bossHP - x1 - x2, manaSpent + spell[i][0], path + [i])
            inPlay = inPlayBkp.copy()
            inPlay[i] = 0


f = open('input.txt', 'r')
lines = [line for line in f]
a, b = lines[0].split(': ')
bossHP = int(b)
a, b = lines[1].split(': ')
bossDMG = int(b)
f.close()

#(mana cost, effect? (turns), damage, armor, add hp, add mana)
spell = [ (53, 1, 4, 0, 0, 0), (73, 1, 2, 0, 2, 0), (113, 6, 0, 7, 0, 0), (173, 6, 3, 0, 0, 0), (229, 5, 0, 0, 0, 101) ]
#magic missile, drain, shield, poison, recharge
inPlay = [0, 0, 0, 0, 0]


minCost = 10**10
#mana, HP, bossHP, manaSpent
play(500, 50, bossHP, 0, [])
print(minCost)