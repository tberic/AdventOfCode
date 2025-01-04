def parseRound(round):
    dice = [0, 0, 0]
    for die in round.split(', '):
        n, color = die.split(' ')
        n = int(n)
        if (color == 'red'):
            dice[0] = n
        if (color == 'green'):
            dice[1] = n
        if (color == 'blue'):
            dice[2] = n
    return dice

f = open('input.txt', 'r')

sumId = 0

for line in f:
    gameId, game = line.strip().split(': ')
    _, id = gameId.split(' ')
    possible = True
    for round in game.split('; '):
        dice = parseRound(round)
        
        if (dice[0] > 12 or dice[1] > 13 or dice[2] > 14):
            possible = False
            break
    
    if (possible):
        sumId += int(id)
        print(id)

print(sumId)