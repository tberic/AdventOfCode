def nextDiff(a):
    if all(x == 0 for x in a):
        return 0
    
    diff = []
    for i in range(1, len(a)):
        diff.append(a[i] - a[i-1])
    return a[-1] + nextDiff(diff)


f = open('input.txt', 'r')

histories = []
for line in f:
    history = list(map(int, line.strip().split(' ')))
    histories.append(history)

sum = 0
for history in histories:
    sum += nextDiff(history)

print(sum)