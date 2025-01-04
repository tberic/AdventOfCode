import re

f = open('input.txt')

total = 0
for line in f:

    #first remove everything between don't() and do()
    line = re.sub(r"don't[(][)].*?do[(][)]", "DELETED", line)
    line = re.sub(r"don't[(][)].*$", "DELETED", line)
    print(line)
    
    matches = re.findall(r'mul[(]([0-9]+),([0-9]+)[)]', line)

    for match in matches:
        x, y = map(int, match)
        total += x*y

print(total)