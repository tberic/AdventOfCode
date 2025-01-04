f = open('input.txt', 'r')
lines = [line.strip() for line in f]
f.close()

weight = {}

# first pass just to get the names
for line in lines:
    left, *right = line.split(' -> ')
    weight[ left.split()[0] ] = int(left.split()[1][1:-1])

names = set(weight.keys())

# in the second pass we remove all the programs that appear on the right side
for line in lines:
    left, *right = line.split(' -> ')
    if right:
        for x in right[0].split(', '):
            #print(x, end=' ')
            names.discard(x)
        #print()

print(names)