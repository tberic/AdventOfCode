def overlaps(range1, range2):
    return range1[0] < range2[1] + range2[2] and range1[0] + range1[2] > range2[1]

def inside(range1, range2):
    return range1[0] >= range2[1] and range1[0] + range1[2] <= range2[1] + range2[2]

def compose(f, g):
    h = f
    overlapsExist = True
    while overlapsExist:
        overlapsExist = False
        f = h
        for range1 in f:
            for range2 in g:
                if inside(range1, range2):
                    continue
                if overlaps(range1, range2):
                    overlapsExist = True

                    leftRange = []
                    middleRange = range1
                    rightRange = []
                    c, d, m = range2
                    if middleRange[0] < range2[1]:
                        a, b, l = middleRange
                        if d > a:
                            leftRange = [ a, b, d - a ]
                        middleRange = [ d, b + d - a, l - d + a ]
                    if middleRange[0] + middleRange[2] > range2[1] + range2[2]:
                        a, b, l = middleRange
                        middleRange = [ a, b, d + m - a ]
                        rightRange = [ d + m, b + d + m - a, l - (d + m - a) ]

                    if range1 in h:
                        h.remove(range1)

                    if leftRange != [] and leftRange not in h:
                        h.append(leftRange)
                    if middleRange != [] and middleRange not in h: 
                        h.append(middleRange)
                    if rightRange != [] and rightRange not in h: 
                        h.append(rightRange)

    for range1 in h:
        for range2 in g:
            if inside(range1, range2):
                range1[0] = range2[0] + range1[0] - range2[1]
                break

    return h


f = open('input.txt', 'r')

maps = []
currentMap = []

for line in f:
    if line.strip().split(' ')[0] == 'seeds:':
        numbers = line.strip().split(': ')[1]
        seeds = [int(number) for number in numbers.split(' ')]
        continue
    
    if line.strip() == "":
        maps.append(currentMap)
        continue
    
    if line[0] >= 'a' and line[0] <= 'z':
        currentMap = []
        continue

    ranges = [int(x) for x in line.strip().split(' ')]
    currentMap.append(ranges)

maps = maps[1:]
maps.append(currentMap)


seedMap = [ [seeds[2*i], seeds[2*i], seeds[2*i+1]] for i in range(len(seeds) // 2) ]

compositionMap = seedMap
for i in range(len(maps)): # len(maps)
    compositionMap = compose(compositionMap, maps[i])

min = compositionMap[0][0]
for range in compositionMap:
    if range[0] < min:
        min = range[0]
print(min)