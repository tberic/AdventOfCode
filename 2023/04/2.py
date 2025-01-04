f = open('input.txt', 'r')

cardMatches = []

for line in f:
    card, numbers = line.strip().split(': ')
    winningInput, haveInput = numbers.split(' | ')
    winning = [int(x) for x in winningInput.split(' ') if x != '']
    have = [int(x) for x in haveInput.split(' ') if x != '']
    
    matches = 0
    for x in have:        
        if x in winning:
            matches += 1
    cardMatches.append(matches)

print(cardMatches)

cards = [1 for i in range(len(cardMatches))]

for i in range(len(cards)):
    for j in range(cardMatches[i]):
        cards[i + j + 1] += cards[i]

print(sum(cards))