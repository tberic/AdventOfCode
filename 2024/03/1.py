import re

f = open('input.txt')

total = 0
for line in f:
    matches = re.findall(r'mul[(]([0-9]+),([0-9]+)[)]', line)

    for match in matches:
        x, y = map(int, match)
        total += x*y
        # re.findall(r'mul[(][0-9]+,[0-9]+[)]', match)
        # print(x, y)

print(total)