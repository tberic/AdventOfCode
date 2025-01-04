def sumWeights(name):
    global subtree, weight

    if name not in subtree:
        return weight[name]

    s = weight[name]
    for x in subtree[name]:
        s += sumWeights(x)
    return s


f = open('input.txt', 'r')
lines = [line.strip() for line in f]
f.close()

weight = {}

# first pass just to get the names
for line in lines:
    left, *right = line.split(' -> ')
    weight[ left.split()[0] ] = int(left.split()[1][1:-1])

subtree = {}

# in the second pass we remove all the programs that appear on the right side
for line in lines:
    left, *right = line.split(' -> ')
    if right:
        subtree[left.split()[0]] = right[0].split(', ')

#head = "eugwuhl"
#head = "smaygo"
#head = "hmgrlpj"
head = "drjmjug"
totalWeight = {}
for x in subtree[head]:
    totalWeight[x] = sumWeights(x)
sortedWeights = dict(sorted(totalWeight.items(), key=lambda item: item[1]))
print(sortedWeights)