from copy import deepcopy

def isSafe(levels):
    if levels[0] == levels[1]:
        return False
    sign = lambda x: (1, -1)[x<0]
    incdec = sign(levels[1] - levels[0])
    previous = levels[0] - incdec * 1

    for level in levels:
        if (level == previous) or ((level - previous) * incdec < 0):
            return False
        if abs(level - previous) > 3:
            return False
        previous = level
    
    return True

f = open('input.txt')

safe = 0
for line in f:
    levels = [int(x) for x in line.split(' ')]
    
    res = isSafe(levels)
    if res:
        safe += 1
    else:        
        for i in range(len(levels)):
            levelsCopy = deepcopy(levels)
            del levelsCopy[i]
            if isSafe(levelsCopy):
                safe += 1
                break

print(safe)