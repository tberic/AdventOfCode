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

powers = 0

for line in f:
    gameId, game = line.strip().split(': ')
    _, id = gameId.split(' ')
    
    diceMin = [0, 0, 0]
    for round in game.split('; '):
        dice = parseRound(round)

        for i, d in enumerate(dice):
            if (d > diceMin[i]):
                diceMin[i] = d

    powers += diceMin[0] * diceMin[1] * diceMin[2]

print(powers)  
