def nextDiff(a):
    if all(x == 0 for x in a):
        return 0
    
    diff = []
    for i in range(len(a)-1):
        diff.append(a[i+1] - a[i])
    return a[0] - nextDiff(diff)


f = open('input.txt', 'r')

histories = []
for line in f:
    history = list(map(int, line.strip().split(' ')))
    histories.append(history)

sum = 0
for history in histories:
    sum += nextDiff(history)

print(sum)