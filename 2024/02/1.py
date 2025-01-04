f = open('input.txt')

safe = 0
for line in f:
    levels = [int(x) for x in line.split(' ')]

    if levels[0] == levels[1]:
        continue
    sign = lambda x: (1, -1)[x<0]
    incdec = sign(levels[1] - levels[0])
    previous = levels[0] - incdec * 1
    isSafe = True
    for level in levels:
        if (level == previous) or ((level - previous) * incdec < 0):
            isSafe = False
        if abs(level - previous) > 3:
            isSafe = False
        previous = level
    if isSafe:
        safe += 1

print(safe)