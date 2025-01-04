def correct(update):
    for i in range(len(update) - 1):
        for j in range(i+1, len(update)):
            if update[j] in after and update[i] in after[update[j]]:
                return False
    return True

f = open('input.txt')

lines = [line for line in f]

after = {}
V = []
lineNum = 0
for lineNum, line in enumerate(lines):
    if line == "\n":
        break
    a, b = list(map(int, line.strip().split('|')))
    if a not in after:
        after[a] = []
        V.append(a)
    after[a].append(b)

updates = []
for i in range(lineNum + 1, len(lines)):
    updates.append(list(map(int, lines[i].strip().split(','))))

total = 0
for update in updates:
    if correct(update):
        total += update[ len(update) // 2 ]

print(total)