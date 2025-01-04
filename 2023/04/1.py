f = open('input.txt', 'r')

points = 0

for line in f:
    _, numbers = line.strip().split(': ')
    winningInput, haveInput = numbers.split(' | ')
    winning = [int(x) for x in winningInput.split(' ') if x != '']
    have = [int(x) for x in haveInput.split(' ') if x != '']
    
    matches = 0
    for x in have:        
        if x in winning:
            matches += 1
    if matches:
        points += 2 ** (matches-1)

print(points)