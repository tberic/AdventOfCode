f = open('input.txt', 'r')

# lines = [line.strip() for line in f if line.strip() != ""]

maps = []
currentMap = []
instructions = ""

for line in f:
    if line.strip().split(' ')[0] == 'seeds:':
        numbers = line.strip().split(': ')[1]
        seeds = [int(number) for number in numbers.split(' ')]
        continue
    
    if line.strip() == "":
        maps.append(currentMap)
        continue
    
    if line[0] >= 'a' and line[0] <= 'z':
        # instructions, _ = line.strip().split(' ')
        # print(instructions)
        currentMap = []
        continue

    ranges = [int(x) for x in line.strip().split(' ')]
    currentMap.append(ranges)
    # a, b, l = ranges
    # for i in range(l):
    #     currentMap[b + i] = a + i

maps = maps[1:]
maps.append(currentMap)

# print(maps)

locs = []
for seed in seeds:
    loc = seed
    for m in range(len(maps)):
        for ranges in maps[m]:
            if loc >= ranges[1] and loc <= ranges[1] + ranges[2]:
                loc = ranges[0] + loc - ranges[1]
                break
    
    locs.append(loc)
    
print(min(locs))